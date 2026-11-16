# Molybdenum workstream progress (as of 2026-11-16)

Status keys: [x] done (rows written), [-] dropped (reason), [ ] not done (reason)

Files: suppliers.jsonl 63 rows; offtakes.jsonl 9; excluded.jsonl 13; sources.jsonl 98. Validator: 0 errors, 0 warnings.

**Method limit:** the shared WebSearch budget for the turn ran out early (after the Centerra/Molymet steps). Everything after that was checked by direct fetches of company sites, exchange/regulator filings and USGS PDFs only. Entities whose sites were unreachable were left out or written at low confidence; 2026 news could not be searched for those (stated in each row's notes).

## Chain checks
- [x] USGS MCS 2026 molybdenum chapter (downloaded; producers: US, Armenia, Australia, Canada, Chile, China, Iran, Kazakhstan, N. Korea, S. Korea, Mexico, Mongolia, Peru, Russia, Uzbekistan)
- [x] US government awards since 2020: Elmet (DoW $450M committed investment; DLA Strategic Materials ~$36M TZM and Mo/W wire; DoW $4.3M Mo interceptor components), Amaero (EXIM $22.8M). USGS: no government stockpile Mo actions (coordinator: FY2025 AMP lists Mo actions "None"). Dedicated search pass could not be run (budget); checked coordinator cross-check list and company releases.
- [x] Allied programs: Canada CMRDD contribution to Greenland Resources (2026); EU RESourceEU priority mention for Malmbjerg (Dec 2025); CFIUS clearance of Molymet/Rhenium Alloys (2026)
- [x] DFARS / statute status (in chain_notes.md)

## Mining / concentrate
- [x] Climax Molybdenum (FCX): Climax mine, Henderson mine
- [x] FCX by-product: Sierrita, Bagdad, Morenci, Cerro Verde (Chino: no Mo reported in 10-K)
- [x] Centerra: Thompson Creek (construction, first production mid-2027)
- [x] Rio Tinto Kennecott Bingham Canyon (medium; Rio production page not reached; flagged minority Chinalco holding in parent)
- [x] Southern Copper: Buenavista, La Caridad, Toquepala, Cuajone (SMM volumes; 10-Q text not machine-readable)
- [x] Codelco: Chuquicamata (incl. Radomiro Tomic ore), El Teniente, Andina (Ministro Hales: no Mo listed in Memoria)
- [x] Antofagasta: Los Pelambres, Centinela
- [x] Anglo American: Los Bronces (low), Collahuasi (low), Quellaveco (medium) - Anglo does not report Mo by mine
- [x] Sierra Gorda (KGHM 55% / South32 45%)
- [x] Teck: Highland Valley, Quebrada Blanca; Antamina (Teck 22.5%)
- [x] Taseko (now Trekor Metals) Gibraltar
- [x] Lundin Caserones (low; SMM only)
- [x] MMG Las Bambas (Chinese-owned, flagged)
- [x] Chinalco Toromocho (Chinese-owned, flagged)
- [x] Erdenet (Mongolia, SOE)
- [x] Almalyk MMC (Uzbekistan; low)
- [x] Zangezur CMC (Armenia; ownership opaque, flagged unknown)
- [x] Greenland Resources Malmbjerg (planned; offtakes with Outokumpu, SSAB; Molymet MOU)
- [ ] Hudbay Constancia - site returned 403; no Mo data fetched (gap)
- [ ] Montana Resources (Butte; USGS's Montana by-product op) - site 403; not written (gap)
- [-] KGHM Robinson (NV) - only ~0.03 Mlb Mo in H1 2026 (KGHM H1 2026 presentation); too small, noted in Sierra Gorda row
- [ ] Agarak (Armenia), Kazakhstan producers (4,300 t), Republic of Korea producer (500 t), Australian producer (1,000 t) - not identified (search budget); gap
- [ ] Kitsault (BC), Mt Hope (NV), Spinifex Ridge / Merlin / Molyhil (Australia), Knaben (Norway), Amerigo MVC (Chile), CuMo, Resolution - not checked (search budget). None appeared in sources read as producing before 2029.
- [-] Centerra Endako (BC): care and maintenance, 75% Centerra / 25% Moon River Capital; no restart plan (Centerra 2024 plan; Q3 2026 MD&A) -> closed

## Roasting / chemical
- [x] Climax Fort Madison IA; Rotterdam NL; Stowmarket UK (FeMo); Sierrita roasters; Bagdad pressure-leach
- [x] Centerra Langeloth PA
- [x] Molymet: Nos, Molynor, Molymex, Molymet Belgium (ex-Sadaci); China plant stake (Luoyang Hi-Tech) sold to CMOC ~2020 (excluded row); only Beijing sales office remains
- [x] Codelco Molyb (Mejillones) - location from general knowledge, flagged
- [x] Taiyo Koko (Japan) - FeMo, MoO3, molybdates
- [x] Treibacher (Austria) - FeMo, FeNiMo
- [-] Kennecott Mo processing - concentrate is tolled by Molymet (Molymet AR 2025); no Kennecott roaster row
- [ ] Korean roasters/FeMo producers (Korea = 21% of US FeMo imports 2021-24) - not identified (search budget); key gap
- [ ] Indian FeMo producers, Armenian FeMo converters - not identified (search budget)

## Metal powder / mill products
- [x] Plansee Reutte (powder + mill products); Plansee USA Franklin not written separately (production role not stated on group site)
- [x] H.C. Starck Solutions successor = Elmet Technologies (acquired 2023): Lewiston ME, Euclid OH, Coldwater MI + powder row; Newton MA not listed by Elmet
- [x] ams OSRAM Schwabmunchen (Germany) - being acquired by Elmet (closing Q1 2027)
- [x] Rhenium Alloys (North Ridgeville OH) - acquired by Molymet Aug 2026 (Molymet Alloys)
- [x] Molymet Germany (Bitterfeld) Mo powder 1,700 t/yr; MolymetNos plasma spherical powders
- [x] Climax - no Mo metal powder production found
- [x] A.L.M.T. (Japan): Toyama Works powder; Toyama/Sakata mill products
- [x] Toho Kinzoku (Taiyo Koko subsidiary) - Mo wire/rod/plate (low)
- [x] Global Tungsten & Powders Towanda - PM Mo and MT-104 TZM-type billets
- [x] Amaero (McDonald TN) - coordinator lead; EXIM US$22.8M; Mo powders confirmed on company site
- [ ] Japan New Metals (site unreachable), Nippon Tungsten (no Mo found on homepage), Ultramet, Materion, Tekna, 6K Additive, Korean target makers - not checked (search budget)

## Recycling
- [x] Taiyo Koko (spent HDS catalysts, since 1978)
- [x] Treibacher Althofen (spent refinery catalysts)
- [x] AMG Vanadium (Cambridge OH; FeNiMoly) - low
- [ ] Gulf Chemical & Metallurgical (Freeport TX) - site connection failed; not written (gap)
- [ ] Shell & AMG Recycling (Saudi), Moxba-Metrex, other catalyst recyclers - not checked (search budget)

## Excluded (China / Russia / Iran) - 13 rows
- [x] China: JDC (Jinduicheng mine, Dongou mine, roasting/chemical, metal processing); CMOC (Sandaozhuang, Shangfanggou, Luanchuan smelter); Luoyang Hi-Tech Metals; Jiangxi Copper (Dexing)
- [x] Russia: Zhireken GOK; Polema (Tula)
- [x] Iran: NICICO Sarcheshmeh; Sungun
- [ ] Sorsk GOK, Bystrinsky (Nornickel), Zijin, Huludao/Liaoning roasters, Iranian FeMo - no accessible source found without search; not written

## Offtakes - 9 rows
- [x] Molymet tolling: Codelco, Sierra Gorda, Rio Tinto Commercial Americas
- [x] Elmet: DLA Strategic Materials (~$36M), DoW ($4.3M)
- [x] Greenland Resources: Outokumpu, SSAB (binding); Molymet MOU; other EU steel MOUs
