# Scope: what the rule covers

*Checked against primary sources on 16 November 2026. This file governs the rest of the database.*

## The short version

1. **Who it binds.** The Department of Defense (DoD, now styled the Department of War) and, through contract clauses, every prime contractor and subcontractor at any tier that delivers a covered material or an item containing one.
2. **Covered countries.** North Korea, China, Russia and Iran. No other countries are covered.
3. **Covered materials under the statute today (10 U.S.C. 4872(f)):**
   - samarium-cobalt (SmCo) magnets
   - neodymium-iron-boron (NdFeB) magnets
   - tungsten metal powder
   - tungsten heavy alloy, and any finished or semi-finished part containing it
   - tantalum metals and alloys
   - **molybdenum**, added by the FY2026 NDAA (Pub. L. 119-60, sec. 844(a), enacted 18 Dec 2025). The DFARS clause text has not caught up yet.
   - **gallium and germanium**, added by the same law (sec. 844(b)). They only take effect on **18 December 2027**.
4. **Production stages that count.**
   - Until 31 Dec 2026: material that was *melted or produced* in a covered country.
   - From 1 Jan 2027: material that was *mined, refined, separated, melted, or produced* in a covered country. In practice that means the whole chain from the mine (or the recycled feedstock) to the finished product.
5. **The 2027 trigger: delivery date or award date.** This is the most important change in 2026.
   - The FY2026 NDAA (sec. 848) rewrote the pending expansion as a ban on DoD *entering into a contract* for covered material mined, refined or separated in a covered nation.
   - DoD followed in **Class Deviation 2026-O0041, Revision 1** (reported as signed 1 July 2026). It created a new clause, **DFARS 252.225-7961 (JUN 2026)**, which applies the mined/refined/separated ban to contracts **awarded on or after 1 Jan 2027**. Contracting officers were told to use 7961 in new solicitations and to swap it into existing contracts in place of 252.225-7052.
   - Where an older contract still carries **252.225-7052 (MAY 2024)**, the ban applies to **deliveries on or after 1 Jan 2027**, however old the contract or the inventory.
   - The ban on covered-country melting and production keeps applying either way.
6. **Waivers are getting harder.** Executive Order 14415 (20 July 2026) tells DoD to stop issuing non-availability waivers from 1 Jan 2027 unless the contractor has an accepted mitigation plan. It also starts rules for supply-chain mapping and supplier vetting, and a ban on material from "unreliable foreign suppliers", meaning entities under the foreign ownership, control or influence (FOCI) of a covered nation.
7. **Pending, not law (as of 16 Nov 2026).**
   - The House-passed FY2027 NDAA (H.R. 8800, sec. 1803) would repeal the 1 Jan 2027 expansion and replace it with a two-tier regime (details below).
   - The Senate has not passed its bill.
   - A separate delay bill (H.R. 9073, to 2032) sits in committee.
   - Until something is enacted, plan for 1 Jan 2027.

## What each stage means, material by material (from 1 January 2027)

Source: DFARS 225.7018-2 and clause 252.225-7052(b), as revised by the final rule in DFARS Case 2021-D015 (89 FR 46814, 30 May 2024).

| Material | Restricted stages from 1 Jan 2027 (verbatim scope) |
|---|---|
| SmCo magnets | "the entire supply chain from mining or production of a **cobalt and samarium** ore or feedstock, including recycled material, through production of finished magnets" |
| NdFeB magnets | "the entire supply chain from mining of **neodymium, iron, and boron** through production of finished magnets" |
| Tantalum metals and alloys | "mining or production of a tantalum ore or feedstock, including recycled material, through production of metals of any kind and alloys" |
| Tungsten metal powder and tungsten heavy alloy | "mining or production of a tungsten ore or feedstock, including recycled material, through production of tungsten metal powders, tungsten heavy alloy, or any finished or semi-finished component containing tungsten heavy alloy" |
| Molybdenum | In the statute since 18 Dec 2025, but not yet defined in DFARS. No stage list has been issued, so we apply the general "mined, refined, separated, melted, or produced" test. |
| Gallium, germanium | Statute only, effective 18 Dec 2027. No DFARS text yet. |

Two consequences matter for sourcing:
- **Cobalt is explicitly in scope for SmCo.** A SmCo magnet made outside China with China-refined cobalt fails the 2027 test. That is why this map includes non-China cobalt refiners.
- **Iron and boron are explicitly in scope for NdFeB.** Ferroboron is a small, often overlooked input, and much of it is Chinese. We list known non-China ferroboron and boron sources under the `ancillary_inputs` stage.

