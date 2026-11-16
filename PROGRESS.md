# Progress checklist

Use this list to resume if the session is interrupted. Each research workstream writes to `data/staging/<workstream>/`. Its own `progress.md` there lists entities done, pending and dropped.

## Step 0: rule
- [x] Read DFARS 252.225-7052 / 225.7018 (final rule 89 FR 46814, 30 May 2024)
- [x] Read 10 U.S.C. 4872 as amended by FY2026 NDAA (Pub. L. 119-60 secs. 843, 844, 848)
- [x] Class Deviation 2026-O0041 Rev 1 / DFARS 252.225-7961 (JUN 2026). Read via law-firm summaries; the DoD site was unreachable
- [x] Executive Order 14415 (20 Jul 2026)
- [x] Delays, waivers and amendments: House FY2027 NDAA sec. 1803 (pending), H.R. 9073 (pending), no official delay found
- [x] docs/scope.md written; docs/decisions.md started

## Infrastructure
- [x] tools/schema.py, tools/validate.py, tools/append_rows.py, tools/agent_brief.md
- [x] tools/build.py (merge to CSV + XLSX), tools/stats.py, tools/sample_for_verification.py, tools/verify_brief.md
- [x] Independent award cross-check list: data/staging/verification/award_crosscheck.md

## Research workstreams (parallel agents)
- [x] tungsten (`data/staging/tungsten`): 78 rows (incl. coordinator gap-fill: EQR Mt Carbine, Tungsten Mining Watershed, Tungsten Heavy Powder), 29 excluded, 13 offtakes. Gaps: search budget ran out after ~45 searches; Pasto Bueno (Peru), Uzbekistan, Brazil, Mongolia not verified; ownership of several Asian RMI-listed smelters unverified
- [x] tantalum (`data/staging/tantalum`): 57 rows, 25 excluded, 9 offtakes. Gaps: search budget ran out early; Kenticha (Ethiopia), Noventa (Mozambique), Kyocera AVX not covered; GAM ultimate owner unresolved; Telex, PowerX unverified
- [x] NdFeB upstream (`data/staging/ndfeb_upstream`): 66 rows (37 mining, 29 separation), 16 excluded, 38 offtakes. Gaps: search budget ran out after ~15 searches; Solvay, REEtec, Pensana thinly verified; Vietnam, Madagascar, Thailand, Nigeria producers not researched
- [x] NdFeB downstream (`data/staging/ndfeb_downstream`): 65 rows, 16 excluded, 39 offtakes. Gaps: no non-China ferroboron producer verified; Star Group, JS Link (Korea), India REPM awardees, Santoku, Resonac not verified
- [x] SmCo + cobalt (`data/staging/smco_cobalt`): 17 smco + 35 cobalt rows, 19 excluded, 13 offtakes. Coordinator added IREL REPM SmCo plant and 3 Chinese SmCo screening entries. Gaps: search budget ran out; no SmCo recyclers found; Shin-Etsu/Proterial/TOKIN SmCo status unconfirmed; ERG, Ambatovy, Nornickel Harjavalta not verified
- [x] molybdenum (`data/staging/molybdenum`): 63 rows, 13 excluded, 9 offtakes. Gaps: search budget ran out early (many rows checked against company/regulator pages only); Kazakhstan, Australia, South Korea producers and Korean FeMo makers not identified; Gulf Chemical & Metallurgical, Hudbay Constancia, Montana Resources unverified
- [x] gallium + germanium (`data/staging/gallium_germanium`): 48 rows (27 Ga, 21 Ge), 20 excluded, 11 offtakes. Gaps: search budget ran out mid-way; China US-export-ban suspension status after 27 Nov 2026 unconfirmed; start-up status of Alcoa/Atalco/ERG gallium plants unconfirmed
- [x] traders/stockholders/DLA + labs (`data/staging/traders_labs`): 58 rows (32 trader, 26 lab), 14 offtakes. Gap: per-agent web-search budget ran out, so several rows were checked against company sites only (medium/low confidence); not included: Mitsui, Hanwa, Mitsubishi RtM, Sumitomo Corp, Marubeni, Intertek, SGS (own row), BGR, RCS Global

## Verification and outputs
- [ ] Verification pass: re-check a sample of rows per chain against sources (`data/staging/verification`)
- [ ] Apply verification fixes
- [ ] Build data/suppliers.csv, offtakes.csv, excluded.csv, sources.csv
- [ ] Build suppliers.xlsx (one tab per chain plus offtakes, excluded, sources)
- [ ] REPORT.md (per-chain analysis, gaps, completeness checks)
- [ ] docs/method.md, README.md
- [ ] Final commit and push
