#!/usr/bin/env python3
"""Fill the <!-- TOP10_x --> placeholders in REPORT.md with curated top-10 tables.

Each entry names the row by chain + stage + substrings of company/facility; the
script looks up the current supplier_id and score in data/suppliers.csv so the
tables stay in sync with the spreadsheet. Run after tools/build.py.
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (chain, stage, company substring, facility substring, one-line why)
TOP10 = {
    "ndfeb": ("Top 10 broker prospects (NdFeB)", [
        ("ndfeb", "separation", "Ucore Louisiana", "", "DoW-funded medium/heavy-RE separation from 2027, uncommitted; needs both feed and customers"),
        ("ndfeb", "magnet_sintered", "e-VAC Magnetics", "", "2,000 t/yr sintered, mostly uncommitted after GM's exit (Oct 2026); DLA-qualified; upstream chain must be documented"),
        ("ndfeb", "magnet_sintered", "USA Rare Earth", "Stillwater", "600 rising to 1,200 t/yr sintered, no named offtakes; well funded (Commerce CHIPS); needs proof of alloy origin"),
        ("ndfeb", "separation", "Iluka", "Refinery", "~90% of NdPr and Dy/Tb from 2028 uncommitted; Australian-government financed; seeking customers"),
        ("ndfeb", "metal_alloy", "Korean Metals Plant", "", "Main merchant non-China NdFeB alloy and NdPr metal (Energy Fuels); act before it becomes captive to VAC"),
        ("ndfeb", "magnet_sintered", "Noveon Magnetics Inc.", "San Marcos", "US recycled route fits the statutory recycled-magnet exemption; DLA-qualified; fresh funding"),
        ("ndfeb", "separation", "Rainbow Rare Earths", "", "60% of NdPr uncommitted (Neo has only an MoU); DFC-backed; first production 2028"),
        ("ndfeb", "mining_concentrate", "Pensana", "", "First production 2027, uncommitted, pursuing a US route (EXIM LOI); low confidence"),
        ("ndfeb", "mining_concentrate", "BZNM", "", "12,000 t/yr MREC from Q2 2027 with no offtake; verify the African feed origin and the co-owner"),
        ("ndfeb", "substitute", "Niron Magnetics", "Sartell", "Rare-earth-free substitute, 1,500 t/yr, uncommitted, DoW-backed; not a covered material, so it sidesteps the rule where the design allows"),
    ], "Runners-up: Phoenix Tailings (US metal and separation), HyProMag USA (recycling), Vulcan Elements (10,000 t/yr, commissioning 2027), Caremag (Dy/Tb), REalloys/SRC (Dy/Tb metal 2028), Neo Narva (EU magnets)."),
    "tungsten": ("Top 10 broker prospects (tungsten)", [
        ("tungsten", "metal_powder", "Buffalo Tungsten", "", "Merchant W and WC powder made from non-Chinese oxide, sold to outside customers of any size; owned by Sandvik since Dec 2023"),
        ("tungsten", "mining_concentrate", "EQ Resources Limited (Mt Carbine)", "", "Small Australian producer ramping up, with an A$39M expansion due early 2027 and no offtake found"),
        ("tungsten", "mining_concentrate", "Tungsten West", "", "UK concentrate from 2027, freshly funded; offtakes not found"),
        ("tungsten", "metal_powder", "Elmet Technologies LLC (Lewiston)", "", "US tungsten powder now and a DoW-funded fivefold expansion; much output tied to its own defense programs"),
        ("tungsten", "heavy_alloy_fabrication", "Elmet Technologies LLC (Euclid)", "", "US heavy-alloy and plate producer expanding with DoW money; clean non-PRC feed"),
        ("tungsten", "chemical_intermediate", "Masan Tungsten Chemicals", "", "Largest non-China APT/oxide plant, selling spare capacity as tolling; document origin lot by lot"),
        ("tungsten", "recycling", "Tungco Inc.", "Madisonville", "Independent US scrap processor with uncommitted volumes; scrap-origin paperwork needed for the recycled route"),
        ("tungsten", "mining_concentrate", "Almonty Korea Tungsten Corp. (AKTC)", "Sangdong", "Phase II (~+2,300 t/yr concentrate, 2027) is outside the 21-year GTP contract"),
        ("tungsten", "mining_concentrate", "Group 6 Metals", "", "Small, clean Tasmanian producer ramping up; existing offtakes may be partial"),
        ("tungsten", "mining_concentrate", "Nui Phao Mining", "", "Largest non-China mine, expanding and openly seeking strategic investors and offtakers"),
    ], "Runners-up: Panasqueira (Almonty, Portugal), Guardian Pilot Mountain (Nevada, later), Wolfmet (UK) and Wolfram Industrie (Germany) for heavy alloy, Blue Moon Springer (Nevada, Q4 2027, partly committed to Elmet)."),
    "tantalum": ("Top 10 broker prospects (tantalum)", [
        ("tantalum", "mining_concentrate", "PLS Group", "", "Clean Australian by-product tantalite (~220,600 lb concentrate in FY26) with no disclosed buyer"),
        ("tantalum", "chemical_processing", "AMG Brasil", "", "Mid-size, clean mine-to-oxide chain (Mibra), no disclosed oxide offtakes, rising tantalum volumes"),
        ("tantalum", "mining_concentrate", "Uis Tin Mining", "", "Small Namibian producer marketing traceable, conflict-free concentrate; AIM-listed and seeking capital"),
        ("tantalum", "mining_concentrate", "Trinity Metals", "Musha", "US-backed (DFC, TechMet) Rwandan producer, expanding and courting US buyers"),
        ("tantalum", "chemical_processing", "Metallurgical Products India", "", "Small independent RMAP-conformant K-salt/oxide producer; feed documentation needed"),
        ("tantalum", "recycling", "D Block Metals", "", "US RMAP-conformant tantalum recycler; fits the statutory recycled route if scrap origin is documented"),
        ("tantalum", "recycling", "Exotech", "", "Independent US scrap processor that buys and sells; recycled route with origin paperwork"),
        ("tantalum", "alloy_mill_products", "STEREON Metals", "", "Mid-size EU mill-product and target maker with large stock for aerospace and defense"),
        ("tantalum", "metal_powder_ingot", "Metalysis Ltd", "", "Small UK producer marketing tantalum and C-103 powders to Western defense buyers"),
        ("tantalum", "recycling", "Avon Specialty Metals", "", "RMAP-conformant recycler in a qualifying country (UK)"),
    ], "Runners-up: Resind (Brazil, slag-derived), Globe Metals Kanyika (Malawi, 2028), Eastinco/Aterian via Wogen (Rwanda), and Global Advanced Metals Boyertown. GAM is the key compliant US source, but it is large and its ingot output is tied to DLA."),
    "smco": ("Top 10 broker prospects (SmCo)", [
        ("smco", "magnet", "Electron Energy", "", "The only US SmCo maker; doubling capacity and seeking compliant samarium and cobalt"),
        ("smco", "metal", "LSCV", "", "240 t/yr samarium metal from 2027 on Lynas oxide, aimed at defense SmCo demand"),
        ("smco", "metal", "Less Common Metals", "", "The only operating Western samarium metal plant; supply tight until the Q3 2027 expansion"),
        ("smco", "alloy", "Less Common Metals", "", "Key non-China SmCo alloy source; cobalt origin must be documented"),
        ("smco", "separation", "Solvay", "", "One of few non-China samarium oxide producers, able to scale; feed origin needs verifying"),
        ("smco", "separation", "Lynas Malaysia", "", "Clean samarium oxide since Mar 2026; half of heavy-RE output committed to JARE"),
        ("smco", "magnet", "Arnold Magnetic Technologies AG", "Lupfig", "Established aerospace/defense SmCo maker that must replace Chinese samarium; Thailand line doubles capacity mid-2027"),
        ("smco", "magnet", "Magneti Ljubljana", "", "Independent EU SmCo maker that may welcome buyers; ownership and inputs need diligence"),
        ("smco", "separation", "Ucore", "", "Small, government-funded future Sm/Gd separation source (Louisiana)"),
        ("smco", "magnet", "Vacuumschmelze", "", "Large EU SmCo maker; Energy Fuels acquisition pending (early 2027) could change its sourcing"),
    ], "Also watch REalloys (Ohio, samarium metal, design stage)."),
    "cobalt": ("Top 10 broker prospects (cobalt for SmCo)", [
        ("cobalt", "refining_metal", "Jervois group - Sao Miguel Paulista", "", "~2,000 t/yr uncommitted cobalt cathode from late 2027 under a US-controlled owner; screen the feed"),
        ("cobalt", "powder", "Jervois Finland", "", "One of few non-China fine cobalt powder makers, US-owned; feed probably CMOC-linked, so document each lot"),
        ("cobalt", "refining_metal", "Managem", "", "Small, clean primary-cobalt cathode from its own Moroccan mine"),
        ("cobalt", "refining_metal", "Jervois Finland", "", "Operating non-China cobalt refiner selling to aerospace and defense; same feed caveat"),
        ("cobalt", "refining_metal", "Vale Base Metals - Long Harbour", "", "Clean Canadian electrolytic cobalt rounds; large seller with direct customers"),
        ("cobalt", "refining_metal", "Vale Base Metals - Port Colborne", "", "Clean Canadian electrolytic cobalt; large seller"),
        ("cobalt", "refining_metal", "Umicore Olen", "", "Major non-China cobalt metal and powder supplier with audited sourcing; large group"),
        ("cobalt", "refining_metal", "Glencore - Murrin Murrin", "", "Clean integrated Australian cobalt, marketed directly by Glencore"),
        ("cobalt", "refining_metal", "Electra", "", "Only planned North American cobalt refinery (H2 2027); sulfate, so not SmCo grade"),
        ("cobalt", "recycling", "Nth Cycle", "", "Small DOE-backed US cobalt recycler; site and timing not set"),
    ], "Sherritt (Canada) is excluded in practice: its cobalt is Cuban-origin and barred by the US embargo."),
    "molybdenum": ("Top 10 broker prospects (molybdenum)", [
        ("molybdenum", "roasting_chemical", "Langeloth", "", "~27-29 Mlb/yr idle US roasting capacity buying third-party concentrate; clean owner. A broker can supply documented feed"),
        ("molybdenum", "metal_powder", "Molymet Germany", "", "1,700 t/yr molybdenum powder from Chilean oxide; the clearest compliant powder source"),
        ("molybdenum", "mill_products_alloys", "Elmet Technologies LLC", "Lewiston", "US Mo/TZM mill products, DoW- and DLA-backed and expanding; verify feed"),
        ("molybdenum", "mill_products_alloys", "Rhenium Alloys", "", "Small US Mo-Re and Mo mill-product maker for defense; new owner (Molymet) investing"),
        ("molybdenum", "metal_powder", "Amaero", "", "US spherical refractory powders (AS9100, ITAR), EXIM-financed; verify molybdenum feed"),
        ("molybdenum", "recycling", "Treibacher", "", "EU recycled molybdenum (FeMo/FeNiMo) from European spent catalysts"),
        ("molybdenum", "metal_powder", "Molymet (MolymetNos)", "plasma", "New spherical Mo/Re powder line seeking additive-manufacturing customers"),
        ("molybdenum", "roasting_chemical", "Climax Molybdenum Company", "Fort Madison", "Fully US mine-to-pure-oxide/ADM chain (precursor for powder)"),
        ("molybdenum", "mill_products_alloys", "Plansee", "", "TZM, ML and MoRe semis made from Molymet oxide; large group"),
        ("molybdenum", "mining_concentrate", "Gibraltar", "", "Clean Canadian concentrate sold at the mine gate (Trekor Metals)"),
    ], "Also watch Centerra Thompson Creek (Idaho, restart mid-2027, captive to Langeloth) and Greenland Resources Malmbjerg (planned)."),
    "gallium_germanium": ("Top 10 broker prospects (gallium and germanium)", [
        ("gallium", "primary_extraction", "METLEN", "", "50 t/yr gallium from Q3 2027, clean EU chain, ~59% not yet publicly contracted"),
        ("gallium", "primary_extraction", "ATALCO", "", "First US primary gallium (pilot late 2026, 50 t/yr target); only the DLA stockpile contract is public"),
        ("germanium", "primary_extraction", "KEMCO", "", "New uncommitted germanium from 2027 with only a non-binding Lockheed MoU; confirm zinc-concentrate origin"),
        ("germanium", "products_optics_wafers", "Lattice Materials", "", "Small ITAR-registered US germanium crystal maker expanding with DPA money"),
        ("gallium", "refining_high_purity", "Indium Corporation", "", "The only US high-purity gallium refiner, building non-China feed; could toll-refine compliant crude"),
        ("gallium", "refining_high_purity", "CMK", "", "Small EU 7N gallium refiner that could refine non-China crude (e.g., METLEN)"),
        ("germanium", "metal_high_purity", "5N Plus", "", "US germanium metal, wafers and optics with three DoD/DoW awards; backlog-constrained"),
        ("germanium", "refining_chemical", "Teck Metals", "", "The cleanest primary GeO2/GeCl4 source (Red Dog feed); large, expansion undated"),
        ("germanium", "primary_extraction", "Blue Moon", "", "Ge/Ga-bearing ore from Apex, Utah (from Q3 2027), seeking buyers"),
        ("gallium", "primary_extraction", "ElementUSA", "", "DPA-funded gallium/scandium demonstration from bauxite residue, uncommitted, no dates"),
    ], "Alcoa Wagerup (Australia, 100 t/yr) is the biggest new source but is committed to its partners."),
    "traders": ("Top 10 partner prospects (traders, stockholders)", [
        ("trader", "trader", "Traxys North America", "", "Independent; contracted non-China NdPr/DyTb (Arafura) and NioCorp output; Project Vault supplier"),
        ("trader", "trader", "Traxys Europe", "", "El Moto tungsten exclusive (from 2029) and Arafura NdPr; independent merchant"),
        ("trader", "trader", "Wogen Resources", "", "Employee-held minor-metals house with Rwandan tantalum exclusive and W/Mo/Co books; must keep lots separate from its China desk"),
        ("trader", "distributor", "Magnetic Component Engineering", "", "The only distributor found advertising DFARS-compliant magnet stock; check the 2027 basis"),
        ("trader", "trader", "Sojitz", "", "Controls Lynas Dy/Tb/Sm flows and future JAGA gallium; Japan-earmarked but worth asking for surplus"),
        ("trader", "trader", "Glencore", "", "Non-China refined cobalt brands (Nikkelverk, Murrin Murrin); large and already supplying DLA and the Vault"),
        ("trader", "trader", "Darton Commodities", "", "Cobalt-metal specialist offering consignment and finance"),
        ("trader", "stockholder", "TRADIUM", "", "Owner-managed stockholder with physical minor-metal stock in a bonded warehouse; prove origin lot by lot"),
        ("trader", "stockholder", "Midwest Tungsten", "", "ITAR-registered US stock of W, WHA, Ta and Mo mill products; no origin data"),
        ("trader", "distributor", "Dexter Magnetic", "", "AS9100 US magnet distributor and assembler with sister SmCo/NdFeB brands"),
    ], ""),
    "labs": ("Top 10 verification partners (labs)", [
        ("lab", "provenance_lab", "Source Certain", "", "Commercial trace-element and isotope origin verification with a US office; reference libraries needed for W/Ta/REE"),
        ("lab", "provenance_lab", "BGR", "", "The best-established origin method for tantalum and tungsten concentrates (Analytical Fingerprint); government body"),
        ("lab", "inspection_sampling", "Alex Stewart", "", "Minor-metals sampling, weighing and assays in 40+ countries"),
        ("lab", "inspection_sampling", "Alfred H Knight (AHK)", "", "Independent inspection and supervision; US lab in Spartanburg, SC"),
        ("lab", "inspection_sampling", "Ledoux", "", "US umpire assays accepted for settlement; on-site witnessing; ISO/IEC 17025"),
        ("lab", "assay_lab", "EAG Laboratories", "", "GDMS full-survey impurity profiles to match high-purity lots to producer signatures"),
        ("lab", "assay_lab", "NSL Analytical", "", "ISO/IEC 17025, Nadcap, ITAR; aerospace spec chemistry"),
        ("lab", "assay_lab", "SGS Canada", "", "Accredited rare-earth methods and pilot-scale processing know-how (Lakefield, Ontario)"),
        ("lab", "provenance_lab", "Isobar Science", "", "US commercial Pb/Sr isotope analyses for concentrate provenance (SGS-owned)"),
        ("lab", "assay_lab", "Activation Laboratories", "", "Allied (Canadian) geochemistry lab with an isotope and geochronology line"),
    ], "For chain-of-custody documentation (not testing): ITSCI (Great Lakes tin, tantalum and tungsten), Circulor (digital traceability), Cartograph (supplier-origin requests)."),
}


def find(rows, chain, stage, comp, fac):
    c = [r for r in rows if r["material_chain"] == chain and r["stage"] == stage
         and comp.lower() in r["company_name"].lower() and fac.lower() in r["facility_name"].lower()]
    return c[0] if c else None


def main():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "data", "suppliers.csv"), encoding="utf-8-sig")))
    rp = os.path.join(ROOT, "REPORT.md")
    text = open(rp, encoding="utf-8").read()
    missing = []
    for key, (title, entries, footer) in TOP10.items():
        lines = [f"**{title}**", "", "| # | ID | Company - facility (country) | Score | Why |", "|---|---|---|---|---|"]
        for i, (chain, stage, comp, fac, why) in enumerate(entries, 1):
            r = find(rows, chain, stage, comp, fac)
            if not r:
                missing.append(f"{key}: {comp} / {stage}")
                continue
            lines.append(f"| {i} | {r['supplier_id']} | {r['company_name']} - {r['facility_name']} ({r['country']}) | {r['broker_fit_score']} | {why} |")
        if footer:
            lines += ["", footer]
        block = "\n".join(lines)
        text, n = re.subn(rf"<!-- TOP10_{key} -->(.*?<!-- /TOP10_{key} -->)?", f"<!-- TOP10_{key} -->\n{block}\n<!-- /TOP10_{key} -->", text, flags=re.S)
        if n == 0:
            missing.append(f"placeholder TOP10_{key} not found")
    open(rp, "w", encoding="utf-8").write(text)
    if missing:
        print("NOT FOUND:")
        for m in missing:
            print("  " + m)
        sys.exit(1)
    print("top-10 tables written")


if __name__ == "__main__":
    main()
