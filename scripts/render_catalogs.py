#!/usr/bin/env python3
import json
from pathlib import Path
from collections import defaultdict
root = Path(__file__).resolve().parents[1]
rows = [json.loads(l) for l in (root/"data"/"tools.jsonl").read_text().splitlines() if l.strip()]
by = defaultdict(list)
for r in rows:
    by[r["closed_loop_stage"]].append(r)
out = root/"catalogs"
out.mkdir(exist_ok=True)
index = ["# Catalogs by closed-loop stage\n"]
for stage in sorted(by):
    items = sorted(by[stage], key=lambda x: (-(x.get("stars") or -1), x["name"]))
    body = [f"# {stage}\n", f"_{len(items)} entries_\n"]
    for r in items:
        stars = r.get("stars")
        star_s = f"★{stars}" if stars is not None else "★?"
        tags = ", ".join(r.get("use_tags") or [])
        body.append(f"- **[{r['name']}]({r['url']})** {star_s} — {r['one_line']}  \n  tags: `{tags}`  \n  smoke: {r.get('smoke_notes')}\n")
    (out/f"{stage}.md").write_text("\n".join(body))
    index.append(f"- [{stage}]({stage}.md) ({len(items)})")
(out/"README.md").write_text("\n".join(index)+"\n")
print("rendered", len(by), "stages")
