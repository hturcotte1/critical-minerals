# traders_labs progress (started 2026-11-16)

NOTE: the shared WebSearch budget (200 calls across all agents) ran out early in this workstream.
After that, entities were verified only by fetching their own websites / known primary pages
(no 2026 news search possible). Such rows say so in `notes` and carry medium/low confidence.

## Done - government stockpiles / reserves (6)
- [x] DLA Strategic Materials (NDS) - FY2025 AMP from USGS MCS 2026; FY2026/FY2027 AMP not released; FY2026 IDIQ buys
- [x] VaultCo / Project Vault (EXIM $10B loan; Glencore, Mercuria, Hartree, Traxys)
- [x] Export Finance Australia - Critical Minerals Strategic Reserve (Arafura preliminary offtake)
- [x] JOGMEC (Japan)
- [x] KOMIR (Korea) - low confidence
- [x] EU RESourceEU stockpiling/joint purchasing - planned, low confidence

## Done - traders / distributors / stockholders (24)
- [x] Traxys North America; Traxys Europe (2 rows)
- [x] Wogen Resources
- [x] Sojitz
- [x] Toyota Tsusho (low confidence)
- [x] Glencore (cobalt)
- [x] Darton Commodities (cobalt; Marex link unconfirmed)
- [x] Gerald Group (low relevance)
- [x] Tradium
- [x] Cronimet
- [x] Hartree Partners (low confidence)
- [x] Mercuria Americas
- [x] Midwest Tungsten Service; Eagle Alloys; ESPI Metals; Goodfellow
- [x] Dexter Magnetic Technologies; MCE; Adams Magnetic; Bunting; IBS Magnet
- [x] Stanford Materials; Stanford Advanced Materials; Edgetech Industries

## Done - additional distributors (2)
- [x] Torrey Hills Technologies; Allstar Magnetics (low confidence)

## Done - labs (26)
- [x] assay_lab (16): EAG; NSL Analytical; Luvak; Element; LTI; ATS (now SGS); Dirats; IMR Test Labs (Curtiss-Wright); Actlabs; SRC Geoanalytical; ALS; Nagrom; ANSTO; Ames Lab MPC; AHK North America (Spartanburg); WMT&R
- [x] inspection_sampling (5): Bureau Veritas; Alex Stewart International; Alfred H Knight (UK); Ledoux & Co.; Cotecna
- [x] provenance_lab (2): Source Certain; Isobar Science
- [x] audit_certification (3): ITSCI; Circulor; Cartograph (DFARS-compliance software, competitor/partner)

## Done - other files
- [x] offtakes.jsonl: 14 rows (Traxys x4, Wogen, Australia CMSR, DLA x4, VaultCo, JARE/Lynas x2, JAGA gallium)
- [x] chain_notes.md written (DLA sales/AMP, Project Vault, allied stockpiles, DFARS-claim traders, origin-evidence labs, top-10 lists)
- [ ] excluded.jsonl: NOT compiled - Chinese trader sites unreachable (chinatungsten.com 503; en.minmetals.com.cn DNS) and no search budget; optional item

## Dropped / not included (with reason)
- Mitsui & Co.: no 2025-2026 release on rare earths/minor metals found on its release pages; trading role in covered metals not verifiable without search.
- Hanwa Co.: company site shows no rare earth/W/Mo/Co/Ta/Ga/Ge business; not verifiable.
- Mitsubishi Corporation RtM, Sumitomo Corporation, Marubeni, Iwatani: not verified (search budget exhausted); not included.
- Ultra Minor Metals: website host does not resolve (www.ultraminormetals.com); not verified.
- HMW Hauner: site describes small-lot manufacture of pure metals/alloys; no evidence of trading/stockholding of covered metals; not included.
- Atlantic Equipment Engineers (Micron Metals): domain parked/for sale; likely defunct or rebranded; not included.
- Admat, Ed Fagan, NewMet, Integrated Magnetics, American Elements: websites returned 403/503; not verified, not included.
- Kohlhase, Metal-Tech, AMG (trading), Trafigura, Thermo Fisher/Alfa Aesar, Ulbrich, Rolled Alloys, H Cross: not verified (search budget exhausted) or low relevance; not included.
- Labs not included: Intertek (403), SGS own site (403; SGS covered via ATS and Isobar ownership notes), RCS Global (403), LRQA/ELEVATE (403/redirect), BGR AFP (HTTP 400 on all BGR URLs), Oritain (no minerals/metals offering on site), Minespider (battery-passport focus; no 3T/REE on site), SMX (page empty), Kiwa, TUV, Colorado School of Mines, PCIGR and other academic isotope labs (not verified).
