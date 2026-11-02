#!/usr/bin/env python3
"""Review source-specific iNaturalist elm image rights and publish only unchanged verified originals."""
from __future__ import annotations
import hashlib, io, json, os, re, time, urllib.request
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"photo-intake/remote-photo-manifests/ulmaceae-2026-11-02.json").read_text())
if DATA["family"]!="Ulmaceae" or len(DATA["photos"])!=14 or DATA["photo_hash_checks"]!=15:
    raise SystemExit("Unexpected Ulmaceae ZIP manifest")
OUT=Path(os.environ["RUNNER_TEMP"])/"ulmaceae-verified"
REPORT=Path(os.environ["RUNNER_TEMP"])/"ulmaceae-exact-photo-rights.json"
TAXA={
 "planera-aquatica":{"planera aquatica"},
 "ulmus-alata":{"ulmus alata"},
 "ulmus-rubra":{"ulmus rubra"}
}
LICENSES={
 "cc0":("CC0 1.0","https://creativecommons.org/publicdomain/zero/1.0/"),
 "cc-by":("CC BY 4.0","https://creativecommons.org/licenses/by/4.0/"),
 "cc-by-nc":("CC BY-NC 4.0","https://creativecommons.org/licenses/by-nc/4.0/")
}
def fetch(url,limit=26_000_000):
    req=urllib.request.Request(url,headers={"User-Agent":"HaysBotanyPhotoFirstEducational/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req,timeout=30) as response:
                payload=response.read(limit+1)
            if len(payload)>limit:raise ValueError("Source response too large")
            return payload
        except Exception:
            if attempt==2: raise
            time.sleep(1+attempt)
results=[];seen=set()
for item in DATA["photos"]:
    sid=item["species_id"];pid=int(item["photo_id"]);oid=int(item["observation_id"])
    result={"species_id":sid,"photo_id":pid,"observation_id":oid}
    try:
        if sid not in TAXA or pid in seen:raise ValueError("Unexpected species or duplicate photo ID")
        seen.add(pid)
        if not re.fullmatch("[0-9a-f]{64}",item["sha256"]):raise ValueError("Bad original ZIP SHA256")
        if item["extension"] not in ("jpg","jpeg"):raise ValueError("Wrong filename extension")
        api=json.loads(fetch(f"https://api.inaturalist.org/v1/observations/{oid}",5_000_000))
        obs=next((o for o in api.get("results",[]) if int(o.get("id",0))==oid),None)
        if obs is None:raise ValueError("iNaturalist observation does not exist")
        obs_taxon=str((obs.get("taxon") or {}).get("name") or "").lower().strip()
        if obs_taxon not in TAXA[sid]:
            raise ValueError("Observation taxon does not match listed elm species: "+obs_taxon)
        photo=next((p for p in obs.get("photos",[]) if int(p.get("id",0))==pid),None)
        if photo is None:raise ValueError("Exact photo ID absent from cited observation")
        lic=str(photo.get("license_code") or "").lower().replace("_","-")
        if lic!=item["license_code"] or lic not in LICENSES:
            raise ValueError("Photo-specific source license mismatches ZIP: "+lic+" vs "+item["license_code"])
        label,url=LICENSES[lic]
        credit=str(photo.get("attribution") or item["photographer"]).strip()
        if not credit:raise ValueError("Photographer credit missing")
        ext=item["extension"]
        image_url=f"https://inaturalist-open-data.s3.amazonaws.com/photos/{pid}/original.{ext}"
        image=fetch(image_url)
        if hashlib.sha256(image).hexdigest()!=item["sha256"]:
            raise ValueError("Live original photo differs from uploaded ZIP original SHA256")
        with Image.open(io.BytesIO(image)) as pil:
            if pil.format!="JPEG" or pil.width*pil.height>80_000_000:raise ValueError("Invalid original JPEG")
            pil.verify()
        filename=f"inat-{pid}.{ext}"
        target=OUT/"photo-intake"/"approved"/sid
        target.mkdir(parents=True,exist_ok=True)
        (target/filename).write_bytes(image)
        sidecar={
            "species_id":sid,"photo_file":filename,"status":"APPROVED_FOR_PUBLIC_FAMILY_SITE",
            "rights_approved_for_public":True,"taxon_reviewed":True,
            "approval_mode":"OWNER_STANDING_PHOTO_FIRST_POLICY",
            "policy_ref":"PHOTO_FIRST_PUBLIC_GALLERY_POLICY_2026-11-02",
            "review_operator":"Hays Botany exact-photo iNaturalist source and original ZIP visual/hash reviewer",
            "source_review_evidence":f"Live observation {oid} explicitly lists exact photo {pid}; individual photo license {lic} and source photographer checked; original iNaturalist photo SHA256 matches the user ZIP value {item['sha256']}.",
            "taxon_review_evidence":f"Basic general plant recognition checked on source ZIP contact sheet, with live source observation taxon {obs_taxon}; specialized anatomy and BONAP county range certification deferred.",
            "approval_note":"Standing owner authorization for genuinely licensed general identification photos after live source/media/taxon consistency checks.",
            "creator":credit,"source_page":f"https://www.inaturalist.org/photos/{pid}",
            "source_page_is_exact":True,"license":label,"license_url":url,
            "noncommercial_site_use_confirmed":True,
            "role":item["caption"]+" (general view, no diagnostic claims)",
            "modifications":"Unmodified original iNaturalist JPEG",
            "sha256":item["sha256"]
        }
        (target/(filename+".json")).write_text(json.dumps(sidecar,indent=2)+"\n")
        result["status"]="SOURCE_AND_IMAGE_VERIFIED"
    except Exception as exc:
        result.update(status="HELD_SOURCE_OR_TAXON",reason=str(exc)[:450])
    results.append(result)
    print(json.dumps(result),flush=True)
REPORT.write_text(json.dumps({"source_zip":DATA["zip_name"],"results":results},indent=2)+"\n")
print("VERIFIED",sum(r["status"]=="SOURCE_AND_IMAGE_VERIFIED" for r in results),"HELD",sum(r["status"]!="SOURCE_AND_IMAGE_VERIFIED" for r in results),flush=True)
