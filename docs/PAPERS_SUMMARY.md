# UEFI papers / datasets / vulns crawl summary

Generated: 2026-09-10 (Asia/Shanghai). Scope: PC/server UEFI/BIOS/SMM/Secure Boot/measured boot only.
Method: WebSearch/WebFetch/gh only — **no clones**. Taxonomy stages from `prompts/taxonomy.md`.

## Counts
| Artifact | Path | Count | Threshold |
|---|---|---:|---:|
| papers/talks | `/workspace/firmware-atlas-work/uefi/papers.jsonl` | 71 | >=40 |
| datasets | `/workspace/firmware-atlas-work/uefi/datasets.jsonl` | 12 | >=8 |
| vulns | `/workspace/firmware-atlas-work/uefi/vulns.jsonl` | 22 | >=15 |
| summary | `/workspace/firmware-atlas-work/uefi/papers_summary.md` | 1 | — |

**Success criteria: MET.**

## Required inclusions checklist
- FUZZUER NDSS25 — yes (`BreakingBoot/FuzzUEr`, DOI 10.14722/ndss.2025.240400)
- HBFA — yes (Intel whitepaper + `tianocore/edk2-staging` HBFA)
- RSFUZZER — yes (IEEE S&P 2023; code UNCERTAIN/not public)
- EXCITE — yes (WOOT15 Bazhaniuk + Intel Simics/EXCITE article)
- efi_fuzz — yes (Sentinel-One)
- Binarly — yes (efiXplorer, FwHunt, LogoFAIL, PKfail, BH talks)
- CHIPSEC papers/talks — yes (CanSecWest 2014 + later)
- Black Hat / DEF CON mapped to tools — yes throughout

## Best paper–repro pairs
| Paper / talk | Artifact | Why best |
|---|---|---|
| FUZZUER NDSS25 | `https://github.com/BreakingBoot/FuzzUEr` | Best modern EDK2 interface fuzzer; open code+paper; needs Simics/TSFFS |
| efi_fuzz | `https://github.com/Sentinel-One/efi_fuzz` | Open Qiling+AFL++ NVRAM fuzzer with full blog trilogy |
| HBFA | `https://github.com/tianocore/edk2-staging/tree/HBFA` | Intel host-based EDK2 fuzz/symbolic; open + whitepaper |
| PixieFail | `https://github.com/quarkslab/pixiefail` | Scapy PoCs + detailed blog; pairs with STASE paper |
| ThinkPwn | `https://github.com/Cr4sh/ThinkPwn` | Classic SMM callout PoC + writeup |
| efiXplorer + FwHunt | `https://github.com/binarly-io/efiXplorer` | Static RE + detection rules; BH talks + scale case studies |
| brick | `https://github.com/Sentinel-One/brick` | SMM antipattern scanner; Sentinel blogs |
| DVUEFI | `https://github.com/hacking-support/DVUEFI` | BH Arsenal lab platform for teaching |
| CHIPSEC | `https://github.com/chipsec/chipsec` | Runtime assess de-facto; CSW2014 origin |
| TSFFS | `https://github.com/intel/tsffs` | Simics snapshot fuzzer used by FUZZUER |
| BlackLotus / CVE-2022-21894 | `https://github.com/Wack0/CVE-2022-21894` | Baton Drop PoC + ESET analysis |
| SmmBackdoor | `https://github.com/Cr4sh/SmmBackdoor` | Research SMM implant paired with Cr4sh writeups |

## UNCERTAIN / paywalled
- SPENDER (S&P 2022), RSFUZZER (S&P 2023), UEFUZZER, SmuFuzz, some ACM/IEEE PDFs: abstracts/secondary sources used; full PDF or code often paywalled or unreleased.
- RSFUZZER authors indicated tool could not be made public (per STASE/SoK commentary).
- ESET/Kaspersky bootkit samples: analyses public; malware corpora not redistributed.
- LVFS: public firmware downloads exist but vendor licenses may restrict redistribution; ~650k EFI modules historically scanned by FwHunt (not a single downloadable research dump).
- ESET ML UEFI landscape: methodology public; underlying corpus proprietary.

## Stage coverage (papers)
- `offense_poc`: 21
- `vuln_intel`: 18
- `emulate_fuzz`: 9
- `paper_map`: 6
- `runtime_assess`: 6
- `static_re`: 6
- `defend_harden`: 4
- `lab_teaching`: 1

## Seeds credited
- [river-li/awesome-uefi-security](https://github.com/river-li/awesome-uefi-security)
- atlas `data/seeds/SOURCES.md` (PreOS-Security/awesome-firmware-security, killvxk/awesome_uefi_code, dwendt/awesome-uefi)
- NDSS / IEEE / USENIX / ACM pages; Binarly, ESET, Kaspersky, Eclypsium, Quarkslab, SentinelOne, NCC Group, Synacktiv public writeups
