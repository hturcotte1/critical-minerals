#!/usr/bin/env python3
"""Append a batch of rows (a JSON array in a file) to a staging JSONL file.

Usage:
    python3 tools/append_rows.py data/staging/tungsten/suppliers.jsonl batch.json

The kind of file (suppliers / offtakes / excluded / sources) is taken from the
target file name. Missing fields are filled with "" so every line has the full
schema. Unknown keys are rejected so typos are caught early. For sources, a URL
that is already present in the target file is skipped (no duplicates).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema as S  # noqa: E402

KIND_FIELDS = {
    "suppliers": S.SUPPLIER_FIELDS,
    "offtakes": S.OFFTAKE_FIELDS,
    "excluded": S.EXCLUDED_FIELDS,
    "sources": S.SOURCE_FIELDS,
}


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    target, batch = sys.argv[1], sys.argv[2]
    kind = os.path.basename(target).split(".")[0]
    if kind not in KIND_FIELDS:
        sys.exit(f"target must be one of {list(KIND_FIELDS)}.jsonl")
    fields = KIND_FIELDS[kind]
    with open(batch, encoding="utf-8") as f:
        rows = json.load(f)
    if isinstance(rows, dict):
        rows = [rows]
    existing_urls = set()
    if kind == "sources" and os.path.exists(target):
        with open(target, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        existing_urls.add(json.loads(line).get("url", "").strip())
                    except json.JSONDecodeError:
                        pass
    bad = []
    out = []
    for i, r in enumerate(rows):
        unknown = [k for k in r if k not in fields]
        if unknown:
            bad.append(f"row {i}: unknown keys {unknown}")
            continue
        if kind == "sources":
            u = str(r.get("url", "")).strip()
            if u in existing_urls:
                continue
            existing_urls.add(u)
        full = {k: ("" if r.get(k) is None else r.get(k)) for k in fields}
        out.append(full)
    if bad:
        print("REJECTED (nothing written):")
        for b in bad:
            print("  " + b)
        sys.exit(1)
    os.makedirs(os.path.dirname(os.path.abspath(target)), exist_ok=True)
    with open(target, "a", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"appended {len(out)} row(s) to {target}")


if __name__ == "__main__":
    main()
