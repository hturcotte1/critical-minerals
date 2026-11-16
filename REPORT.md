# Non-China critical-metals supplier map: report

*Research date: 16 November 2026. Written for a non-technical reader. The data behind every statement is in `suppliers.xlsx` / `data/*.csv`, where every row is dated and sourced.*

## Summary

**What we built.**
- **495 supplier rows** (one per company, facility and production stage) across 58 countries.
- **149 known supply agreements.**
- **140 facilities inside China, Russia, Iran and North Korea**, listed for screening paperwork.
- **826 cited sources.**
- Every row has a compliance screen, a capacity-commitment flag, a broker-fit score and its sources.

| Chain | Supplier rows | Notes |
|---|---|---|
| NdFeB (rare-earth magnets) | 133 | mining 37, separation 29, metal/alloy 12, sintered magnets 25, bonded 6, recycling 19, iron/boron 3, substitutes 2 |
| Tungsten | 79 | all 5 stages |
| Molybdenum | 63 | added because the FY2026 NDAA put it in the statute |
| Tantalum | 57 | all 5 stages |
| Cobalt (for SmCo) | 35 | |
| Gallium / germanium | 27 / 21 | covered from 18 Dec 2027 |
| SmCo magnets | 17 | |
| Traders, stockholders, stockpiles | 34 | |
| Labs | 29 | |

**The rule, as of 16 November 2026** (details in `docs/scope.md`):
- **The ban.** From 1 January 2027, DoD material may not be mined, refined, separated, melted or produced in China, Russia, North Korea or Iran. Under the new deviation clause 252.225-7961 (June 2026), the upstream part applies to contracts awarded from that date. The older 252.225-7052 clause applies it to deliveries.
- **Molybdenum is now covered by statute**, and gallium and germanium follow on 18 December 2027.
- **Executive Order 14415** ends most non-availability waivers from 1 January 2027 and prepares a ban on suppliers under covered-country ownership or influence.
- **No delay has been enacted.** The House FY2027 NDAA would rewrite the regime, including a test requiring 50% of cost from US-owned producers for key materials, but it is not law.

### The five most important findings

1. **The choke points are a handful of midstream steps, not mining or magnet-making in general.**
   - Each choke point has only a few non-China plants, and most of their output is already committed:
     - separated **dysprosium/terbium** and heavy rare earth metal;
     - **samarium metal**: one Western plant, short of feed;
     - **US tungsten APT** conversion: none independent until about 2029;
     - **molybdenum powder** with a documented feed;
     - **primary gallium**: about 3 t outside China in 2025.
   - These are where a broker who can find and document supply is worth the most.
2. **"Made outside China" is not the same as compliant.**
   - Of 432 producing-chain rows, only **117 are operating and screen as likely compliant**. Another 200 are `at_risk`, mostly because their feed is Chinese or undisclosed.
   - Examples:
     - Japan's TDK runs on stockpiled Chinese rare earths.
     - Kazakhstan's Ulba tantalum plant now buys Russian feed.
     - A.L.M.T. (Japan) has a molybdenum plant in China, 70% owned by Xiamen Tungsten.
     - A "Korean" tungsten smelter appears to be a Xiamen Tungsten affiliate.
     - Western gallium refiners run on Chinese crude.
   - Origin cannot be proven by lab testing once material is refined. Documentation and witnessed sampling are the product.
3. **The US government is the biggest competing buyer, not a seller.**
   - DLA has stopped publishing stockpile disposals. Instead it signed purchase contracts:
     - tungsten from Elmet, up to $2B;
     - cobalt from Glencore, up to $900M (reported);
     - gallium from ATALCO, up to $350M;
     - tantalum ingot from GAM, up to $100M.
   - DoD/DoW took equity in MP Materials, Elmet ($450M), ATALCO and Alcoa's gallium plant.
   - Project Vault ($10B EXIM) is stockpiling for manufacturers.
   - Compliant spot inventory at distributors is essentially unavailable: only one (MCE) even claims DFARS-compliant stock.
4. **Ownership changed fast in 2024-2026; check it on every deal.**
   - Changes by buyer:
     - Energy Fuels: bought ASM's Korean Metals Plant; buying VAC/e-VAC.
     - USA Rare Earth: bought Less Common Metals, Serra Verde and all of Round Top.
     - Mitsubishi Materials: H.C. Starck Tungsten.
     - Sandvik: Buffalo Tungsten.
     - Molymet: Rhenium Alloys.
     - Elmet: buying ams OSRAM's tungsten/molybdenum plant.
   - Chinese owners now hold assets that sit *outside* China:
     - Mineração Taboca (Brazil tantalum, CNMC);
     - Tanco (Canada, Sinomine);
     - Peak's Ngualla (Tanzania, Shenghe);
     - Boguty (Kazakhstan tungsten);
     - Las Bambas and Toromocho (Peru molybdenum).

     These pass today's location test but are exposed to the coming ownership tests.
