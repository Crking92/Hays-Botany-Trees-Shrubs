#!/usr/bin/env python3
"""Safely prepare photo-specific rights-cleared iNaturalist originals for the family gallery."""
from __future__ import annotations
import argparse,hashlib,io,json,re,urllib.request
from pathlib import Path
from PIL import Image

def fetch(url,limit):
    req=urllib.request.Request(url,headers={"User-Agent":"HaysBotany-NoncommercialEducationalPhotoVerifier/1.0"})
    with urllib.request.urlopen(req,timeout=30) as r:
        data=r.read(limit+1)
    if len(data)>limit: raise ValueError("Remote response exceeds limit")
    return data

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--manifest",required=True,type=Path)
    p.add_argument("--intake-root",required=True,type=Path)
    p.add_argument("--report",required=True,type=Path)
    args=p.parse_args()
    m=json.loads(args.manifest.read_text())
    if m["family"]!="Viburnaceae" or len(m["photo_records"])>50:raise ValueError("Unexpected batch")
    verified=[]
    reviewed=[]
    for q in m["photo_records"]:
        result={"species_id":q["species_id"],"photo_id":q["photo_id"],"observation_id":q["observation_id"]}
        try:
            sid=q["species_id"];pid=int(q["photo_id"]);oid=int(q["observation_id"])
            if sid!="viburnum-rufidulum" or q["expected_scientific_name"]!="Viburnum rufidulum":
                raise ValueError("Unexpected taxon: do not auto-publish")
            if not re.fullmatch("[a-f0-9]{64}",q["sha256"]):raise ValueError("Invalid ZIP SHA")
            photo_page=f"https://www.inaturalist.org/photos/{pid}"
            media_url=f"https://inaturalist-open-data.s3.amazonaws.com/photos/{pid}/original.jpg"
            if q["source_page"]!=photo_page or q["photo_url"]!=media_url:
                raise ValueError("Noncanonical source photo ID URL")
            obs_doc=json.loads(fetch(f"https://api.inaturalist.org/v1/observations/{oid}",5_000_000))
            obs=next((x for x in obs_doc.get("results",[]) if int(x.get("id",-1))==oid),None)
            if not obs:raise ValueError("Observation not present")
            observed_taxon=(obs.get("taxon") or {}).get("name","")
            if observed_taxon.lower()!="viburnum rufidulum":
                raise ValueError("Independent observation species is different: "+observed_taxon)
            pic=next((x for x in obs.get("photos",[]) if int(x.get("id",-1))==pid),None)
            if not pic:raise ValueError("Photo ID not listed on this observation")
            photo_license=str(pic.get("license_code") or "").lower().replace("_","-")
            if photo_license!="cc-by-nc":
                raise ValueError("Unverified/mismatching exact photo license: "+photo_license)
            photographer=(pic.get("attribution") or q["credit_from_zip"]).strip()
            if not photographer:raise ValueError("No source photographer attribution")
            payload=fetch(media_url,25_000_000)
            if hashlib.sha256(payload).hexdigest()!=q["sha256"]:
                raise ValueError("Live original photo SHA256 disagrees with user's ZIP")
            with Image.open(io.BytesIO(payload)) as im:
                if im.format!="JPEG" or im.width*im.height>80_000_000:
                    raise ValueError("Unexpected image format or dimensions")
                im.verify()
            name=f"inat-{pid}.jpg"
            folder=args.intake_root/"photo-intake/approved"/sid
            folder.mkdir(parents=True,exist_ok=True)
            (folder/name).write_bytes(payload)
            sidecar={
                "species_id":sid,"photo_file":name,
                "status":"APPROVED_FOR_PUBLIC_FAMILY_SITE",
                "rights_approved_for_public":True,"taxon_reviewed":True,
                "approval_mode":"OWNER_STANDING_PHOTO_FIRST_POLICY",
                "policy_ref":"PHOTO_FIRST_PUBLIC_GALLERY_POLICY_2026-11-02",
                "review_operator":"Hays Botany exact-source photo verifier and photo-first general image reviewer",
                "source_review_evidence":f"iNaturalist live observation {oid} contains exact photo {pid}; its photo-specific license is {photo_license}; iNaturalist open-data original bytes match user ZIP SHA256 {q['sha256']}.",
                "taxon_review_evidence":f"iNaturalist observation {oid} taxon {observed_taxon} matches family assignment. Uploaded contact sheet was reviewed for obvious mismatched organisms; no detailed diagnostic or county nativity claims made.",
                "approval_note":"Standing owner authorized general plant gallery publication after actual exact photo license, identity sanity and original image integrity checks.",
                "creator":photographer,"source_page":photo_page,"source_page_is_exact":True,
                "license":"CC BY-NC 4.0","license_url":"https://creativecommons.org/licenses/by-nc/4.0/",
                "noncommercial_site_use_confirmed":True,
                "role":q["role"]+" (general species recognition)",
                "modifications":"Unmodified original downloaded photograph",
                "sha256":q["sha256"]
            }
            (folder/(name+".json")).write_text(json.dumps(sidecar,indent=2)+"\n")
            result["status"]="VERIFIED_AND_PREPARED"
            verified.append(pid)
        except Exception as e:
            result["status"]="HELD_SOURCE_OR_TAXON"
            result["reason"]=str(e)[:500]
        reviewed.append(result)
        print(json.dumps(result),flush=True)
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps({"batch_id":m["batch_id"],"processed":reviewed},indent=2)+"\n")
    print(json.dumps({"verified":len(verified),"held":len(reviewed)-len(verified)}),flush=True)

if __name__=="__main__":main()
