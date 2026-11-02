#!/usr/bin/env python3
"""One-time Vitaceae archived-ZIP rights audit and candidate installation.
Only source-proven original bytes with photo-level license, creator and plausible taxonomy may publish.
Unverified candidates are held; no fake reviewer/rights data is asserted.
"""
import datetime, hashlib, json, re, subprocess, sys, tempfile, time, urllib.request, urllib.error
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"workflow/vitaceae-photo-first-candidate-audit-2026-11-02.json"
REPORT=ROOT/"workflow/vitaceae-photo-first-execution-2026-11-02.json"
SITE=ROOT/"site"
USERAGENT="HaysBotanyPhotoFirst/1.0 (noncommercial educational photo verification)"
MAP={"cc-by":("CC BY 4.0","https://creativecommons.org/licenses/by/4.0/"),
     "cc-by-nc":("CC BY-NC 4.0","https://creativecommons.org/licenses/by-nc/4.0/"),
     "cc-by-sa":("CC BY-SA 4.0","https://creativecommons.org/licenses/by-sa/4.0/"),
     "cc-by-nc-sa":("CC BY-NC-SA 4.0","https://creativecommons.org/licenses/by-nc-sa/4.0/"),
     "cc0":("CC0 1.0","https://creativecommons.org/publicdomain/zero/1.0/")}
ALIASES={"nekemias-arborea":{"Nekemias arborea","Ampelopsis arborea"},
         "parthenocissus-heptaphylla":{"Parthenocissus heptaphylla"},
         "parthenocissus-quinquefolia":{"Parthenocissus quinquefolia"}}
