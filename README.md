# Non-China critical-metals supplier map for US defense sourcing

This folder is a sourced database of companies that could supply US defense contractors with the materials restricted by **DFARS 252.225-7052** and **10 U.S.C. 4872**. The restriction tightens on **1 January 2027**. It was built on 16 November 2026.

Everything here opens by double-clicking. No software beyond Excel (or any spreadsheet program) and a text or Markdown viewer is needed.

## Start here

| If you want to... | Open |
|---|---|
| See the findings in plain English: who matters, where the bottlenecks are, the best broker prospects, the gaps | **REPORT.md** |
| Browse or filter the database | **suppliers.xlsx**: one tab per material, plus prospects, offtakes, excluded facilities and sources |
| Understand exactly what the rule covers and from when | **docs/scope.md** |
| See the judgment calls made along the way | **docs/decisions.md** |
| See how the research was done and what could not be verified | **docs/method.md** |

## What's inside (as built on 16 November 2026)

| Item | Count |
|---|---|
| Supplier rows (company + facility + stage) | 495, across 58 countries |
| - NdFeB magnets, from mine to magnet and recycling | 133 |
| - Tungsten | 79 |
| - Molybdenum | 63 |
| - Tantalum | 57 |
| - Cobalt (for SmCo) | 35 |
| - Gallium / germanium | 27 / 21 |
| - SmCo magnets | 17 |
| - Traders, stockholders and government stockpiles | 34 |
| - Assay, inspection and origin-testing labs | 29 |
| Known supply agreements (`offtakes`) | 149 |
| Covered-country facilities for screening (`excluded`) | 140 (China 121, Russia 16, Iran 2, North Korea 1) |
| Sources cited | 826 |

About 15% of rows (74) were independently re-checked after the research; all issues found were corrected. See REPORT.md, section 12.

## The files

**`suppliers.xlsx`**: the whole database in one workbook. Each tab has a frozen header row and filters.
- `About`: what each tab contains.
- `tungsten`, `tantalum`, `ndfeb`, `smco`, `cobalt`, `molybdenum`, `gallium`, `germanium`: supplier facilities, one row per company + facility + production stage.
- `traders`: traders, distributors, stockholders and government stockpiles.
- `labs`: assay, inspection and origin-testing labs.
- `top_prospects`: every row scored 4 or 5 for broker fit.
- `offtakes`: known supply agreements.
- `excluded`: major facilities *inside* China, Russia, North Korea and Iran, for spotting their names on paperwork.
- `sources`: every source used.

**`data/` folder**: the same data as plain CSV files (they open in Excel):
- `data/suppliers.csv`: all supplier rows across all materials.
- `data/offtakes.csv`: one row per known supply agreement.
- `data/excluded.csv`: covered-country facilities for screening.
- `data/sources.csv`: every source, with title, publisher, date, web address and type.

**Other files:**
- `REPORT.md`: the analysis.
- `docs/`: the scope, decisions and method notes.
- `PROGRESS.md`: the work checklist.
- `tools/`: scripts that rebuild the spreadsheet. You do not need to touch them.
- `data/staging/`: raw research notes per workstream. You do not need to touch it either.

## What the main columns mean (suppliers)

| Column | Meaning |
|---|---|
| `supplier_id` | Row ID (W- tungsten, TA- tantalum, ND- NdFeB, SM- SmCo, CO- cobalt, MO- molybdenum, GA- gallium, GE- germanium, TR- traders, LB- labs) |
| `company_name`, `parent_company`, `ultimate_owner`, `owner_country` | Who runs the facility and who ultimately owns it |
| `covered_country_tie` + `tie_detail` | Any link to China, Russia, North Korea or Iran: `ownership`, `control`, `financing`, `feedstock`, `none` or `unknown`. More than one can apply |
| `material_chain`, `stage` | Which material, and which step of the chain (for example mining, separation, metal powder, magnets). Stage names are defined in docs/scope.md |
| `products` | Specific products and grades |
| `facility_name`, `city`, `state_region`, `country` | Where the plant or mine is |
| `facility_status`, `expected_production_date` | `operating` / `commissioning` / `construction` / `planned` / `closed`, and the company's stated start date if not yet operating |
| `capacity_value`, `capacity_unit`, `capacity_year`, `capacity_source` | Capacity as stated by a source, in the source's own unit (never estimated) |
| `feedstock_origin` | Where its input material comes from, and whether that passes through a covered country |
| `committed_offtakes` | Known buyers who have already contracted output |
| `government_awards` | US and allied government grants, loans, equity or offtakes |
| `rmi_rmap_status` | Responsible Minerals Initiative audit status (tungsten and tantalum smelters), from public sources |
| `dfars_7052_assessment` + `dfars_7052_reason` | Our judgment of 2027 compliance: `likely_compliant`, `at_risk`, `likely_noncompliant` or `unknown`. This is not legal advice |
| `capacity_availability` | `uncommitted`, `partially_committed`, `fully_committed` or `unknown` |
| `broker_fit_score` + `broker_fit_rationale` | 1 = unlikely to work with a broker, 5 = strong prospect, with the reason |
| `commercial_contact_url` | The company's own sales or contact page (no personal contact details are collected) |
| `sources`, `date_accessed`, `confidence` | Where each fact came from, when it was checked, and how solid it is (`high` / `medium` / `low`) |
| `gbd_capability` | For NdFeB magnet makers: can they do grain-boundary diffusion of dysprosium/terbium |

## Important cautions

- **This is research, not legal advice.** The compliance column is a screening judgment based on public information. Before a deal, get the supplier's own origin documentation and have counsel review it.
- **Facts age quickly.** Ownership, offtakes and project status in this sector change month to month. Every row is dated and sourced; re-check before acting.
- **Gaps are left blank, not guessed.** If a capacity or owner could not be verified, the cell is blank or says "unknown" and confidence is lowered.
- **The scope goes slightly beyond the original brief.** It includes molybdenum, gallium and germanium, because the statute added them (see docs/scope.md).
- **The law may change soon.** The pending FY2027 defense bill could change the rule (see docs/scope.md, "Pending legislation").

## Rebuilding the spreadsheet (only if someone edits the raw data)

A technical user can run `python3 tools/validate.py --all` and then `python3 tools/build.py`. This regenerates the CSV files and `suppliers.xlsx` from `data/staging/`.
