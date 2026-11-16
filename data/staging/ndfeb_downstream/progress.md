# NdFeB downstream workstream - progress (2026-11-16) - COMPLETE

Stages: metal_alloy, magnet_sintered, magnet_bonded, recycling, ancillary_inputs, substitute.
Totals: 65 supplier rows, 39 offtakes, 16 excluded, 103 sources; validate.py: 0 errors, 0 warnings.

Session constraint: the shared WebSearch budget ran out after ~10 searches by this agent. Everything after
that was verified by WebFetch of company / filing / government pages and URLs surfaced earlier (no
search-engine queries). Where 2026 news could not be checked, rows say so and carry low/medium confidence.

## Done (rows written)
- MP Materials: Independence metal_alloy + magnet_sintered; 10X Northlake (construction); Mountain Pass recycling line (planned)
- VAC group: eVAC Sumter; VAC Hanau; VAC Horna Streda (Slovakia); Neorem Ulvila (Finland)
- Energy Fuels/ASM Korean Metals Plant (metal_alloy); Energy Fuels American Metals Plant (planned, OSC-backed)
- USA Rare Earth: Stillwater; Blacksburg SC (magnet + metal); Wheat Ridge (recycling); LCM Ellesmere Port; LCM Europe Lacq
- Noveon: San Marcos (magnet + M2M recycling); Noveon-Kangwon Korea JV (MoU)
- Vulcan Elements: RTP (operating), Benson (construction)
- ReElement (recycling route); Cyclic Materials (Mesa, Kingston, South Carolina)
- HyProMag: USA Northlake (recycling + magnet), USA SC and NV pre-processing spokes, UK Tyseley (recycling + magnet), Pforzheim DE
- Ionic Technologies Belfast; Caremag Lacq; MagREEsource; Geomega; Momentum Technologies
- Phoenix Tailings: Exeter (operating metal), Freedom Facility Rochester (planned)
- REalloys Euclid; SRC Saskatoon; REalloys HREMF (Dy/Tb metal, 2028)
- Neo: Narva magnets; Magnequench Korat powder; Project GAUSS metallization (planned)
- Japan: Shin-Etsu Takefu (magnet + recycling); Shin-Etsu Vietnam; Daido Nakatsugawa + Thailand; Aichi Steel MAGFINE; Proterial Japan (low conf.) + Proterial India (planned); TDK (low conf.)
- Europe small: Magneti Ljubljana (sintered + bonded); MS-Schramberg (bonded)
- US others: Arnold (Rochester); MCE (fabricator, low conf.); Advanced Magnet Lab (DLA $2M; low conf.); Hertha Metals (high-purity iron)
- Ancillary: Rio Tinto/U.S. Borax (Boron, CA); Eti Maden (Turkey)
- Substitute: Niron Sartell + Minneapolis pilot
- Excluded (16): JL Mag Ganzhou, Ningbo Yunsheng, Zhenghai Yantai, Earth-Panda Hefei, China Northern RE Baotou, Magnequench Tianjin, Neo Chuzhou, Shin-Etsu Changting alloy, Daido Guangdong, Arnold Shenzhen, Arnold GQD Ganzhou JV mine, VAC Shenyang, Zhejiang Aichi, Shenghe affiliate (ex-Neo China separation), TDK China, Proterial China JV
- Offtakes (39): see offtakes.jsonl (MP-DoD x2, MP-GM, MP-Apple, eVAC-GM terminated, eVAC/Noveon-DLA, Noveon-Nidec/GM/ABB, ASM-Noveon/VAC/Magnequench, Solvay-Noveon, Lynas-Noveon MoU, Torngat/Pensana-VAC MoUs, Cyclic-VAC, Serra Verde-US SIIE, ReElement-Vulcan/POSCO, ERI-ReElement, Ucore-Vulcan MoU, Vulcan-Army, Neo-Bosch MoU, Neo-Tier1, Carester-Neo, Carester-Stellantis, Carester-LCM Europe, Cyclic-Neo MoU, ERI-Cyclic, SRC-REalloys, Critical Metals-REalloys, REalloys-JS Link LOI, REalloys-Army ROFO, ILS-HyProMag USA, Ionic-DNA Link MoU, Rainbow-Neo MoU)

## Coordinator leads (status)
- ReElement $80M OSC (Nov 2025): recorded; "fell through" (Reuters) is noted as an unverified lead
- ReElement $25M DoW (13 Jul 2026): confirmed (ReElement newsroom)
- Vulcan $620M OSC + $50M CHIPS LOI: recorded (InvestorNews; ReElement newsroom); closing not confirmed
- HyProMag USA EXIM LOI $92M (12 Jun 2025): confirmed (CoTec news + InvestorNews)
- USAR CHIPS LOI 26 Jan 2026 -> definitive 3 Jun 2026: confirmed (NIST)
- MCE: row added as fabricator (DFARS claim likely pre-2027 test)
- DLA FY2025 AMP (450 t NdFeB block, 300 t NdPr oxide): in chain_notes (USGS MCS 2026)
- Proterial India 1,200 t/yr plant (Jul 2026): confirmed (SMM), planned row added; HRE-free sample lead not verified

## Not verified / dropped (with reason)
- Santoku, Resonac/Showa Denko alloy (Japan/Vietnam): no accessible primary page (santoku.co.jp is a supermarket; Resonac site has no RE content) - no row
- Star Group (domain unresolvable), JS Link (HTTP 403), POSCO International US magnet complex (MoU, no timeline) - no rows
- India REPM scheme awardees (Sona Comstar, Uno Minda, Midwest Advanced Materials), IREL NdFeB: could not verify - no rows
- VTRE (Vietnam): 2024-2026 status unverifiable - dropped
- Quadrant (US): only a 2022 DOE mention of a 2024 plan - dropped
- Heraeus Remloy, REEcycle (sites HTTP 503), Minebea Mitsumi, CIT SENAI Brazil, Ionic/Viridion Brazil (no timeline): not entered
- Ferroboron producers (India/Turkey/Japan/Russia KZF): none named in accessible sources - gap noted
- Russian NdFeB/RE metal producers: none verified - no excluded rows
- Chinese makers Zhong Ke San Huan, Tianhe, Innuovo, AT&M, Golden Century, Baotou INST, Ningbo Jintian: sites unreadable - not in excluded
- DMEGC: site shows ferrite/PV only, no NdFeB - not entered
- Nichia SmFeN: not NdFeB - out of scope
