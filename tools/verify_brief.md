# Verification brief (independent re-check of sampled rows)

Today is 2026-11-16. Your job is to re-check a random sample of supplier rows against their cited sources and fresh searches. **Do not trust the row.** Verify it as if you were an auditor.

## Input

`/home/user/critical-minerals/data/staging/verification/sample_<workstream>.json`: a JSON array of sampled rows.
- `_line` is the row's line number in `data/staging/<workstream>/suppliers.jsonl`.
- Field definitions are in `/home/user/critical-minerals/tools/agent_brief.md` (section 5).
- The rule is in `/home/user/critical-minerals/docs/scope.md`.

## What to check for each sampled row (in this order)

1. **Company identity and ownership.** Check `company_name`, `parent_company`, `ultimate_owner` and `owner_country`. Look for any 2024-2026 change.
2. **Location.** Check `facility_name`, `city` and `country`, and that `stage` matches what the facility actually does.
3. **Status.** Check `facility_status` and `expected_production_date`.
4. **Capacity.** Check that `capacity_value`, `capacity_unit` and `capacity_year` match the source exactly.
5. **Offtakes and awards.** Check `committed_offtakes` and `government_awards` for existence, counterparty, amount and date.
6. **Covered-country ties.** Check `covered_country_tie` and `tie_detail`, and look for ties the row missed.
7. **Assessment.** Check that `dfars_7052_assessment` is consistent with the facts and the definitions.
8. **Sources.** Check that each URL in `sources` is real and supports what the row says. Open at least the main one.

## Output

Append one JSON object per sampled row to `/home/user/critical-minerals/data/staging/verification/results_<workstream>.jsonl` (one line each), with these keys:

```
{"workstream": "...", "_line": 12, "company_name": "...", "facility_name": "...", "stage": "...",
 "overall": "confirmed" | "minor_issues" | "major_issues" | "unverifiable",
 "checks": [ {"field": "capacity_value", "status": "confirmed|corrected|unverifiable", "row_value": "...",
              "correct_value": "...", "evidence_url": "https://...", "note": "..."} ],
 "summary": "one sentence"}
```

Use a short Python snippet to append (`json.dumps` plus newline), so the JSON stays valid.

**How to grade `overall`:**
- `major_issues`: a wrong owner, wrong country or status, an invented or wrong capacity, a non-existent offtake or award, or a missed covered-country tie.
- `minor_issues`: outdated details, small number mismatches, wording.

**Rules:**
- Only report a correction you can support with a URL.
- If you cannot confirm a fact either way, mark it `unverifiable`.
- Do **not** edit the suppliers files yourself. The coordinator applies corrections.
- Do not run git.
- Do not collect personal contact details.

## When finished

Reply in under 200 words, covering:
- counts of confirmed / minor / major / unverifiable;
- the major issues, one line each;
- any systematic pattern, for example "capacities often nameplate not actual" or "ownership outdated".
