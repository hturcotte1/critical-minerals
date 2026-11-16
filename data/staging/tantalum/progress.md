# Tantalum workstream progress (final, 2026-11-16)

Note: the shared WebSearch budget ran out early in this session (after ~25 searches). Everything after that point was
verified by direct fetches of company sites, filings (SEC Form SD exhibits, ASX/AIM releases), trade-association
archives (International Tin Association) and government pages only. Rows where 2026 news could not be checked say so.

Final counts: 57 supplier rows, 25 excluded, 9 offtakes, 130 sources; validate.py: 0 errors, 0 warnings.

## Done (rows written)
- [x] USGS MCS 2026 tantalum chapter (production table, import shares, DLA award text)
- [x] ITA/DOC Oct 2022 list of global tantalum concentrate consumers (facility baseline)
- [x] SEC Form SD 2026 smelter lists: Flex (CIDs + RMAP status), Texas Instruments, Celestica (non-RMAP legacy names)
- [x] Global Advanced Metals: Boyertown (chem, powder/ingot, mill), Aizu (powder), Greenbushes secondary plant, Wodgina TRPs; DLA x2, DoD MCEIP, EXIM; offtakes (DLA Ta, DLA Nb, General Atomics, PLS 2017)
- [x] Talison Greenbushes (Sn-Ta concentrate for GAM; Tianqi control)
- [x] PLS Pilgangoora (FY26 tantalite 220,585 lb)
- [x] TANIOBIS: Goslar (chem, powder, recycling), Laufenburg (chlorides), Map Ta Phut (chem, powder; expansion from 2027-H1), Mito (powder)
- [x] AMG Brasil: Mibra mine and Sao Joao del Rei oxides; TANIOBIS preferential rights offtake
- [x] Ulba (chem, powder/ingot, mill): Russian feed (Solikamsk/Lovozero audits Apr 2026) -> likely_noncompliant
- [x] NPM Silmet (chem, metal); Neo: no sale found in 2026 news
- [x] Mitsui Kinzoku Omuta; Taki Chemical; MPIL Taloja; Resind
- [x] Recyclers: Exotech, Avon Specialty Metals, D Block Metals, QuantumClean (UCT), Telex Metals (low confidence)
- [x] Materion Newton (powder/metal; mill products); KEMET de Mexico (K-salt, powder; captive)
- [x] Andrada Uis; Eastinco/Aterian (coordinator lead: Wogen exclusive, first exports Feb 2026); Trinity Musha (DFC grant)
- [x] Tanco (Sinomine; flagged); SMB Rubaya (conflict; flagged); MMR (DRC); Tantalex Manono (DRC); Penouta (Spain, restart planned)
- [x] Mineracao Taboca: Pitinga and FeNbTa/Pirapora; CNMC ownership confirmed (ITA 2024-11-27 and 2025-08-29)
- [x] PowerX (Rwanda; low confidence)
- [x] Mill products/targets: Plansee, STEREON Metals Hermsdorf (ex-QSIL/H.C. Starck Hermsdorf), Solstice (ex-Honeywell EM, Spokane), ATI Albany, JX Hitachinaka, JX Mesa, Tokyo Denkai
- [x] Globe Metals Kanyika (planned 2028; mine + refinery)
- [x] Metalysis (UK) and Meta Material DOOEL (North Macedonia, low confidence)
- [x] Excluded: 23 China smelters/refiners (with CIDs from Flex 2026 where shown) + Solikamsk and Lovozero (Russia)
- [x] Coordinator lead: Argus source added to GAM DLA award row and offtake
- [x] chain_notes.md written

## Dropped (with reason)
- Hi-Temp Specialty Metals: domain parked ("lander"); legacy name without RMAP status in Celestica 2026 Form SD; no evidence of operation.
- CP Metals Inc.: domain parked; legacy name without RMAP status in Celestica 2026 Form SD; no evidence of operation.
- Kyocera AVX: tantalum capacitor maker (electronic components), not a tantalum metal/powder producer.
- H.C. Starck Solutions Euclid OH: now Elmet Technologies (acquired 2023); product range lists Mo, W, Nb only (no tantalum). Niobium capability noted.
- Bikita (Zimbabwe, Sinomine): tantalum present in the LCT pegmatite but no tantalum production found; noted in the Tanco row.
- Kenticha (Ethiopia): state tantalum mine halted Dec 2017 (Wikipedia); no current operator verified.
- Bald Hill (MinRes): restarted May 2026 for spodumene; originally a tantalum mine but no current tantalum output found.
- Mt Cattlin, Marropino (Noventa), Abu Dabbab, Ghurayyah: no 2025-2026 evidence of tantalum production or an active development timeline could be fetched (search budget exhausted; Abu Dabbab last reported "in limbo", ITA 2015).
- CBMM / Niobec: niobium only, no tantalum product.
- Malaysia Smelting Corp / Thaisarco (tin slag): no 2026 evidence of tantalum-slag sales; TANIOBIS buys slag only from unnamed RMAP tin smelters. Not given rows.
- Tosoh SMD (Grove City OH) and Admat (PA): websites blocked automated access; nothing verifiable this session.
- 5D Production OU (Estonia): appears only as a legacy name in Celestica 2026 Form SD; no verifiable information.
- KEMET Blue Powder (NV): legacy name without RMAP status in Celestica 2026 Form SD; not verified as an operating plant (noted in KEMET row).
- Wodgina tantalum is recorded as GAM's recovery-plant row (MinRes/Albemarle mine operator has no separate tantalum product).
