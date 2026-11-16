#!/usr/bin/env python3
"""Merge staging JSONL files into the final deliverables.

Outputs:
    data/suppliers.csv, data/offtakes.csv, data/excluded.csv, data/sources.csv
    suppliers.xlsx (About tab, one tab per material chain, top prospects,
                    offtakes, excluded, sources)

CSV files are written as UTF-8 with a byte-order mark so Excel shows accents
and symbols correctly when the file is double-clicked.
"""
import csv
import json
import math
import os
import re
import sys
from collections import Counter, OrderedDict
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema as S  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING = os.path.join(ROOT, "data", "staging")
DATA = os.path.join(ROOT, "data")

CHAIN_ORDER = {c: i for i, c in enumerate(S.MATERIAL_CHAINS)}
TAB_NAMES = OrderedDict([
    ("tungsten", "tungsten"), ("tantalum", "tantalum"), ("ndfeb", "ndfeb"),
    ("smco", "smco"), ("cobalt", "cobalt"), ("molybdenum", "molybdenum"),
    ("gallium", "gallium"), ("germanium", "germanium"), ("trader", "traders"),
    ("lab", "labs"),
])


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


def clean(v):
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    if isinstance(v, (list, tuple)):
        v = "; ".join(str(x) for x in v)
    s = str(v).replace("\r", " ").strip()
    return s


def load_all(kind):
    rows = []
    for ws in sorted(os.listdir(STAGING)):
        d = os.path.join(STAGING, ws)
        if not os.path.isdir(d) or ws == "verification":
            continue
        p = os.path.join(d, f"{kind}.jsonl")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"WARNING: {p}:{n} invalid JSON skipped ({e})")
                    continue
                obj = {k: clean(v) for k, v in obj.items()}
                obj["_ws"] = ws
                rows.append(obj)
    return rows


def filled(r, fields):
    return sum(1 for k in fields if str(r.get(k, "")).strip())


def dedupe(rows, keyfn, fields, label):
    best = OrderedDict()
    dups = 0
    for r in rows:
        k = keyfn(r)
        if k in best:
            dups += 1
            if filled(r, fields) > filled(best[k], fields):
                best[k] = r
        else:
            best[k] = r
    if dups:
        print(f"{label}: merged {dups} duplicate row(s)")
    return list(best.values())


def split_urls(s):
    return [u.strip() for u in str(s or "").split(";") if u.strip()]