Dysprosium and terbium (the heavy rare earths used for high-temperature grades) are not named in the NdFeB stage list. They are, however, part of the covered material (the magnet), and the general test covers anything mined, refined or separated in a covered country. We treat them as in scope. That is the conservative reading, and it is how industry reads the rule.

## Exceptions that matter for a broker

Based on DFARS 225.7018-3 and 252.225-7052(c), unless noted.

- **COTS items are exempt**, except a COTS item that is 50% or more covered material by weight (from 1 Jan 2027; before that the 50% test applied to tungsten only).
- **Mill products are not exempt** from 1 Jan 2027. That means a covered material sold as bar, billet, slab, wire, cube, sphere, block, blank, plate or sheet that is not yet built into an end item, subsystem, assembly or component. This is the core of the broker opportunity: raw and semi-finished covered materials sold to the defense supply chain must be compliant.
- **Electronic devices are exempt** unless the contract says otherwise. EO 14415 sec. 2(f) orders DoD to review how it applies this exemption.
- **Recycled NdFeB magnets are exempt** if the milling of the recycled material and the sintering of the final magnet take place in the United States.
- **Recycled SmCo magnets** get the same treatment under the statute (FY2026 NDAA sec. 844(a)(2)). The DFARS clause has not added this yet.
- **Recycled tantalum, tungsten and molybdenum** are exempt under the statute if two conditions hold:
  - the recycled material was produced outside a covered nation, and
  - the melting and all further processing take place in the United States or in a "qualifying country" (a country with a defense procurement agreement with the US; 10 U.S.C. 4863(m)(11)).

  Gallium and germanium join this exception on 18 Dec 2027. The DFARS clause has not added it yet. Note the tension: the DFARS text says the restriction covers "feedstock, including recycled material." Until DFARS catches up, check every recycled-feed claim against both texts.
- **Other routes** (from secondary sources; not checked against the 7961 text):
  - Purchases at or below the simplified acquisition threshold.
  - Items bought and used outside the US, for example in contingency operations.
  - A non-availability determination (DFARS 225.7018-4).
  - A national security waiver (10 U.S.C. 4872(e)). The FY2026 NDAA sec. 843 lets a 10 U.S.C. 4863(k) specialty-metals national security waiver also cover 4872.

## Executive Order 14415 (20 July 2026)

Title: *Securing America's Defense Supply Chains and Ensuring Domestic Acquisition of Critical Materials.* It relies on the statute's lists and adds no materials or countries. Its main effects:

- **Waivers (sec. 2).** From 1 Jan 2027, DoD stops issuing 4872(c)(1) non-availability waivers unless the contractor submits a formal mitigation plan that DoD accepts. The plan must cover:
  - the source of the non-compliant material,
  - evidence of exhaustive efforts to find compliant material,
  - steps to remove the non-compliant material, and
  - a strict timeline.

  Failing to qualify a domestic source does not count as non-availability unless the contractor shows active, adequately funded efforts to qualify one. Fraud or wilful non-compliance can be referred to the Attorney General.
- **Supply-chain mapping (sec. 3).** DoD guidance is due within 180 days (about 16 Jan 2027) and regulations 90 days after that. Contractors will need:
  - a full indentured bill of materials traced to raw-material origin,
  - written vetting of suppliers for financial, FOCI and manufacturing risk, and
  - to stop using covered material from "unreliable foreign suppliers". The order defines these as persons under FOCI of a covered nation, plus any other nation the Secretary designates.
- **Qualifying alternatives (sec. 4).** Contractors that rely on unreliable foreign suppliers must qualify alternative sources. DoD must also speed up qualification of new sources; a strategy was due about 18 Oct 2026.
- **Carve-out (sec. 6).** Nothing in the order affects Project Vault (the US strategic critical minerals reserve) or foreign projects financed by EXIM, DFC, State, War, Commerce or Energy.

**Why this matters for the map:** DFARS 7052/7961 tests *where* each stage happened. The EO, and the pending House bill, also test *who owns or controls* the supplier. A Chinese-owned mine in Canada passes the location test but may fail the future FOCI test. We therefore flag ownership, control and financing ties as `at_risk` even where location alone would pass.

## Pending legislation and other developments (not yet law)

