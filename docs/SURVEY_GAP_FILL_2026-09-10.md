# UEFI survey gap-fill (2026-09-10)

Cross-checked Bootloader SoK / SMM SoK / UEFI ATT&CK-like SoK against `tools.jsonl`.
See `survey-hunt/CROSSCHECK_UEFI.md`.

## Added LIVE / fringe
- SeaBIOS
- GRUB
- rustBoot
- FMMT
- Platbox
- dreamboot
- vector-edk

## Added UNCERTAIN (index_only, no public code)
- STASE
- SPENDER
- SymUEFI
- EXCITE
- SimFuzzer
- RSFuzzer

## Datasets
- oss-bootloaders

## Deferred / aliased
- **UEFUZZER** → aliases on existing `breakingboot_fuzzuer` (FuzzUEr)
- Low-confidence / OUT_OF_DOMAIN items left in `survey-hunt/gaps_uefi.jsonl` extras / CROSSCHECK report
