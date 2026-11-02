# Hays Botany — Trees & Shrubs

**Historical source transfer complete; public family learner active. PHOTO-FIRST gallery enrichment is now the active user priority (November 2, 2026): publish credited, source-verified general photos before anatomy arrows.**

[Open the family Visual Learner](https://crking92.github.io/Hays-Botany-Trees-Shrubs/site/) · [Original read-only Hays Botany hub](https://crking92.github.io/Hays-County-Botany/) · [Current botanical write routing](https://github.com/Crking92/Hays-County-Botany/blob/main/workflow/ACTIVE_NEW_PLANT_WRITE_ROUTING_20261028.json)

This collection contains **133 existing species lessons across 36 assigned families**. Its complete original scientific/photo source is preserved on branch [`staging/original-source-transfer`](https://github.com/Crking92/Hays-Botany-Trees-Shrubs/tree/staging/original-source-transfer), whereas its photo-backed public learner lives under `main/site`. New botanical edits go to the approved family branch, not to the legacy hub.

## Current photo-first operating direction — November 2, 2026

Read [photo-first publication policy](workflow/PHOTO_FIRST_PUBLIC_GALLERY_POLICY_2026-11-02.md) before family photo batches. [Paste-ready ChatGPT Project instructions](workflow/CHATGPT_PROJECT_PHOTO_FIRST_INSTRUCTIONS_2026-11-02.md) are included for alignment across chats. The user prioritizes multiple useful general views per species **without waiting for arrows or finished anatomy lessons**. The public site currently has **108 photos across 52 photographed species** after the first separately credited November 2 general-photo addition; these counts change as photo batches are installed.

The Trees & Shrubs automatic photo publisher now supports two honestly documented review modes: the original named-human source/taxon approval, or the owner-standing photo-first policy with actual photo-specific source and identity evidence. **Neither mode allows invented proof or uncertain image rights.** The publisher also accepts CC BY-NC and CC BY-NC-SA only when each photo confirms noncommercial site use; the site clearly labels NC restrictions. Exact-photo rights/ID review and GitHub Pages QA remain required. An eligible general image need not show anatomy or have arrows. Preserve the historical audit counts below as an October migration snapshot, not today's site totals.

## Migration-only source/file results — October 30, 2026

- **790/790 original files** match their destination's Git blob SHA in the transferred source manifest; **0 missing and 0 changed bytes**.
- Original content: **470 text/source-credit files and 320 original photograph binaries**.
- Existing public learner: **133 species lesson files and 107 hosted public-gallery photographs across 51 species**.
- **246/353 original image metadata references remain excluded from the public gallery** pending individual source, license or permissions review. Those held references do **not** indicate incomplete source-file transfer.
- All `staging/*` and historical photo-hold branches are accessible while the repository is PUBLIC, even if the Pages photo gallery filters held pictures. Do not add any new license-uncertain files, and do not delete or rewrite original source/history as an unapproved workaround.
- Obsolete text-only publish workflows intentionally refuse to overwrite the existing photo-backed family site; do not bypass them.

[Source manifest](https://github.com/Crking92/Hays-Botany-Trees-Shrubs/blob/staging/original-source-transfer/migration/original-source-transfer-manifest.json) · [Existing photo release report](site/photo-source-migration-report.json) · [Migration audit checkpoint](migration/TREES_SHRUBS_TRANSFER_QA_20261030.md)

## Verification and next phases

`python3 scripts/verify_existing_site.py` checks all species JSON, exact public media bytes vs recorded Git source SHA, source/license credits and gallery indexes. [Automated public Pages QA](.github/workflows/verify-existing-site-gallery.yml) adds per-file live HTTP checks; count live readiness as passed only if that GitHub Action succeeds. Blank inherited anatomy lesson fields are recorded as deferred content enrichment, not fabricated during migration.

No new imagery, plant additions, photo permissions changes, hub edits, automation restarts, or navigation cutover are authorized by the source migration. Future plant writes follow the hub's active family write registry.
