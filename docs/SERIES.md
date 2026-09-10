# Firmware-atlas series plan

| Repo | Domain | Inclusion core | Status |
|---|---|---|---|
| [uefi-firmware-atlas](https://github.com/vulragrag-star/uefi-firmware-atlas) | PC/server UEFI/BIOS/PI | EDK2, SMM/DXE/PEI, Secure Boot, LVFS platform capsules | **seeded** |
| linux-kernel-atlas | Linux kernel security research | syzkaller, KFENCE, KASAN, LKRG, kernel CTF corpora — not distro packaging | planned |
| iot-firmware-atlas | Embedded Linux device firmwares | router/camera/NAS dumps, binwalk/FACT/EMBA, Firmadyne/FirmAE | planned |
| rtos-firmware-atlas | RTOS images & tools | FreeRTOS, Zephyr, ThreadX, NuttX analysis | planned |
| mcu-firmware-atlas | Bare-metal MCU/SoC | Cortex-M/ESP dumps, Ghidra loaders, SVD, Unicorn MCU | planned |

Each repo copies: TAXONOMY stages (may rename domain-specific), METHOD completeness gates, JSONL schema, SETTING + SMOKE, catalogs render scripts.
Cross-links only — never merge IoT corpora into the UEFI repo.
