#!/usr/bin/env python3
"""Draw a reproducible random sample of supplier rows per workstream for the
verification pass. Writes data/staging/verification/sample_<workstream>.json

Usage: python3 tools/sample_for_verification.py [fraction] [min] [max]
"""
import json
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING = os.path.join(ROOT, "data", "staging")
OUT = os.path.join(STAGING, "verification")


def main():
    frac = float(sys.argv[1]) if len(sys.argv) > 1 else 0.15
    lo = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    hi = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    os.makedirs(OUT, exist_ok=True)
    rng = random.Random(20261116)
    for ws in sorted(os.listdir(STAGING)):
        p = os.path.join(STAGING, ws, "suppliers.jsonl")
        if ws == "verification" or not os.path.exists(p):
            continue
        rows = []
        with open(p, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                if line.strip():
                    r = json.loads(line)
                    r["_line"] = n
                    rows.append(r)
        if not rows:
            continue
        k = max(lo, min(hi, round(len(rows) * frac)))
        k = min(k, len(rows))
        # prefer rows that matter most: weight high-score and operating rows a bit higher
        weights = []
        for r in rows:
            w = 1.0
            if str(r.get("broker_fit_score")) in ("4", "5"):
                w += 1.0
            if r.get("facility_status") == "operating":
                w += 0.5
            weights.append(w)
        chosen = set()
        while len(chosen) < k:
            chosen.add(rng.choices(range(len(rows)), weights=weights)[0])
        sample = [rows[i] for i in sorted(chosen)]
        keep = ["_line", "company_name", "parent_company", "ultimate_owner", "owner_country",
                "covered_country_tie", "tie_detail", "material_chain", "stage", "products",
                "facility_name", "city", "state_region", "country", "facility_status",
                "expected_production_date", "capacity_value", "capacity_unit", "capacity_year",
                "capacity_source", "feedstock_origin", "committed_offtakes", "government_awards",
                "rmi_rmap_status", "dfars_7052_assessment", "dfars_7052_reason",
                "capacity_availability", "broker_fit_score", "sources"]
        sample = [{k2: r.get(k2, "") for k2 in keep} for r in sample]
        with open(os.path.join(OUT, f"sample_{ws}.json"), "w", encoding="utf-8") as f:
            json.dump(sample, f, ensure_ascii=False, indent=1)
        print(f"{ws}: {len(rows)} rows -> sampled {len(sample)}")


if __name__ == "__main__":
    main()
