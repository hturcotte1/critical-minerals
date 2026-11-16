# NdFeB upstream notes (workstream ndfeb_upstream: mining_concentrate + separation), as of 2026-11-16

Method caveat: the shared web-search budget ran out after about 15 searches. Everything after that was confirmed by fetching primary sources directly: ASX announcement PDFs, SEC EDGAR 10-Q/10-K/8-K/20-F/424B3 filings, and company and government pages. Entities whose own pages blocked fetching (Solvay, Pensana, SRC news pages, Iluka web pages) have lower confidence. Files: suppliers.jsonl (66 rows: 37 mining_concentrate, 29 separation), offtakes.jsonl (38), excluded.jsonl (16), sources.jsonl (102).

## Who matters at each stage (non-covered-country only)

**Mining / concentrate / cracking (mining_concentrate)**
- **MP Materials, Mountain Pass (US).** 50,692 t REO in concentrate in 2025. Captive since sales to China stopped in Jul 2025; the Shenghe offtake expired Jan 2026.
- **Lynas, Mt Weld and Kalgoorlie (Australia).** Mt Weld supports 12 ktpa NdPr. Kalgoorlie cracks and leaches to MREC for Malaysia. Fully captive.
- **Serra Verde, Pela Ema (Brazil).** USA Rare Earth bought it on 3 Sep 2026. It is the only scaled non-Asian source of all four magnet REEs (Nd, Pr, Dy, Tb). 100% of Phase 1 output is sold to US SIIE LLC for about 15 years, with floors of Tb US$2,050/kg, Dy US$575/kg and Nd/Pr US$110/kg. The DFC loan facility is up to US$565M.
- **Lindian, Kangankunde (Malawi).** First concentrate Dec 2026; Stage 1 is fully allocated (Iluka, the SARECO plant in Kazakhstan, and an unnamed refining group).
- **Near-term merchant intermediates (2027):** Hastings/BZNM Kabin Buri plant (Thailand), 12,000 t/yr MREC planned from Q2 2027, uncommitted, feed is African monazite from Enuo; Pensana Longonjo (Angola), first production 2027; Lindian SARECO (Kazakhstan), first processing Q4 2026.
- **Captive feed for 2028+:** Donald (Australia, Astron/Energy Fuels JV; FID by end-2026; ~7,100 t/yr REEC to Utah), VHM Goschen (all output to Iluka), Viridis Colossus (~70% to Solvay), Meteoric Caldeira (being acquired by Lynas), Arafura Nolans (integrated with its own separation).
- **Other operating sources:** IREL OSCOM (India; 11,200 t/yr mixed RE chloride, state-captive); Chemours mineral-sands monazite (Florida/Georgia; to Energy Fuels since 2021).

**Separation**
- **Lynas Malaysia (LAMP).** Nameplate 900 t NdPr/month. Record 2,082 t NdPr and 23 t Dy+Tb in the Sep 2026 quarter. Commercial Dy since May 2025 and Tb since Jun 2025; Sm since Mar 2026. The expanded HRE plant (5,000 t/yr HRE feed) targets the full suite by late 2027. Floor-price deals cover more than 50% of output.
- **MP Materials, Mountain Pass.** Designed for ~6,075 t/yr NdPr at anticipated rates; 2025 actual 2,599 t; Q3 2026 1,018 t. The HREE circuit (200 t/yr Dy+Tb) is commissioning, with commercial output from Q4 2026, mostly for MP's own magnets. The DoW price floor of US$110/kg runs to 2035.
- **Energy Fuels, White Mesa (Utah).** The Phase 1 circuit makes up to ~1,000 t/yr NdPr in campaigns. A Phase 1 heavy RE expansion (122 t Dy + 21 t Tb per year) is under construction for as early as Q1 2028. Phase 2 (5,229 t NdPr, 240 t Dy, 66 t Tb) is planned for mid-2029. Energy Fuels completed the ASM acquisition on 28 Aug 2026; the VAC acquisition is pending.
- **Iluka, Eneabba (Western Australia).** 65% built. Capacity is 5,500 t/yr NdPr and 750 t/yr Dy/Tb with third-party feed (3,500 t and 170 t from its own stockpile). Commissioning mid-2027. Only about 10% of output is contracted (1,200 t to an automaker over 4 years from 2028). Backed by an A$1.65bn Australian Government loan.
- **Caremag (Carester), Lacq (France).** Start-up end-2026. Design output ~600 t/yr Dy+Tb oxide and ~800 t/yr NdPr from 5,000 t concentrates plus 2,000 t recycled magnets. Partly committed: Japan (JOGMEC/Iwatani), Stellantis (>3,400 t over 10 years) and Neo (term sheet).
- **Ucore, Louisiana SMC (Alexandria).** Machine A (600 t/yr TREO, medium and heavy REE) received commissioning feed in Nov 2026; supply from 2027. Total DoW funding is US$27M (US$4.0M + US$18.4M + US$4.6M).
- **Other separators:**
  - SRC Saskatoon (Dy/Tb oxides and NdPr metal; operational 2027).
  - NPM Silmet (Estonia; in transition, with Silmet 2.0 named an EU CRMA project).
  - Solvay La Rochelle (operating; capacity not verified).
  - IREL Aluva (India; no Dy/Tb listed).
  - Phoenix Tailings Rochester (4,400 t/yr REO; ramp 2027, full 2028; US$500M OSC conditional loan).
  - Aclara Project Dynamo (Louisiana; 200 t Dy + 35 t Tb + 1,300 t NdPr; construction done H2 2028; EXIM LOI up to US$750M).
  - Arafura Nolans (4,440 t NdPr; FID 21 May 2026).