- **House FY2027 NDAA, H.R. 8800 sec. 1803.** Passed the House on 22 July 2026. It would:
  - Repeal the 1 Jan 2027 "mined, refined, or separated" amendment, effective on the earlier of 31 Dec 2026 or enactment.
  - Rewrite 4872 around material "sourced from, by, or through" a covered nation. That means any mining, refining, separation, melting, processing or manufacturing done in the nation *or by an entity located in the nation*. The new rules would apply to solicitations and contracts 180 days after enactment.
  - Create **Tier 1** materials:
    - NdFeB and SmCo magnets
    - tungsten metal powder and heavy alloy
    - Nd, Pr and NdPr oxides and metals, and their ores and concentrates
    - tantalum, including ores, oxides, concentrates, metal, powder and alloys
    - molybdenum metals, powders and alloys, and gallium/GaN and germanium (all three from 18 Dec 2027)

    Tier 1 bans covered-nation sourcing. It also requires that **at least 50% of the cost come from "domestically owned entities"** (US-organized and US-controlled).
  - Create **Tier 2** materials:
    - oxides, metals and alloys of Gd, Sm, Nd, Pr and Tb
    - tungsten precursors (ores, concentrates, APT, AMT, tungstic acid, sodium tungstate, oxides), plus tungsten carbide from 2029
    - **niobium**

    Tier 2 phases in the share that must come from outside covered nations: 25% in 2028, 50% in 2029, 75% in 2030 and 100% from 2031. It would not apply to solicitations or contracts before 1 Jan 2028.
  - Add two-year waivers with binding-supplier transition plans, contractor certifications with 10-year record keeping, a "preferred domestic manufacturer or producer" designation, and a 12-month expedited source-qualification process.
- **Senate.** The Senate's FY2027 NDAA (S. 4784) has not passed; a cloture vote failed 50-46 on 14 July 2026. Commentators expect a House-Senate compromise in the lame-duck session (Nov-Dec 2026). Section 1803 may change or disappear in conference.
- **H.R. 9073** (introduced 29 May 2026, referred to House Armed Services; no action since). It would delay the expansion to the earlier of 1 Jan 2032 or 180 days after DoD certifies that enough commercially viable non-covered-nation suppliers exist.
- **Industry pressure.** In May 2026 major contractors were reported to be lobbying for a second delay (Financial Times, via Adamas Intelligence). In October 2026, S&P Global reported that waivers are expected to bridge the gap. We found no official postponement.
- **30 July 2026 DPA determination.** It declares "recoverable critical minerals and materials" scarce and critical, and delegates export-control authority over items such as swarf, black mass and finished rare-earth magnets. This is relevant to magnet and swarf recyclers.

**How this database handles it:**
- We assess every facility against the strict 2027 standard: no covered-country stage anywhere from mine or recycled feed to finished product.
- We separately flag ownership, control and financing ties to covered countries, because both EO 14415 and the House bill point that way.
- Where the House bill would change the answer, mainly the 50% domestically-owned test for Tier 1, we note it in REPORT.md rather than in each row.

## Material chains in this database

The prompt listed tungsten, tantalum, NdFeB, SmCo and cobalt. Because "follow the rule, not this prompt," we added:
- **molybdenum**, which is covered under the statute now, and
- **gallium and germanium**, enacted and covered from 18 Dec 2027, inside the 2027-2028 planning window.

Gallium and germanium are mapped more lightly, at the main producers by stage. Niobium is only in the pending House bill, so it is not mapped as a chain; tantalum rows note niobium capability where relevant.

## Fixed stage vocabulary (the `stage` column)

