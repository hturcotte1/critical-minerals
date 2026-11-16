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
- [ ] tungsten (`data/staging/tungsten`)
- [ ] tantalum (`data/staging/tantalum`)
- [ ] NdFeB upstream: mining + separation (`data/staging/ndfeb_upstream`)
- [ ] NdFeB downstream: metal/alloy, magnets, recycling, ancillary, substitutes (`data/staging/ndfeb_downstream`)
- [ ] SmCo + cobalt (`data/staging/smco_cobalt`)
- [ ] molybdenum (`data/staging/molybdenum`)
- [ ] gallium + germanium (`data/staging/gallium_germanium`)
- [x] traders/stockholders/DLA + labs (`data/staging/traders_labs`): 58 rows (32 trader, 26 lab), 14 offtakes. Gap: per-agent web-search budget ran out, so several rows were checked against company sites only (medium/low confidence); not included: Mitsui, Hanwa, Mitsubishi RtM, Sumitomo Corp, Marubeni, Intertek, SGS (own row), BGR, RCS Global

## Verification and outputs
- [ ] Verification pass: re-check a sample of rows per chain against sources (`data/staging/verification`)
- [ ] Apply verification fixes
- [ ] Build data/suppliers.csv, offtakes.csv, excluded.csv, sources.csv
- [ ] Build suppliers.xlsx (one tab per chain plus offtakes, excluded, sources)
- [ ] REPORT.md (per-chain analysis, gaps, completeness checks)
- [ ] docs/method.md, README.md
- [ ] Final commit and push
