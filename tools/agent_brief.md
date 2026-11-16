# Research brief for workstream agents (read fully before starting)

Today is **2026-11-16**. Your training data stops earlier, so **every fact must be confirmed by a web search or fetch made now**, and you must search for **2026 news on every entity** before finalizing its row. Ownership and offtakes changed a lot in 2024-2026.

## 1. Business context

We are building a buy-side sourcing and brokerage service for the US defense supply chain. We act as an agent and never take title.
- Defense contractors and their sub-tier suppliers need compliant supply of covered metals and magnets. We find supply, compare offers, verify compliance and close deals.
- Supply is the scarce side. The real suppliers are mostly **processors** (refiners, separators, powder makers, metal makers, magnet makers), not mines.
- The database answers four questions: who can supply what, from where, how much is already committed, and who is most likely to work with a broker.

## 2. The rule (read /home/user/critical-minerals/docs/scope.md, it governs everything)

- Covered countries: **China, Russia, North Korea, Iran**.
- From 1 Jan 2027, no stage of the covered material's chain may be mined, refined, separated, melted or produced in a covered country, including recycled feedstock.
- For SmCo, the chain explicitly includes **cobalt and samarium**. For NdFeB it includes **neodymium, iron and boron**; treat Dy/Tb as in scope too.
- Molybdenum is covered by statute now. Gallium and germanium are covered from 18 Dec 2027.
- EO 14415 and pending legislation also target **ownership/control by covered-country entities**, so flag those ties even where the facility is outside the covered countries.

## 3. Who counts as a supplier

- **Include** an entity if it operates, or credibly plans to operate by end of 2028, a facility at any stage of your chain located **outside** the covered countries.
  - "Credibly plans" means at least a company-announced project with a stated timeline (feasibility study, funding, permits or construction). Do not include grassroots exploration with no development plan.
  - Advanced projects with production targets in 2029 or later may be included, but must be marked `planned`, given a low broker score, and noted.
- **Flag but still include** non-covered-country facilities with ownership, control, financing or feedstock ties to covered countries. Examples:
  - a Chinese-owned mine in Canada;
  - a processor buying Chinese intermediate;
  - a Kazakh processor with Russian ties;
  - a Vietnamese plant owned by a Chinese group.

  Record the tie and your assessment.