| material_chain | stage | What it means |
|---|---|---|
| tungsten | `mining_concentrate` | Mining and beneficiation to wolframite or scheelite concentrate |
| tungsten | `chemical_intermediate` | APT, AMT, tungsten oxides (BTO/YTO/WO3), tungstic acid, sodium tungstate |
| tungsten | `metal_powder` | Reduction to tungsten metal powder (carbide makers that make W powder in-house included; WC noted in products) |
| tungsten | `heavy_alloy_fabrication` | Tungsten heavy alloy (W-Ni-Fe, W-Ni-Cu), pressed/sintered/forged tungsten, mill products (rod, wire, sheet, plate), fabricated parts |
| tungsten | `recycling` | Processing tungsten scrap (hard or soft) back to APT, oxide or powder (chemical or zinc process), or scrap processors producing a tungsten intermediate |
| tantalum | `mining_concentrate` | Tantalite/coltan concentrate, tantalum-bearing tin slag, by-product concentrate from lithium or tin mines |
| tantalum | `chemical_processing` | Digestion and solvent extraction to K2TaF7 (potassium heptafluorotantalate) or Ta2O5 |
| tantalum | `metal_powder_ingot` | Reduction to tantalum powder (capacitor or metallurgical grade), electron-beam melting to ingot, unwrought metal |
| tantalum | `alloy_mill_products` | Tantalum alloys (Ta-W, Ta-Nb), sheet, plate, wire, rod, tube, sputtering targets, fabricated parts |
| tantalum | `recycling` | Tantalum scrap processing (capacitor, target, superalloy, machining scrap) |
| ndfeb | `mining_concentrate` | Rare-earth mining, beneficiation and pre-separation processing (cracking/leaching to mixed rare-earth carbonate/chloride, MREC) |
| ndfeb | `separation` | Solvent extraction or other separation to individual oxides or salts (NdPr oxide, Dy oxide, Tb oxide, etc.) |
| ndfeb | `metal_alloy` | Reduction to rare-earth metal (NdPr, Dy, Tb, DyFe, TbFe) and NdFeB alloy making (strip-cast flake, master alloys) |
| ndfeb | `magnet_sintered` | Sintered NdFeB magnets (grain-boundary diffusion capability recorded in `gbd_capability`) |
| ndfeb | `magnet_bonded` | Bonded and hot-deformed NdFeB magnets and rapid-quenched (MQ-type) powders for them |
| ndfeb | `recycling` | Recovery of rare earths or magnet alloy from swarf, scrap or end-of-life magnets (short-loop/HPMS or long-loop/hydromet) |
| ndfeb | `ancillary_inputs` | Other named inputs: ferroboron/boron, high-purity iron |
| ndfeb | `substitute` | Rare-earth-free permanent-magnet alternatives (e.g., iron nitride). Not a covered material. Listed separately |
| smco | `mining_concentrate` | Samarium-bearing ore or concentrate (only where samarium is actually recovered) |
| smco | `separation` | Separation to samarium oxide (or an SEG samarium-europium-gadolinium intermediate) |
| smco | `metal` | Samarium metal production |
| smco | `alloy` | SmCo alloy or powder (SmCo5, Sm2Co17) |
| smco | `magnet` | SmCo magnets, sintered or bonded |
| smco | `recycling` | SmCo scrap or swarf recovery |
| cobalt | `mining_intermediate` | Non-Chinese-controlled cobalt mining and intermediates (hydroxide, MHP, matte) that feed non-China refiners |
| cobalt | `refining_metal` | Refined cobalt metal (cathode, briquettes, rounds) and refined cobalt chemicals |
| cobalt | `powder` | Cobalt powder (extra-fine, submicron) suitable for SmCo and hardmetals |
| cobalt | `recycling` | Cobalt recovery from scrap, batteries or superalloys |
| molybdenum | `mining_concentrate` | Molybdenite concentrate (primary mines or copper by-product) |
| molybdenum | `roasting_chemical` | Roasting to technical molybdic oxide, ferromolybdenum, pure MoO3, ADM, sodium molybdate |
| molybdenum | `metal_powder` | Molybdenum metal powder |
| molybdenum | `mill_products_alloys` | Mo, TZM, Mo-Re, Mo-La mill products, sheet, rod, wire, targets, fabricated parts |
| molybdenum | `recycling` | Spent-catalyst and molybdenum scrap recovery |
| gallium | `primary_extraction` | Primary gallium recovery from alumina (Bayer) liquor or zinc residues |
| gallium | `refining_high_purity` | Refining to 4N-7N gallium |
| gallium | `compounds_wafers` | GaAs, GaN, TMGa and other gallium compounds and wafers |
| gallium | `recycling` | Gallium recovery from GaAs or other scrap |
| germanium | `primary_extraction` | Germanium concentrate from zinc residues or coal fly ash |
| germanium | `refining_chemical` | GeCl4, GeO2 |
| germanium | `metal_high_purity` | Zone-refined germanium metal and ingot |
| germanium | `products_optics_wafers` | Germanium optics blanks, substrates and wafers |
| germanium | `recycling` | Germanium recovery from scrap |
| trader | `trader` | Merchant traders and trading houses |
| trader | `distributor` | Distributors holding inventory and reselling |
| trader | `stockholder` | Stockholders and service centers (warehoused spot metal) |
| trader | `government_stockpile` | Government stockpiles that sell or release material (DLA Strategic Materials, allied stockpiles) |
| lab | `assay_lab` | Grade and chemistry testing (XRF, ICP-OES/MS, GDMS, LECO, etc.) |
| lab | `inspection_sampling` | Independent inspection, sampling, weighing, witnessing, umpire assays |
| lab | `provenance_lab` | Origin and provenance testing (isotope ratios, analytical fingerprinting, forensic trace-element methods) |
| lab | `audit_certification` | Supply-chain audit and chain-of-custody certification (e.g., RMAP assessors) |

