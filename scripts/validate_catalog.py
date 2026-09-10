#!/usr/bin/env python3
import json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
schema_stages = {"spec","acquire","parse","static_re","emulate_fuzz","runtime_assess","offense_poc","defend_harden","vuln_intel","dataset","paper_map","lab_teaching"}
tags_ok = {"paper-repro","daily-ops","lab-usable","hw-required","dataset","reference-impl"}
path = root/"data"/"tools.jsonl"
req = ["id","name","url","closed_loop_stage","use_tags","one_line","why_in_scope"]
bad = 0
n = 0
for i,line in enumerate(path.read_text().splitlines(),1):
    if not line.strip():
        continue
    n += 1
    o = json.loads(line)
    for k in req:
        if k not in o:
            print(f"L{i}: missing {k}"); bad += 1
    if o.get("closed_loop_stage") not in schema_stages:
        print(f"L{i}: bad stage {o.get('closed_loop_stage')}"); bad += 1
    for t in o.get("use_tags",[]):
        if t not in tags_ok:
            print(f"L{i}: bad tag {t}"); bad += 1
print(f"checked {n} tools, issues={bad}")
sys.exit(1 if bad else 0)
