# Smoke plan — what works on a plain Linux cloud VM

Assumption: x86_64 Linux, no SPI programmer, no FPGA DMA, no SIMICS license.

## Green (try first)
| Action | Tool | Expect |
|---|---|---|
| Parse a public/capsule dump | UEFITool / `utk` (fiano) / uefi-firmware-parser | Tree of FV/FFS; extract DXE |
| Rule scan | fwhunt-scan + FwHunt YAML | Match/no-match JSON |
| Emulate subset | Qiling EFI mode / efi_dxe_emulator | Partial exec; not full boot |
| Build reference FW | edk2 OVMF | QEMU bootable firmware |
| Teaching | DVUEFI | Lab VMs/challenges |
| Secure Boot keys (software) | sbctl (generate keys) | Keys only; no NVRAM enroll |

## Yellow (partial)
| Action | Tool | Blocker |
|---|---|---|
| CHIPSEC modules | chipsec | Many checks need `/dev/mem`, MSR, or real firmware surface |
| fwupd | fwupd | Metadata OK; apply needs device |
| Ghidra/IDA plugins | efiSeek, efiXplorer, brick | Need RE product licenses/install |

## Red (do not claim success on cloud VM alone)
| Action | Tool |
|---|---|
| SPI dump/flash | flashrom + programmer |
| DMA attacks | PCILeech + FPGA |
| SIMICS snapshot fuzz | intel/tsffs |
| Production Secure Boot enroll | Platform-specific |

## Box log template
```
date:
tool@commit:
input_blob_sha256:
command:
result: ok|fail|blocked-hw
notes:
```
