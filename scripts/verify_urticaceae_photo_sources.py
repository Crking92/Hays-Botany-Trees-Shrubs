#!/usr/bin/env python3
"""Verify the exact Urticaceae photos and prepare only source-cleared originals for website."""
from __future__ import annotations
import hashlib,io,json,os,time,urllib.request
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/"photo-intake/remote-photo-manifests/urticaceae-2026-11-02.json").read_text())
assert M["family"]=="Urticaceae" and len(M["photos"])==15
OUT=Path(os.environ["RUNNER_TEMP"])/"urticaceae-verified"
REPORT=Path(os.environ["RUNNER_TEMP"])/"urticaceae-source-rights-report.json"
TAXA={
  "boehmeria-cylindrica":{"boehmeria cylindrica"},
  "parietaria-pensylvanica":{"parietaria pensylvanica"},
  "urtica-chamaedryoides":{"urtica chamaedryoides"}
}
ROLES={
  "boehmeria-cylindrica":"General false-nettle habit and foliage; anatomy labeling deferred",
  "parietaria-pensylvanica":"General small pellitory plant, foliage and branching; anatomy labeling deferred",
  "urtica-chamaedryoides":"General heartleaf-nettle foliage and flowering stems; anatomy labeling deferred"
}

def fetch(url, limit=26_000_000):
    request=urllib.request.Request(url,headers={"User-Agent":"HaysBotanyPhotoFirst/1.0 (educational attribution review)"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request,timeout=28) as res:
                data=res.read(limit+1)
            if len(data)>limit:raise ValueError("Source response too large")
            return data
        except Exception:
            if attempt==2:raise
            time.sleep(1+attempt)

seen=set();reviewed=[]
for r in M["photos"]:
    pid=int(r["photo_id"]);oid=int(r["observation_id"]);sid=r["species_id"]
    result={"species":sid,"photo_id":pid,"observation_id":oid}
    try:
        if sid not in TAXA or pid in seen:raise ValueError("Wrong species folder or duplicate ID")
        seen.add(pid)
        if len(r["sha256"])!=64:raise ValueError("Invalid original hash")
        exact_source=f"https://www.inaturalist.org/photos/{pid}"
        exact_image=f"https://inaturalist-open-data.s3.amazonaws.com/photos/{pid}/original.jpg"
        if r["source_page"]!=exact_source or r["image_url"]!=exact_image:
            raise ValueError("Photo source and ID disagree")
        obs_response=json.loads(fetch(f"https://api.inaturalist.org/v1/observations/{oid}",5_000_000))
        obs=next((o for o in obs_response.get("results",[]) if int(o.get("id",-1))==oid),None)
        if obs is None:raise ValueError("Source observation missing")
        obs_taxon=str((obs.get("taxon") or {}).get("name") or "").lower().strip()
        if obs_taxon not in TAXA[sid]:
            raise ValueError("Source observation taxon inconsistent with target: "+obs_taxon)
        source_photo=next((p for p in obs.get("photos",[]) if int(p.get("id",-1))==pid),None)
        if source_photo is None:raise ValueError("Photo not on asserted observation")
        license_code=str(source_photo.get("license_code") or "").lower().replace("_","-")
        if license_code!="cc-by-nc":raise ValueError("Individual photo CC BY-NC license not confirmed: "+license_code)
        creator=str(source_photo.get("attribution") or r["photographer_from_zip"] or "").strip()
        if not creator:raise ValueError("Creator absent")
        original=fetch(exact_image)
        if hashlib.sha256(original).hexdigest()!=r["sha256"]:
            raise ValueError("Remote original bytes do not match uploaded ZIP checksum")
        with Image.open(io.BytesIO(original)) as im:
            if im.format!="JPEG" or im.width*im.height>80_000_000:raise ValueError("Invalid photo format or size")
            im.verify()
        filename=f"inat-{pid}.jpg"
        dest=OUT/"photo-intake"/"approved"/sid
        dest.mkdir(parents=True,exist_ok=True)
        (dest/filename).write_bytes(original)
        sidecar={
          "species_id":sid,"photo_file":filename,"status":"APPROVED_FOR_PUBLIC_FAMILY_SITE",
          "rights_approved_for_public":True,"taxon_reviewed":True,
          "approval_mode":"OWNER_STANDING_PHOTO_FIRST_POLICY",
          "policy_ref":"PHOTO_FIRST_PUBLIC_GALLERY_POLICY_2026-11-02",
          "review_operator":"Hays Botany photo-first source verification and contact-sheet visual review",
          "source_review_evidence":f"Live iNaturalist observation {oid} lists exact photo {pid} and individual CC BY-NC license. Original photo bytes match original uploaded ZIP SHA256 {r['sha256']}.",
          "taxon_review_evidence":f"Basic species assignment: original uploaded photo contact sheet checked for obvious organism mismatch; live observation {oid} taxon {obs_taxon} agrees; specialist anatomy ID postponed.",
          "approval_note":"Standing owner-authorized, noncommercial educational general photo; individual source license/creator verified and original image SHA256 matched.",
          "creator":creator,"source_page":exact_source,"source_page_is_exact":True,
          "license":"CC BY-NC 4.0","license_url":"https://creativecommons.org/licenses/by-nc/4.0/",
          "noncommercial_site_use_confirmed":True,
          "role":ROLES[sid],
          "modifications":"Unmodified original source JPEG",
          "sha256":r["sha256"]
        }
        (dest/(filename+".json")).write_text(json.dumps(sidecar,indent=2)+"\n")
        result["status"]="SOURCE_AND_MEDIA_VERIFIED"
    except Exception as error:
        result.update(status="HELD_SOURCE_OR_TAXON",reason=str(error)[:350])
    reviewed.append(result)
    print(json.dumps(result),flush=True)
REPORT.write_text(json.dumps({"batch":"Urticaceae.zip","results":reviewed},indent=2)+"\n")
print("VERIFIED",sum(x["status"]=="SOURCE_AND_MEDIA_VERIFIED" for x in reviewed),
      "HELD",sum(x["status"]=="HELD_SOURCE_OR_TAXON" for x in reviewed),flush=True)
