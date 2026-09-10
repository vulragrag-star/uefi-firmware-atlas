# Setting book — UEFI research closed-loop

How to *use* this atlas in real work. Stages match `docs/TAXONOMY.md`.

## 1. Paper experiment (machine-checkable path)
1. Pick a claim in `data/papers.jsonl` with `artifacts.code` or a clearly linked tool.
2. Freeze inputs: firmware blob (LVFS/OEM/DVUEFI) + tool commit hash.
3. Prefer `lab-usable` tools first (UEFITool, uefi-firmware-parser, fiano, fwhunt-scan, Qiling EFI, OVMF builds).
4. Record command lines and hashes in your lab notebook (see `docs/SMOKE.md`).
5. If the paper needs SIMICS/DMA/SPI, mark `hw-required` and do not fake results on a cloud VM.

## 2. Daily ops (IT / OEM / Linux platform)
- **Update/acquire:** fwupd/LVFS, vendor capsules, BIOSUtilities unpack.
- **Assess:** CHIPSEC (supported platforms), FWTS, sbctl/shim status.
- **Inspect dumps:** UEFITool / fiano before any flash.
- Never flash from a random GitHub release without signature/hash checks.

## 3. Paper reproduction library
Rows tagged `paper-repro` are the shortlist. Cross-read:
- tools ↔ papers ↔ vulns (FwHunt rules often encode the vuln side).
Treat missing public harnesses as `UNCERTAIN` — do not invent scripts.

## 4. Firmware datasets
- **Rules/intel:** FwHunt
- **Teaching:** DVUEFI + CTF SMM challenges listed under `lab_teaching`
- **Field corpus:** LVFS (license-constrained). This atlas stores *pointers*, not mirrored OEM blobs.

## 5. Offense research ethics
`offense_poc` entries are for detection engineering and historical study. No step-by-step exploit runbooks live here — only links + stage tags + detector pointers.
