# Vitaceae existing-assets review — 2026-11-02

**Scope:** All nine Vitaceae species in the Hays Botany Trees & Shrubs collection. This is a non-publishing photo and anatomical-gap reconciliation. It does not authorize public media publication, mark taxon identity verified, or change BONAP/native status.

## Inventory verified

- **9 indexed species** in `main/site/data/collection-index.json`.
- **11 presently published photo references** in the nine family-site cards: Ampelopsis cordata 1, Cissus trifoliata 3, Nekemias arborea 0, Parthenocissus heptaphylla 0, Parthenocissus quinquefolia 0, Vitis berlandieri 1, V. cinerea 2, V. mustangensis 3, V. palmata 1.
- **50 historical image metadata entries** in those nine species records on `staging/original-source-transfer`. Their source-image bytes were covered by the collection's October 30 preservation ledger; not all 50 are cleared for public reuse.
- **15 newly supplied general photos** across Nekemias arborea, Parthenocissus heptaphylla and P. quinquefolia (five each); recorded license distribution 12 CC BY-NC 4.0, 3 CC BY.
- **18 additional targeted images** in uploaded `Vitaceae(2).zip`: 17 recorded CC BY and one recorded CC0. Exact ZIP SHA-256 values matched the bundled metadata; none of these 18 is an exact byte duplicate of the 15 earlier uploaded images.
- All 33 downloaded images remain **review candidates**, not approved GitHub media. No current live source-page identity/license check was completed for those 18 iNaturalist photo IDs; observation annotations alone do not certify what a photograph depicts.
- The master Google Sheet `Hays_Botany_ID_Master_Curation_Tracker`, tab `Photo Needs Queue`, has **24 Vitaceae structure-specific entries**. https://docs.google.com/spreadsheets/d/15dcpbk3msvOiGtAo2GRQkCfdhBR9iav-yQ0HoTjS6wM/edit#gid=1187574813

## Targeted photo screening: 18 images

