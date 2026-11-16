# Decisions log

These are judgment calls made while building the database, recorded so you can see and challenge them. Newest decisions are added at the bottom.

## Scope

1. **Added molybdenum, gallium and germanium as material chains.**
   - The FY2026 NDAA (Pub. L. 119-60, sec. 844) added molybdenum to the statutory covered-material list from 18 Dec 2025, and gallium and germanium from 18 Dec 2027.
   - The prompt said to follow the rule, not the prompt, so molybdenum is mapped as a full chain.
   - Gallium and germanium are mapped at the main-producer level, because they only become covered in December 2027.
   - The DFARS clause text has not yet added any of the three. Contracts may not flow them down until DoD updates DFARS. The statute already binds DoD.
2. **One strict compliance standard for every row.**
   - The 1 Jan 2027 trigger is the *award date* under the new deviation clause 252.225-7961, and the *delivery date* under the older 252.225-7052.
   - We assess every supplier against the 2027 test either way: no mining, refining, separation, melting or production in a covered country at any point, including recycled feed.
3. **Ownership, control and financing ties are flagged as risk even when location passes.**
   - The DFARS test is about *where* each stage happens. EO 14415 (sec. 3(b)) and the House FY2027 NDAA bill also look at foreign ownership, control or influence (FOCI).
   - A facility outside the covered countries but owned or controlled by a covered-country entity is therefore marked `at_risk`, not `likely_compliant`.
4. **Cobalt is in scope** because the clause text for SmCo covers "mining or production of a cobalt and samarium ore or feedstock." **Iron and boron are in scope for NdFeB** because the clause names them. We map non-China ferroboron sources under the `ancillary_inputs` stage; high-purity iron is not mapped.
5. **Dysprosium and terbium are treated as in scope** for NdFeB, even though the stage list names only neodymium, iron and boron. This is the conservative reading.
6. **Niobium is not mapped as a chain.** It appears only in the pending House bill (Tier 2). Tantalum rows note niobium capability where relevant.
7. **Substitutes** (rare-earth-free magnets such as Niron's iron nitride) are listed under `ndfeb` / `substitute`. They are not covered materials; they are listed so you can see the alternative.

## Data structure

8. **One row per company + facility + stage.** An integrated plant doing two stages (for example APT and tungsten powder) gets two rows.
9. **Two columns beyond the requested list:**
   - `dfars_7052_reason`: the one-line reason the prompt asked for alongside the assessment.
   - `gbd_capability`: grain-boundary diffusion of Dy/Tb, for NdFeB magnet rows. Elsewhere it is `n/a` or blank.
10. **`covered_country_tie` can hold more than one value**, separated by semicolons (for example `ownership; feedstock`), with the main tie first. `tie_detail` explains them.
11. **Status mapping.**
    - A site on care and maintenance with an announced restart plan is `planned`, and the note says "restart".
    - A site on care and maintenance with no restart plan is `closed`.
    - A plant producing at reduced rates is `operating`.
12. **Capacity is recorded in the unit the source used** (for example "t WO3 in concentrate per year", "t NdPr oxide per year", "t magnets per year"). We do not convert units, which avoids conversion errors.
    - `capacity_year` is the year the figure refers to.
    - Planned capacities are nameplate targets, not forecasts.
13. **`excluded.csv` lists only major facilities inside the covered countries.**
    - It is for screening paperwork, not a complete list.
    - Name aliases are included so a supplier's certificate can be matched to the parent group.
    - Smelter IDs (CIDs) are included where they appear in public company filings.
14. **IDs are assigned at the end** by a script, by chain prefix: W-, TA-, ND-, SM-, CO-, MO-, GA-, GE-, TR-, LB- and X- (excluded). They may change if the database is rebuilt; join on company and facility names when comparing versions.

## Sources and verification

15. **RMI smelter lists.** The Responsible Minerals Initiative website asks visitors to accept terms that forbid copying, redistributing or making derivative works from its lists. We did not accept those terms on your behalf and did not scrape the lists.
    - `rmi_rmap_status` comes from public secondary sources: company statements, SEC Form SD conflict-minerals exhibits, and Apple's published Smelter and Refiner List (April 2025, covering suppliers as of 31 Dec 2024). Each row names its source.
    - Before relying on a status, check it yourself on the RMI site; it changes monthly.
    - The RMI completeness check in REPORT.md uses these public lists as a stand-in for the RMI list.
16. **We used no personal contact details.** `commercial_contact_url` holds company contact or sales web pages only.
17. **Never invent.** A capacity, owner, offtake or award appears only if a source found in this research states it. Gaps are blank or "unknown", with confidence lowered.
18. **The DoD class-deviation text could not be retrieved.** The DPCAP website returned errors. The details of 252.225-7961 come from three law-firm and practitioner summaries, cited in `docs/scope.md`.

## Scoring

19. **How the `broker_fit_score` (1-5) is built.** For supplier rows it rewards five things:
    - (a) uncommitted or partly committed capacity;
    - (b) small or mid-size, without an entrenched direct-buyer book;
    - (c) a clean compliance profile;
    - (d) material available in 2027-2028;
    - (e) signals of looking for buyers or capital: only non-binding MoUs, recent fundraising, stated offtake search, a government financing application.

    The bands:
    - **5** = meets (a)-(d) with at least one (e) signal.
    - **4** = one weakness.
    - **3** = mixed.
    - **2** = large and mostly committed, or not producing before 2029.
    - **1** = captive, fully committed, closed, or likely non-compliant.
20. **Traders and labs** are scored for usefulness as partners, not as supply.
    - Traders: independent minor-metals traders with traceable non-China stock score high. Traders tied to covered countries, and captive trading arms, score low.
    - Labs: labs with origin or provenance methods, US or allied locations and defense-relevant accreditations score high.
21. **The `dfars_7052_assessment` values:**
    - `likely_compliant`: the facility is outside the covered countries, the known feedstock chain is outside them, and there is no material ownership, control or financing tie.
    - `at_risk`: outside the covered countries, but with covered-country feedstock dependence, a covered-country ownership/control/financing tie, or unclear feedstock for a stage that the 2027 rule reaches.
    - `likely_noncompliant`: known covered-country stage in its supply chain for the product (for example, metal made from Chinese-separated oxide), or a covered-country-controlled operation whose product already traces through a covered country.
    - `unknown`: not enough information.
