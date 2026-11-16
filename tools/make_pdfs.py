#!/usr/bin/env python3
"""Make PDF versions of REPORT.md and suppliers.xlsx (built from data/*.csv).

Outputs (repo root): REPORT.pdf and suppliers.pdf
Needs: pandoc, node with Playwright/Chromium (tools/print_pdf.js).
"""
import csv
import html
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema as S  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRINT_JS = os.path.join(ROOT, "tools", "print_pdf.js")
E = html.escape

BASE_CSS = """
body { font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif; color: #1b1f24; }
a { color: #1F4E78; text-decoration: none; }
"""

REPORT_CSS = BASE_CSS + """
body { font-size: 9.4pt; line-height: 1.4; }
h1 { font-size: 21pt; color: #1F4E78; border-bottom: 2.5px solid #1F4E78; padding-bottom: 5px; margin: 0 0 6px 0; }
h2 { font-size: 15pt; color: #1F4E78; border-bottom: 1px solid #c9d6e3; padding-bottom: 3px; margin-top: 4pt;
     break-before: page; break-after: avoid; }
h2.nobreak { break-before: avoid; margin-top: 16pt; }
h3 { font-size: 11pt; color: #2E5C8A; margin: 12pt 0 4pt; break-after: avoid; }
p { margin: 5pt 0; }
ul, ol { margin: 4pt 0 6pt 0; padding-left: 18pt; }
li { margin: 1.5pt 0; }
table { border-collapse: collapse; width: 100%; font-size: 7.7pt; line-height: 1.3; margin: 6pt 0 10pt; }
thead { display: table-header-group; }
th { background: #1F4E78; color: #fff; text-align: left; padding: 3pt 4pt; font-weight: bold; }
td { border: 1px solid #d0d7de; padding: 3pt 4pt; vertical-align: top; }
tr { break-inside: avoid; }
tbody tr:nth-child(even) td { background: #f5f7fa; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; background: #eef1f4; padding: 0 2px; border-radius: 2px; }
hr { display: none; }
em { color: #3a4450; }
.subtitle { color: #555; font-size: 9pt; margin-bottom: 10pt; }
"""

BOOK_CSS = BASE_CSS + """
body { font-size: 7.2pt; line-height: 1.28; }
h1 { font-size: 20pt; color: #1F4E78; border-bottom: 2.5px solid #1F4E78; padding-bottom: 4px; margin: 0 0 6px; }
h2 { font-size: 13pt; color: #fff; background: #1F4E78; padding: 4pt 7pt; margin: 0 0 6pt; break-before: page; }
h2.first { break-before: avoid; }
h3 { font-size: 10pt; color: #1F4E78; margin: 10pt 0 4pt; }
.intro { font-size: 8.4pt; line-height: 1.4; }
.intro table { font-size: 8.2pt; }
.sec-note { font-size: 7.6pt; color: #444; margin: 0 0 6pt; }
table { border-collapse: collapse; width: 100%; table-layout: fixed; }
thead { display: table-header-group; }
th { background: #DCE6F0; color: #1F4E78; text-align: left; padding: 2.5pt 3pt; border: 1px solid #b9c7d6; font-size: 6.9pt; }
td { border: 1px solid #d6dde4; padding: 2.5pt 3pt; vertical-align: top; word-wrap: break-word; overflow-wrap: anywhere; }
tbody.rec { break-inside: avoid; }
tbody.rec tr.main td { background: #f4f7fb; border-top: 1.6px solid #8aa4c0; }
tbody.rec tr.det td { font-size: 6.8pt; color: #26313c; background: #fff; }
tr.row { break-inside: avoid; }
tr.row:nth-child(even) td { background: #f7f9fb; }
.co { font-weight: bold; font-size: 7.6pt; color: #10273d; }
.sm { color: #5a6570; font-size: 6.6pt; }
.k { font-weight: bold; color: #1F4E78; }
.b { display: inline-block; padding: 0.6pt 3pt; border-radius: 3px; font-weight: bold; font-size: 6.6pt; white-space: nowrap; }
.lc { background: #d6f0dd; color: #14532d; } .ar { background: #fdebc8; color: #7a4b00; }
.nc { background: #f9d0d0; color: #7f1d1d; } .un { background: #e5e7eb; color: #374151; }
.tn { background: #e7f5ea; color: #14532d; } .tu { background: #eceff3; color: #374151; } .tr { background: #fde2e2; color: #7f1d1d; }
.av-u { background: #d6f0dd; color: #14532d; } .av-p { background: #fdebc8; color: #7a4b00; } .av-f { background: #f9d0d0; color: #7f1d1d; } .av-x { background: #e5e7eb; color: #374151; }
.sc { display: inline-block; min-width: 13pt; text-align: center; font-weight: bold; font-size: 8.5pt; border-radius: 3px; padding: 0.5pt 2pt; color: #fff; }
.s5 { background: #14532d; } .s4 { background: #2f855a; } .s3 { background: #b7791f; } .s2 { background: #9c4221; } .s1 { background: #7f1d1d; }
.legend td { border: none; padding: 1.5pt 4pt; font-size: 7.6pt; }
.src a { margin-right: 4pt; }
.url { font-size: 6.4pt; }
"""

