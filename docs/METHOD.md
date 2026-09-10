# Method — how this atlas stays domain-complete (not a kitchen sink)

## Goal
Maximize **recall within UEFI/BIOS platform firmware research**, while keeping **precision** high enough that an IoT/MCU/kernel item does not sneak in.

## Pipeline
1. **Seed harvest** — ingest known curated lists (see `data/seeds/`).
2. **Graph expand** — GitHub `topic:uefi`, keyword searches (`chipsec`, `uefi-firmware-parser`, `efiXplorer`, `fwhunt`, `OVMF`, `SMM`, bootkit names), plus paper artifact links.
3. **Normalize** — one JSON object per artifact into `data/*.jsonl` per `data/schema.json`.
4. **Gate** — apply inclusion/exclusion from `docs/TAXONOMY.md`. Tempting rejects go to `data/rejected.jsonl` with reason.
5. **Enrich** — `scripts/gh_enrich.py` fills stars / `pushed_at` / license via GitHub API (never invent).
6. **Render** — `scripts/render_catalogs.py` rebuilds `catalogs/*.md`.
7. **Smoke** — `docs/SMOKE.md` + `lab/` notes for `lab-usable` rows on a plain Linux VM / QEMU+OVMF.

## Completeness checks
- Every closed-loop stage has ≥1 `lab-usable` or explicit `hw-required` note.
- Papers with public code must cross-link `related_tools`.
- Bootkits/CVEs link detection tooling when known (FwHunt, CHIPSEC modules, etc.).

## What we refuse
- Dumping every repo with “firmware” in the name.
- Mixing router/OpenWrt corpora into this repo (→ `iot-firmware-atlas`).
- Tutorial-length exploit writeups (pointers + research labels only).
