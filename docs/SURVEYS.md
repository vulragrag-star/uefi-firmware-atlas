# Surveys as maps

Surveys/SoKs are indexed in `data/papers.jsonl` with `themes: ["survey"]` and listed in `catalogs/surveys.md`.

## PDF policy
1. Prefer **final published OA** (USENIX, SpringerOpen, MDPI, author final on personal site).
2. If only arXiv exists and no published OA yet, store preprint and mark `version_kind: preprint`.
3. If later a final OA appears, **replace** the preprint file and update the manifest (do not keep both as current).
4. Paywalled publisher HTML is not a PDF — do not commit.

## Firmware / large artifacts
- Do **not** git-mirror copyrighted vendor firmware.
- Store **official portal URLs** in `data/datasets.jsonl` (`status: OFFICIAL_LINK` or `LICENSE_BOUND`).
- Large OA PDFs (<~50MB) may live under `papers/pdf/` with sha256 in `papers/PDF_MANIFEST.jsonl`.
