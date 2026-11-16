# Traders, stockpiles and labs notes (workstream traders_labs), as of 2026-11-16

**How to read this.** The shared web-search budget (200 searches across all agents) ran out early in this workstream. Searches and 2026 news checks were completed for DLA, Project Vault, the allied stockpiles, Traxys and Wogen. Every other row was checked only against the company's own website (fetched 16 Nov 2026); those rows say so in `notes` and are rated medium or low confidence. Lines marked **(assessment)** are our judgment, not a sourced fact.

Rows: 32 trader-chain rows (6 government stockpiles, 11 traders, 12 distributors, 3 stockholders) and 26 lab-chain rows (16 assay labs, 5 inspection/sampling, 2 provenance labs, 3 audit/chain-of-custody). There are 14 offtakes. `excluded.jsonl` is empty because the Chinese trader sites could not be reached (see the end of this file).

## 1. How DLA Strategic Materials sells (and now mostly buys)

**Sales mechanics** (from DLA documents seen through search snippets; DLA blocks automated fetches):
- All sales run under one standing solicitation, **DLA-Stockpile Materials-001**. The Basic Ordering Agreement (BOA) version was issued 3 Jul 2017, and there is a separate auction version with a bid-price section.
- A buyer registers once (single-point registration). The Stockpile Sales Officer then issues an acceptance letter, and from that point the firm can bid competitively on offerings under the BOA.
- DLA posts the results of each month's BOA sales:
  - June 2024: ferrochrome sold (1,000 units, about $1.30M), with chromium metal and tin also offered.
  - September 2024: no sales of chromium metal or tin.
  - March 2023: tungsten ores and concentrates sold, alongside tin.
  - September 2025 (announced 7 Oct 2025): no ferrochrome awards.
- Sources:
  - https://www.dla.mil/Portals/104/Documents/Strategic Materials/Solicitation Docs/DLA-Stockpile Materials-001_BOA_FINAL POSTING COPY.pdf
  - https://www.dla.mil/Portals/104/Documents/Strategic Materials/Announcements/3252 BOA All June 2024 Sales.pdf
  - https://www.dla.mil/Portals/104/Documents/Strategic Materials/Announcements/3273 BOA All September 2025 Sales.pdf
- **What a broker would do (assessment):** register under the BOA, watch the monthly offerings, and buy only lots whose origin records support a 2027-compliant chain. Legacy stockpile lots carry no public origin data.

**The Annual Materials Plan (AMP).** The AMP sets ceilings for potential acquisitions and disposals and used to be published each October.
- **FY2025 AMP** (USGS MCS 2026):

  | Material | Potential disposals | Potential acquisitions |
  |---|---|---|
  | Tungsten ores and concentrates | 499 t W content | — |
  | Tungsten | — | 2,041 t |
  | Germanium (gross weight) | 5,000 kg | — |
  | Tantalum metal | 0.09 t | 29.26 t |
  | Cobalt alloys | — | 60 t |
  | NdPr oxide | — | 300 t |
  | NdFeB magnet block | — | 450 t |
  | SmCo alloy | — | 60 t |
  | Lanthanum | — | 1,100 t |

  USGS lists molybdenum as "None" and gallium as "Not available". Sources: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-tungsten.pdf, mcs2026-tantalum.pdf, mcs2026-germanium.pdf, mcs2026-cobalt.pdf, mcs2026-rare-earths.pdf.
