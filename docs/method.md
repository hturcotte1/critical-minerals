# Method

*How the database was built, and what could not be verified. Research date: 16 November 2026.*

## 1. Confirming the rule first

Before any supplier research, the governing texts were read from primary sources:
- the DFARS final rule of 30 May 2024, which carries the clause text for 252.225-7052 and 225.7018;
- the US Code section, 10 U.S.C. 4872;
- the FY2026 NDAA enrolled text (Pub. L. 119-60);
- Executive Order 14415;
- the House-passed FY2027 NDAA (H.R. 8800);
- the H.R. 9073 bill text.

The DoD class-deviation memo (2026-O0041 Rev. 1) and the new clause 252.225-7961 could not be downloaded, because the DoD website returned errors. Their content was taken from three law-firm and practitioner summaries published September to November 2026. The result is `docs/scope.md`, which fixes the covered materials, countries, stages and the stage vocabulary used in every row.

One finding changed the scope: the FY2026 NDAA added molybdenum (now) and gallium and germanium (from 18 Dec 2027) to the statute. Those chains were added (see `docs/decisions.md`).

## 2. Research workstreams

The work was split into eight parallel research workstreams. Each followed one written brief (`tools/agent_brief.md`) with the same field definitions, controlled vocabularies, scoring rules and sourcing rules:

| Workstream | Chains and stages |
|---|---|
| Tungsten | All five tungsten stages, scrap recyclers, covered-country screening list |
| Tantalum | All five tantalum stages, tin-slag and by-product sources, recyclers |
| NdFeB upstream | Rare-earth mining/concentrate and separation (including Dy/Tb) |
| NdFeB downstream | Rare-earth metal/alloy, sintered and bonded magnets, recyclers, ferroboron, rare-earth-free substitutes |
| SmCo and cobalt | Samarium separation, metal, SmCo alloy and magnets; non-China cobalt mining intermediates, refining, powder, recycling |
| Molybdenum | Mining, roasting/chemicals, metal powder, mill products, recycling |
| Gallium and germanium | Main producers by stage (lighter mapping) |
| Traders and labs | Traders, distributors, stockholders, government stockpiles (incl. how DLA sells), and assay/inspection/provenance labs |

Each workstream started from your seed list plus additional leads. Leads were explicitly treated as unverified. Each workstream then ran discovery searches for missing players at every stage, using:
- the USGS Mineral Commodity Summaries 2026 country tables;
- public smelter lists;
- government award announcements;
- industry news from 2025-2026.

## 3. Sourcing rules applied to every row

- **Primary sources first:** company annual reports, investor presentations and exchange filings (SEC, ASX, TSX/SEDAR+, LSE RNS); government award notices (DoD/war.gov, DLA, Office of Strategic Capital, EXIM, DOE, DFC; allied programmes); USGS. Trade press was used to find leads and confirmed against primary sources where possible.
- **Recent news on every entity.** Each one was searched for 2026 news before its row was finalised, because ownership and offtakes changed frequently in 2024-2026.
- **Nothing invented.** Capacity, owner, offtake, award and status appear only when a source found during the research states them. Otherwise the field is blank or "unknown", and confidence is lowered.
- **Every row carries:**
  - its source URLs;
  - a date accessed;
  - a confidence level: high, medium or low.
- **No personal contact details** were collected. Only company sales or contact pages appear.

## 4. RMI smelter status

The Responsible Minerals Initiative's website requires visitors to accept terms that forbid copying or redistributing its smelter lists. We did not accept those terms or scrape the site.

RMAP status was taken from public secondary sources:
- company statements;
- SEC Form SD conflict-minerals exhibits;
- Apple's published Smelter and Refiner List (April 2025 edition, covering Apple's supply chain as of 31 December 2024).

The RMI completeness check in REPORT.md uses those public lists as a stand-in for the RMI list. Re-check statuses on the RMI site before relying on them.

## 5. Merging and checks

- **Merging.** Workstreams wrote JSON Lines files in `data/staging/`. A validation script checked every row against the controlled vocabularies (stage, status, assessment, availability, score, confidence) and checked that every cited URL is listed as a source. A build script merged the workstreams, removed duplicate rows, assigned IDs, and wrote the CSV files and `suppliers.xlsx`.
- **Verification pass.** After the research, separate verifiers re-checked a random sample of rows from every chain against the cited sources. They checked owner, location, status, capacity, offtakes, awards and assessment. Discrepancies were corrected in the data, and the results are summarised in REPORT.md.

## 6. What could not be verified

This section is completed from the workstream notes (`data/staging/*/chain_notes.md`) and the verification pass; see the end of this file.