ASSESS = {"likely_compliant": ("lc", "likely compliant"), "at_risk": ("ar", "at risk"),
          "likely_noncompliant": ("nc", "likely non-compliant"), "unknown": ("un", "unknown")}
AVAIL = {"uncommitted": ("av-u", "uncommitted"), "partially_committed": ("av-p", "partly committed"),
         "fully_committed": ("av-f", "fully committed"), "unknown": ("av-x", "unknown")}
CHAIN_TITLES = [
    ("ndfeb", "NdFeB magnets (rare earths: mining, separation, metal/alloy, magnets, recycling, iron/boron, substitutes)"),
    ("tungsten", "Tungsten"), ("tantalum", "Tantalum"), ("smco", "SmCo magnets (samarium-cobalt)"),
    ("cobalt", "Cobalt (input for SmCo magnets)"), ("molybdenum", "Molybdenum"),
    ("gallium", "Gallium (covered from 18 Dec 2027)"), ("germanium", "Germanium (covered from 18 Dec 2027)"),
    ("trader", "Traders, distributors, stockholders and government stockpiles"),
    ("lab", "Assay, inspection and origin-testing labs"),
]


def read(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def domain(u):
    try:
        d = urlparse(u).netloc.lower()
    except ValueError:
        d = ""
    return d[4:] if d.startswith("www.") else (d or u[:30])


def links(s, label=None):
    out = []
    for u in [x.strip() for x in str(s or "").split(";") if x.strip()]:
        if u.startswith("http"):
            out.append(f'<a href="{E(u, quote=True)}">{E(label or domain(u))}</a>')
        else:
            out.append(E(u))
    return " ".join(out)


def badge(cls, text):
    return f'<span class="b {cls}">{E(text)}</span>'


def tie_badge(t):
    first = (t or "").split(";")[0].strip()
    cls = "tn" if first == "none" else ("tu" if first in ("unknown", "") else "tr")
    return badge(cls, t or "unknown")


def score(s):
    s = str(s or "").strip()
    return f'<span class="sc s{E(s)}">{E(s)}</span>' if s in "12345" and s else E(s)


def stage_label(s):
    return s.replace("_", " ")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd)}\n{r.stderr}")
    return r.stdout


# ---------------------------------------------------------------- REPORT.pdf
def build_report(tmp):
    body = run(["pandoc", "-f", "gfm", "-t", "html", os.path.join(ROOT, "REPORT.md")])
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    # first two h2 (Summary, How to read) stay on the title page flow
    n = [0]

    def h2(m):
        n[0] += 1
        return m.group(0).replace("<h2", '<h2 class="nobreak"', 1) if n[0] <= 2 else m.group(0)
    body = re.sub(r"<h2[^>]*>", h2, body)
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>Supplier map report</title>
<style>{REPORT_CSS}</style></head><body>{body}</body></html>"""
    p = os.path.join(tmp, "report.html")
    open(p, "w", encoding="utf-8").write(doc)
    out = os.path.join(ROOT, "REPORT.pdf")
    run(["node", PRINT_JS, p, out, "Letter", "portrait", "Non-China critical-metals supplier map - Report (16 Nov 2026)"])
    return out


# ------------------------------------------------------------- suppliers.pdf
def supplier_records(rows):
    head = """<table><colgroup><col style="width:4.5%"><col style="width:17%"><col style="width:15%"><col style="width:8.5%">
