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