- **Facilities inside covered countries** go in `excluded.jsonl`, major ones only, for screening (so a broker can recognise a Chinese refinery's name on paperwork). Include common name variants or aliases and the parent group.

## 4. Where to write (your workstream folder is given in your task)

Write **JSON Lines** files in your workstream folder, `data/staging/<workstream>/`:

| File | Contents |
|---|---|
| `suppliers.jsonl` | One JSON object per line, one row per company + facility + stage |
| `offtakes.jsonl` | One row per known supply agreement involving your chain |
| `excluded.jsonl` | Major covered-country facilities for your chain |
| `sources.jsonl` | Every URL you cite, one row per URL |
| `chain_notes.md` | Your analysis for the final report (template in section 9) |
| `progress.md` | Your own checklist of entities: to-do / done / dropped (with reason) |

**How to write rows safely.** Write a batch as a JSON array to a temporary file in your folder (for example `data/staging/<ws>/batch.json`), then append it with:

```
python3 /home/user/critical-minerals/tools/append_rows.py /home/user/critical-minerals/data/staging/<ws>/suppliers.jsonl /home/user/critical-minerals/data/staging/<ws>/batch.json
```

Do the same for the offtakes, excluded and sources files. `append_rows.py` fills missing fields with "" and rejects unknown keys. **Save after every 3-6 entities**, not only at the end. If you run out of context, the saved rows survive.

**Validate often:**

```
python3 /home/user/critical-minerals/tools/validate.py /home/user/critical-minerals/data/staging/<ws>
```

Fix all ERRORS before you finish. To fix a bad row, rewrite the file with a short Python script (load lines, edit, write back). Do not hand-edit with sed.

Do **not** run git commands. Do not touch other workstreams' folders. Field names and vocabularies are in `/home/user/critical-minerals/tools/schema.py`.

## 5. Supplier row fields (all strings unless noted; use "" when unknown)

- `supplier_id`: leave "". Assigned later.
- `company_name`: the operating company (for example "Global Tungsten & Powders Corp.").
- `parent_company`: the immediate parent.
- `ultimate_owner`: the top owner (a listed company, PE fund, state, or family). For listed companies with dispersed holders, the company itself, plus major (>10%) holders in `tie_detail`/`notes` if relevant.
- `owner_country`: the country of the ultimate owner.
- `covered_country_tie`: one or more of `none` / `ownership` / `control` / `financing` / `feedstock` / `unknown`, separated by `; ` with the main one first.
  - `ownership`: a covered-country entity holds an equity stake. Note the % if it is a minority stake.
  - `control`: board or operational control, or a management contract.
  - `financing`: debt or offtake prepayments from covered-country entities.
  - `feedstock`: input material comes from or passes through a covered country.
- `tie_detail`: required whenever the tie is not `none`. Give facts and dates.
- `material_chain`: one of `tungsten` / `tantalum` / `ndfeb` / `smco` / `cobalt` / `molybdenum` / `gallium` / `germanium` / `trader` / `lab`.
- `stage`: the fixed vocabulary for the chain (see `docs/scope.md`).
- `products`: specific forms and grades, for example "APT; WO3 (yellow oxide); W powder 0.5-50 µm FSSS".
- `facility_name`, `city`, `state_region`, `country`: the physical facility location (not head office).
- `facility_status`: `operating` / `commissioning` / `construction` / `planned` / `closed`. Care and maintenance with a restart plan = `planned` (note "restart"); without one = `closed`.
- `expected_production_date`: for non-operating sites, the company's stated target (for example "2027-H2 (company target, Aug 2026)"). For operating sites, blank or "operating since YYYY".
- `capacity_value`: a number as reported (for example "6000"). Leave blank if no source states it. **Never estimate.**
- `capacity_unit`: as reported (for example "t APT/yr", "t WO3 in concentrate/yr", "t NdPr oxide/yr", "t magnets/yr", "lb Ta2O5/yr").
- `capacity_year`: the year the figure applies to (nameplate year or reporting year).
- `capacity_source`: the URL the capacity figure came from.
- `feedstock_origin`: where the input comes from, and whether it passes through a covered country. Write "unknown" if not found.
- `committed_offtakes`: counterparty, term, share of output, date; or "none found". Also put each agreement in `offtakes.jsonl`.
- `government_awards`: program, amount and date, for example "DoD DPA Title III $X (2024-05); DLA; OSC loan $X (2025); EXIM LOI $X; DOE; DFC; JOGMEC; EU CRMA Strategic Project (2025-03); UK/Canada/Australia programs". Write "none found" if none.
- `rmi_rmap_status`: required for tungsten and tantalum smelter/refiner rows (also cobalt refiners where known). It must start with `conformant`, `active`, `not_listed`, `n/a` or `unknown`, followed by the source and date in brackets, for example "conformant (Apple Smelter & Refiner List Apr 2025; company site 2026)". Use `n/a` for mines and non-smelter stages.
  - **Do not accept terms on, or scrape, the RMI website**: its terms forbid copying the lists.
  - Use instead: company statements, SEC Form SD conflict-minerals exhibits (sec.gov), and Apple's public list. A local extract of Apple's April 2025 list (as of 31 Dec 2024) is at `/tmp/claude-0/-home-user-critical-minerals/46337f1a-274f-53da-b939-8448550e6878/scratchpad/dl/apple/apple2025.txt`, but **cite the URL** https://s203.q4cdn.com/367071867/files/doc_downloads/2025/04/Apple-Smelter-Refiner-List.pdf.
  - Apple's list says all listed smelters "participated in a third-party audit". That supports "conformant or active", not necessarily conformant, so word the status carefully.
- `dfars_7052_assessment`: one of the following.
  - `likely_compliant`: outside the covered countries, the known feedstock chain is outside them, and there is no material ownership, control or financing tie.
  - `at_risk`: outside the covered countries, but with covered-country feedstock dependence, a covered-country ownership/control/financing tie, or unclear feedstock for a stage the 2027 rule reaches.
  - `likely_noncompliant`: a known covered-country stage in the product's chain (for example, magnets made from Chinese-separated oxides or Chinese alloy).
  - `unknown`: not enough information.
- `dfars_7052_reason`: one line, required.
- `capacity_availability`: `uncommitted` / `partially_committed` / `fully_committed` / `unknown`. Base it on offtakes found: binding offtakes covering most output = fully. Captive internal use counts as committed.
- `broker_fit_score`: an integer 1-5, scored against the five criteria below.
  - The criteria:
    - (a) uncommitted or partly committed capacity;
    - (b) small or mid-size (big processors already have direct buyers);
    - (c) a clean compliance profile;
    - (d) production available in 2027-2028;
    - (e) signals of seeking buyers or capital: only non-binding MoUs, recent fundraising, a stated offtake search, a recent government financing application.
  - The bands:
    - **5** = meets (a)-(d) plus at least one (e) signal;
    - **4** = one weakness;
    - **3** = mixed;
    - **2** = large and mostly committed, or nothing before 2029;
    - **1** = captive, fully committed, closed, or likely non-compliant.
  - Traders and labs are scored as partners, as described in the traders/labs task.
- `broker_fit_rationale`: one or two sentences naming the criteria that drove the score.
- `commercial_contact_url`: the company sales or contact web page only. **No personal names, emails or phone numbers anywhere.**
- `sources`: the URLs supporting the row, separated by semicolons. Every one must also be in `sources.jsonl`.
- `date_accessed`: "2026-11-16" (or the actual date you accessed).
- `confidence`:
  - `high`: the key facts (owner, status, location, capacity) are confirmed in primary sources dated 2025-2026.
  - `medium`: mostly confirmed, some trade-press only or older data.
  - `low`: thin or old sources, or key facts unknown.
- `notes`: anything else useful. Recent 2026 news (with date), ownership changes, qualification status (for example aerospace/defense approvals, AS9100, ITAR registration), and whether they sell to the defense market.
- `gbd_capability`: NdFeB magnet rows only: `yes` / `no` / `planned` / `unknown`. Use `n/a` (or "") elsewhere.

## 6. Other files

- **`offtakes.jsonl`** fields:
  - `seller`, `buyer`, `material_chain`, `material`, `form`, `volume` (as stated), `term` (years/dates);
  - `binding_status`: `binding` / `non-binding` / `unknown`. MoU, LOI and term sheet = non-binding; a definitive offtake or supply agreement = binding;
  - `price_mechanism` (if public, for example "floor price $110/kg NdPr", "market-linked"), `announcement_date` (YYYY-MM-DD), `source` (URL), `notes` (status: active, expired, terminated; any amendments).
  - Include government offtakes, for example DoD price-floor or offtake commitments.
- **`excluded.jsonl`** fields:
  - `company_name`, `aliases` (name variants, English and pinyin, former names; separated by semicolons), `parent_company`, `ultimate_owner`;
  - `covered_country` (China / Russia / North Korea / Iran), `material_chain`, `stage`, `products`, `facility_name`, `city`, `state_region`;
  - `rmi_smelter_id` (CID number if shown in a public company filing or company site, otherwise ""), `notes`, `sources`, `date_accessed`.
  - Aim for the 10-30 most important covered-country facilities for your chain: the biggest producers, plus any that appear often on supplier paperwork, such as RMI-listed smelters.
- **`sources.jsonl`** fields:
  - `title`, `publisher`, `date` (publication date YYYY-MM-DD, YYYY-MM or YYYY; "undated" if none), `url`, `date_accessed`;
  - `type`: one of `primary filing` (SEC, ASX, TSX/SEDAR+, LSE RNS, other exchange or regulator filings, annual reports), `government` (agency pages, award notices, USGS, DoD releases), `company release` (press releases, company websites, investor presentations not filed with a regulator), `trade press`, `other`.

## 7. Research method

1. **Start from the candidate list in your task, but do not stop there.** Run discovery searches for missing players at every stage, for example:
   - "APT producer Vietnam", "tungsten powder manufacturer USA ITAR", "rare earth separation plant 2026", "magnet plant groundbreaking 2026";
   - lists from the USGS Mineral Commodity Summaries 2026, government award lists, and industry association member lists.
2. **Prefer primary sources:** company annual reports and investor presentations; SEC 10-K/20-F/40-F/8-K; ASX announcements; SEDAR+; LSE RNS; government award notices (war.gov / defense.gov contract announcements, DoD/DLA releases, the Office of Strategic Capital, EXIM, DOE, DFC); USGS MCS 2026. Use trade press (Fastmarkets, Argus, Benchmark, Adamas, Project Blue, Metal Tech News, Mining.com, Reuters) to find leads, then confirm with primary sources where possible.
3. **For each entity, run at least one search for 2026 news** ("<company> 2026"). Check for ownership changes, financing, offtakes, commissioning, closures, and Chinese or Russian stakes.
4. **Never invent** a capacity, owner, agreement, award or status. If you cannot verify something, leave it blank or write "unknown" and set confidence `low`. If two sources conflict, use the most recent primary source and describe the conflict in `notes`.
5. **Drop entities** that do not qualify (for example exploration only, closed with no restart plan, or in a covered country; the last go to `excluded`). Record each drop with its reason in `progress.md`.
6. **Do not collect personal contact details.**
7. **Be efficient.**
   - Use WebSearch "standard" mode by default and "extended" only when standard results are thin.
   - Use WebFetch on primary pages to extract specific facts.
   - When a site blocks fetching, rely on search snippets from reputable outlets and lower confidence.
   - Do not re-fetch the same page.
8. **Volume.** Your task gives a target row count. Rows must be real facility-stage rows, not padding.

## 8. Things worth recording carefully

- **Integrated groups.** Make separate rows per facility and stage, for example Plansee Reutte vs GTP Towanda; MP Mountain Pass vs Fort Worth.
- **Ownership changes in 2024-2026.** Examples to check: Energy Fuels acquiring ASM and VAC; USA Rare Earth acquiring LCM; Mitsubishi Materials acquiring H.C. Starck Tungsten; Taboca and Tanco ownership; Sandvik/Wolfram; Masan's tungsten unit; Almonty's US move. Confirm or refute each.
- **US government support since 2020.** This includes DoD DPA Title III awards, IBAS/IBP, the Office of Strategic Capital, DLA stockpile purchases, DoD equity or price-floor deals (for example the 2025 MP Materials deal), EXIM, DOE, DFC, and allied programs (JOGMEC, KOMIR, EU CRMA Strategic Projects, the UK, Canada's critical minerals funds, Australia's Critical Minerals Facility/NRF).

  Every company receiving a US government award for your chain's materials since 2020 must appear in the file. Make a dedicated search pass for this.
- **Defense qualification signals:** ITAR registration, AS9100, MIL-spec products, existing DoD supply.
- **Where the feedstock comes from.** For example, a Japanese or Korean processor that buys Chinese APT or Chinese oxides is `at_risk` or `likely_noncompliant` for 2027.

## 9. `chain_notes.md` template (write this at the end; keep it factual and dated)

```
# <Chain> notes (workstream <ws>), as of 2026-11-16
## Who matters at each stage (3-8 bullets per stage, non-covered-country only)
## The real bottleneck (which stage, why, numbers with sources)
## Uncommitted non-China capacity for 2027 (best estimate with stated basis; say "unknown" if you cannot support a number)
## Top 10 broker prospects (one line each: company - facility - why)
## Gaps: stages with zero or near-zero compliant supply
## Completeness checks
- USGS MCS 2026: countries with non-zero 2025 production for this commodity, and whether their main producers are listed (or why not)
- RMI-equivalent check (W/Ta only): which non-covered smelters/refiners on the public lists are in the file
- US government awards since 2020: list of awardees and confirmation that each has a row
- Every stage has at least one operating non-covered supplier? (yes/no per stage)
## What could not be verified
```

## 10. When finished

1. Validate until there are 0 errors.
2. Make sure `progress.md` and `chain_notes.md` are complete.
3. Reply with a **short** summary (under 250 words): row counts by stage, the 3 most important findings, and the biggest open gaps.

Do not paste the data into your reply. It is in the files.
