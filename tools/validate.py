#!/usr/bin/env python3
"""Validate one staging workstream folder (or all of them).

Usage:
    python3 tools/validate.py data/staging/tungsten
    python3 tools/validate.py --all

Checks suppliers.jsonl, offtakes.jsonl, excluded.jsonl, sources.jsonl for
JSON syntax, required fields, controlled vocabularies, and that every URL cited
in a supplier/excluded row is also listed in sources.jsonl.
"""
import json
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema as S  # noqa: E402

DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def load_jsonl(path, errors):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"{os.path.basename(path)} line {n}: invalid JSON ({e})")
                continue
            if not isinstance(obj, dict):
                errors.append(f"{os.path.basename(path)} line {n}: not a JSON object")
                continue
            obj["_line"] = n
            rows.append(obj)
    return rows


def split_urls(s):
    return [u.strip() for u in str(s or "").split(";") if u.strip()]


def validate_dir(d):
    errors, warnings = [], []
    sup = load_jsonl(os.path.join(d, "suppliers.jsonl"), errors)
    off = load_jsonl(os.path.join(d, "offtakes.jsonl"), errors)
    exc = load_jsonl(os.path.join(d, "excluded.jsonl"), errors)
    src = load_jsonl(os.path.join(d, "sources.jsonl"), errors)

    src_urls = set()
    for r in src:
        u = str(r.get("url", "")).strip()
        if not u.startswith("http"):
            errors.append(f"sources.jsonl line {r['_line']}: url missing/invalid")
        src_urls.add(u)
        if r.get("type") not in S.SOURCE_TYPES:
            errors.append(f"sources.jsonl line {r['_line']}: type '{r.get('type')}' not in {S.SOURCE_TYPES}")
        for k in ("title", "publisher"):
            if not str(r.get(k, "")).strip():
                warnings.append(f"sources.jsonl line {r['_line']}: empty {k}")

    stage_counts = Counter()
    for r in sup:
        ln = f"suppliers.jsonl line {r['_line']} ({r.get('company_name', '?')})"
        unknown_keys = [k for k in r if k not in S.SUPPLIER_FIELDS and k != "_line"]
        if unknown_keys:
            errors.append(f"{ln}: unknown keys {unknown_keys}")
        for k in ("company_name", "material_chain", "stage", "country", "facility_status",
                  "dfars_7052_assessment", "capacity_availability", "broker_fit_score",
                  "sources", "confidence", "covered_country_tie"):
            if not str(r.get(k, "")).strip():
                errors.append(f"{ln}: required field '{k}' empty")
        chain = r.get("material_chain")
        if chain not in S.STAGES:
            errors.append(f"{ln}: material_chain '{chain}' not in {S.MATERIAL_CHAINS}")
        elif r.get("stage") not in S.STAGES[chain]:
            errors.append(f"{ln}: stage '{r.get('stage')}' not valid for {chain}: {S.STAGES[chain]}")
        stage_counts[(chain, r.get("stage"))] += 1
        ties = [t.strip() for t in str(r.get("covered_country_tie", "")).split(";") if t.strip()]
        for t in ties:
            if t not in S.TIE_VALUES:
                errors.append(f"{ln}: covered_country_tie value '{t}' not in {S.TIE_VALUES}")
        if ties and ties != ["none"] and not str(r.get("tie_detail", "")).strip():
            errors.append(f"{ln}: tie flagged but tie_detail empty")
        if r.get("facility_status") not in S.FACILITY_STATUS:
            errors.append(f"{ln}: facility_status '{r.get('facility_status')}' not in {S.FACILITY_STATUS}")
        if r.get("dfars_7052_assessment") not in S.ASSESSMENT:
            errors.append(f"{ln}: dfars_7052_assessment '{r.get('dfars_7052_assessment')}' not in {S.ASSESSMENT}")
        if not str(r.get("dfars_7052_reason", "")).strip():
            errors.append(f"{ln}: dfars_7052_reason empty")
        if r.get("capacity_availability") not in S.AVAILABILITY:
            errors.append(f"{ln}: capacity_availability '{r.get('capacity_availability')}' not in {S.AVAILABILITY}")
        try:
            sc = int(str(r.get("broker_fit_score", "")).strip())
            if not 1 <= sc <= 5:
                raise ValueError
        except ValueError:
            errors.append(f"{ln}: broker_fit_score must be integer 1-5")
        if not str(r.get("broker_fit_rationale", "")).strip():
            errors.append(f"{ln}: broker_fit_rationale empty")
        if r.get("confidence") not in S.CONFIDENCE:
            errors.append(f"{ln}: confidence '{r.get('confidence')}' not in {S.CONFIDENCE}")
        g = str(r.get("gbd_capability", "")).strip()
        if g not in S.GBD:
            errors.append(f"{ln}: gbd_capability '{g}' not in {S.GBD}")
        rm = str(r.get("rmi_rmap_status", "")).strip()
        if rm and not any(rm.lower().startswith(p) for p in S.RMAP_PREFIXES):
            errors.append(f"{ln}: rmi_rmap_status must start with one of {S.RMAP_PREFIXES}")
        if chain in ("tungsten", "tantalum") and not rm:
            warnings.append(f"{ln}: rmi_rmap_status empty for {chain} row (use n/a for mines etc.)")
        da = str(r.get("date_accessed", "")).strip()
        if not DATE_RE.match(da):
            errors.append(f"{ln}: date_accessed '{da}' not YYYY-MM-DD")
        urls = split_urls(r.get("sources"))
        for u in urls:
            if not u.startswith("http"):
                errors.append(f"{ln}: source '{u}' is not a URL")
            elif u not in src_urls:
                warnings.append(f"{ln}: source URL not in sources.jsonl: {u}")
        cu = str(r.get("commercial_contact_url", "")).strip()
        if cu and not cu.startswith("http"):
            errors.append(f"{ln}: commercial_contact_url must be a URL or blank")
        if any(EMAIL_RE.search(str(v)) for v in r.values()):
            warnings.append(f"{ln}: possible email address found - personal contact details are not allowed")
        if r.get("capacity_value") not in (None, "") and not str(r.get("capacity_unit", "")).strip():
            errors.append(f"{ln}: capacity_value given without capacity_unit")

    for r in off:
        ln = f"offtakes.jsonl line {r['_line']}"
        unknown_keys = [k for k in r if k not in S.OFFTAKE_FIELDS and k != "_line"]
        if unknown_keys:
            errors.append(f"{ln}: unknown keys {unknown_keys}")
        for k in ("seller", "buyer", "material_chain", "material", "binding_status", "source"):
            if not str(r.get(k, "")).strip():
                errors.append(f"{ln}: required field '{k}' empty")
        if r.get("binding_status") not in S.BINDING:
            errors.append(f"{ln}: binding_status '{r.get('binding_status')}' not in {S.BINDING}")
        for u in split_urls(r.get("source")):
            if u not in src_urls:
                warnings.append(f"{ln}: source URL not in sources.jsonl: {u}")

    for r in exc:
        ln = f"excluded.jsonl line {r['_line']} ({r.get('company_name', '?')})"
        unknown_keys = [k for k in r if k not in S.EXCLUDED_FIELDS and k != "_line"]
        if unknown_keys:
            errors.append(f"{ln}: unknown keys {unknown_keys}")
        if r.get("covered_country") not in S.COVERED_COUNTRIES:
            errors.append(f"{ln}: covered_country '{r.get('covered_country')}' not in {S.COVERED_COUNTRIES}")
        chain = r.get("material_chain")
        if chain not in S.STAGES:
            errors.append(f"{ln}: material_chain '{chain}' invalid")
        elif r.get("stage") not in S.STAGES[chain]:
            errors.append(f"{ln}: stage '{r.get('stage')}' not valid for {chain}")
        if not split_urls(r.get("sources")):
            errors.append(f"{ln}: sources empty")
        for u in split_urls(r.get("sources")):
            if u not in src_urls:
                warnings.append(f"{ln}: source URL not in sources.jsonl: {u}")

    print(f"== {d}")
    print(f"suppliers: {len(sup)}  offtakes: {len(off)}  excluded: {len(exc)}  sources: {len(src)}")
    for (c, s), n in sorted(stage_counts.items(), key=lambda x: (str(x[0][0]), str(x[0][1]))):
        print(f"   {c:12s} {s:26s} {n}")
    print(f"ERRORS ({len(errors)}):")
    for e in errors[:200]:
        print("  - " + e)
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings[:100]:
        print("  - " + w)
    return len(errors)


if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "staging")
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        dirs = [os.path.join(root, x) for x in sorted(os.listdir(root))
                if os.path.isdir(os.path.join(root, x)) and x != "verification"]
    else:
        dirs = sys.argv[1:]
    total = sum(validate_dir(d) for d in dirs)
    sys.exit(1 if total else 0)