## Primary sources read for this scope (all accessed 16 Nov 2026)

- **DFARS Case 2021-D015 final rule.** Revised 225.7018-2, 225.7018-3 and clause 252.225-7052 (MAY 2024). 89 FR 46814, 30 May 2024: https://www.govinfo.gov/content/pkg/FR-2024-05-30/pdf/2024-11513.pdf
- **Clause pages.** DFARS 252.225-7052 on acquisition.gov (our requests timed out; text taken from the Federal Register rule above): https://www.acquisition.gov/dfars/252.225-7052-restriction-acquisition-certain-magnets-tantalum-and-tungsten.
- **10 U.S.C. 4872**, as amended through Pub. L. 119-60: https://www.law.cornell.edu/uscode/text/10/4872
- **FY2026 NDAA, Pub. L. 119-60** (18 Dec 2025), secs. 843, 844 and 848: https://www.govinfo.gov/content/pkg/PLAW-119publ60/html/PLAW-119publ60.htm
- **Executive Order 14415** (20 July 2026): https://www.whitehouse.gov/presidential-actions/2026/07/securing-americas-defense-supply-chains-and-ensuring-domestic-acquisition-of-critical-materials/
- **H.R. 8800**, FY2027 NDAA as engrossed in the House (sec. 1803): https://www.govinfo.gov/content/pkg/BILLS-119hr8800eh/html/BILLS-119hr8800eh.htm
- **H.R. 9073** (introduced 29 May 2026): https://www.govinfo.gov/content/pkg/BILLS-119hr9073ih/html/BILLS-119hr9073ih.htm
- **Class Deviation 2026-O0041 and DFARS 252.225-7961.** We could not retrieve the deviation memo or the 7961 text from DoD: the DPCAP site (acq.osd.mil) returned HTTP 503 and certificate errors. The 7961 details above come from these law-firm and practitioner summaries:
  - Pillsbury, "Time Running Short to Update DFARS Covered Materials Clauses," 21 Oct 2026: https://www.pillsburylaw.com/en/news-and-insights/time-running-short-update-dfars-covered-materials-clauses.html
  - Cartograph, "DFARS 252.225-7961 vs 252.225-7052," 26 Sep 2026: https://www.cartograph.ai/blog/dfars-252-225-7052
  - Faegre Drinker, "Third Quarter 2026 Government Contracts Policy and Regulatory Review," Nov 2026: https://www.faegredrinker.com/en/insights/publications/2026/11/third-quarter-2026-government-contracts-policy-and-regulatory-review
- **Background on the FY2026 NDAA changes and the EO:**
  - Pillsbury, "FY2026 NDAA Sourcing Restrictions," 27 Feb 2026: https://www.pillsburylaw.com/en/news-and-insights/fy2026-ndaa-sourcing-restrictions-critical-minerals-advanced-batteries.html
  - Holland & Knight on EO 14415, 30 July 2026: https://www.hklaw.com/en/insights/publications/2026/07/president-trump-signs-executive-order-on-defense-supply-chains
  - Greenberg Traurig, "Recent Executive Actions Affecting Critical Minerals and Materials," Aug 2026: https://www.gtlaw.com/ar/insights/2026/8/recent-executive-actions-affecting-critical-minerals-and-materials
- **NDAA status:**
  - Trade Compliance Resource Hub, "Congress returns: provisions to watch in the FY2027 NDAA," 2 Nov 2026: https://www.tradecomplianceresourcehub.com/2026/11/02/congress-returns-national-security-and-trade-provisions-to-watch-in-the-fy2027-ndaa/
  - SAFE / The Fuse on House sec. 1801/1803, 9 Jun 2026: https://thefuse.org/ndaa-defense-critical-minerals-policy-sourcing-restrictions/

**Open items to re-check before relying on this scope for a specific contract:**
- the exact 7961 text and any revision after Revision 1;
- whether a DFARS rule adds molybdenum;
- the final FY2027 NDAA text, if enacted.
