# UEFI tools crawl summary

Generated: 2026-09-10 15:44 CST (Asia/Shanghai)

## Totals
- In-scope catalog entries: **130** (success criterion ≥80)
- Stars/last_push/license/language: live `gh api` metadata
- Seeds: river-li/awesome-uefi-security, PreOS-Security/awesome-firmware-security, killvxk/awesome_uefi_code, dwendt/awesome-uefi
- Expansion: GitHub `topic:uefi` + queries chipsec, uefi-firmware-parser, efiXplorer, fwhunt, OVMF, SMM backdoor, BlackLotus, UEFITool, fwupd, flashrom, …
- Method: gh API / gh search / WebFetch only — **no repo clones**

## Counts by closed_loop_stage
| stage | count |
|-------|------:|
| spec | 5 |
| acquire | 4 |
| parse | 14 |
| static_re | 10 |
| emulate_fuzz | 6 |
| runtime_assess | 12 |
| offense_poc | 27 |
| defend_harden | 17 |
| vuln_intel | 5 |
| dataset | 1 |
| paper_map | 7 |
| lab_teaching | 22 |
| **total** | **130** |

## Top 15 must-have tools

- **UEFITool** (5663★) — `parse` — Cross-platform UEFI firmware image browser/editor/extractor — https://github.com/LongSoft/UEFITool
- **chipsec** (3299★) — `runtime_assess` — Platform security assessment framework (SPI/SMM/Secure Boot/DMA) — https://github.com/chipsec/chipsec
- **edk2** (6238★) — `spec` — EDK II open-source UEFI/PI reference implementation including OVMF — https://github.com/tianocore/edk2
- **uefi-firmware-parser** (923★) — `parse` — Python library/CLI to parse UEFI firmware volumes and capsules — https://github.com/theopolis/uefi-firmware-parser
- **efiXplorer** (1128★) — `static_re` — IDA/Ghidra plugin for UEFI firmware reverse engineering — https://github.com/REhints/efiXplorer
- **FwHunt** (248★) — `vuln_intel` — FwHunt YAML ruleset for detecting known UEFI vulnerabilities — https://github.com/binarly-io/FwHunt
- **fwhunt-scan** (244★) — `static_re` — Scanner that applies FwHunt rules to firmware images — https://github.com/binarly-io/fwhunt-scan
- **flashrom** (1169★) — `acquire` — Utility to read/write SPI flash chips (BIOS/UEFI ROM) — https://github.com/flashrom/flashrom
- **fwupd** (4151★) — `acquire` — Linux firmware update daemon with LVFS backend for platform capsules — https://github.com/fwupd/fwupd
- **fiano** (373★) — `parse` — Go toolkit to parse/transform UEFI firmware images (utk) — https://github.com/linuxboot/fiano
- **efi_fuzz** (154★) — `emulate_fuzz` — Coverage-guided UEFI DXE protocol fuzzer (Qiling-based) — https://github.com/Sentinel-One/efi_fuzz
- **tsffs** (331★) — `emulate_fuzz` — Snapshot/fuzz framework for SIMICS targeting firmware — https://github.com/intel/tsffs
- **fwts** (30★) — `runtime_assess` — Firmware Test Suite (ACPI/UEFI/SMBIOS compliance & security tests) — https://github.com/ColinIanKing/fwts
- **sbctl** (2256★) — `defend_harden` — User-friendly Secure Boot key manager — https://github.com/Foxboron/sbctl
- **shim** (1103★) — `defend_harden` — First-stage UEFI bootloader for Secure Boot (distro signed) — https://github.com/rhboot/shim

## Exclusion notes (tempting misses)
- ventoy/Ventoy — generic bootable USB creator; out unless Secure Boot lab fringe (excluded).
- pbatard/rufus — USB formatter; out of platform-firmware scope.
- CTCaer/hekate — Nintendo Switch bootloader; out.
- firmadyne/firmadyne — embedded/IoT Linux firmware emulator; belongs in iot-firmware-atlas.
- openbmc/openbmc — BMC stack; server mgmt plane, not host UEFI SPI ROM atlas.
- attify/firmware-analysis-toolkit / OWASP/IoTGoat — IoT firmware; out.
- Generic U-Boot trees — MCU/embedded boot; out unless explicitly PC/server UEFI.
- microsoft/MSRC-Security-Research — general MSRC corpus; not UEFI-focused (excluded).

## Fringe (included with notes)
- acidanthera/OpenCorePkg, Metabolix/HackBGRT, xCuri0/ReBarUEFI, pbatard/uefi-ntfs, Zero-Tang/NoirVisor, tandasat/MiniVisorPkg — UEFI-adjacent but not core security toolchain.

## Scope reminders
- **IN**: PC/server UEFI/BIOS/EDK2/OVMF/PI, Secure Boot, SMM/DXE/PEI, SPI ROM, ACPI platform fw, CHIPSEC/FWTS/UEFITool, bootkits research, FwHunt, efiXplorer, LVFS/fwupd.
- **OUT**: Linux kernel atlas, IoT/OpenWrt, MCU/ESP32, RTOS, generic USB creators.

## Smoke notes
- Crawl is metadata + curated classification; in-VM smoke of lab-usable subset not executed this pass.
- Practical starters: UEFITool NE, CHIPSEC (Linux root), OVMF+QEMU Secure Boot (rhuefi/qemu-ovmf-secureboot), fwupd/LVFS for capsule acquire, flashrom for SPI dump.