<col style="width:9%"><col style="width:11%"><col style="width:9%"><col style="width:10%"><col style="width:8.5%"><col style="width:7.5%"></colgroup>
<thead><tr><th>ID</th><th>Company / owner</th><th>Facility / location</th><th>Stage</th><th>Status</th><th>Capacity</th>
<th>2027 DFARS screen</th><th>Covered-country tie</th><th>Capacity availability</th><th>Broker fit / confidence</th></tr></thead>"""
    out = [head]
    for r in rows:
        cls, lab = ASSESS.get(r["dfars_7052_assessment"], ("un", r["dfars_7052_assessment"]))
        acl, alab = AVAIL.get(r["capacity_availability"], ("av-x", r["capacity_availability"]))
        owner = r["ultimate_owner"] or r["parent_company"]
        own_html = f'<div class="sm">Owner: {E(owner)}{(" (" + E(r["owner_country"]) + ")") if r["owner_country"] else ""}</div>' if owner else ""
        if r["parent_company"] and r["parent_company"] != owner:
            own_html = f'<div class="sm">Parent: {E(r["parent_company"])}</div>' + own_html
        loc = ", ".join(x for x in (r["city"], r["state_region"], r["country"]) if x)
        cap = " ".join(x for x in (r["capacity_value"], r["capacity_unit"]) if x)
        if cap and r["capacity_year"]:
            cap += f' ({r["capacity_year"]})'
        status = E(r["facility_status"]) + (f'<div class="sm">{E(r["expected_production_date"])}</div>' if r["expected_production_date"] else "")
        main = (f'<tr class="main"><td><b>{E(r["supplier_id"])}</b></td>'
                f'<td><div class="co">{E(r["company_name"])}</div>{own_html}</td>'
                f'<td>{E(r["facility_name"])}<div class="sm">{E(loc)}</div></td>'
                f'<td>{E(stage_label(r["stage"]))}</td><td>{status}</td><td>{E(cap) or "<span class=sm>not published</span>"}</td>'
                f'<td>{badge(cls, lab)}</td><td>{tie_badge(r["covered_country_tie"])}</td><td>{badge(acl, alab)}</td>'
                f'<td>{score(r["broker_fit_score"])} <span class="sm">conf.: {E(r["confidence"])}</span></td></tr>')
        parts = []

        def add(label, val, raw=False):
            if val and str(val).strip():
                parts.append(f'<span class="k">{E(label)}:</span> {val if raw else E(val)}')
        add("Products", r["products"])
        add("Feedstock origin", r["feedstock_origin"])
        add("Tie detail", r["tie_detail"])
        add("Screen reason", r["dfars_7052_reason"])
        add("Committed offtakes", r["committed_offtakes"])
        add("Government awards", r["government_awards"])
        if r["rmi_rmap_status"] and not r["rmi_rmap_status"].startswith("n/a"):
            add("RMI/RMAP", r["rmi_rmap_status"])
        if r["gbd_capability"] and r["gbd_capability"] != "n/a":
            add("Grain-boundary diffusion (Dy/Tb)", r["gbd_capability"])
        add("Broker-fit rationale", r["broker_fit_rationale"])
        add("Notes", r["notes"])
        if r["capacity_source"].startswith("http"):
            add("Capacity source", links(r["capacity_source"]), raw=True)
        add("Sources", f'<span class="src">{links(r["sources"])}</span>', raw=True)
        if r["commercial_contact_url"]:
            add("Company contact page", links(r["commercial_contact_url"]), raw=True)
        add("Accessed", r["date_accessed"])
        det = f'<tr class="det"><td></td><td colspan="9">{" &nbsp;|&nbsp; ".join(parts)}</td></tr>'
        out.append(f'<tbody class="rec">{main}{det}</tbody>')
    out.append("</table>")
    return "\n".join(out)


def simple_table(cols, widths, rows, cells):
    cg = "".join(f'<col style="width:{w}%">' for w in widths)
    th = "".join(f"<th>{E(c)}</th>" for c in cols)
    body = []
    for r in rows:
        body.append('<tr class="row">' + "".join(f"<td>{c}</td>" for c in cells(r)) + "</tr>")
    return f'<table><colgroup>{cg}</colgroup><thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table>'


def build_book(tmp):
    sup = read("suppliers.csv")
    off = read("offtakes.csv")
    exc = read("excluded.csv")
    src = read("sources.csv")
    cc = Counter(r["material_chain"] for r in sup)
    chains = [c for c, _ in CHAIN_TITLES]
    secs = []
    # ---- cover / about
    tabs = "".join(f"<tr><td>{E(t)}</td><td style='text-align:right'>{cc.get(c, 0)}</td></tr>" for c, t in CHAIN_TITLES)
    prospects = [r for r in sup if r["broker_fit_score"] in ("4", "5")]
    secs.append(f"""<h1>Non-China critical-metals supplier map: database (PDF edition)</h1>
