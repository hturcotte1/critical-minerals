# Tungsten workstream progress (as of 2026-11-16)

Final counts: 75 supplier rows, 12 offtakes, 29 excluded rows, 109 sources. Validator: 0 errors, 0 warnings.

Method note: the shared WebSearch budget ran out after about 45 searches (early in the run). After that, all work used direct fetches of primary pages: company websites, SEC EDGAR (Form SD, 10-K, S-1, 8-K), USGS MCS 2026 and Minerals Yearbooks, LSE RNS headlines and Traxys releases. An attempt to page the ASX data API was denied by the permission system, so it was not used again. ASX announcement PDFs need terms to be accepted, so they were not read. Entities that only ASX documents or search could confirm have low confidence or were left out (see below).

## Done (rows written)
- USGS MCS 2026 tungsten chapter fetched: country list and DLA Annual Materials Plan figures recorded in chain_notes.
- Almonty: Sangdong mine, Panasqueira, Los Santos tailings restart, Gentung (MT), Yeongwol oxide plant (planned), Almonty Rwanda. 6 rows, 3 offtakes (GTP 21-yr, TPW/Metal Tech, WBH Los Santos).
- Plansee Group: GTP Towanda (chem, powder, recycling), GTP Finland (Jyvaskyla), Plansee Reutte (powder, mill products), Plansee Composite Materials Lechbruck, CIME Bocuze / Plansee Tungsten Alloys, Mi-Tech Tungsten Metals (Indianapolis). 9 rows, 1 offtake (Manhattan Five oxide reserve JV).
- Elmet Group: Coldwater MI, Euclid OH, Lewiston ME, Springer APT JV (NV, planned) and ams OSRAM Schwabmuenchen (powder plus fabrication; acquisition pending Q1 2027); Blue Moon Springer mine/mill. 7 rows. Offtakes: DLA IDIQ US$2bn, Blue Moon concentrate.
- Masan: Nui Phao mine and Masan Tungsten Chemicals (2 rows). Offtakes: Elmet ~1,250 t WO3/yr for 8 years or more; GB Innovation tolling.
- H.C. Starck Tungsten Goslar (chem, powder, recycling), Japan New Metals Akita (chem, powder, recycling), A.L.M.T. Toyama (powder, mill products), Kennametal Fallon, Huntsville and La Paz (Bolivia). 11 rows.
- WBH (Sandvik): Mittersill mine, St. Martin smelter (chem, powder, recycling), Chiplun India recycling. 5 rows.
- Buffalo Tungsten (Depew NY), Niagara Refining (Depew NY, Sumitomo; chem and recycling), Wolfmet / M&I Materials, TaeguTec, Tungco (Madisonville KY; Limerick IE), Asia Tungsten Products Vietnam (FeW), Jing Yuan (Taiwan), Tungamoy Metals (Korea, Xiamen Tungsten affiliate), KENEE Mining Vietnam, S.P.T. spol. s r.o. 14 rows.
- Remaining RMI-listed smelters: Cronimet Brasil, TANIOBIS Smelting, Lianyou Metals, Lianyou Resources, Philippine Bonway, Philippine Chuangxin, Tungsten Vietnam JSC. 7 rows, mostly low confidence.
- Projects and award recipients: Fireweed Mactung, Guardian Pilot Mountain, Northcliff Sisson, Tungsten West Hemerdon, Group 6 Dolphin, Abenojar El Moto, Amaero (TN), Trinity Nyakabingo, EQ Resources Barruecopardo, GB Innovation, Boguty (Kazakhstan, Chinese-owned), Upper Kairakty JV (planned). 12 rows, 4 offtakes (Traxys/El Moto, WBH/Dolphin, Traxys/Dolphin, EQR/Elmet).
- Wolfram Industrie (Nussdorf; Dachau), Treibacher Industrie (Althofen), 6K Additive (Burgettstown PA). 4 rows.
- Excluded: 29 rows covering China (Xiamen Tungsten, CTHM/Minmetals, Shizhuyuan, JXTC, CMOC, Jiangwu H.C. Starck, and the other RMI-listed Chinese smelters, plus Kennametal Tianjin), Russia (Gidrometallurg, KZTS, Primorskiy GOK, Lermontovskoye, Novoorlovsk, Tyrnyauz, Bom-Gorkhon/Zakamensk) and North Korea (Man-nyon).
- SEC Form SD pass: TI (filed 2026-06-01), AMD (2026-05-28), Micron (2026-05-20) and Kennametal (2026-05-21) exhibits read. RMAP statuses as of Jan 2026 applied. New non-covered smelters added: Jing Yuan, KENEE, S.P.T., Tungamoy.
- US government awards pass: Elmet (DoW US$450m; DLA US$2bn IDIQ), Fireweed (DPA III US$15.8m), Guardian (DPA III US$6.2m), Sisson (DPA III per USGS, amount not verified), Amaero (EXIM US$22.8m), 6K Additive (DPAI US$23.4m), Blue Moon (indirect via Elmet). All have rows.
- Coordinator leads: Amaero, Guardian, Fireweed, Elmet DLA, El Moto/Traxys and DLA AMP figures, all incorporated.

## Dropped (with reason)
- Almonty Valtreixal (Spain): no development timeline found ("when market conditions warrant").
- Kennametal Latrobe PA: technology centre (R&D), not a listed production site in the FY2026 10-K. Kennametal penetrator/armor production site not identified.
- American Tungsten Corp. IMA mine (Idaho): exploration and drilling with a PEA in progress (Oct 2026); no development timeline.
- Guardian Tempiute (NV) and Garfield Flats: exploration or option stage; mentioned in the Pilot Mountain row notes.
- Patriot Critical Minerals: identity could not be verified.
- Cantung (Canada): closed, no restart plan found (not re-checked; WebSearch exhausted).
- Ceratizit: no separate row, because its tungsten powder and recycling run through GTP (USA and Finland). Stadler Raw Materials is a scrap collector only.
- Sandvik recycling: covered by the WBH St. Martin and Chiplun rows.
- Woltech Korea, KGETS, ACL Metais, Albasteel, Avon Specialty Metals: not on the TI, AMD or Micron 2026 Form SD tungsten lists; websites unreachable, parked or under construction. No rows.
- Nui Phao H.C. Starck Tungsten Chemicals: covered by the Masan Tungsten Chemicals row.
- Tejing (Vietnam) Tungsten: no source reachable; not on 2026 SD lists.
- Iscar (Israel) and Korea Tungsten: Iscar's own powder production not verified. TaeguTec has a row.

## Not completed (open leads, unverified)
- EQ Resources Mt Carbine (QLD): operating mine, but no readable source (company site behind a bot checkpoint; ASX documents need terms). No row.
- Tungsten Mining NL (Watershed, QLD): ASX headline "Watershed DFS Delivers Outstanding Economics" (15 Nov 2026) seen, but the document could not be read. No row.
- Other Australian projects (Molyhil/Thor, Kilba, Big Hill, Hatches Creek, O'Callaghans): not checked.
- Uzbekistan (UzKTJM Chirchiq; Ingichka/Koytash), Mongolia, Bolivian cooperatives, Peru (Pasto Bueno/Malaga), Brazil scheelite (Brejui), Myanmar, Uganda/Burundi/DRC: not verified. No rows.
- Kazakhstan North Katpar: not verified.
- Nippon Tungsten (Fukuoka): website unreachable.
- Ownership of Lianyou Metals/Resources, Philippine Bonway/Chuangxin, Tungsten Vietnam JSC, KENEE, S.P.T., Trinity Metals, Boguty and the Upper Kairakty JV: not verified.
