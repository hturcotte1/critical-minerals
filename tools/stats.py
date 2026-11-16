#!/usr/bin/env python3
"""Print summary statistics from data/suppliers.csv for writing REPORT.md.

Usage: python3 tools/stats.py [chain ...]
"""
import csv
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema as S  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    with open(os.path.join(ROOT, "data", "suppliers.csv"), encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    chains = sys.argv[1:] or S.MATERIAL_CHAINS
    print(f"TOTAL supplier rows: {len(rows)}")
    print("Rows per chain:", dict(Counter(r["material_chain"] for r in rows)))
    for c in chains:
        cr = [r for r in rows if r["material_chain"] == c]
        if not cr:
            continue
        print("\n" + "=" * 100)
        print(f"{c.upper()}  rows={len(cr)}")
        print("stage x status:")
        for st in S.STAGES[c]:
            sr = [r for r in cr if r["stage"] == st]
            sc = Counter(r["facility_status"] for r in sr)
            ac = Counter(r["dfars_7052_assessment"] for r in sr)
            op_ok = [r for r in sr if r["facility_status"] == "operating" and r["dfars_7052_assessment"] == "likely_compliant"]
            print(f"  {st:26s} n={len(sr):3d} status={dict(sc)} assess={dict(ac)} operating&likely_compliant={len(op_ok)}")
        print("countries:", dict(Counter(r["country"] for r in cr).most_common()))
        print("availability:", dict(Counter(r["capacity_availability"] for r in cr)))
        print("ties:", dict(Counter(r["covered_country_tie"].split(";")[0].strip() for r in cr)))
        print("confidence:", dict(Counter(r["confidence"] for r in cr)))
        print("capacity (operating/commissioning, by stage):")
        by = defaultdict(list)
        for r in cr:
            if r["capacity_value"] and r["facility_status"] in ("operating", "commissioning", "construction"):
                by[r["stage"]].append(f'{r["company_name"]} [{r["facility_status"][:4]}|{r["dfars_7052_assessment"][:10]}|{r["capacity_availability"][:7]}] {r["capacity_value"]} {r["capacity_unit"]} ({r["capacity_year"]})')
        for st in S.STAGES[c]:
            for x in by.get(st, []):
                print(f"    {st}: {x}")
        print("top prospects (score>=4):")
        for r in sorted(cr, key=lambda r: -int(r["broker_fit_score"] or 0)):
            if r["broker_fit_score"] in ("4", "5"):
                print(f'   {r["broker_fit_score"]} {r["supplier_id"]} {r["company_name"]} | {r["facility_name"]} | {r["stage"]} | {r["facility_status"]} | {r["broker_fit_rationale"][:160]}')


if __name__ == "__main__":
    main()
