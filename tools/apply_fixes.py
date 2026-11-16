#!/usr/bin/env python3
"""Apply verification corrections to staging supplier rows.

Usage: python3 tools/apply_fixes.py fixes.json

fixes.json is a JSON array of objects:
  {"ws": "tungsten",                # staging workstream folder
   "line": 12,                      # 1-indexed line in suppliers.jsonl
   "expect_company": "Masan",       # substring that must appear in company_name (safety check)
   "set": {"field": "new value"},   # fields to overwrite
   "append": {"notes": "text"},     # text appended to existing field (with a space)
   "add_sources": [{"url": "...", "title": "...", "publisher": "...", "date": "...", "type": "..."}]}

Source URLs in add_sources are appended to the row's `sources` field and to the
workstream's sources.jsonl (deduplicated by URL).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    fixes = json.load(open(sys.argv[1], encoding="utf-8"))
    by_ws = {}
    for f in fixes:
        by_ws.setdefault(f["ws"], []).append(f)
    for ws, fl in by_ws.items():
        d = os.path.join(ROOT, "data", "staging", ws)
        sp = os.path.join(d, "suppliers.jsonl")
        lines = open(sp, encoding="utf-8").read().splitlines()
        src_path = os.path.join(d, "sources.jsonl")
        src_urls = set()
        if os.path.exists(src_path):
            for l in open(src_path, encoding="utf-8"):
                if l.strip():
                    src_urls.add(json.loads(l).get("url", "").strip())
        new_src = []
        for f in fl:
            i = f["line"] - 1
            row = json.loads(lines[i])
            if f.get("expect_company", "").lower() not in row["company_name"].lower():
                sys.exit(f"SAFETY STOP: {ws} line {f['line']} is '{row['company_name']}', expected '{f.get('expect_company')}'")
            for k, v in f.get("set", {}).items():
                if k not in row:
                    sys.exit(f"unknown field {k}")
                row[k] = v
            for k, v in f.get("append", {}).items():
                row[k] = (str(row.get(k, "")).rstrip() + " " + v).strip()
            for s in f.get("add_sources", []):
                u = s["url"].strip()
                cur = [x.strip() for x in str(row.get("sources", "")).split(";") if x.strip()]
                if u not in cur:
                    cur.append(u)
                row["sources"] = "; ".join(cur)
                if u not in src_urls:
                    src_urls.add(u)
                    new_src.append({"title": s.get("title", ""), "publisher": s.get("publisher", ""),
                                    "date": s.get("date", "undated"), "url": u,
                                    "type": s.get("type", "other"), "date_accessed": "2026-11-16"})
            lines[i] = json.dumps(row, ensure_ascii=False)
            print(f"fixed {ws} line {f['line']}: {row['company_name']}")
        with open(sp, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        if new_src:
            with open(src_path, "a", encoding="utf-8") as fh:
                for s in new_src:
                    fh.write(json.dumps(s, ensure_ascii=False) + "\n")
            print(f"  added {len(new_src)} source(s) to {ws}/sources.jsonl")


if __name__ == "__main__":
    main()