## The real bottleneck (which stage, why, numbers with sources)
- **The constraint is heavy rare earth separation, and above all compliant HRE feed. NdPr is much less tight.**
  - USGS MCS 2026 says no US company produced sustained commercial-scale heavy RE compounds in 2025. US heavy RE imports were 100% reliant on imports, with Tb from China at 100%.
- **The only commercial non-China Dy/Tb producer is small.** Lynas made 8-26 t of Dy+Tb per quarter in FY26 and 23 t in the Sep 2026 quarter (Lynas ASX, 29 Oct 2026), against NdPr output of about 2,000 t per quarter.
- **Most non-China HRE feed is already locked up:**
  - Serra Verde: 100% to US SIIE.
  - Meteoric Caldeira: to Lynas.
  - Viridis Colossus: ~70% to Solvay.
  - Lindian SEGH: 70% to Carester.
  - Aclara: captive.
  - Northern Minerals Browns Range: to Iluka, and only from 2029.
- **Myanmar (USGS: 22,000 t REO in 2025, estimated from China's import data) is the largest non-China HRE source,** but its output is separated in China.
- **Light RE capacity is also concentrated in two groups (Lynas and MP).** The 2025 output gap against China is large: USGS puts China's mine production at 270,000 t REO against 390,000 t for the world.

## Uncommitted non-China capacity for 2027 (best estimate with stated basis)
**Basis.** Nameplate or stated figures for facilities operating or commissioning in 2027, from company filings in this file. "Uncommitted" means not covered by binding or announced offtakes or by captive use. It is an estimate; counterparties' undisclosed contracts make it uncertain.

**Separated NdPr oxide (2027)**
- Sourced nameplate is about 19,000-20,000 t/yr:
  - Lynas 10,800 t;
  - MP ~6,075 t design (run-rate ~4,000 t in H2 2026);
  - Energy Fuels ≤1,000 t (campaign-based);
  - Caremag ~800 t (ramping);
  - REEtec 720 t (status unverified).
- Iluka's 5,500 t starts ramping only from mid-2027; most of its deliveries begin in 2028.
- Silmet and Solvay capacities are not quantified.
- Likely 2027 output is ~13,000-15,000 t.
- Commitments:
  - Lynas: JARE MoU for at least 5,000 t/yr, JS Link exclusivity, the DoW LOI, and floor deals covering more than 50% of output.
  - MP: captive magnet demand plus direct customers.
  - Energy Fuels: earmarked for its own KMP/VAC chain.
  - Caremag: Stellantis, Japan and Neo.
  - REEtec: 80% contracted in 2022.
- Our estimate of genuinely uncommitted, broker-accessible NdPr in 2027 is roughly 1,000-3,000 t. It would come mainly from incremental MP and Lynas volumes and residual Caremag and Energy Fuels output.
- From 2028, Iluka's uncommitted ~90% (about 4,000+ t/yr NdPr equivalent once ramped) is the largest pool.

**Separated Dy+Tb oxide (2027)**
- Sourced nameplate is about 900+ t/yr:
  - Caremag ~600 t;
  - MP 200 t;
  - Lynas current ~90-100 t/yr run-rate (expansion late 2027);
  - Ucore Machine A within 600 t TREO;
  - SRC (not quantified).
- Realistic 2027 output is probably only a few hundred tonnes, because the new plants are ramping and HRE feed is short.
- Uncommitted volume is unknown but small (tens of tonnes):
  - Lynas HRE: JARE holds rights to 50-75%.
  - MP: captive.
  - Caremag: Japan, Stellantis and Neo.
- Ucore and SRC are the main potentially uncommitted Dy/Tb sources in 2027. Iluka (up to 750 t/yr with third-party feed, ~170 t from its stockpile) and Energy Fuels (143 t/yr) add supply from 2028.

**MREC / concentrate (merchant, 2027)**
- Hastings/BZNM: 12,000 t/yr MREC, uncommitted; feed origin to be verified.
- Pensana Longonjo: uncommitted.
- Lindian: Stage 2 and MREC/SEGH are being marketed.
- All other major concentrate streams are captive or contracted.

## Top 10 broker prospects
1. **Ucore - Louisiana SMC (US).** Uncommitted DoW-funded medium/heavy REE separation from 2027; needs both feed and customers. Score 5.
2. **Iluka - Eneabba refinery (Australia).** About 90% of 2028+ NdPr and Dy/Tb output is uncommitted; actively seeking customers; Australian Government financed. Score 4.
3. **Rainbow Rare Earths - Phalaborwa (South Africa).** 60% of NdPr and 35% of SEG+ are uncommitted (Neo has only an MOU); DFC-backed via TechMet; first production targeted 2028. Score 4.
4. **Pensana - Longonjo (Angola).** First production 2027, uncommitted, pursuing a US route; EXIM LOI. Score 4, low confidence.
5. **Hastings/BZNM - Kabin Buri (Thailand).** 12,000 t/yr MREC from Q2 2027 with no offtake. Verify the African feed origin and the co-owner first. Score 3.
6. **Caremag - Lacq (France).** About 600 t/yr Dy+Tb design and partly uncommitted; confirm the origin of each feed lot. Score 3.
7. **Energy Fuels - White Mesa (US).** Spare NdPr in campaigns. It is also the main US buyer of compliant monazite/MREC, so a broker can sell it feed. Score 3.
8. **Phoenix Tailings - Freedom Separation, Rochester (US).** 4,400 t/yr REO in 2027-2028; needs third-party feed; OSC conditional loan. Score 3.
9. **SRC - Saskatoon (Canada).** Dy/Tb oxides from 2027; government-owned with REalloys as anchor partner. Score 3.
10. **Lindian - Kangankunde Stage 2 / SARECO (Malawi/Kazakhstan).** Monazite, MREC and SEGH, with North American interest. Check the Kazakhstan transit route. Score 3. Runners-up are Aclara Dynamo (2028) and REEtec (needs feed).

## Gaps: stages with zero or near-zero compliant supply
- **Uncommitted separated Dy/Tb in 2027:** near zero. Lynas HRE is pre-committed to JARE (Japan), and MP's HRE is captive.
- **Compliant HRE feedstock (ionic-clay MREC, xenotime):** nearly all contracted.
- **US heavy RE separation at commercial scale:** only MP (commissioning) and Ucore (commissioning) in 2027. Energy Fuels follows in 2028, and Aclara and Phoenix in 2028.
- **Europe:** Silmet is in transition. The CRMA projects (Silmet 2.0, Pulawy, LKAB Luleå) come after 2028.
- **Feed with clear provenance for new separators** (Phoenix, Ucore, REEtec, Caremag, Energy Fuels MREC route): undersupplied.

## Completeness checks
**USGS MCS 2026 (countries with 2025 mine production > 0)**
- United States 51,000 t: MP Mountain Pass and Chemours monazite are listed.
- Australia 29,000 t: Lynas Mt Weld/Kalgoorlie and the Iluka Eneabba stockpile are listed.
- Brazil 2,000 t: Serra Verde is listed.
- Burma 22,000 t: a Kachin ionic-clay row is listed (feeds China).
- China 270,000 t: in excluded.jsonl.
- India 2,900 t: IREL OSCOM and Aluva are listed.
- Russia 2,600 t: Lovozero and Solikamsk are in excluded.jsonl.
- Thailand 4,800 t: estimated from China's import data; producers were not identified. The Hastings/BZNM plant is the only Thai facility listed.
- Madagascar 2,700 t: producers not identified (probably mineral-sands monazite or clay exported to China). Energy Fuels' Vara Mada is listed but is not producing.
- Nigeria 1,500 t: artisanal tin/columbite tailings monazite exported to China; no formal producer, so none is listed.
- Malaysia 110 t and Vietnam 150 t: producers not identified. Lynas Malaysia's separation is listed; it has no mine in Malaysia.

**RMI-equivalent check:** n/a for NdFeB.

**US government awards since 2020: awardees and rows**
- MP Materials: DoD 2020 US$9.6M; 2022 US$35M; Jul 2025 DoW package (US$400M equity, US$110/kg floor, US$150M loan, 10X offtake); DoW financing for the Maaden JV. Rows: yes.
- Lynas: DoD 2021 US$30.4M; 2022-23 US$120M then ~US$258M for Seadrift; 2026 DoW LOI for ~US$96M of oxides. Rows: yes.
- Ucore: DoD/DoW US$4.0M, US$18.4M and US$4.6M. Row: yes.
- NioCorp: DPA up to US$10M; EXIM term sheet ~US$800M. Row: yes.
- Serra Verde: DFC up to US$565M; US-government-backed offtake by US SIIE. Row: yes.
- USA Rare Earth: Commerce CHIPS US$277M direct funding plus US$1.3bn loan guarantee; Commerce equity. Rows: yes.
- ReElement: OSC US$80M conditional; status disputed. Row: yes.
- Phoenix Tailings: OSC US$500M conditional. Row: yes.
- Rare Element Resources: DOE ~US$24.2M. Row: yes.
- Energy Fuels: a "previously announced conditional US government loan commitment" (program not identified). Row: yes.
- Aclara: EXIM LOI up to US$750M. Row: yes.
- Northern Minerals: EXIM LOI up to US$230M. Row: yes.
- Pensana: EXIM LOI up to US$160M. Row: yes.
- American Rare Earths: EXIM LOI up to US$456M. Row: yes.
- Critical Metals: EXIM LOI up to US$120M. Row: yes.
- Rainbow: DFC US$50M via TechMet. Row: yes.
- Mkango: DFC US$4.6M for FEED. Row: yes.
- Altona: USTDA. Row: yes.
- Not mapped here: Vulcan Elements and HyProMag USA are downstream (magnets and recycling).
- Not identified: DLA's FY2025 potential acquisition of 300 t NdPr oxide (USGS) and DOE's 2026 REE pilot-scale awards ($45M across 19 projects).

**Every stage has at least one operating non-covered supplier?**
- mining_concentrate: yes.
- separation: yes. For Dy/Tb, only Lynas Malaysia operates commercially; MP is commissioning.

## What could not be verified
- **Not fetched or blocked:** 2026 status of Solvay La Rochelle (capacity, feed origin), REEtec (start-up, feed), Pensana (2026 RNS detail, investor identity), Torngat (ownership, financing), Neo Silmet capacity and legacy feed origin, and ReElement's OSC loan status (reported fell through) and ~US$25M 2026 DoD award.
- **Not researched (search budget exhausted):**
  - Shin-Etsu Takefu separation and its feedstock origin; Vietnam (VTRE, Dong Pao); Madagascar (Harena, QMM monazite); Thailand and Laos producers; Malaysian ionic clay; Indonesia (PT Timah).
  - Eti Maden (Turkey), Steenkampskraal (South Africa), US Critical Materials (Sheep Creek), Search Minerals, Commerce Resources, Medallion, Defense Metals timeline, Leading Edge Norra Kärr, Rare Earths Norway (Fen).
- **Excluded list gaps:** Xiamen Tungsten rare earth (Changting), Guangdong Rising, Sichuan Mianning (Maoniuping, Jiangxi Copper) and the Chepetsk plant could not be sourced, so they are absent. Constituent and plant names for China Rare Earth Group come partly from Wikipedia and industry knowledge (flagged in the notes).
- **Lindian buyer:** the identity of its 30 kt monazite "major refining group" buyer, which may be Chinese.
- **Japanese agreements:** the size of Caremag's HRE agreement with Japan, and the exact JARE HRE share (sources conflict: 50%, 65% or 75%).
