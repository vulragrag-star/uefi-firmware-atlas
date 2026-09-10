# Agent guide — adding entries

1. Read `docs/TAXONOMY.md` inclusion/exclusion.
2. Add one JSON line to the right `data/*.jsonl` matching `data/schema.json`.
3. Run `python scripts/validate_catalog.py` and `python scripts/render_catalogs.py`.
4. Never invent `stars` / dates — leave `null` or run `scripts/gh_enrich.py`.
5. Out-of-domain hits → `data/rejected.jsonl` with `reason`.
6. `offense_poc`: research label only; no exploit tutorials.