5. **There is real, uncommitted volume to broker for 2027-2028, mostly at mid-size, newly funded producers:**
   - **e-VAC** (2,000 t/yr magnets, freed by GM's exit);
   - **USA Rare Earth Stillwater** (magnets, no named buyers);
   - **Ucore** (heavy rare earth separation);
   - **Iluka Eneabba** (~90% uncommitted from 2028);
   - **Centerra's Langeloth roaster** (idle molybdenum capacity);
   - **Buffalo Tungsten** and **EQ Resources** (tungsten);
   - **PLS** (tantalite with no buyer);
   - **METLEN** and **ATALCO** (gallium);
   - **Electron Energy** (SmCo) and **LS Eco Energy Vietnam** (samarium metal);
   - **Jervois Brazil** (cobalt).

### The biggest gaps

These stages have zero or near-zero compliant supply in 2027 (full table in section 10):
- uncommitted Dy/Tb oxide and any heavy rare earth metal;
- samarium metal and SmCo recycling;
- ferroboron;
- independent US tungsten APT;
- primary gallium;
- US refined cobalt;
- validated origin testing for refined products.

---

## How to read this report

- **"Compliant"** means passing the strict 2027 test: no mining, refining, separation, melting or production in China, Russia, North Korea or Iran at any stage, including recycled feed. It is our screening judgment from public information (column `dfars_7052_assessment`), not legal advice.
- **"At risk"** usually means the plant is outside the covered countries but either buys feed of undisclosed or Chinese origin, or has Chinese, Russian or other covered-country ownership or financing.
- **The broker-fit score (1-5)** rates how likely a supplier is to sell through us:
  - higher for small and mid-size firms with uncommitted volume, a clean profile, output in 2027-28, and signs they are seeking buyers or capital;
  - lower for captive, fully committed or non-compliant suppliers.
- **"Top 10 broker prospects"** lists in each chain are drawn mainly from the highest scores. A few entries are placed by judgment, for timing or strategic importance; for example, BGR's origin-fingerprinting method ranks above higher-scored grade labs. Each table shows the row's ID and score, so you can find it in `suppliers.xlsx`.
- **Capacity figures** are in the unit the source used. Where nobody publishes a number, we say "unknown" rather than estimate.

---

## 1. NdFeB magnets (neodymium-iron-boron)

**Bottom line:**
- **The tightest point is the heavy rare earths, dysprosium (Dy) and terbium (Tb), and the metal and alloy step.** Magnet-making capacity is not the constraint.
- **Lynas is the only commercial non-China producer of separated Dy and Tb.** It made 23 t in the September 2026 quarter, against about 2,000 t of NdPr, and most of that is pre-committed to Japan (JARE).
- **Non-China heavy-rare-earth feed is mostly locked up:**
  - Serra Verde (Brazil) sells 100% to a US-government-backed buyer.
  - Caldeira (Brazil) goes to Lynas.
  - Colossus (Brazil) sends about 70% to Solvay.
- **Downstream:** USA Rare Earth said its Q3 2026 output was capped by a shortage of non-China dysprosium oxide, priced at 14-16 times the Chinese price.
- **Magnet capacity outside China in 2027 is about 22,000-25,000 t/yr** (sintered nameplate, an order-of-magnitude estimate). Only about 1,000-3,000 t/yr of it can be shown to run on a fully non-China mine-to-metal chain, mostly MP Materials, which is committed.
- **The large Japanese makers disclose no China-free sourcing:** Shin-Etsu, Proterial and Daido are marked `at_risk`. Shin-Etsu runs a 3,000 t/yr alloy plant in China, and VAC's German plant buys Chinese alloy flake. TDK said in February 2026 that its magnet production runs on stockpiled Chinese rare earths, so it is marked `likely_noncompliant`.
- **The clause names iron and boron too.** Boron is plentiful outside China (Rio Tinto in California, Eti Maden in Turkey). But we could not verify any non-China ferroboron producer, and the US makes none.

**Who matters at each stage (outside covered countries)**

| Stage | Key suppliers |
|---|---|
| Mining / concentrate | MP Materials Mountain Pass (US, ~50,700 t REO in 2025, captive); Lynas Mt Weld and Kalgoorlie (Australia, captive); Serra Verde (Brazil; bought by USA Rare Earth Sep 2026; 100% sold to US SIIE ~15 years with price floors); Lindian Kangankunde (Malawi, first concentrate Dec 2026, Stage 1 allocated); merchant intermediates in 2027 from **Hastings/BZNM Kabin Buri** (Thailand, 12,000 t/yr MREC, uncommitted) and **Pensana Longonjo** (Angola); captive 2028+ feed from Donald, Goschen, Colossus, Caldeira and Nolans; IREL (India, state-captive). *Flagged:* Peak Rare Earths' Ngualla mine (Tanzania), now owned by China's Shenghe; Myanmar's Kachin clays (separated in China) |
| Separation (NdPr; Dy/Tb) | **Lynas Malaysia** (nameplate 10,800 t/yr NdPr; Dy since May 2025, Tb since June 2025; heavy-RE expansion late 2027); **MP Mountain Pass** (~6,075 t/yr NdPr design; 200 t/yr Dy+Tb circuit commissioning, mostly captive); **Energy Fuels White Mesa** (Utah; up to ~1,000 t NdPr in campaigns; heavy-RE expansion 2028); **Iluka Eneabba** (Australia; 5,500 t NdPr + 750 t Dy/Tb; commissioning mid-2027; ~90% uncommitted); **Caremag** (France; ~600 t Dy+Tb + ~800 t NdPr; start end-2026; partly committed); **Ucore** (Louisiana; 600 t/yr medium/heavy REE from 2027); SRC Saskatoon (Canada); NPM Silmet (Estonia); Solvay La Rochelle (France); Phoenix Tailings (NY, 2027-28); Aclara Dynamo (Louisiana, 2028); Arafura Nolans (Australia, FID May 2026) |
| Metal and alloy | **Korean Metals Plant** (Energy Fuels since Aug 2026; 1,300 t/yr alloy rising to 3,600 t/yr; the main merchant seller, likely to become captive to VAC); **Less Common Metals** (UK; USA Rare Earth-owned; increasingly captive); MP Fort Worth (captive); SRC Saskatoon (~525 t/yr NdPr metal from 2027, ~80% to REalloys); Phoenix Tailings (NH); heavy-RE metal: REalloys (2028, ~30 t Dy + 15 t Tb) |
| Sintered magnets (GBD noted in data) | **MP Independence** (Fort Worth, ~1,000 t, GBD; 10X plant 2028 under DoD offtake); **e-VAC** (Sumter SC, 2,000 t/yr; GM terminated its ~90% offtake in Oct 2026, now in arbitration; DLA-qualified); **USA Rare Earth Stillwater** (OK, 600 t/yr, rising to 1,200 t/yr in Q2 2027); **Noveon** (TX, recycled feed, DLA-qualified); **Vulcan Elements** (NC, 10,000 t/yr Benson plant commissioning 2027); **Neo Narva** (Estonia, 2,000 t/yr since Sep 2026); VAC (Germany, Slovakia, Finland); Star Group (Korea); Shin-Etsu, TDK, Proterial (Japan/Vietnam; Proterial planning 1,200 t/yr in India) |
| Bonded / hot-deformed | Neo Magnequench Korat (Thailand, 2,000 t/yr powder, the only sizeable non-China MQ powder plant); Daido Electronics (Japan, Thailand); Aichi Steel; MS-Schramberg (Germany); Magneti Ljubljana (Slovenia) |
| Recycling | **Noveon** (US milling and sintering, which fits the recycled-magnet exemption); **HyProMag** (UK and Germany operating; US plant in Texas from 2027-28, EXIM LOI $92M); **Cyclic Materials** (Mesa AZ, Kingston ON); ReElement (Indiana, DoD $25M); Caremag; smaller demonstration plants |
| Iron and boron | Boron: Rio Tinto/U.S. Borax (California), Eti Maden (Turkey). Ferroboron: **no verified non-China producer**. High-purity iron: Hertha Metals (Texas, under construction) |
| Rare-earth-free substitute | **Niron Magnetics** (iron nitride; 1,500 t/yr Sartell MN plant under construction; DoW $150M conditional) |

**Uncommitted non-China capacity for 2027** (estimates; basis in `data/staging/ndfeb_*/chain_notes.md`):
- **Separated NdPr oxide:** roughly 1,000-3,000 t genuinely available to a broker. Likely 2027 non-China output is ~13,000-15,000 t, but Lynas, MP, Energy Fuels and Caremag have committed most of it. From 2028, Iluka's ~90% uncommitted output (~4,000+ t/yr NdPr) becomes the largest pool.
- **Separated Dy+Tb oxide:** only tens of tonnes uncommitted. Ucore and SRC are the main possible sources. Iluka and Energy Fuels add supply from 2028.
- **Sintered magnets:** about 3,000-4,000 t/yr of identifiable uncommitted capacity:
  - e-VAC's ~1,800 t freed by GM's exit;
  - USA Rare Earth's 600-1,200 t;
  - parts of Noveon, Narva and Vulcan's pilot plant.

  Almost none of it has a documented non-China oxide-to-metal chain yet. **Closing that documentation gap is the broker's job.**
- **Merchant intermediates:** Hastings/BZNM MREC (12,000 t/yr from Q2 2027) and Pensana (2027), both uncommitted.
- **Defense demand for scale:** DLA's FY2025 plan listed possible purchases of 450 t of NdFeB magnet block and 300 t of NdPr oxide.

**Ownership changes in 2026 to know about:**
- Energy Fuels closed its acquisition of ASM, including the Korean Metals Plant, on 28 August 2026. Its acquisition of VAC/e-VAC is pending, with closing expected in early 2027.
- USA Rare Earth bought Less Common Metals (November 2025) and Serra Verde (September 2026).
- Lynas is acquiring Meteoric (Caldeira), and Wyloo now owns 60% of Yangibana.
- China's Shenghe owns Peak (Ngualla) and holds about 3% of MP Materials, a passive stake.

<!-- TOP10_ndfeb -->
**Top 10 broker prospects (NdFeB)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | ND-065 | Ucore Louisiana LLC (Ucore Rare Metals) - Louisiana Strategic Metals Complex (SMC), England Airpark (United States) | 5 | DoW-funded medium/heavy-RE separation from 2027, uncommitted; needs both feed and customers |
| 2 | ND-093 | e-VAC Magnetics LLC - eVAC Sumter plant (United States) | 4 | 2,000 t/yr sintered, mostly uncommitted after GM's exit (Oct 2026); DLA-qualified; upstream chain must be documented |
| 3 | ND-100 | USA Rare Earth, Inc. - Stillwater magnet plant (Phase 1a/1b) (United States) | 4 | 600 rising to 1,200 t/yr sintered, no named offtakes; well funded (Commerce CHIPS); needs proof of alloy origin |
| 4 | ND-039 | Iluka Resources Limited - Eneabba Rare Earths Refinery (Australia) | 4 | ~90% of NdPr and Dy/Tb from 2028 uncommitted; Australian-government financed; seeking customers |
| 5 | ND-071 | Australian Strategic Materials - Korean Metals Plant (Energy Fuels subsidiary) - Korean Metals Plant (KMP) (South Korea) | 4 | Main merchant non-China NdFeB alloy and NdPr metal (Energy Fuels); act before it becomes captive to VAC |
| 6 | ND-098 | Noveon Magnetics Inc. - San Marcos magnet plant (United States) | 4 | US recycled route fits the statutory recycled-magnet exemption; DLA-qualified; fresh funding |
| 7 | ND-053 | Rainbow Rare Earths Limited (Phalaborwa) - Phalaborwa Rare Earths Project (South Africa) | 4 | 60% of NdPr uncommitted (Neo has only an MoU); DFC-backed; first production 2028 |
| 8 | ND-001 | Pensana plc (Ozango Minerais, Longonjo) - Longonjo NdPr project (Angola) | 4 | First production 2027, uncommitted, pursuing a US route (EXIM LOI); low confidence |
| 9 | ND-030 | BZNM Co Ltd (Hastings 49%) - Kabin Buri hydrometallurgical plant (Thailand) | 3 | 12,000 t/yr MREC from Q2 2027 with no offtake; verify the African feed origin and the co-owner |
| 10 | ND-133 | Niron Magnetics, Inc. - Sartell full-scale manufacturing plant (United States) | 4 | Rare-earth-free substitute, 1,500 t/yr, uncommitted, DoW-backed; not a covered material, so it sidesteps the rule where the design allows |

Runners-up: Phoenix Tailings (US metal and separation), HyProMag USA (recycling), Vulcan Elements (10,000 t/yr, commissioning 2027), Caremag (Dy/Tb), REalloys/SRC (Dy/Tb metal 2028), Neo Narva (EU magnets).
<!-- /TOP10_ndfeb -->

---

## 2. Tungsten

**Bottom line:**
- **Covered countries dominate mining.** Of about 85,000 t of tungsten mined in 2025, China produced 67,000 t, Russia about 2,000 t and North Korea about 2,000 t. That is roughly 84% (USGS MCS 2026).
- **Mine supply that passes the 2027 test is about 11,600 t W a year.** This excludes Kazakhstan's new Chinese-owned Boguty mine.
- **The real choke point is converting concentrate into APT and oxide, the chemical step before powder.** The US has no independent APT plant.
  - Its existing chemical capacity is captive: Global Tungsten & Powders (owned by Plansee), Niagara Refining (owned by Sumitomo Electric) and Kennametal.
  - The first independent US APT plant is a ~4,000 t/yr joint venture at Springer, Nevada (Elmet, Blue Moon, EQ Resources). It is not due before late 2028 or early 2029.

**Who matters at each stage (outside covered countries)**

| Stage | Key suppliers |
|---|---|
| Mine / concentrate | Masan Nui Phao (Vietnam, ~2,000 t W/yr, plans 5,000-6,000 t); Almonty Sangdong (Korea, first concentrate Sep 2026; ~90% of Phase I sold to GTP for 21 years); Wolfram Bergbau Mittersill (Austria, captive to Sandvik); Panasqueira (Portugal, Almonty); EQ Resources Barruecopardo (Spain) and Mt Carbine (Australia, expanding early 2027); Group 6 Dolphin (Tasmania, ramping up). Next wave: Hemerdon (UK, 2027), Springer (Nevada, Q4 2027), El Moto (Spain, 2029, exclusive to Traxys), Pilot Mountain (Nevada), Mactung and Sisson (Canada) |
| APT / oxide | Masan Tungsten Chemicals (Vietnam, >9,000 t/yr, selling spare capacity); GTP Towanda PA (~10,000-12,000 t/yr oxide, mostly recycled feed); WBH St. Martin (Austria); H.C. Starck Goslar (Germany, Mitsubishi Materials); Japan New Metals (feed origin undisclosed); Niagara Refining (captive) |
| Metal powder | GTP; H.C. Starck; WBH; **Buffalo Tungsten** (NY; merchant powder seller, Sandvik-owned since 2023); **Elmet** Lewiston ME (tungsten powder now) and Coldwater MI (new tungsten furnace ~Q1 2027; DoW-funded fivefold expansion); H.C. Starck Sarnia, Canada (tolls tungsten powder for Elmet); Plansee; Treibacher; Kennametal (captive); Japanese/Korean makers (feed origin undisclosed) |
| Heavy alloy and parts | Plansee group (CIME Bocuze, France, penetrator material; Plansee Composite Materials; Mi-Tech Indianapolis); Elmet Euclid OH and Lewiston ME; Wolfmet (UK); Wolfram Industrie (Germany); A.L.M.T. (Japan) |
| Scrap recycling | GTP (largest US recycler); H.C. Starck Goslar (expanding to ~7,000 t/yr by 2028); WBH; Japan New Metals; Tungco (Kentucky); GTP Finland |

**The real bottleneck:** the chemical step (APT/oxide) and the primary concentrate behind it.
- **Elmet is now the US government's tungsten platform.** In September 2026 it received a $450M Department of War investment (preferred equity plus warrants for up to 19.9%). DLA also gave it a five-year purchase contract of up to $2B for concentrate and sodium tungstate.
- **Prices show the squeeze.** Rotterdam APT rose from US$331 to US$675/mtu during 2025 (USGS), and European APT averaged about US$2,800/mtu in Q3 2026 (Almonty).

**Uncommitted non-China capacity for 2027:** no defensible total exists, because most producers publish neither capacity nor contracts. Identifiable free volume:
- Almonty Sangdong Phase II: about +2,300 t/yr concentrate, outside the GTP contract.
- Masan's spare conversion capacity, offered as tolling.
- Tungsten West Hemerdon, starting 2027; offtakes not found.
- EQ Resources Mt Carbine expansion: about +500 t WO3/yr, no offtake found.
- Buffalo Tungsten powder and Tungco scrap: volumes not published.

**Red flags for screening:**
- Tungamoy Metals, an RMAP-listed "Korean" smelter, appears from its Korean name to be a Xiamen Tungsten affiliate.
- Boguty in Kazakhstan is Chinese-owned.
- Several Asian APT plants on public smelter lists have owners we could not verify: Lianyou ×2 (Taiwan), Philippine Bonway, Philippine Chuangxin, Tungsten Vietnam JSC and KENEE.

<!-- TOP10_tungsten -->
**Top 10 broker prospects (tungsten)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | W-050 | Buffalo Tungsten Inc. - Buffalo Tungsten Depew plant (United States) | 4 | Merchant W and WC powder made from non-Chinese oxide, sold to outside customers of any size; owned by Sandvik since Dec 2023 |
| 2 | W-001 | EQ Resources Limited (Mt Carbine) - Mt Carbine tungsten mine (Australia) | 4 | Small Australian producer ramping up, with an A$39M expansion due early 2027 and no offtake found |
| 3 | W-018 | Tungsten West plc (Hemerdon) - Hemerdon (Drakelands) tungsten-tin mine (United Kingdom) | 4 | UK concentrate from 2027, freshly funded; offtakes not found |
| 4 | W-052 | Elmet Technologies LLC (Lewiston) - Elmet Lewiston plant (United States) | 4 | US tungsten powder now and a DoW-funded fivefold expansion; much output tied to its own defense programs |
| 5 | W-064 | Elmet Technologies LLC (Euclid) - Elmet Euclid plant (former H.C. Starck Solutions) (United States) | 4 | US heavy-alloy and plate producer expanding with DoW money; clean non-PRC feed |
| 6 | W-038 | Masan Tungsten Chemicals (Masan High-Tech Materials; formerly Nui Phao H.C. Starck Tungsten Chemicals) - Nui Phao tungsten chemical plant (Vonfram Masan) (Vietnam) | 4 | Largest non-China APT/oxide plant, selling spare capacity as tolling; document origin lot by lot |
| 7 | W-079 | Tungco Inc. - Tungco Madisonville facility (United States) | 4 | Independent US scrap processor with uncommitted volumes; scrap-origin paperwork needed for the recycled route |
| 8 | W-013 | Almonty Korea Tungsten Corp. (AKTC) - Sangdong Tungsten Mine and processing plant (South Korea) | 3 | Phase II (~+2,300 t/yr concentrate, 2027) is outside the 21-year GTP contract |
| 9 | W-002 | Group 6 Metals Limited (Dolphin) - Dolphin Tungsten Mine and processing plant (Australia) | 3 | Small, clean Tasmanian producer ramping up; existing offtakes may be partial |
| 10 | W-022 | Nui Phao Mining Company (Masan High-Tech Materials) - Nui Phao polymetallic mine (Vietnam) | 3 | Largest non-China mine, expanding and openly seeking strategic investors and offtakers |

Runners-up: Panasqueira (Almonty, Portugal), Guardian Pilot Mountain (Nevada, later), Wolfmet (UK) and Wolfram Industrie (Germany) for heavy alloy, Blue Moon Springer (Nevada, Q4 2027, partly committed to Elmet).
<!-- /TOP10_tungsten -->

---

## 3. Tantalum

**Bottom line:**
- **Documentable mine supply is thin.** Of about 2,500 t of tantalum mined in 2025, the DRC (1,300 t), Rwanda (400 t) and Nigeria (390 t) supplied about 84%. That output is mostly artisanal and mostly processed in China. Documentable non-covered mine supply is a few hundred tonnes a year.
- **Most past US metal imports would fail the 2027 test.** US imports of tantalum metal and powder in 2021-24 came 47% from China and 16% from Kazakhstan. Kazakhstan means Ulba, which now runs on Russian feed: its 2025-26 due-diligence report records supplier audits at Solikamsk and Lovozero in Russia.
- **Global Advanced Metals (GAM) in Boyertown, PA is the only US ore-to-metal processor with a documented non-covered (Australian) feed.** DLA treats it as the sole source for tantalum ingot.

**Who matters at each stage (outside covered countries)**

| Stage | Key suppliers |
|---|---|
| Mine / concentrate | GAM (Greenbushes and Wodgina, Australia; captive to Boyertown); **PLS Pilgangoora** (Australia, ~220,600 lb concentrate in FY26, no buyer disclosed); AMG Mibra (Brazil); Andrada Uis (Namibia); Trinity Metals Musha (Rwanda, DFC-backed); Eastinco/Aterian (Rwanda, marketed by Wogen). *Flagged:* Mineração Taboca (Brazil) is owned by China's CNMC since 2025; Tanco (Canada) is owned by Sinomine; Greenbushes' operator Talison is controlled through China's Tianqi |
| Chemical (K-salt, oxide) | GAM Boyertown (captive); TANIOBIS Goslar and Map Ta Phut (JX Advanced Metals; feed origin not public); **AMG Brasil** (oxides from its own mine); Metallurgical Products India; NPM Silmet (Estonia); Mitsui Kinzoku and Taki Chemical (Japan) |
| Powder / ingot | GAM Boyertown (DLA ingot supplier) and Aizu (Japan); TANIOBIS (Germany, Thailand, Japan); Materion Newton MA (feed undisclosed); NPM Silmet; Metalysis (UK, small) |
| Alloys and mill products | GAM; ATI (Albany, OR); Materion; Plansee; STEREON Metals (Germany, ex-H.C. Starck Hermsdorf); sputtering-target makers Solstice (ex-Honeywell) and JX |
| Recycling | D Block Metals (NC); Exotech (FL); Avon Specialty Metals (UK); QuantumClean; TANIOBIS closed loop |

**The real bottleneck:** primary tantalum powder and ingot, and the chemical step behind them, made from feed whose origin can be documented.
- **Feed origin is opaque almost everywhere.** Outside GAM (Australian feed) and AMG (its own Brazilian mine), almost every processor buys intermediates of undisclosed origin. That includes TANIOBIS, Materion, Mitsui, Taki, NPM Silmet, ATI, Plansee and the target makers.
- **Prices hit 20-year highs in 2026.** The trigger was the Rubaya landslides in the DRC.

**Uncommitted non-China capacity for 2027:** unknown. No non-China processor publishes tantalum capacity or its contract book.
- The one quantified flow that appears free is PLS's by-product tantalite.
- New processing capacity: TANIOBIS Thailand reaches about 1.5× its 2022 level from early 2027, and GAM is expanding purification (EXIM $25M, August 2026).

**DLA as a competitor for supply:** DLA holds a sole-source tantalum ingot contract with GAM (ceiling $100M; orders of $8.6M and $15.1M so far). It also holds a niobium ingot contract (up to $50M).

<!-- TOP10_tantalum -->
**Top 10 broker prospects (tantalum)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | TA-003 | PLS Group Limited (Pilbara Minerals) - Pilgangoora operation (Pilgan and Ngungaju plants) (Australia) | 4 | Clean Australian by-product tantalite (~220,600 lb concentrate in FY26) with no disclosed buyer |
| 2 | TA-018 | AMG Brasil S.A. - Materiais Especiais unit, Sao Joao del Rei plant (BR-383 km 94) (Brazil) | 4 | Mid-size, clean mine-to-oxide chain (Mibra), no disclosed oxide offtakes, rising tantalum volumes |
| 3 | TA-014 | Uis Tin Mining Company (Pty) Ltd (Andrada Mining) - Uis mine and tin processing plant (Namibia) | 4 | Small Namibian producer marketing traceable, conflict-free concentrate; AIM-listed and seeking capital |
| 4 | TA-016 | Trinity Metals Limited (Trinity Musha) - Musha mine (incl. Ntunga area), 6,094 ha concession (Rwanda) | 4 | US-backed (DFC, TechMet) Rwandan producer, expanding and courting US buyers |
| 5 | TA-022 | Metallurgical Products India Pvt. Ltd. (MPIL) - MPIL Taloja plant (T-27 MIDC Taloja) (India) | 4 | Small independent RMAP-conformant K-salt/oxide producer; feed documentation needed |
| 6 | TA-054 | D Block Metals, LLC - D Block Metals Lincolnton HQ and main processing facility (1808 Indian Creek Rd); second site Gastonia NC (United States) | 4 | US RMAP-conformant tantalum recycler; fits the statutory recycled route if scrap origin is documented |
| 7 | TA-055 | Exotech, Inc. - Exotech Pompano Beach facilities (1851 Blount Road; three buildings, ~58,000 sq ft) (United States) | 4 | Independent US scrap processor that buys and sells; recycled route with origin paperwork |
| 8 | TA-044 | STEREON Metals Hermsdorf GmbH (formerly QSIL Metals Hermsdorf; ex-H.C. Starck Hermsdorf) - STEREON Metals Hermsdorf plant (sister site Calne, UK) (Germany) | 4 | Mid-size EU mill-product and target maker with large stock for aerospace and defense |
| 9 | TA-040 | Metalysis Ltd - Metalysis production site (Rotherham area, South Yorkshire) (United Kingdom) | 4 | Small UK producer marketing tantalum and C-103 powders to Western defense buyers |
| 10 | TA-053 | Avon Specialty Metals Ltd. - Avon Specialty Metals (Gloucester area, England; site address not verified) (United Kingdom) | 4 | RMAP-conformant recycler in a qualifying country (UK) |

Runners-up: Resind (Brazil, slag-derived), Globe Metals Kanyika (Malawi, 2028), Eastinco/Aterian via Wogen (Rwanda), and Global Advanced Metals Boyertown. GAM is the key compliant US source, but it is large and its ingot output is tied to DLA.
<!-- /TOP10_tantalum -->

---

## 4. SmCo magnets (samarium-cobalt)

**Bottom line:**
- **Samarium metal is the tightest point in any chain we mapped.**
  - Less Common Metals (UK, owned by USA Rare Earth since November 2025) is the only established Western producer. In Q3 2026 its owner reported that samarium shortages were limiting output. The next ~30% capacity step is Q3 2027.
  - The only near-term addition is LS Eco Energy's Vietnam plant: 240 t/yr, with trial production in December 2026 on Lynas oxide.
- **Samarium oxide outside China is new and committed.** Lynas made its first samarium oxide only in March 2026, and half of its heavy-rare-earth output is committed to Japan (JARE) to 2038. Solvay supplies "limited volumes".
- **The 2027 test also covers cobalt.** A SmCo magnet made from China-refined cobalt fails.
- **No SmCo magnet maker in the file rates `likely_compliant`.**
  - Arnold discloses Chinese samarium through its Ganzhou joint venture.
  - EEC/Permag, VAC and Magneti Ljubljana do not disclose where their samarium or cobalt comes from.
  - IREL's Indian plant is captive to Indian programs.

**Who matters at each stage (outside covered countries)**

| Stage | Key suppliers |
|---|---|
| Samarium oxide | Lynas Malaysia (since March 2026); Solvay La Rochelle (France, small volumes, feed origin undisclosed); IREL Aluva (India, state-owned). Planned: Energy Fuels White Mesa (2028), Ucore Louisiana (DoW $4.6M) |
| Samarium metal | **Less Common Metals** (UK, the only operating Western plant, capacity-short); **LS Eco Energy / LSCV** (Vietnam, 240 t/yr, trial production December 2026). Planned: REalloys (Ohio, 300 t/yr Sm+Gd, design stage) |
| SmCo alloy | Less Common Metals; Santoku (Japan; single source); in-house at Arnold |
| SmCo magnets | **Electron Energy / Permag** (Landisville, PA; calls itself the only US SmCo maker; doubling capacity; AS9100, ITAR); Arnold (Lupfig, Switzerland; new Thailand line mid-2027); VAC (Hanau, Germany; Energy Fuels acquisition pending); Magneti Ljubljana (Slovenia); IREL Visakhapatnam (India, 3 t/yr, captive) |
| Recycling | **None found outside China.** This matters because the statute exempts recycled SmCo magnets only if milling and sintering happen in the US |

**Not confirmed:** we could not confirm that Shin-Etsu, TDK, Proterial or TOKIN still make SmCo magnets. Shin-Etsu's own magnet site lists only NdFeB. We also found no current SmCo product from Permanent Magnets Ltd (India) or Thomas & Skinner, which appears to be a distributor.

**Uncommitted capacity for 2027:** unknown at every stage. No producer publishes SmCo capacity. EEC is doubling and Arnold Thailand doubles Arnold's capacity by mid-2027, but both need compliant samarium first.

<!-- TOP10_smco -->
**Top 10 broker prospects (SmCo)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | SM-017 | Electron Energy Corporation (EEC) - EEC Landisville plant (United States) | 4 | The only US SmCo maker; doubling capacity and seeking compliant samarium and cobalt |
| 2 | SM-008 | LSCV (LS Eco Energy Vietnam subsidiary) - LSCV rare earth metal plant (Vietnam) | 4 | 240 t/yr samarium metal from 2027 on Lynas oxide, aimed at defense SmCo demand |
| 3 | SM-006 | Less Common Metals Ltd (LCM) - LCM Hooton Park plant, Ellesmere Port (United Kingdom) | 3 | The only operating Western samarium metal plant; supply tight until the Q3 2027 expansion |
| 4 | SM-010 | Less Common Metals Ltd (LCM) - LCM Hooton Park plant, Ellesmere Port (United Kingdom) | 3 | Key non-China SmCo alloy source; cobalt origin must be documented |
| 5 | SM-001 | Solvay SA (La Rochelle rare earths plant) - Solvay La Rochelle plant (France) | 3 | One of few non-China samarium oxide producers, able to scale; feed origin needs verifying |
| 6 | SM-003 | Lynas Malaysia Sdn Bhd - Lynas Advanced Materials Plant (LAMP), Gebeng (Malaysia) | 3 | Clean samarium oxide since Mar 2026; half of heavy-RE output committed to JARE |
| 7 | SM-014 | Arnold Magnetic Technologies AG - Arnold Lupfig SmCo plant (RECOMA) (Switzerland) | 3 | Established aerospace/defense SmCo maker that must replace Chinese samarium; Thailand line doubles capacity mid-2027 |
| 8 | SM-013 | Magneti Ljubljana d.d. - Magneti Ljubljana plant (Slovenia) | 3 | Independent EU SmCo maker that may welcome buyers; ownership and inputs need diligence |
| 9 | SM-005 | Ucore Rare Metals Inc. (Louisiana Strategic Metals Complex) - Louisiana Strategic Metals Complex (SMC) (United States) | 3 | Small, government-funded future Sm/Gd separation source (Louisiana) |
| 10 | SM-011 | Vacuumschmelze GmbH & Co. KG (VAC) - VAC Hanau headquarters plant (Germany) | 3 | Large EU SmCo maker; Energy Fuels acquisition pending (early 2027) could change its sourcing |

Also watch REalloys (Ohio, samarium metal, design stage).
<!-- /TOP10_smco -->

---

## 5. Cobalt (input for SmCo magnets)

**Bottom line:**
- **The issue is proving origin, not quantity.** Refined cobalt made outside China is available from Vale (Canada), Glencore (Norway, Australia), Sumitomo Metal Mining (Japan), Managem (Morocco) and Umicore (Belgium, Finland).
- **The risk is the feed.** The DRC mined about 73% of world cobalt in 2025 and Indonesia 14%. Much of both is Chinese-owned, for example CMOC's Tenke Fungurume and Kisanfu mines and Chinese-partnered nickel-cobalt (HPAL) plants in Indonesia. A non-China refiner must show its feed did not come from those.
- **Only two non-China cobalt refiners appear on Apple's public list,** both Umicore's, against 13 in China.
- **The cleanest chains are refiners fed by their own mines:**
  - Sumitomo Metal Mining (its own Philippine nickel-cobalt plants);
  - Managem (its own Bou-Azzer mine);
  - Murrin Murrin (Australian ore);
  - Vale (Canadian nickel ores).
- **Sherritt (Canada) is unusable.** Its cobalt is Cuban, which US embargo rules bar, and its production was halted in 2026.

**Who matters at each stage**

| Stage | Key suppliers |
|---|---|
| Mining / intermediate | Glencore KCC and Mutanda (DRC); Sumitomo Coral Bay and Taganito (Philippines, captive); Managem Bou-Azzer (Morocco); Eagle (Michigan, concentrate exported). *Flagged:* CMOC's Tenke Fungurume and Kisanfu (DRC), and Harita/Obi HPAL in Indonesia (Chinese partner) |
| Refined metal | Vale Long Harbour and Port Colborne (Canada); Glencore Nikkelverk (Norway) and Murrin Murrin (Australia); Sumitomo Niihama (Japan); Managem (650 t cathode); Umicore Olen. Coming: **Jervois São Miguel Paulista** (Brazil, 2,000 t/yr cathode from late 2027, uncommitted, US owner) |
| Powder | Jervois Finland (Kokkola; fine powders; US-owned since May 2025); Umicore |
| Recycling | Redwood Materials; Jervois Finland and Umicore (hardmetal scrap). Planned: Nth Cycle |

**Government activity:**
- DLA's August 2025 cobalt tender (7,480 t, up to $500M) was cancelled in October 2025.
- A later DLA cobalt contract with Glencore of up to $900M (May 2026) is reported by Argus but was not independently verified.
- Electra Battery Materials (Ontario) makes battery-grade sulfate from H2 2027. That product is not suitable for SmCo.

<!-- TOP10_cobalt -->
**Top 10 broker prospects (cobalt for SmCo)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | CO-017 | Jervois group - Sao Miguel Paulista (SMP) refinery - Sao Miguel Paulista nickel-cobalt refinery (Brazil) | 4 | ~2,000 t/yr uncommitted cobalt cathode from late 2027 under a US-controlled owner; screen the feed |
| 2 | CO-030 | Jervois Finland Oy - Jervois Finland Kokkola refinery (Finland) | 4 | One of few non-China fine cobalt powder makers, US-owned; feed probably CMOC-linked, so document each lot |
| 3 | CO-027 | Managem S.A. (CMBA cobalt cathode) - Managem cobalt cathode plant (hydrometallurgical; site not named on product page) (Morocco) | 4 | Small, clean primary-cobalt cathode from its own Moroccan mine |
| 4 | CO-023 | Jervois Finland Oy - Jervois Finland Kokkola refinery (Finland) | 4 | Operating non-China cobalt refiner selling to aerospace and defense; same feed caveat |
| 5 | CO-021 | Vale Base Metals - Long Harbour Processing Plant - Long Harbour Processing Plant (Canada) | 3 | Clean Canadian electrolytic cobalt rounds; large seller with direct customers |
| 6 | CO-022 | Vale Base Metals - Port Colborne refinery - Port Colborne refinery (Canada) | 3 | Clean Canadian electrolytic cobalt; large seller |
| 7 | CO-016 | Umicore Olen (Cobalt & Specialty Materials) - Umicore Olen plant (Belgium) | 3 | Major non-China cobalt metal and powder supplier with audited sourcing; large group |
| 8 | CO-015 | Glencore - Murrin Murrin Operations - Murrin Murrin (Australia) | 2 | Clean integrated Australian cobalt, marketed directly by Glencore |
| 9 | CO-018 | Electra Battery Materials Corporation - Electra cobalt refinery, Temiskaming Shores (Canada) | 3 | Only planned North American cobalt refinery (H2 2027); sulfate, so not SmCo grade |
| 10 | CO-034 | Nth Cycle, Inc. - Nth Cycle new refining facility (DOE-selected; site not stated) (United States) | 3 | Small DOE-backed US cobalt recycler; site and timing not set |

Sherritt (Canada) is excluded in practice: its cobalt is Cuban-origin and barred by the US embargo.
<!-- /TOP10_cobalt -->

---

## 6. Molybdenum

**Status of the rule:**
- **The statute covers molybdenum now; the DFARS clause does not yet.** The FY2026 defense authorization act added it to the statute on 18 December 2025, but DFARS has not defined which forms count.
- **The forms most likely to be covered are molybdenum metal:** powder, mill products and alloys such as TZM and Mo-Re. The pending House bill names "molybdenum metals, powders, and alloys".
- **Steel additives are an open question.** Whether ferromolybdenum and technical oxide used in steel are covered is unresolved.

**Bottom line:**
- **Mines and roasters are not the constraint.** About 61% of 2025 mine output was outside the covered countries. Molymet (Chile) alone holds about 35% of world roasting capacity.
- **The bottleneck is molybdenum metal powder and mill products, and proof of the oxide feeding them.**
  - Only one non-China plant publishes a powder capacity: Molymet Germany, 1,700 t/yr from Chilean oxide.
  - Most US and Japanese powder and mill-product makers don't disclose their oxide source, so they are marked `at_risk`.
  - China put export controls on molybdenum powders in February 2025.

**Who matters at each stage**

| Stage | Key suppliers |
|---|---|
| Mine / concentrate | Freeport-McMoRan/Climax (Climax, Henderson, Sierrita, Bagdad, Morenci; Cerro Verde, Peru; 92 Mlb in 2025); Codelco; Southern Copper; Antofagasta; Teck; Antamina; Sierra Gorda; Trekor (Gibraltar, BC); Erdenet (Mongolia). Restart: Centerra Thompson Creek (Idaho, mid-2027). *Flagged:* Las Bambas (MMG) and Toromocho (Chinalco), both Chinese-owned in Peru |
| Roasting / chemicals | Molymet (Chile, Mexico, Belgium; 207 Mlb/yr capacity; Plansee now owns 31%); Climax Fort Madison IA, Rotterdam and Stowmarket; **Centerra Langeloth PA** (40 Mlb/yr nameplate, running at about a third); Codelco Molyb; Treibacher; Taiyo Koko |
| Metal powder | **Molymet Germany** (1,700 t/yr); Plansee (captive); A.L.M.T. (Japan); Elmet; Amaero (Tennessee, spherical powder, EXIM-financed); MolymetNos plasma powders |
| Mill products / alloys | Plansee; **Elmet** (Lewiston, Euclid, Coldwater; buying ams OSRAM's German W/Mo plant); Rhenium Alloys (Ohio; Molymet bought it in August 2026); GTP; A.L.M.T.; Toho Kinzoku |
| Recycling | Treibacher (Austria, spent catalysts); Taiyo Koko (Japan); AMG Vanadium (Ohio) |

**Uncommitted non-China capacity for 2027:**
- **Roasting:** about 27-29 Mlb/yr (about 12,000-13,000 t Mo) of idle capacity at Langeloth, Pennsylvania. Thompson Creek's restart will fill part of it from mid-2027.
- **Concentrate:** mostly captive or under long-term tolling contracts. Gibraltar sells at the mine gate.
- **Powder and mill products:** unknown.

**Government:** Elmet received the Department of War's $450M investment (shared with tungsten), plus a DLA contract of about $36M for TZM and Mo/W wire and $4.3M for molybdenum interceptor parts. Amaero has EXIM financing of $22.8M.

<!-- TOP10_molybdenum -->
**Top 10 broker prospects (molybdenum)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | MO-045 | Langeloth Metallurgical Company LLC (Centerra Gold) - Langeloth metallurgical facility (six roasters) (United States) | 5 | ~27-29 Mlb/yr idle US roasting capacity buying third-party concentrate; clean owner. A broker can supply documented feed |
| 2 | MO-048 | Molymet Germany GmbH (formerly Chemiemetall) - Molymet Germany plant (Germany) | 4 | 1,700 t/yr molybdenum powder from Chilean oxide; the clearest compliant powder source |
| 3 | MO-056 | Elmet Technologies LLC - Elmet Lewiston plant and HQ (1560 Lisbon St) (United States) | 4 | US Mo/TZM mill products, DoW- and DLA-backed and expanding; verify feed |
| 4 | MO-060 | Rhenium Alloys LLC (operating as Molymet Alloys) - Rhenium Alloys plant (United States) | 4 | Small US Mo-Re and Mo mill-product maker for defense; new owner (Molymet) investing |
| 5 | MO-050 | Amaero Inc. - Amaero atomization and PM-HIP facility (United States) | 4 | US spherical refractory powders (AS9100, ITAR), EXIM-financed; verify molybdenum feed |
| 6 | MO-061 | Treibacher Industrie AG - Treibacher Althofen works (Austria) | 4 | EU recycled molybdenum (FeMo/FeNiMo) from European spent catalysts |
| 7 | MO-047 | Molymet (MolymetNos) - MolymetNos plasma spheroidization system (Chile) | 4 | New spherical Mo/Re powder line seeking additive-manufacturing customers |
| 8 | MO-042 | Climax Molybdenum Company - Fort Madison Operations (roasting and chemical conversion) (United States) | 3 | Fully US mine-to-pure-oxide/ADM chain (precursor for powder) |
| 9 | MO-052 | Plansee SE - Plansee Reutte works (Austria) | 3 | TZM, ML and MoRe semis made from Molymet oxide; large group |
| 10 | MO-002 | Gibraltar Mines Ltd (Trekor Metals, formerly Taseko Mines) - Gibraltar mine and molybdenum plant (Canada) | 3 | Clean Canadian concentrate sold at the mine gate (Trekor Metals) |

Also watch Centerra Thompson Creek (Idaho, restart mid-2027, captive to Langeloth) and Greenland Resources Malmbjerg (planned).
<!-- /TOP10_molybdenum -->

---

## 7. Gallium and germanium (covered from 18 December 2027)

**Bottom line:**
- **Gallium is the most concentrated supply chain in this report.**
  - In 2025 China produced about 99% of the world's ~900 t of primary gallium.
  - Compliant primary gallium was about 3 t, all in Japan and used in-house.
  - Non-China refiners (DOWA, Indium Corporation, CMK) mostly refine Chinese crude.
- **Rescue capacity is arriving 2026-28 and is mostly spoken for.** About 219 t/yr of new non-China primary capacity is announced:
  - Alcoa Wagerup (Australia): 100 t/yr; DoW equity of about $174M; offtake split among its partners.
  - METLEN (Greece): 50 t/yr from Q3 2027; about 59% not yet contracted.
  - ATALCO (Louisiana): first US primary gallium from a pilot; 50 t/yr target; DoW equity; DLA stockpile contract of up to $350M.
  - ERG (Kazakhstan): 15 t/yr; sold to Mitsubishi.
  - Rio Tinto (Quebec): demonstration plant.
- **Germanium:** non-China supply rests on a few sources:
  - Teck Trail (Canada), fed by Red Dog;
  - Umicore (Belgium, US), partly fed by DRC slag;
  - 5N Plus (Utah);
  - Korea Zinc's new Onsan line, about 10 t/yr from 2027.

  Even Western refiners may hold Chinese germanium: Belgium and Germany took 52% of China's 2025 germanium metal exports.
- **China's export regime:**
  - Licensing for gallium and germanium since August 2023.
  - A ban on exports to the US since December 2024.
  - In November 2025 China suspended the US-specific ban until 27 November 2026, but licensing and the bar on US military end users stayed. We could not confirm whether the suspension has been extended.

**Who matters at each stage**

| Stage | Key suppliers |
|---|---|
| Gallium primary | DOWA/Akita Zinc (Japan, ~3 t, captive); Alcoa Wagerup (construction); METLEN (2027); ATALCO (pilot); ERG Pavlodar (Kazakhstan); Rio Tinto (pilot/demonstration) |
| Gallium refining | DOWA (Japan); Indium Corporation (NY, the only US refiner); CMK (Slovakia, 7N) |
| Gallium compounds and wafers | Freiberger (Germany, GaAs); Sumitomo Chemical/SCIOCS (Japan, GaN); IQE (UK/US); CMK; 5N Plus |
| Gallium recycling | DOWA; Indium Corporation; Neo Rare Metals (Canada); CMK. Planned: Metallium (Texas, DLA), ReElement (Indiana, DoD $25M) |
| Germanium primary | Teck Trail (Canada); STL/Gécamines (DRC, to Umicore); Korea Zinc Onsan (from Q1 2027) |
| Germanium refining, metal, optics | Umicore (Olen, Belgium; Quapaw, OK); Teck; 5N Plus (Utah; DPA $18.1M to raise zone refining to 20 t/yr); **Lattice Materials** (Montana, optics crystals, DPA $18.5M); Photonic Sense (Germany) |

**Uncommitted for 2027:**
- **Gallium:** probably under ~15 t, mainly METLEN and ATALCO's early output. ATALCO's may go first to DLA.
- **Germanium:** Korea Zinc's ~10 t/yr is the only identified free block. It is covered only by a non-binding Lockheed Martin MoU.

<!-- TOP10_gallium_germanium -->
**Top 10 broker prospects (gallium and germanium)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | GA-003 | METLEN Energy & Metals S.A. - Aluminium of Greece plant - Aluminium of Greece alumina refinery - gallium plant (Greece) | 4 | 50 t/yr gallium from Q3 2027, clean EU chain, ~59% not yet publicly contracted |
| 2 | GA-006 | Atlantic Alumina Company, LLC (ATALCO) - Gramercy alumina refinery - primary gallium circuit (United States) | 4 | First US primary gallium (pilot late 2026, 50 t/yr target); only the DLA stockpile contract is public |
| 3 | GE-003 | KEMCO (Korea Zinc subsidiary) - Onsan germanium line - Onsan smelter complex - germanium line (South Korea) | 4 | New uncommitted germanium from 2027 with only a non-binding Lockheed MoU; confirm zinc-concentrate origin |
| 4 | GE-016 | Lattice Materials LLC - Lattice Materials crystal growth and machining facility (~30,000 sq ft) (United States) | 4 | Small ITAR-registered US germanium crystal maker expanding with DPA money |
| 5 | GA-014 | Indium Corporation - Rome and Utica, NY gallium refining facilities (United States) | 3 | The only US high-purity gallium refiner, building non-China feed; could toll-refine compliant crude |
| 6 | GA-013 | CMK, s.r.o. (CMK Ltd.) - Zarnovica plant (Slovakia) | 3 | Small EU 7N gallium refiner that could refine non-China crude (e.g., METLEN) |
| 7 | GE-011 | 5N Plus Inc. - St. George, Utah facility - 5N+ St. George production facility (United States) | 3 | US germanium metal, wafers and optics with three DoD/DoW awards; backlog-constrained |
| 8 | GE-007 | Teck Metals Ltd. - Trail Operations - Trail Operations metallurgical complex (Canada) | 3 | The cleanest primary GeO2/GeCl4 source (Red Dog feed); large, expansion undated |
| 9 | GE-004 | Blue Moon Metals Inc. - Apex project - Apex mine (past-producing Ge/Ga/Cu underground mine) (United States) | 3 | Ge/Ga-bearing ore from Apex, Utah (from Q3 2027), seeking buyers |
| 10 | GA-008 | ElementUSA - Gramercy bauxite-residue demonstration facility (initial development at Cedar Park, TX accelerator) (United States) | 3 | DPA-funded gallium/scandium demonstration from bauxite residue, uncommitted, no dates |

Alcoa Wagerup (Australia, 100 t/yr) is the biggest new source but is committed to its partners.
<!-- /TOP10_gallium_germanium -->

---

## 8. Traders, stockholders and government stockpiles

**Bottom line:**
- **Compliant spot stock is scarce.** Only one distributor (MCE) publicly advertises "DFARS compliant" rare-earth magnet stock, and that claim probably reflects the pre-2027 test. No other distributor publishes the origin of its stock.
- **The traceable non-China volumes we found are mostly committed:**
  - Traxys holds Arafura and NioCorp offtakes and the El Moto tungsten exclusive.
  - Sojitz/JARE holds Lynas heavy rare earths and samarium.
  - Glencore's cobalt goes to DLA and Project Vault.
- **Government stockpiles are buying, not selling.**
  - DLA has published no disposal plan for FY2026 or FY2027. The last list (FY2025) offered only 499 t of tungsten ores and 5,000 kg of germanium.
  - DLA is signing large purchase contracts instead: Elmet tungsten up to $2B, Glencore cobalt up to $900M, ATALCO gallium up to $350M, GAM tantalum ingot up to $100M.
  - So DLA competes with defense contractors for the same compliant supply.
- **How DLA sells (when it does):**
  - All sales go through one standing solicitation (DLA-Stockpile Materials-001).
  - A buyer registers once under a Basic Ordering Agreement, receives an acceptance letter, and can then bid on the monthly offerings.
  - Legacy stockpile lots carry no public origin data.
- **Project Vault (US Strategic Critical Minerals Reserve):**
  - Structure: a $10B EXIM loan to VaultCo LLC, a partnership of manufacturers and investors, approved 2 February 2026.
  - Participants: traders Hartree, Mercuria and Traxys; commitments from Glencore and Mercuria.
  - It has published no rules on origin. Its first delivery (October 2026) was DRC copper linked to a mine 80% owned by China's CMOC.
  - Material held in the Vault is therefore not automatically compliant.

<!-- TOP10_traders -->
**Top 10 partner prospects (traders, stockholders)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | TR-013 | Traxys North America LLC - Traxys North America office (United States) | 4 | Independent; contracted non-China NdPr/DyTb (Arafura) and NioCorp output; Project Vault supplier |
| 2 | TR-006 | Traxys Europe S.A. - Traxys Group headquarters (Luxembourg) | 4 | El Moto tungsten exclusive (from 2029) and Arafura NdPr; independent merchant |
| 3 | TR-009 | Wogen Resources Limited - Wogen Resources head office (United Kingdom) | 4 | Employee-held minor-metals house with Rwandan tantalum exclusive and W/Mo/Co books; must keep lots separate from its China desk |
| 4 | TR-022 | Magnetic Component Engineering LLC (MCE) - MCE (United States) | 4 | The only distributor found advertising DFARS-compliant magnet stock; check the 2027 basis |
| 5 | TR-004 | Sojitz Corporation - Sojitz head office (Japan) | 3 | Controls Lynas Dy/Tb/Sm flows and future JAGA gallium; Japan-earmarked but worth asking for surplus |
| 6 | TR-007 | Glencore (cobalt marketing) - Glencore head office (cobalt marketing) (Switzerland) | 3 | Non-China refined cobalt brands (Nikkelverk, Murrin Murrin); large and already supplying DLA and the Vault |
| 7 | TR-008 | Darton Commodities Ltd - Darton UK office (United Kingdom) | 3 | Cobalt-metal specialist offering consignment and finance |
| 8 | TR-026 | TRADIUM GmbH - TRADIUM / METLOCK bonded warehouse (Germany) | 3 | Owner-managed stockholder with physical minor-metal stock in a bonded warehouse; prove origin lot by lot |
| 9 | TR-028 | Midwest Tungsten Service, Inc. - Midwest Tungsten Service (United States) | 3 | ITAR-registered US stock of W, WHA, Ta and Mo mill products; no origin data |
| 10 | TR-019 | Dexter Magnetic Technologies - Dexter Magnetic Technologies HQ (United States) | 3 | AS9100 US magnet distributor and assembler with sister SmCo/NdFeB brands |
<!-- /TOP10_traders -->

---

## 9. Assay, inspection and origin-testing labs

**Bottom line:**
- **Origin testing works only on concentrates.** The proven methods match a sample against reference data, using trace elements, isotopes and mineralogy:
  - BGR's Analytical Fingerprint for coltan and wolframite;
  - Source Certain's trace-element and stable-isotope analysis;
  - isotope labs such as Isobar Science.
- **Refining strips most of that signal.** No commercial lab offers validated origin testing for refined tantalum, tungsten or molybdenum metal, separated rare-earth oxides or finished magnets.
- **Evidence for refined products therefore has to come from documents and witnessed sampling:**
  - chain-of-custody records;
  - independent witnessed sampling with sealed retained samples (Alex Stewart, Alfred H Knight, Ledoux);
  - impurity-profile checks, for example GDMS at EAG, which compare each lot with the stated producer's known signature.
- **Grade testing is plentiful in the US and allied countries:** EAG, NSL Analytical, Luvak, LTI, Dirats, IMR, Element, SGS Lakefield, Intertek, ALS, Actlabs and others.

<!-- TOP10_labs -->
**Top 10 verification partners (labs)**

| # | ID | Company - facility (country) | Score | Why |
|---|---|---|---|---|
| 1 | LB-024 | Source Certain - Source Certain (offices Perth WA; Colorado, USA; York, UK) (Australia) | 4 | Commercial trace-element and isotope origin verification with a US office; reference libraries needed for W/Ta/REE |
| 2 | LB-025 | BGR - Federal Institute for Geosciences and Natural Resources (Analytical Fingerprint) - BGR Hannover (Germany) | 3 | The best-established origin method for tantalum and tungsten concentrates (Analytical Fingerprint); government body |
| 3 | LB-021 | Alex Stewart International - Alex Stewart International laboratory (Aintree) (United Kingdom) | 4 | Minor-metals sampling, weighing and assays in 40+ countries |
| 4 | LB-022 | Alfred H Knight (AHK) - AHK group headquarters (United Kingdom) | 4 | Independent inspection and supervision; US lab in Spartanburg, SC |
| 5 | LB-023 | Ledoux & Co. - Ledoux & Co. laboratory (United States) | 4 | US umpire assays accepted for settlement; on-site witnessing; ISO/IEC 17025 |
| 6 | LB-012 | EAG Laboratories - EAG Syracuse (Liverpool) NY laboratory (one of 9 North American EAG sites) (United States) | 4 | GDMS full-survey impurity profiles to match high-purity lots to producer signatures |
| 7 | LB-017 | NSL Analytical Services, Inc. - NSL Analytical (4450 Cranwood Pkwy) and NSL Metallurgical (United States) | 4 | ISO/IEC 17025, Nadcap, ITAR; aerospace spec chemistry |
| 8 | LB-007 | SGS Canada Inc. (Natural Resources - Minerals, Lakefield) - SGS Lakefield Metallurgical Centre of Excellence (Canada) | 4 | Accredited rare-earth methods and pilot-scale processing know-how (Lakefield, Ontario) |
| 9 | LB-026 | Isobar Science - Isobar Science laboratory (United States) | 3 | US commercial Pb/Sr isotope analyses for concentrate provenance (SGS-owned) |
| 10 | LB-005 | Activation Laboratories Ltd. (Actlabs) - Actlabs headquarters laboratory (Canada) | 3 | Allied (Canadian) geochemistry lab with an isotope and geochronology line |

For chain-of-custody documentation (not testing): ITSCI (Great Lakes tin, tantalum and tungsten), Circulor (digital traceability), Cartograph (supplier-origin requests).
<!-- /TOP10_labs -->

---

## 10. Gaps: stages with zero or near-zero compliant supply

These are the places where a defense buyer will struggle to find any supply that passes the 2027 test, whatever the price. They are also where a broker adds the most value, by finding the few sources and building the documentation.

| Chain | Stage | Why it's a gap | Earliest relief |
|---|---|---|---|
| NdFeB | Separated **Dy/Tb oxide**, uncommitted | Lynas is the only commercial non-China producer (~23 t/quarter), and most of its heavy rare earths are committed to Japan; MP's are captive | Ucore and SRC (2027, small); Iluka and Energy Fuels (2028) |
| NdFeB | **Heavy rare earth metal** (Dy, Tb, DyFe, TbFe) | No verified operating non-China merchant capacity | REalloys Saskatoon (2028, ~45 t/yr) |
| NdFeB | **Ferroboron** | No non-China producer could be verified. The US makes none (DOE), and known producers are in China, India and Turkey | None identified |
| NdFeB | Bonded and MQ powder with a documented chain | Neo's Korat plant (Thailand) is the only sizeable non-China powder plant, and its oxide/alloy origin is undisclosed | None identified |
| SmCo | **Samarium metal** | One operating Western plant (LCM, UK), capacity-short | LS Eco Energy Vietnam (trial Dec 2026, 240 t/yr); LCM +30% (Q3 2027); REalloys (later) |
| SmCo | **SmCo magnet recycling** | None found outside China, yet the statute's recycled-SmCo exemption requires US milling and sintering | None identified |
| SmCo | SmCo magnets with a fully documented chain | No SmCo magnet maker rates `likely_compliant`: samarium or cobalt origin is undisclosed or Chinese | EEC/Permag and Arnold switching to LCM/Solvay/Lynas samarium |
| SmCo | US samarium separation | None operating | Energy Fuels (2028); Ucore adds Sm/Gd |
| Cobalt | **US refined cobalt** | None operating; US supply is imports plus scrap | Electra (Canada, H2 2027, sulfate); Jervois US refinery (no date) |
| Tungsten | **Independent US APT/oxide** | US chemical capacity is captive (GTP, Niagara, Kennametal) | Springer APT JV (late 2028 - early 2029) |
| Tungsten | Recycled-exemption processing in qualifying countries | Several recyclers sit in non-qualifying countries (Taiwan, India, Brazil) | Use US, EU and Japanese recyclers |
| Tantalum | **US tantalum metal/powder with a documented feed** | Only GAM Boyertown; Materion's feed is undisclosed | GAM expansion (EXIM, 2027) |
| Tantalum | Merchant K-salt/oxide with a transparent feed | Mostly captive (GAM, KEMET, TANIOBIS) or opaque | AMG Brasil is the clearest merchant case |
| Molybdenum | **US molybdenum powder** | No published US capacity; Elmet's feed and site are undisclosed | Elmet expansion (DoW-funded) |
| Gallium | **Primary gallium** | ~3 t/yr outside China in 2025 (Japan, captive) | ATALCO (pilot 2026), METLEN (Q3 2027), Alcoa Wagerup (2027-28) |
| Gallium | High-purity refining on non-China feed | Refiners exist (DOWA, Indium, CMK) but run on mostly Chinese crude | Pairing new primary projects with these refiners |
| Germanium | Traceable non-China germanium | Only Teck (Red Dog feed) and STL/Umicore (DRC slag) have documented feed | Korea Zinc Onsan (2027) |
| All | **Origin testing for refined products** | No validated commercial method for refined metal, oxide or magnets | Documentation and witnessed sampling instead |
| All | **Compliant spot inventory** | Distributors don't publish origin; traceable volumes are committed to governments | None. DLA and Project Vault are competing buyers |

---

## 11. Completeness checks

### Check 1: USGS Mineral Commodity Summaries 2026, countries with non-zero 2025 production

**Tungsten:**

| Country (2025 t W) | Main producers listed? |
|---|---|
| China (67,000), Russia (2,000), North Korea (2,000) | Covered countries: major facilities are in `excluded.csv` |
| Vietnam (3,000) | Yes: Masan Nui Phao |
| Kazakhstan (2,400) | Yes: Boguty (flagged as Chinese-owned); Upper Kairakty (planned). North Katpar not verified |
| Bolivia (1,700) | Partly: Kennametal La Paz. Cooperatives and artisanal miners are not listed individually |
| Rwanda (1,300) | Yes: Trinity Nyakabingo, Almonty Rwanda. The artisanal remainder is not listed |
| Australia (1,000) | Yes: Group 6 Dolphin, EQ Resources Mt Carbine, Tungsten Mining Watershed (planned) |
| Austria (840) | Yes: WBH Mittersill |
| Spain (800) | Yes: Barruecopardo, Los Santos (restart), El Moto (construction) |
| Portugal (700) | Yes: Panasqueira |
| Other (2,400) | South Korea: yes (Sangdong, GB Innovation). **Not verified:** Myanmar (artisanal, mostly feeds China), Peru (Pasto Bueno: no current information found), Brazil, Mongolia, Uzbekistan, Uganda, Burundi, DRC |

**Tantalum:**

| Country (2025 t Ta) | Main producers listed? |
|---|---|
| DRC (1,300) | Partly: SMB Rubaya (conflict-area risk), MMR, Tantalex Manono. Most output is artisanal and sold through traders |
| Rwanda (400) | Yes: Trinity Musha, Eastinco/Aterian, PowerX smelter |
| Nigeria (390) | No: artisanal, with no formal producer to list |
| Brazil (190) | Yes: Taboca (Chinese-owned, flagged), AMG Mibra, Resind |
| China (80), Russia (30) | Covered countries: processors are in `excluded.csv` |
| Australia (50) | Yes: GAM Greenbushes and Wodgina, PLS Pilgangoora, Talison (flagged) |
| Ethiopia (40) | No: the state Kenticha mine has been halted since 2017 and its licence was revoked in 2024; the producer behind the USGS estimate could not be identified |
| Bolivia (2), Burundi (2), Mozambique (1) | No: tiny or artisanal; Marropino has been closed since 2013 |

**Rare earths:**

| Country (2025 t REO) | Main producers listed? |
|---|---|
| China (270,000), Russia (2,600) | Covered countries: major facilities are in `excluded.csv` |
| United States (51,000) | Yes: MP Mountain Pass, Chemours monazite, Energy Fuels |
| Australia (29,000) | Yes: Lynas Mt Weld and Kalgoorlie, Iluka Eneabba |
| Burma/Myanmar (22,000) | Yes, flagged: Kachin ionic clays, separated in China |
| Thailand (4,800) | Partly: Hastings/BZNM plant. Mine producers were not identified |
| India (2,900) | Yes: IREL |
| Madagascar (2,700) | Not identified; Energy Fuels' Vara Mada project is listed but not producing |
| Brazil (2,000) | Yes: Serra Verde |
| Nigeria (1,500) | No: artisanal monazite exported to China |
| Vietnam (150), Malaysia (110) | Not identified (very small) |

The cobalt, molybdenum, gallium and germanium country checks are in each workstream's `chain_notes.md`. In short:
- **Cobalt:** refiners are listed for all the main US import sources (Norway, Finland, Canada, Japan).
- **Molybdenum:** the US, Chile, Peru, Mexico, Canada, Mongolia, Armenia and Uzbekistan are listed. Producers in Kazakhstan, Australia and Korea were not identified.
- **Gallium and germanium:** all producing countries are covered.

### Check 2: RMI conformant smelters outside covered countries (public proxy)

We used public lists (Apple's April 2025 Smelter and Refiner List and 2026 SEC Form SD exhibits) in place of the RMI site, whose terms forbid copying its list.
- **Tungsten:** all 17 non-China tungsten smelters on Apple's list have rows:
  - A.L.M.T., Asia Tungsten Products Vietnam and Cronimet Brasil;
  - Global Tungsten & Powders and H.C. Starck Tungsten;
  - Japan New Metals, Kennametal Fallon and Kennametal Huntsville;
  - Lianyou Metals and Lianyou Resources;
  - Masan High-Tech Materials, Niagara Refining and Philippine Bonway;
  - Philippine Chuangxin, TANIOBIS Smelting, Tungsten Vietnam JSC and WBH.

  2026 Form SD additions also have rows: Jing Yuan (Taiwan), KENEE (Vietnam), S.P.T. (Czechia) and Tungamoy Metals (Korea, flagged as a likely Xiamen Tungsten affiliate).
- **Tantalum:** all 20 non-China tantalum smelters on Apple's list have rows:
  - AMG Brasil, D Block Metals and GAM Aizu;
  - GAM Boyertown, KEMET de Mexico and Materion Newton;
  - Metallurgical Products India, Mineração Taboca and Mitsui Kinzoku;
  - NPM Silmet, PowerX and QuantumClean;
  - Resind and Taki Chemical;
  - TANIOBIS Thailand, TANIOBIS GmbH, TANIOBIS Japan and TANIOBIS Smelting;
  - Telex Metals and Ulba.

  Avon Specialty Metals (UK) also has a row.
- **Cobalt:** both non-China cobalt refiners on Apple's list (Umicore Olen, Umicore Finland) have rows.

**Re-check every status on the RMI site before relying on it.**

### Check 3: every company with a US government award for these materials since 2020

All of the following awardees appear in the file as their own rows. They were checked against an independent list compiled from DoD, DLA, OSC, EXIM, DOE, DFC and Commerce announcements (`data/staging/verification/award_crosscheck.md`):

| Material | Awardees |
|---|---|
| Tungsten | Elmet, Fireweed, Guardian/Golden Metal, Sisson, Amaero, 6K Additive |
| Tantalum | Global Advanced Metals (DLA ingot and niobium contracts, DoD niobium oxide, EXIM), Trinity Metals (DFC) |
| Rare-earth mining and separation | MP Materials, Lynas, Ucore, NioCorp, Serra Verde, USA Rare Earth, ReElement, Phoenix Tailings, Rare Element Resources, Energy Fuels, Aclara, Northern Minerals, Pensana, American Rare Earths, Critical Metals, Rainbow, Mkango, Altona, Iluka (Australian government) |
| NdFeB magnets and recycling | e-VAC, Noveon, Vulcan Elements, USA Rare Earth, HyProMag USA, Niron, Hertha Metals, REalloys, Advanced Magnet Lab, REEcycle |
| Samarium and cobalt | REalloys, Ucore, Lynas, Electra, Fortune Minerals, Talon, Jervois, Nth Cycle, Redwood, Li-Cycle, Ascend Elements, Glencore (DLA cobalt contract, reported) |
| Gallium and germanium | Alcoa (Wagerup), ATALCO, ElementUSA, 5N Plus, Lattice Materials, Korea Zinc/Crucible, Indium Corporation, Metallium/Flash Metals, ReElement |
| Molybdenum | Elmet, Amaero |

Deliberately left out:
- Trilogy Metals: its DoW equity is for a copper-zinc project, and cobalt is not a planned product.
- Nathan Trotter: its DoD award is for tin.

Limitation: the per-session web-search cap stopped the agents from sweeping every DoD contract announcement. DLA purchase contracts in particular are often not public unless the awardee discloses them, so smaller awards may be missing.

### Check 4: at least one operating non-covered supplier at every stage?

| Chain | Stages with an operating non-covered supplier | Stages without one, or only nominally |
|---|---|---|
| Tungsten | All 5 stages | None. US APT is captive, though |
| Tantalum | All 5 stages | None. Only GAM has a fully documented feed at the metal stage |
| NdFeB | Mining, separation, metal/alloy, sintered, bonded, recycling, substitute (pilot) | **Ancillary inputs:** boron yes, but **ferroboron has no verified non-China producer**. **Dy/Tb separation:** only Lynas commercially |
| SmCo | Separation, metal (LCM only), alloy, magnet | **Recycling: none.** Mining: no samarium-specific mine; samarium comes from the general rare-earth feeds mapped under NdFeB |
| Cobalt | All 4 stages | None. Feed-origin proof is the issue |
| Molybdenum | All 5 stages | None. Proof of the oxide feeding powder makers is the issue |
| Gallium | All 4 stages | **Primary extraction is nominal:** about 3 t/yr in Japan, captive |
| Germanium | All 5 stages | None. Traceability is the issue |

---

## 12. Verification pass

After the research, independent verifiers re-checked a random sample of **74 rows, about 15% of the file, drawn from every chain**. They checked each row against its cited sources and, where needed, fresh searches. Rows with high broker-fit scores were sampled slightly more often.

| Result | Rows | Share |
|---|---|---|
| Confirmed as written | 36 | 49% |
| Minor issues (outdated detail, missing award, wording) | 28 | 38% |
| Major issues (wrong owner, missed covered-country tie, wrong status) | 9 | 12% |
| Could not be verified | 1 | 1% |

**Every issue found was corrected in the data.** The corrections and the evidence for each are in `data/staging/verification/`.

The nine major issues:
- **Wrong owner (5 rows):**
  - Isobar Science is owned by SGS.
  - Hartree is owned by its managers and Oaktree/Brookfield funds.
  - Nouryon is owned by Carlyle and GIC.
  - Buffalo Tungsten was sold to Sandvik in 2023, so its score dropped from 5 to 4.
  - ReElement is standalone after American Resources' deconsolidation; its $80M OSC loan was withdrawn.
- **Missed covered-country tie (2 rows):**
  - TDK runs on Chinese rare earths; it is now `likely_noncompliant`.
  - A.L.M.T. has a molybdenum plant in China, 70% owned by Xiamen Tungsten.
- **Wrong status (1 row):** Elmet Coldwater does not make tungsten powder until about Q1 2027.
- **Mislabelled offtake (1 row):** Asia Tungsten Products Vietnam's "offtake" was really a pending acquisition agreement.

The unverifiable row, Tungsten Heavy Powder (San Diego), had no sign of operating since about 2003. **It was removed.**

**Patterns the verifiers found, and how we responded across the whole file:**
- **Ownership fields sometimes stopped at the operating company,** and some 2025-26 ownership changes and awards were missed. We corrected every sampled case and fixed sibling rows of the same companies. Treat `ultimate_owner` as a lead to confirm, not a final answer.
- **Processors with undisclosed feed were graded inconsistently.** We applied one rule (decision 21a in `docs/decisions.md`):
  - 10 rows moved from `likely_compliant` to `at_risk`;
  - 28 rows changed their tie from "none" to "unknown".
- **Capacities matched their sources.** No invented numbers were found. Several are nameplate rather than actual output, as labelled.
- **Government awards and letters of interest were under-recorded.** Missed items found in the sample were added, for example:
  - Jervois $15M (DPA, 2023);
  - Energy Fuels $725M (OSC conditional, 2026);
  - USA Rare Earth $19.3M (DOE, 2026);
  - ASM US$600M (EXIM letter of interest, 2024).

  Expect a few more in rows that were not sampled.

**How much to trust the file:**
- Confidence ratings: 95 rows are `high`, 299 `medium` and 101 `low`.
- A row marked `low` should be treated as a lead to verify, not a fact.
- The per-session web-search cap meant many rows got no separate 2026 news check (see `docs/method.md`).