def write_csv(path, fields, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def build():
    # ---------------- suppliers ----------------
    sup = load_all("suppliers")
    sup = [r for r in sup if r.get("company_name")]
    sup = dedupe(
        sup,
        lambda r: (r.get("material_chain"), r.get("stage"), norm(r.get("company_name")),
                   norm(r.get("facility_name")), norm(r.get("city")), norm(r.get("country"))),
        S.SUPPLIER_FIELDS, "suppliers")

    def stage_idx(r):
        st = S.STAGES.get(r.get("material_chain"), [])
        return st.index(r.get("stage")) if r.get("stage") in st else 99

    sup.sort(key=lambda r: (CHAIN_ORDER.get(r.get("material_chain"), 99), stage_idx(r),
                            norm(r.get("country")), norm(r.get("company_name")),
                            norm(r.get("facility_name"))))
    counters = Counter()
    for r in sup:
        c = r.get("material_chain")
        counters[c] += 1
        r["supplier_id"] = f"{S.ID_PREFIX.get(c, 'XX')}-{counters[c]:03d}"
        if not r.get("gbd_capability"):
            r["gbd_capability"] = "n/a" if not (c == "ndfeb" and r.get("stage", "").startswith("magnet")) else "unknown"

    # ---------------- offtakes ----------------
    off = load_all("offtakes")
    off = dedupe(
        off,
        lambda r: (norm(r.get("seller")), norm(r.get("buyer")), norm(r.get("material")),
                   r.get("announcement_date", "")[:7]),
        S.OFFTAKE_FIELDS, "offtakes")
    off.sort(key=lambda r: (CHAIN_ORDER.get(r.get("material_chain"), 99), norm(r.get("seller")),
                            r.get("announcement_date", "")))
    for i, r in enumerate(off, 1):
        r["offtake_id"] = f"OT-{i:03d}"

    # ---------------- excluded ----------------
    exc = load_all("excluded")
    exc = [r for r in exc if r.get("company_name")]
    exc = dedupe(
        exc,
        lambda r: (r.get("material_chain"), r.get("stage"), norm(r.get("company_name")),
                   norm(r.get("facility_name"))),
        S.EXCLUDED_FIELDS, "excluded")
    exc.sort(key=lambda r: (CHAIN_ORDER.get(r.get("material_chain"), 99), r.get("covered_country", ""),
                            norm(r.get("company_name"))))
    for i, r in enumerate(exc, 1):
        r["excluded_id"] = f"X-{i:03d}"

    # ---------------- sources ----------------
    src_rows = load_all("sources")
    by_url = OrderedDict()
    for r in src_rows:
        u = r.get("url", "").strip()
        if not u:
            continue
        if u not in by_url:
            by_url[u] = r
        else:
            cur = by_url[u]
            for k in ("title", "publisher", "date", "type", "date_accessed"):
                if not cur.get(k) and r.get(k):
                    cur[k] = r[k]
    cited = []
    for r in sup + exc:
        cited += split_urls(r.get("sources"))
        cited += split_urls(r.get("capacity_source")) if str(r.get("capacity_source", "")).startswith("http") else []
    for r in off:
        cited += split_urls(r.get("source"))
    missing = 0
    for u in cited:
        if u.startswith("http") and u not in by_url:
            missing += 1
            by_url[u] = {"url": u, "title": "(title not recorded)",
                         "publisher": urlparse(u).netloc.replace("www.", ""),
                         "date": "undated", "type": "other", "date_accessed": "2026-11-16"}
    if missing:
        print(f"sources: added {missing} cited URL(s) missing from sources.jsonl as placeholders")
    srcs = list(by_url.values())
    srcs.sort(key=lambda r: (r.get("type", ""), r.get("publisher", "").lower(), r.get("title", "").lower()))
    for i, r in enumerate(srcs, 1):
        r["source_id"] = f"S-{i:04d}"

    # ---------------- write CSVs ----------------
    write_csv(os.path.join(DATA, "suppliers.csv"), S.SUPPLIER_FIELDS, sup)
    write_csv(os.path.join(DATA, "offtakes.csv"), S.OFFTAKE_FIELDS, off)
    write_csv(os.path.join(DATA, "excluded.csv"), S.EXCLUDED_FIELDS, exc)
    write_csv(os.path.join(DATA, "sources.csv"), S.SOURCE_FIELDS, srcs)
    print(f"wrote suppliers={len(sup)} offtakes={len(off)} excluded={len(exc)} sources={len(srcs)}")
    for c in S.MATERIAL_CHAINS:
        print(f"   {c:12s} {counters[c]}")

    build_xlsx(sup, off, exc, srcs)


# ---------------- XLSX ----------------
WIDTHS = {
    "supplier_id": 11, "company_name": 28, "parent_company": 22, "ultimate_owner": 22,
    "owner_country": 13, "covered_country_tie": 14, "tie_detail": 40, "material_chain": 11,
    "stage": 20, "products": 40, "facility_name": 28, "city": 14, "state_region": 14,
    "country": 13, "facility_status": 13, "expected_production_date": 16, "capacity_value": 11,
    "capacity_unit": 18, "capacity_year": 9, "capacity_source": 30, "feedstock_origin": 38,
    "committed_offtakes": 40, "government_awards": 40, "rmi_rmap_status": 28,
    "dfars_7052_assessment": 17, "dfars_7052_reason": 40, "capacity_availability": 17,
    "broker_fit_score": 9, "broker_fit_rationale": 45, "commercial_contact_url": 30,
    "sources": 45, "date_accessed": 12, "confidence": 11, "notes": 60, "gbd_capability": 11,
    # offtakes
    "offtake_id": 11, "seller": 26, "buyer": 26, "material": 18, "form": 18, "volume": 24,
    "term": 18, "binding_status": 13, "price_mechanism": 28, "announcement_date": 14, "source": 45,
    # excluded
    "excluded_id": 11, "aliases": 35, "covered_country": 13, "rmi_smelter_id": 14,
    # sources
    "source_id": 10, "title": 60, "publisher": 28, "date": 12, "url": 60, "type": 16,
}


def write_sheet(ws, fields, rows, header_fill, font_cls, align_cls, fill_cls):
    from openpyxl.utils import get_column_letter
    ws.append(fields)
    hdr_font = font_cls(bold=True, color="FFFFFF")
    for i, _ in enumerate(fields, 1):
        c = ws.cell(row=1, column=i)
        c.font = hdr_font
        c.fill = fill_cls("solid", fgColor=header_fill)
        c.alignment = align_cls(wrap_text=True, vertical="center")
    ws.row_dimensions[1].height = 32
    for r in rows:
        vals = []
        for k in fields:
            v = r.get(k, "")
            if k in ("broker_fit_score", "capacity_year") and str(v).strip().isdigit():
                v = int(v)
            elif k == "capacity_value":
                try:
                    fv = float(str(v).replace(",", ""))
                    v = int(fv) if fv.is_integer() else fv
                except ValueError:
                    pass
            vals.append(v)
        ws.append(vals)
    body_align = align_cls(wrap_text=True, vertical="top")
    for i, k in enumerate(fields, 1):
        ws.column_dimensions[get_column_letter(i)].width = WIDTHS.get(k, 16)
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        max_lines = 1
        for i, cell in enumerate(row):
            cell.alignment = body_align
            txt = str(cell.value or "")
            w = WIDTHS.get(fields[i], 16)
            lines = max(1, math.ceil(len(txt) / max(1.0, w * 1.15)))
            max_lines = max(max_lines, min(lines, 6))
        ws.row_dimensions[row[0].row].height = 15 * max_lines + 2
    ws.freeze_panes = "C2" if "company_name" in fields and fields[0].endswith("_id") else "B2"
    ws.auto_filter.ref = ws.dimensions


def build_xlsx(sup, off, exc, srcs):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill

    wb = Workbook()
    about = wb.active
    about.title = "About"
    chain_counts = Counter(r["material_chain"] for r in sup)
    lines = [
        ["Non-China critical-metals supplier map for US defense sourcing (DFARS 252.225-7052 / 10 U.S.C. 4872)"],
        ["Built 2026-11-16. See README.md, REPORT.md and docs/scope.md for explanations."],
        [""],
        ["Tab", "What it contains", "Rows"],
    ]
    for chain, tab in TAB_NAMES.items():
        lines.append([tab, f"Supplier facility-stage rows for material_chain = {chain}", chain_counts.get(chain, 0)])
    lines += [
        ["top_prospects", "All supplier rows with broker_fit_score 4 or 5, sorted by score", sum(1 for r in sup if str(r.get('broker_fit_score')) in ('4', '5'))],
        ["offtakes", "Known supply agreements (one row per agreement)", len(off)],
        ["excluded", "Major facilities inside covered countries (China, Russia, North Korea, Iran), for screening paperwork", len(exc)],
        ["sources", "Every source cited, with publisher, date and type", len(srcs)],
        [""],
        ["How to use", "Each tab has filters on the header row. Click the arrow in a header cell to filter, e.g. dfars_7052_assessment = likely_compliant, or broker_fit_score = 5."],
        ["Key columns", "dfars_7052_assessment: likely_compliant / at_risk / likely_noncompliant / unknown (our judgment, not legal advice). broker_fit_score: 1 (unlikely partner) to 5 (strong prospect). capacity_availability: uncommitted / partially_committed / fully_committed / unknown."],
        ["Caution", "Ownership, offtakes and status change quickly. Every row has a date_accessed and sources; re-check before acting. RMI RMAP statuses come from public secondary sources, not the RMI website."],
    ]
    for ln in lines:
        about.append(ln)
    about["A1"].font = Font(bold=True, size=14)
    about["A4"].font = about["B4"].font = about["C4"].font = Font(bold=True)
    about.column_dimensions["A"].width = 18
    about.column_dimensions["B"].width = 110
    about.column_dimensions["C"].width = 8
    for row in about.iter_rows(min_row=5):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")

    for chain, tab in TAB_NAMES.items():
        rows = [r for r in sup if r.get("material_chain") == chain]
        ws = wb.create_sheet(tab)
        write_sheet(ws, S.SUPPLIER_FIELDS, rows, "1F4E78", Font, Alignment, PatternFill)

    prospects = [r for r in sup if str(r.get("broker_fit_score")) in ("4", "5")]
    prospects.sort(key=lambda r: (-int(r["broker_fit_score"]), CHAIN_ORDER.get(r["material_chain"], 99),
                                  norm(r.get("company_name"))))
    ws = wb.create_sheet("top_prospects")
    write_sheet(ws, S.SUPPLIER_FIELDS, prospects, "375623", Font, Alignment, PatternFill)

    ws = wb.create_sheet("offtakes")
    write_sheet(ws, S.OFFTAKE_FIELDS, off, "7F6000", Font, Alignment, PatternFill)
    ws = wb.create_sheet("excluded")
    write_sheet(ws, S.EXCLUDED_FIELDS, exc, "C00000", Font, Alignment, PatternFill)
    ws = wb.create_sheet("sources")
    write_sheet(ws, S.SOURCE_FIELDS, srcs, "595959", Font, Alignment, PatternFill)

    out = os.path.join(ROOT, "suppliers.xlsx")
    wb.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    build()
