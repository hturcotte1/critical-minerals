#!/usr/bin/env python3
"""Cross-field consistency checks on staging supplier rows.

Usage: python3 tools/consistency.py            (report only)
       python3 tools/consistency.py --fix      (apply the safe automatic fixes listed below)

Safe automatic fixes (recorded in each row's notes):
  A. tie 'none' + assessment at_risk/likely_noncompliant whose reason cites unknown/undisclosed
     feed origin -> covered_country_tie 'unknown' (tie_detail explains).
  B. facility_status 'closed' with broker_fit_score > 1 -> score 1.
Everything else is reported for manual review.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING = os.path.join(ROOT, "data", "staging")
COVERED = {"china", "russia", "north korea", "iran"}
FEED_RE = re.compile(r"(feed|feedstock|oxide|alloy|powder|concentrate|intermediate|raw material|source|origin|supply|scrap|cobalt|samarium)[^.;]{0,80}(undisclosed|not disclosed|unknown|unverified|not verified|unclear|opaque|not documented|undocumented|not traced|untraced|not public)|(undisclosed|unknown|unverified|unclear|not disclosed)[^.;]{0,40}(feed|origin|source)", re.I)


def main():
    fix = "--fix" in sys.argv
    issues = []
    for ws in sorted(os.listdir(STAGING)):
        p = os.path.join(STAGING, ws, "suppliers.jsonl")
        if ws == "verification" or not os.path.exists(p):
            continue
        rows = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
        changed = 0
        for n, r in enumerate(rows, 1):
            tag = f"{ws}:{n} {r['company_name'][:50]} [{r['stage']}]"
            ties = [t.strip() for t in str(r.get("covered_country_tie", "")).split(";") if t.strip()]
            a = r.get("dfars_7052_assessment")
            score = int(str(r.get("broker_fit_score") or 0))
            reason = str(r.get("dfars_7052_reason", "")) + " " + str(r.get("tie_detail", ""))
            if str(r.get("country", "")).strip().lower() in COVERED:
                issues.append(f"COVERED-COUNTRY ROW in suppliers: {tag} country={r['country']}")
            if ties == ["none"] and a in ("at_risk", "likely_noncompliant"):
                if FEED_RE.search(reason):
                    if fix:
                        r["covered_country_tie"] = "unknown"
                        if not r.get("tie_detail"):
                            r["tie_detail"] = "No covered-country ownership found, but feed/input origin is not disclosed, so a feedstock tie cannot be ruled out."
                        r["notes"] = (str(r.get("notes", "")).rstrip() + " Consistency pass 2026-11-16: tie changed from 'none' to 'unknown' because input origin is undisclosed.").strip()
                        changed += 1
                    else:
                        issues.append(f"A tie none but {a} with unknown-feed reason: {tag}")
                else:
                    issues.append(f"REVIEW tie none but {a}: {tag} | {reason[:140]}")
            if any(t in ("ownership", "control") for t in ties) and a == "likely_compliant":
                issues.append(f"REVIEW ownership/control tie but likely_compliant: {tag} | {r.get('tie_detail','')[:140]}")
            if r.get("facility_status") == "closed" and score > 1:
                if fix:
                    r["broker_fit_score"] = 1
                    r["notes"] = (str(r.get("notes", "")).rstrip() + " Consistency pass 2026-11-16: score set to 1 because the facility is closed.").strip()
                    changed += 1
                else:
                    issues.append(f"B closed but score {score}: {tag}")
            if r.get("capacity_availability") == "fully_committed" and score >= 4:
                issues.append(f"REVIEW fully_committed but score {score}: {tag}")
            if a == "likely_noncompliant" and score > 2:
                issues.append(f"REVIEW likely_noncompliant but score {score}: {tag}")
            if r.get("facility_status") in ("planned",) and score >= 5:
                issues.append(f"REVIEW planned but score 5: {tag}")
        if fix and changed:
            with open(p, "w", encoding="utf-8") as fh:
                for r in rows:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            print(f"{ws}: applied {changed} automatic fix(es)")
    for i in issues:
        print(i)
    print(f"{len(issues)} issue(s) reported")


if __name__ == "__main__":
    main()
