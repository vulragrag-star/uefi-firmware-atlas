# Box smoke log (Grok Bot computer)

Environment: Linux cloud VM (no SPI programmer, no FPGA DMA, no SIMICS). Date zone: Asia/Shanghai (CST).

| date (CST) | tool | result | notes |
|---|---|---|---|
| 2026-09-10 | `scripts/validate_catalog.py` | **ok** | 40 tools, 0 schema issues |
| 2026-09-10 | `scripts/render_catalogs.py` | **ok** | 10 stage markdown catalogs |
| 2026-09-10 | `utk` (fiano `go install github.com/linuxboot/fiano/cmds/utk@latest`) | **ok** | binary runs; `--help` lists cat/count/extract ops — green path for parse |
| 2026-09-10 | PyPI `uefi-firmware-parser` | **fail** | no matching distribution on this Python 3.13 — use git install or stick to fiano/UEFITool |
| 2026-09-10 | prior polluted venv `uefi_firmware` | **fail** | `efi_compressor` import break — do not trust shared venvs |
| 2026-09-10 | `chipsec` pip wheel | **fail** | native build failed — yellow/red without headers+driver |
| 2026-09-10 | flashrom / PCILeech / tsffs | **blocked-hw** | correctly `hw-required` |

## Takeaway
Cloud VM is honest for **parse tooling (fiano/utk) + catalog automation + (next) OVMF/QEMU**. It is the wrong place to claim CHIPSEC platform assessment or DMA/SPI results. Aligns with `docs/SMOKE.md`.