- **FY2026 AMP:** "not released" (USGS footnote).
- **FY2027 AMP:** not released as of November 2026 (Argus, https://www.argusmedia.com/en/news-and-insights/latest-market-news/2903231-us-aims-to-grow-mineral-stockpile).
- **What this means:** there is no published disposal list for FY2026 or FY2027. The only recent disposal quantities for this workstream's metals are the FY2025 lines for germanium (5,000 kg) and tungsten ores (499 t W).

**The stockpile has switched from seller to buyer.**
- **Funding:**
  - The One Big Beautiful Bill Act (July 2025) gave $2B for stockpile purchases, available through FY2029.
  - DLA reported $2B committed in FY2026 (announced 5 Nov 2026) but named no contracts (Northern Miner, https://www.northernminer.com/news/us-reports-2b-in-mineral-stockpile-commitments/1003897547/).
- **Known IDIQs** (ceilings, not guaranteed purchases), about $3.3B in total per Argus:

  | Supplier | Material | Ceiling and terms |
  |---|---|---|
  | Glencore | Cobalt | Up to $900M over 5 years (awarded May 2026) |
  | Atalco (Louisiana) | Gallium | Up to $350M for 55,610 kg |
  | Glencore | Nickel | Up to $65M |
  | Arconic or Rio Tinto (reports conflict) | High-purity aluminium | Up to $995M |
  | Elmet Technologies | Tungsten ores, concentrates, sodium tungstate | Up to $2B, $150M minimum, 5 years from 11 Sep 2026 |
  | Boyertown, PA tantalum processor | Tantalum ingot | $8.6M delivery order (Sep 2025) plus a 5-year contract up to $100M |
  | US Antimony | Antimony | Up to $245M (2025) |

  Elmet's deliveries wait on new mine and processing supply (https://www.manufacturingdive.com/news/dod-war-elmet-group-tungsten-supply-chain-dla-economic-defense-unit/830331/).
- The August 2025 cobalt tender (7,480 t, $500M ceiling) was cancelled in October 2025 (https://www.fastmarkets.com/insights/us-critical-minerals-security-drive-brings-new-era-of-stockpiling-project-investment/).
- **Broker implication (assessment):** DLA matters far more as a **customer** for compliant tungsten, cobalt, gallium, tantalum and rare earths than as a source of stock. Its buying also competes with defense contractors for the same scarce compliant supply.

## 2. How Project Vault works

**Structure**
- EXIM approved a direct loan of up to $10B on 2 Feb 2026 (https://www.exim.gov/news/project-vault). Roughly $1.67-2B of private capital sits alongside it.
- The borrower is VaultCo LLC, an independently governed partnership of manufacturers (OEMs) and private capital providers. EXIM sits on the board only as a non-controlling observer (CSIS, 23 Sep 2026).
- It is separate from the National Defense Stockpile, and EO 14415 sec. 6 says the order does not affect it.

**Participants**
- Suppliers named at launch: Hartree Partners, Mercuria Americas and Traxys.
- Glencore and Mercuria each committed $500M on 23 Sep 2026. Glencore's commitment is cobalt.
- OEMs named: Clarios, GE Vernova, Western Digital and Boeing (EXIM). Later reports add Corning, GM, Google and Stellantis.

**Mechanism** (reported in October 2026; Fastmarkets and Bloomberg via The Oregon Group)
- Manufacturers pay up-front fees and commit to buy the material later at a set inventory price. They also pay carrying costs (interest and storage).
- Drawdown decisions rest with the manufacturers.
- A first tranche of up to about $1B in loans to more than 12 OEMs was being prepared.
- VaultCo keeps its purchase quantities private and says it is in talks with more than 70 firms. Requests include specific magnets, powders and alloys.

**Status**
- First physical delivery: 12,000 t of DRC copper from Mercuria in the week of 15 Oct 2026. It is linked to Gecamines' share of Tenke Fungurume, which is 80% owned by China's CMOC.
- VaultCo has published no rules on sourcing, origin, price floors or buying formulas.

**Broker implication (assessment)**
- Material held in the Vault is not automatically DFARS-compliant.
- Defense clients can join as OEM participants, and Vault demand competes for the same non-China lots.
- Traxys has said some Arafura NdPr/DyTb volumes may go to the Vault.

## 3. Allied stockpiles
- **JOGMEC (Japan).**
  - Holds 34 rare metals; contents are undisclosed.
  - The target is generally 60 days of consumption, and up to about 180 days for high-risk minerals (IEA).
  - Releases go to Japanese industry.
  - JOGMEC also co-invests in non-China supply, e.g., up to C$47.668M in the Lofdal heavy rare-earth project with Toyota Tsusho (July 2026).
- **KOMIR (Korea).**
  - KOMIR holds the rare metals; the Public Procurement Service holds non-ferrous metals.
  - It plans to cut rare-metal release time from 60 days to 30 (IEA).
  - Releases are domestic only.
- **Australia, Critical Minerals Strategic Reserve (Export Finance Australia).**
  - Its powers took effect on 1 Apr 2026: offtakes at fixed or floating prices, forward-offtake trading, aggregation and stockpiling.
  - The package totals A$1.2B.
  - First use: a preliminary agreement for up to 500 t/yr of rare earths from Arafura's Nolans project (24 May 2026). No material is expected before about 2029.
- **EU, RESourceEU** (plan of 3 Dec 2025).
  - Joint purchasing from March 2026 and a stockpiling pilot.
  - Reuters (May 2026): tungsten, rare earths and gallium are shortlisted for the first joint stockpile.
  - Operating status is unconfirmed.
- **(Assessment)** None of these sells to US defense buyers. Australia's reserve is the only one designed to resell to partners.

## 4. Which traders publicly offer DFARS-compliant or non-China material
- **Explicit DFARS claim:** only **Magnetic Component Engineering (MCE)**. It says it "holds a large inventory of DFARS compliant rare earths" and "manufactures DFARS and ITAR compliant magnets" (https://www.mceproducts.com/dfars-itar-compliance/). **(Assessment)** In 2026 marketing, "DFARS compliant" usually means the pre-2027 melted-or-produced test. Ask for mine-to-magnet evidence before relying on it.
- **Documented non-China supply contracts, mostly future:**
  - **Traxys North America:** Arafura NdPr 500 t/yr and DyTb 7.5 t/yr (binding term sheet, May 2026, subject to FID); NioCorp's full rare-earth, scandium and titanium output under a 15-year definitive agreement (Oct 2026).
  - **Traxys Europe:** El Moto (Spain) tungsten concentrate, exclusive for at least 10 years from Q1 2029; Arafura NdPr up to 300 t/yr.
  - **Sojitz (via JARE):** up to 65% of Lynas Dy and Tb (imports since Oct 2025) and 75% of Lynas medium and heavy rare earths, now including samarium (Mar 2026). This supply is earmarked for Japan.
  - **Glencore:** refined cobalt from Nikkelverk (Norway) and Murrin Murrin (Australia), already supplying DLA and the Vault.
  - **Wogen:** exclusive marketing of Rwandan tantalum concentrates (Aterian/Eastinco, 2026).
- **No origin or DFARS statement on their websites:** Midwest Tungsten, Eagle Alloys, ESPI, Goodfellow, Torrey Hills, Stanford Materials, Stanford Advanced Materials, Edgetech, Adams, Bunting, IBS Magnet, Allstar, Dexter, Tradium, CRONIMET, Darton and Gerald.
  - Adams has a Beijing office, Gerald a Shanghai office and Wogen China and Hong Kong desks.
  - Stanford Materials claims to be "US-owned and operated fully integrated" but does not disclose where its oxides come from.
- **(Assessment)** Compliant spot stock for 2027 is scarce. Most documented non-China volumes are already contracted to governments (DLA, Vault, JARE) or start in 2028-2029.

## 5. Which labs can provide origin evidence, not just grade
- **Physical provenance methods (commercial):**
  - **Source Certain** (Perth, with offices in Colorado and York). It tests the material itself, using trace-element analysis (TEA) and stable-isotope ratio analysis (SIRA) against reference profiles from approved sources. Its stated minerals work covers gold, diamonds and exploration; no tungsten, tantalum or rare-earth case was found.
  - **Isobar Science** (Miami). Commercial Pb and Sr isotope fingerprinting; no Nd isotopes and no stated metals programme.
  - **ALS Sweden** runs a trace-metal and isotope laboratory, and **Actlabs** has a geochronology and isotopes line. In neither case could the scope be confirmed.
  - **BGR's Analytical Fingerprint (AFP)** for coltan, cassiterite and wolframite concentrates is the best-known origin method. BGR's site returned errors this session, so it is not in the file and its details are not re-verified.
- **Limitations (assessment):**
  - These methods match a sample to a reference database. They work best on **concentrates**: mineralogy, trace elements and isotopes survive beneficiation.
  - Refining, solvent-extraction separation, reduction and melting strip most of that signal. Origin testing of **refined Ta/W/Mo metal, rare-earth oxides or finished NdFeB/SmCo magnets** is not an established commercial service.
  - For refined products, origin evidence has to come from chain-of-custody documents, witnessed sampling and sealed retained samples. GDMS impurity profiles (for example EAG, to 7N purity) can then check that each lot matches the stated producer's known signature.
- **Grade, impurity and specification labs** (US or allied):
  - EAG (GDMS)
  - NSL Analytical (ISO/IEC 17025, Nadcap, ITAR)
  - Luvak
  - LTI
  - Dirats
  - IMR (Curtiss-Wright)
  - ATS (now SGS)
  - Element
  - WMT&R (mechanical testing)
- **Witnessing and umpire:**
  - Alex Stewart International: minor metals; UKAS ISO 17025 lab in Liverpool.
  - Alfred H Knight: family-owned; US mineral lab in Spartanburg, SC.
  - Ledoux & Co.: US umpire assays; ISO/IEC 17025.
  - Cotecna
  - Bureau Veritas
- **Documentary chain of custody:**
  - ITSCI: tin, tantalum and tungsten from Burundi, DRC, Rwanda and Uganda; about 3,000 mine sites; over 23,000 t/yr.
  - Circulor: has traced 16 critical rare-earth materials back to the mine; Bureau Veritas partner.
  - Cartograph: supplier-origin requests through its "Scout Agent". It notes that mill certificates usually stop at the melt. **(Assessment)** A competitor or partner for a broker's compliance service.

## 6. Top 10 partner prospects (traders)
1. Traxys North America (New York). Independent; contracted non-China NdPr/DyTb (Arafura) and NioCorp REO/Sc/Ti; Project Vault supplier.
2. Traxys Europe (Luxembourg). El Moto tungsten concentrate (from 2029) and Arafura NdPr; APT-indexed, exclusive.
3. Wogen Resources (London). Employee-held minor-metals house; exclusive Rwandan Ta concentrates; W/Mo/Co; has done prepay deals. Must segregate lots from its China desk.
4. Magnetic Component Engineering (US). The only distributor found that advertises DFARS-compliant rare-earth magnet stock.
5. Sojitz (Tokyo). Lynas Dy/Tb/Sm and future JAGA gallium. Japan-earmarked, but worth asking for surplus samarium (SmCo) and gallium.
6. Glencore (Baar). Non-China refined cobalt brands (Nikkelverk, Murrin Murrin) for SmCo and superalloys; large and already committed to DLA and the Vault.
7. Darton Commodities (Guildford). Cobalt-metal specialist offering consignment and finance; origin and its Marex ownership need confirming.
8. TRADIUM (Neu-Isenburg). Owner-managed, with physical rare-earth oxide and minor-metal stock in a bonded warehouse; origin must be proven lot by lot.
9. Midwest Tungsten Service (Willowbrook, IL). ITAR-registered US stock of W, WHA, Ta and Mo mill products; no origin data.
10. Dexter Magnetic Technologies (Elk Grove Village, IL). AS9100 magnet distributor and assembler with sister brands (Permag, EEC, MCE).

## 7. Top 10 verification partners (labs)
1. Source Certain. Commercial TEA and SIRA origin verification, with a US office; needs reference libraries built for W/Ta/REE sources.
2. Alex Stewart International. Minor-metals sampling, weighing and assay; government export certification.
3. Alfred H Knight, including the Spartanburg, SC lab. Independent inspection and supervision; US mineral lab.
4. Ledoux & Co. US umpire assays accepted for settlement; on-site witnessing; ISO/IEC 17025.
5. EAG Laboratories. GDMS full-survey impurity profiles for checking lots of high-purity metal against producer signatures.
6. NSL Analytical. ISO/IEC 17025, Nadcap, NQA-1 and ITAR; aerospace spec chemistry.
7. Isobar Science. US commercial Pb/Sr isotope analyses for provenance studies of concentrates.
8. ITSCI. Chain of custody for Great Lakes tin, tantalum and tungsten (for example Wogen's Rwandan tantalum flows).
9. Circulor. Mine-to-product digital traceability, including rare earths.
10. Actlabs. Allied (Canadian) geochemistry with an isotope and geochronology line.

## 8. The real bottleneck
**(Assessment, from the rows)** Two things are scarce:
- **Compliant spot inventory.** The covered-material stock held by distributors and stockholders is of undisclosed origin, and most of it is probably Chinese. The documented non-China flows are tied up by governments (DLA, Vault, JARE) or start in 2028-2029 (Arafura, NioCorp, El Moto, Lofdal).
- **Origin evidence for refined products.** No commercial lab offers validated origin testing of refined metal, separated oxide or finished magnets.

## 9. Uncommitted non-China capacity for 2027
Unknown. No trader or distributor publishes compliant-stock volumes. MCE's "large inventory" is not quantified. Government stockpile disposals for FY2026 and FY2027 are unpublished.

## 10. Gaps: stages with little or no compliant supply
- **Provenance labs:** only 2 rows. No verified commercial origin test for refined Ta/W/Mo, rare-earth oxides or magnets.
- **Distributors:** only MCE makes an explicit DFARS claim, and its 2027 basis is unverified.
- **Government stockpiles:** none is a net seller of covered metals in 2026.

## 11. Completeness checks
- **USGS MCS 2026 government-stockpile tables:** read for tungsten, tantalum, cobalt, germanium and rare earths (FY2025 AMP figures above). Molybdenum shows "None" and gallium "Not available". FY2026 AMP not released.
- **RMI-equivalent check:** not applicable to traders and labs. RMAP assessor firms could not be confirmed: RCS Global and LRQA returned 403, and the ELEVATE domain now redirects to LRQA. No lab row claims RMI assessor status.
- **US government awards since 2020 to entities in this workstream:**
  - Glencore (DLA cobalt and nickel IDIQs; Project Vault): row exists.
  - Traxys, Hartree and Mercuria (Project Vault suppliers): rows exist.
  - Ames Laboratory (US DOE): row exists.
  - The DLA producer awardees (Elmet, Atalco, the Boyertown tantalum processor, US Antimony) belong in the producer workstreams and are recorded here only in `offtakes.jsonl`.
- **Every stage has at least one operating non-covered entity?**
  - trader: yes
  - distributor: yes
  - stockholder: yes
  - government_stockpile: yes
  - assay_lab: yes
  - inspection_sampling: yes
  - provenance_lab: yes, but neither row has documented work on covered metals
  - audit_certification: yes

## 12. What could not be verified
- **Not included** (website unreachable, not verifiable without search, or no relevant business found): Mitsui, Hanwa, Mitsubishi Corporation RtM, Sumitomo Corporation, Marubeni, Iwatani, Ultra Minor Metals, HMW Hauner, Kohlhase, Metal-Tech, AMG, Trafigura, Admat, Ed Fagan, NewMet, Integrated Magnetics, American Elements, Atlantic Equipment Engineers (domain parked), Intertek, SGS (seen only through ATS and Isobar), RCS Global, BGR, Oritain (no minerals offering on its site), Minespider (battery-focused), Kiwa, TUV, Colorado School of Mines.
- **Second-hand details:**
  - DLA award details come from Argus search snippets; the article could not be fetched.
  - DLA sales mechanics come from snippets of DLA documents.
  - The EU stockpile shortlist comes from a Reuters snippet.
- **Excluded list:** not compiled. The Chinese trader sites (chinatungsten.com, en.minmetals.com.cn) were unreachable, and no source in hand names covered-country traders. Producer-level exclusions are handled by the chain workstreams.