<div class="intro"><p><b>Built 16 November 2026.</b> This is the full contents of <code>suppliers.xlsx</code> laid out for reading and printing.
The spreadsheet remains the working copy, with filters, sorting and the same data as <code>data/*.csv</code>.
Explanations are in <code>REPORT.md</code>/<code>REPORT.pdf</code> and the rule is in <code>docs/scope.md</code>.</p>
<table style="width:60%"><colgroup><col style="width:85%"><col style="width:15%"></colgroup><thead><tr><th>Section</th><th style="text-align:right">Rows</th></tr></thead><tbody>{tabs}
<tr><td>Top prospects (broker-fit score 4-5)</td><td style='text-align:right'>{len(prospects)}</td></tr>
<tr><td>Known supply agreements (offtakes)</td><td style='text-align:right'>{len(off)}</td></tr>
<tr><td>Covered-country facilities for screening (excluded)</td><td style='text-align:right'>{len(exc)}</td></tr>
<tr><td>Sources</td><td style='text-align:right'>{len(src)}</td></tr></tbody></table>
<h3>How to read a supplier record</h3>
<p>Each supplier facility-stage is one record. The <b>shaded line</b> gives the identity and the key screens, and the line beneath carries every
other field from the spreadsheet: products, feedstock, tie detail, the reason for the compliance screen, offtakes, government awards,
RMI status, broker-fit rationale, notes, and clickable source links (shown by website name; full addresses are in the Sources section).</p>
<table class="legend"><colgroup><col style="width:13%"><col style="width:87%"></colgroup><tbody>
<tr><td>{badge('lc','likely compliant')}</td><td>Facility and its known feed are outside China, Russia, North Korea and Iran, with no material ownership/control/financing tie.</td></tr>
<tr><td>{badge('ar','at risk')}</td><td>Outside the covered countries, but with undisclosed or covered-country feed, or a covered-country ownership/control/financing tie.</td></tr>
<tr><td>{badge('nc','likely non-compliant')}</td><td>A known covered-country stage in the product's chain.</td></tr>
<tr><td>{badge('un','unknown')}</td><td>Not enough information.</td></tr>
<tr><td>{score('5')} ... {score('1')}</td><td>Broker fit: 5 = strong prospect (uncommitted, mid-size, clean, 2027-28 supply, seeking buyers/capital) ... 1 = captive, committed, closed or non-compliant.</td></tr>
</tbody></table>
<p class="sm">The compliance column is a screening judgment from public information, not legal advice. Ownership, offtakes and status change quickly:
every record is dated and sourced. RMI/RMAP statuses come from public secondary sources, not the RMI website.</p></div>""")
    # ---- chains
    order = {c: i for i, c in enumerate(S.MATERIAL_CHAINS)}
    for c, title in CHAIN_TITLES:
        rows = [r for r in sup if r["material_chain"] == c]
        rows.sort(key=lambda r: (S.STAGES[c].index(r["stage"]) if r["stage"] in S.STAGES[c] else 99, r["supplier_id"]))
        st = Counter(r["stage"] for r in rows)
        stline = ", ".join(f"{stage_label(s)} {st[s]}" for s in S.STAGES[c] if st.get(s))
        secs.append(f'<h2>{E(title)} - {len(rows)} records</h2><p class="sec-note">Stages: {E(stline)}.</p>' + supplier_records(rows))
    # ---- top prospects
    prospects.sort(key=lambda r: (-int(r["broker_fit_score"]), order.get(r["material_chain"], 99), r["supplier_id"]))
    secs.append("<h2>Top prospects: every record with broker-fit score 4 or 5</h2>" + simple_table(
        ["Fit", "ID", "Company", "Facility (country)", "Chain / stage", "Status", "2027 screen", "Availability", "Why"],
        [3.5, 5, 15, 16, 10, 7, 8, 8, 27.5], prospects,
        lambda r: [score(r["broker_fit_score"]), E(r["supplier_id"]), f'<b>{E(r["company_name"])}</b>',
                   f'{E(r["facility_name"])} <span class="sm">({E(r["country"])})</span>',
                   E(r["material_chain"]) + " / " + E(stage_label(r["stage"])), E(r["facility_status"]),
                   badge(*ASSESS.get(r["dfars_7052_assessment"], ("un", r["dfars_7052_assessment"]))),
                   badge(*AVAIL.get(r["capacity_availability"], ("av-x", r["capacity_availability"]))),
                   E(r["broker_fit_rationale"])]))
    # ---- offtakes
    secs.append("<h2>Known supply agreements (offtakes)</h2>" + simple_table(
        ["ID", "Seller", "Buyer", "Chain", "Material / form", "Volume", "Term", "Binding?", "Price mechanism", "Announced", "Notes", "Source"],
        [4.5, 12, 11, 5, 10, 9, 7, 6, 8.5, 6, 13.5, 7.5], off,
        lambda r: [E(r["offtake_id"]), f'<b>{E(r["seller"])}</b>', E(r["buyer"]), E(r["material_chain"]),
                   E(r["material"]) + (f'<div class="sm">{E(r["form"])}</div>' if r["form"] else ""), E(r["volume"]), E(r["term"]),
                   E(r["binding_status"]), E(r["price_mechanism"]), E(r["announcement_date"]), E(r["notes"]),
                   f'<span class="src">{links(r["source"])}</span>']))
    # ---- excluded
    secs.append("<h2>Covered-country facilities for screening (excluded)</h2>"
                "<p class='sec-note'>Major facilities inside China, Russia, North Korea and Iran, with name variants, so they can be recognised on supplier paperwork. Not a complete list.</p>"
                + simple_table(
                    ["ID", "Company / aliases", "Parent / owner", "Country", "Chain / stage", "Products", "Facility / city", "RMI ID", "Notes", "Sources"],
                    [4, 17, 12, 5.5, 9, 10, 11, 5, 18, 8.5], exc,
                    lambda r: [E(r["excluded_id"]), f'<b>{E(r["company_name"])}</b>' + (f'<div class="sm">Aliases: {E(r["aliases"])}</div>' if r["aliases"] else ""),
                               E(" / ".join(x for x in (r["parent_company"], r["ultimate_owner"]) if x)), E(r["covered_country"]),
                               E(r["material_chain"]) + " / " + E(stage_label(r["stage"])), E(r["products"]),
                               E(", ".join(x for x in (r["facility_name"], r["city"], r["state_region"]) if x)), E(r["rmi_smelter_id"]),
                               E(r["notes"]), f'<span class="src">{links(r["sources"])}</span>']))
    # ---- sources
    secs.append("<h2>Sources</h2>" + simple_table(
        ["ID", "Title", "Publisher", "Date", "Type", "Address (click to open)"],
        [4.5, 33, 17, 6.5, 8, 31], src,
        lambda r: [E(r["source_id"]), E(r["title"]), E(r["publisher"]), E(r["date"]), E(r["type"]),
                   f'<a class="url" href="{E(r["url"], quote=True)}">{E(r["url"])}</a>']))
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>Supplier database</title>
<style>{BOOK_CSS}</style></head><body>{''.join(secs)}</body></html>"""
    p = os.path.join(tmp, "book.html")
    open(p, "w", encoding="utf-8").write(doc)
    out = os.path.join(ROOT, "suppliers.pdf")
    run(["node", PRINT_JS, p, out, "Letter", "landscape", "Non-China critical-metals supplier map - Database (16 Nov 2026)"])
    return out


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        print(build_report(tmp))
        print(build_book(tmp))