**10 useful anatomical candidates (not yet approved):**
- **Nekemias arborea:** flower/inflorescence: [724273064](https://www.inaturalist.org/photos/724273064) and [753121004](https://www.inaturalist.org/photos/753121004); developing fruit: [716973706](https://www.inaturalist.org/photos/716973706), mixed ripening fruit [720460847](https://www.inaturalist.org/photos/720460847), and ripe fruit [739046379](https://www.inaturalist.org/photos/739046379). These add different visual stages; approve only after source photo and taxon comparison.
- **Parthenocissus heptaphylla:** ripe fruit [156748081](https://www.inaturalist.org/photos/156748081), developing fruit [388812413](https://www.inaturalist.org/photos/388812413).
- **Parthenocissus quinquefolia:** reproductive inflorescence [296131856](https://www.inaturalist.org/photos/296131856), buds/small flowers [520982231](https://www.inaturalist.org/photos/520982231), ripe berry cluster [743154330](https://www.inaturalist.org/photos/743154330).

**2 need closer taxon/structure review:** P. heptaphylla [656078246](https://www.inaturalist.org/photos/656078246) appears to include ambiguous buds/young fruit; P. quinquefolia [367568232](https://www.inaturalist.org/photos/367568232) is recorded as CC0 and shows open small star-shaped flowers but exact taxon determination has not been independently confirmed.

**6 do not satisfy their requested anatomy target:** N. arborea [438987057](https://www.inaturalist.org/photos/438987057) shows a different plant's pink flower (reject as Nekemias flower); P. heptaphylla [722465127](https://www.inaturalist.org/photos/722465127), [756421698](https://www.inaturalist.org/photos/756421698), [756555994](https://www.inaturalist.org/photos/756555994) are foliage/vine, not flowers (possible foliage roles only); P. quinquefolia [597856719](https://www.inaturalist.org/photos/597856719) is foliage-only and [678834341](https://www.inaturalist.org/photos/678834341) has off-target/unverified plant identity for fruit evidence.

## Species-by-species remaining photograph review

| Species | Current public photos | Next steps from existing materials | Unresolved photographic target / hold |
| --- | ---: | --- | --- |
| Ampelopsis cordata | 1 | Inspect seven historical source photo records, including a CC0 GBIF occurrence and six other views; do not infer their anatomy from filenames. | Same-shoot continuous white stem pith cut surface; tendril/inflorescence attachment opposite leaf |
| Cissus trifoliata | 3 | Review three existing Texas Commons views and five held historic candidates for distinct structures. | Unbranched tendril, swollen or warty red node, mature fruit cluster |
| Nekemias arborea | 0 | Reconcile five general download images, five strong targeted flower/fruit images, and one older CC BY-NC recognition image. | Mature multiply-compound leaf and tendril attachment |
| Parthenocissus heptaphylla | 0 | Compare five general images, two strong fruit candidates and one historical CC BY recognition image. Do not falsely classify the three foliage-only “flower” downloads. | Verified open flower macro; tendril branching/attachment |
| Parthenocissus quinquefolia | 0 | Compare five general images with three strong new flower/fruit candidates; separately verify the original Cornell Commons CC BY 2.0 habit photo and the CC0 flower candidate before deciding to publish. | Adhesive tendril pads; specimen-level flower/fruit confirmation |
| Vitis berlandieri | 1 | Compare all eight historical photo records, including documented Texas photo and leaf-underside reference, before new download. | Compact heavily glaucous mature cluster; distinct node/branchlet character |
| Vitis cinerea | 2 | Compare eight historical records under strict taxon-concept caution; a CC0 museum image is present in source notes but anatomy and taxon determination are not certified. | **TAXONOMY HOLD**: strict cinerea-vs-berlandieri comparison. Do not label it locally native or collect blind |
| Vitis mustangensis | 3 | Compare existing three gallery views and five historical held photos first. | True densely white/rusty tomentose mature leaf underside macro, fruit size/scale |
| Vitis palmata | 1 | Inspect two earlier USDA public-domain references among eight original source records before requesting images. | Red-purple branchlets with attached lobed leaves; glabrous leaf underside; possible ripe fruit |

## One independently confirmed external license record

The original *Parthenocissus quinquefolia* habit photograph on Wikimedia Commons — NY State IPM Program at Cornell University — lists **CC BY 2.0**, and Commons records an archival Flickr license check. Exact source: https://commons.wikimedia.org/wiki/File:Parthenocissus_quinquefolia_-_whole_plant%2C_stem_(19063471491).jpg. The stage archive contains source image bytes under `migration/private-original-photo-holds/Vitaceae/Parthenocissus/parthenocissus-quinquefolia/images/commons-parthenocissus-quinquefolia.jpg`; current staged Git blob SHA `ae4a244f5f4d5a4cd75b76e15b15094771990a34`. This is a **good priority for dedicated public-intake approval**, but the existing pipeline's human-attributed taxon/rights approval and release testing still apply. Do not silently bypass this gate.

## Release gates / next work

1. Compare the selected image bytes/hash and iNaturalist photo IDs against existing site image hashes and historical source images, to avoid duplicate photographs under different names.
2. Independently verify exact photo-page image license, creator, and observation identification for any proposed published source; reject mixed-species images as diagnostic proof.
3. Obtain specific review approval for selected photographs through the repository's `photo-intake/approved/<species-id>/...` sidecar workflow, which requires human approver and matching metadata. **Never fill approval flags or a reviewer's name without the actual review.**
4. Build and validate the image/credit entries and galleries for all nine species. Confirm Pages photo visibility and correct anatomy descriptions after any approval.
5. Keep missing-photo requests in the shared master tracker. Do not scrape more generic Vitaceae until these image candidates and historic archives are reconciled.

**Repo boundaries:** Future Vitaceae source work belongs in `Crking92/Hays-Botany-Trees-Shrubs` on `staging/original-source-transfer`. Legacy Hays-County-Botany is read-only. No public release, visibility change, auto-resumption or source photo deletion is authorized by this review.

## Follow-on pixel-level archive review (same date)

The following existing **actual image files** were opened from the assigned family's staged hold archive or published media paths. This corrects any earlier speculative assumption that these morphological structures were absent merely because captions were vague:

- **Ampelopsis cordata:** Existing released Commons shot visually shows simple leaves and fruit at multiple ripeness stages. The archived source-record CC0 GBIF photo shows a clear, toothed, simple leaf, not a cut white-pith stem. Therefore the decisive white-pith photographic gap remains.
- **Cissus trifoliata:** Public Texas `cissus-trifoliata-texas-node-3.jpg` shows a trifoliolate leaf with chunky leaflet margins alongside a reddish shoot. It does *not* clearly isolate the decisive unbranched tendril or measure a swollen node.
- **Parthenocissus heptaphylla:** Archived exact-source photo `inat-82833009.jpg` shows an attached mature palmate compound leaf clearly; retain as foliar evidence after exact-image source and identity review. Do not recollect generic leaves for this species.
- **Parthenocissus quinquefolia:** Cornell source image visually depicts a recognizable five-leaflet foliage and spreading habit, not flower anatomy, ripened fruit or adhesive disks. Wikimedia Commons independently labels this specific image CC BY 2.0.
- **Vitis berlandieri:** Original `vitis-berlandieri-texas-second-view.jpg` illustrates climbing habit on a large tree, not diagnostic node hairs. Archived `vitis-berlandieri-leaf-underside.jpg` is a useful clear macro of visible blade tissue and sparse hairs (cultivated French reference, not a Hays County voucher), but source/rights review is still required before any newly published entry.
- **Vitis cinerea:** Archived USDA `vitis-cinerea-usda-leaf.jpg` demonstrates the pale/gray-green lower leaf surface and node architecture; this does NOT resolve strict `V. cinerea` taxonomic identity or Hays target-range status.
- **Vitis mustangensis:** **Correction** — the *currently published* `site/media/vitis-mustangensis/vitis-mustangensis-north-texas-leaves.jpg` already gives an excellent close view of the densely white-woolly leaf underside against the upper green leaf. Do **not** request another generic underside image unless a measured finer macro is demonstrably necessary. The master queue was updated accordingly.
- **Vitis palmata:** Two archived USDA `vitis-palmata-usda-leaf.jpg` and `vitis-palmata-usda-plant.jpg` show entire deeply lobed leaves well. Neither alone documents diagnostic red-purple young branchlets, a near-glabrous leaf underside macro, or ripe fruit.

**Status:** The actual images support improving a few existing photo roles now, and leaving a much narrower list of true missing structures. This was a spot inspection of 11 historical image files across the collection, **not** a claim that all 50 original photo records were opened or that every source license was revalidated.

## Continuation: restored anatomical roles and structured 18-photo queue (2026-11-02)

- Saved a machine-readable photo-by-photo review index at `photo-intake/reviews/VITACEAE_TARGETED_18_CANDIDATES_2026-11-02.json`, retaining all 18 targeted iNaturalist photo IDs and original screening decisions (**10 useful anatomical candidates, 2 ambiguous, 6 off-target**). Original photo bytes/ZIP creator metadata are **not** embedded in this JSON; neither that file nor the queue is an installed gallery.
- Corrected preexisting archived-photo `images[].role` descriptions in the **staging** species cards for *Ampelopsis cordata* (GBIF leaf), *Cissus trifoliata* (Texas shoot), *Parthenocissus heptaphylla* (palmately compound mature leaf), *Vitis cinerea* (USDA leaf/node with taxonomic hold), and *Vitis mustangensis* (existing verified visible woolly underside). The edits remove misleading role gaps while retaining source, rights and review cautions.
- Added the verified exact **source-page** CC BY 2.0 license and Cornell credit evidence to the archived *Parthenocissus quinquefolia* species-image record. The source page notes Flickr license verification in 2021. This does **not** independently match original photo bytes or serve as a human approval.
- No new photographs were installed/published in this continuation; no review gate, deployment config, taxon/range exception, or original hub file was changed. All 18 photo candidates remain unapproved.
- iNaturalist photo pages were inaccessible to the current live browsing environment; therefore photographer names, exact per-photo license and species determinations were **not** marked verified from the original ZIP alone. The raw ZIP/review packet from the previous chat was not available as a mounted file in this continuation. Resume per-photo review from saved IDs and original ZIP or direct exact-photo source rather than running a generic repeat download.

## Uploaded original general ZIP (Vitaceae(3).zip) reopened 2026-11-02

The user supplied the 15-image general photo batch again as `Vitaceae(3).zip`. This **is the earlier-described five-per-species general-foliage cohort**, not a new 15-image increment and not the separate 18-image targeted flower/fruit batch.

- Original ZIP SHA-256: `01d577cd4541067a49a81941ba3e66c7b25081db4d427e327ccb0b5b729c3e9c`. The 15 individual original JPEG bytes each matched the SHA-256 values in their bundled metadata; 15 unique photo IDs and 15 unique hashes. Metadata lists **12 CC BY-NC 4.0 and 3 CC BY 4.0**. Every source has bundled creator/source/credit text, but live exact iNaturalist pages did not load in the verification browser, so these are metadata claims, not current source/rights certification.
- **New enduring machine-readable manifest:** `photo-intake/reviews/VITACEAE_GENERAL_15_BATCH3_REVIEW_2026-11-02.json`, with per-photo byte hashes, original observation/photo URLs, photographer, recorded license, targeted image role, visual screening and publication holds. The JSON saves the source reference but is **not** a backup of actual original image bytes.
- *Nekemias arborea* (5): all show young red or developing foliage, not definitive fully mature compound leaves, flowers, fruit or tendril attachment. Visual review favors photo IDs **630253122** and **631869548** for complementary juvenile leaf appearance; do not use them as adult-leaf proofs.
- *Parthenocissus heptaphylla* (5): **627601615** and **627737702** are strong narrow-leaflet, palmately compound foliage/scale candidates. **630290210** shows broader, five-parted foliage resembling *P. quinquefolia* and requires independent specimen identification before it is used for species-specific diagnosis. No flowers or tendril attachment macro in the five.
- *Parthenocissus quinquefolia* (5): **628590373** shows a well-defined five-leaflet compound leaf; **629130091** supports climbing/habit appearance. No clearly resolved adhesive tendril disks, flower or berry close-ups.
- These photographs are mostly recognition/foliage rather than the currently important reproductive and vine-attachment targets. Continue to prioritize the 10 promising images within the prior **18-photo targeted batch**, original archived photos, and then truly missing structure shots. Do not recollect duplicate general foliage just to add gallery quantity.
- The existing Google Sheet `Photo Needs Queue` was edited in place, specifically rows **2, 3, 6, 7, 10** (status/evidence/next actions). No new Sheet, species, or queue rows were created. No new image bytes were written to the public repository, no public Pages deployment occurred, and none of the new candidates was marked human-approved.

## General-gallery publication update — 2026-11-02

The repository owner clarified that several useful **general recognition / habit photos per plant are welcome without anatomy arrows**; labels and fine-scale diagnostic photos can follow later. This instruction is authorization to install eligible photographs but does not alter source license, identity, attribution, and public-rights requirements. Current site publisher allows public CC0/CC BY/CC BY-SA sources and **does not permit CC BY-NC** without an intentional policy change.

**Installed and verified in `main` site:** The prior archive's Cornell `Parthenocissus quinquefolia` photo was moved as the same unchanged Git blob `ae4a244f5f4d5a4cd75b76e15b15094771990a34` from staged historical holdings to `site/media/parthenocissus-quinquefolia/commons-parthenocissus-quinquefolia.jpg`. Exact Wikimedia Commons page documents Cornell IPM creator and CC BY 2.0; general-vine role and clear source/license links were set in `site/data/species/parthenocissus-quinquefolia.json`. User requested publication of eligible general plant photographs in this chat. Live `main` website data and new image blob verified by readback, commit `464394789a4ece50e6dddb469b166dad3b9c096c`. Gallery index updated from 107 to **108** photos, 51 to **52** species. GitHub Pages cache/browser display was not independently verified.

**ZIP4 intake:** Reopened original `Vitaceae(4).zip` (SHA-256 `9dd86fb02a18e4e3422e76cb7c29411e8704696321edafa2af1f3feda7ef82f5`) and checked all **18/18** original image bytes against bundled SHA-256 values, with no mismatch, photo IDs all unique, license codes 17 `cc-by` and one `cc0`. These are the **same targeted 18** already in `VITACEAE_TARGETED_18_CANDIDATES_2026-11-02.json`; do not double count. Exact live iNaturalist photo-page metadata could not be retrieved this session, so no ZIP4 photograph was human/taxon/source verified for publication and none was added to site; retain 10 strong, 2 ambiguous, 6 off-target screening decisions.

**Next focus:** Use prior existing source images and selected 10 ZIP4 strong candidates for named human exact-photo approval, and then run the already installed `photo-intake/approved/<species-id>/...` publisher pipeline. For the ZIP3 cohort (15 photos), only three are recorded CC BY 4.0 and 12 are recorded CC BY-NC; uploader metadata alone does not establish actual current source rights. Do not relabel off-target flowers or broad-leaf heptaphylla identity hold. General recognition photos are desirable but do not bypass the current website publisher's NC-license exclusion or source/identity checks.