def request(url):
    assert url.startswith("https://")
    error=None
    for k in range(4):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":USERAGENT,"Accept":"application/json" if "/v1/observations/" in url else "image/*"})
            with urllib.request.urlopen(req,timeout=28) as resp:
                if resp.status!=200:raise RuntimeError("HTTP "+str(resp.status))
                return resp.read()
        except (urllib.error.URLError,TimeoutError,OSError,RuntimeError) as ex:
            error=ex;time.sleep(2+k*3)
    raise RuntimeError("Source not accessible: "+str(error))
def clean(s):
    return re.sub(r"\s+"," ",str(s or "")).casefold().strip()
def original_creator(attr):
    s=(attr or "").strip()
    s=re.sub(r"^(?:\(c\)|©)\s*","",s,flags=re.I)
    s=re.sub(r",\s*(?:some|no)\s+rights\s+reserved.*$","",s,flags=re.I)
    return s.strip()
def main():
    data=json.loads(MANIFEST.read_text())
    assert data["repo"]=="Crking92/Hays-Botany-Trees-Shrubs"
    assert data["source_images"]==33 and len(data["candidates"])==13
    all_ids=[x["photo_id"] for x in data["candidates"]]
    assert len(set(all_ids))==len(all_ids)
    created=datetime.datetime.now(datetime.timezone.utc).isoformat()
    report={"batch_id":data["batch_id"],"verified_at":created,"source_images":33,
            "source_file_hashes_distinct":33,"candidate_total":13,
            "not_selected_after_contact_review":20,"ready_count":0,
            "published_count":0,"already_published_count":0,"held_candidate_count":0,"records":[]}
    with tempfile.TemporaryDirectory(prefix="hays-vitaceae-reviewed-") as tmp:
        root=Path(tmp)
        for cand in data["candidates"]:
            result={"species_id":cand["species_id"],"photo_id":cand["photo_id"],"source_page":cand["photo_page"]}
            try:
                sid=cand["species_id"];pid=cand["photo_id"]
                assert sid in ALIASES
                card=json.loads((SITE/"data/species"/(sid+".json")).read_text())
                if any(p.get("source_page")==cand["photo_page"] for p in card["verified_photos"]):
                    result["status"]="ALREADY_PUBLISHED"
                    report["already_published_count"]+=1
                    report["records"].append(result)
                    continue
                obs=json.loads(request("https://api.inaturalist.org/v1/observations/"+str(cand["observation_id"])))
                rows=obs.get("results") or []
                assert len(rows)==1 and rows[0].get("id")==cand["observation_id"],"observation missing or ambiguous"
                observation=rows[0]
                actual_taxon=(observation.get("taxon") or {}).get("name")
                assert actual_taxon in ALIASES[sid], "observed taxon differs from archive: "+str(actual_taxon)
                images=observation.get("photos") or []
                photo=next((p for p in images if p.get("id")==pid),None)
                if photo is None:
                    photo=next((p.get("photo") for p in observation.get("observation_photos",[]) if (p.get("photo") or {}).get("id")==pid),None)
                assert photo is not None,"exact photo ID absent from observation"
                license_code=photo.get("license_code")
                assert license_code in MAP,"unsupported current photo license: "+str(license_code)
                assert license_code==cand["archived_license_code"],"photo-specific license changed from ZIP"
                attr=photo.get("attribution") or ""
                creator=original_creator(attr)
                assert creator and clean(creator)==clean(cand["archived_creator"]), "photo creator does not match exact ZIP record: "+str(attr)
                assert cand["photo_url"].startswith("https://inaturalist-open-data.s3.amazonaws.com/photos/"+str(pid)+"/original.")
                payload=request(cand["photo_url"])
                digest=hashlib.sha256(payload).hexdigest()
                assert digest==cand["sha256"],"exact original file SHA-256 changed from archived ZIP"
                assert 200<len(payload)<=25*1024*1024,"original image is outside size limit"
                license_name,license_url=MAP[license_code]
                relative=Path("photo-intake/approved")/sid/("inat-photo-"+str(pid)+"."+cand["extension"])
                destination=root/relative
                destination.parent.mkdir(parents=True,exist_ok=True)
                destination.write_bytes(payload)
                note=("Original archived in "+cand["photo_first_visual_note"]+" "
                      "Observation-level taxon "+actual_taxon+" confirmed from exact iNaturalist observation. "
                      "This is a general visual sanity check, not a diagnostic species voucher.")
                meta={
                    "species_id":sid,"photo_file":destination.name,
                    "status":"APPROVED_FOR_PUBLIC_FAMILY_SITE",
                    "rights_approved_for_public":True,"taxon_reviewed":True,
                    "approval_mode":"OWNER_STANDING_PHOTO_FIRST_POLICY",
                    "policy_ref":"PHOTO_FIRST_PUBLIC_GALLERY_POLICY_2026-11-02",
                    "review_operator":"Hays Botany archived-ZIP visual review and GitHub Actions live-source check",
                    "source_review_evidence":"Live iNaturalist photo ID "+str(pid)+" inside observation "+str(cand["observation_id"])+"; exact photo license "+license_code+" and creator "+creator+" match the source ZIP; SHA-256 "+digest+" verified against original archived bytes at "+created,
                    "taxon_review_evidence":note,
                    "approval_note":"Owner standing photo-first authorization; independently checked image-specific rights/creator, source observation taxon and original checksum; specialist morphology verification deferred.",
                    "creator":creator,"source_page":cand["photo_page"],"source_page_is_exact":True,
                    "license":license_name,"license_url":license_url,
                    "noncommercial_site_use_confirmed":license_code in {"cc-by-nc","cc-by-nc-sa"},
                    "role":cand["role"],"modifications":"No modifications; exact bytes from ZIP original SHA-256 verified against live source.",
                    "sha256":digest}
                destination.with_name(destination.name+".json").write_text(json.dumps(meta,ensure_ascii=False))
                result.update(status="RIGHTS_VERIFIED_READY",license=license_name,creator=creator,sha256=digest)
                report["ready_count"]+=1
            except Exception as exc:
                result.update(status="HELD",reason=str(exc)[:450])
                report["held_candidate_count"]+=1
            report["records"].append(result)
        if report["ready_count"]:
            pub=ROOT/"scripts/publish_approved_family_photos.py"
            args=[sys.executable,str(pub),"--source-root",str(root),"--site-root",str(SITE)]
            check=subprocess.run(args+["--check"],text=True,capture_output=True)
            if check.returncode:raise RuntimeError("PHOTO_PUBLISHER_CHECK_FAILED: "+check.stdout+check.stderr)
            process=subprocess.run(args,text=True,capture_output=True)
            if process.returncode:raise RuntimeError("PHOTO_PUBLISHER_FAILED: "+process.stdout+process.stderr)
            output=json.loads(process.stdout)
            report["published_count"]=output.get("installed",0)
            report["gallery_after"]={"photo_count":output.get("photo_count"),"photo_species":output.get("photo_species")}
            assert report["published_count"]==report["ready_count"]
        report["eligible_unpublished_count"]=report["ready_count"]-report["published_count"]
        REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
        print(json.dumps({"published":report["published_count"],"already_published":report["already_published_count"],
                          "held_from_candidate":report["held_candidate_count"],
                          "contact_sheet_holds":report["not_selected_after_contact_review"]},sort_keys=True),flush=True)
if __name__=="__main__":main()
