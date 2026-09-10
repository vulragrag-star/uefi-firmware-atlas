# Survey-as-map cross-check (2026-09-10)

Treated domain SoKs/surveys as curated inventories; extracted systems; diffed against atlas `tools.jsonl`; merged high-confidence public artifacts; indexed closed tools as `UNCERTAIN`.

| Atlas | Surveys mined | Added LIVE | Added UNCERTAIN | Notes |
|---|---|---|---|---|
| uefi-firmware-atlas | Bootloader SoK, SMM SoK, UEFI ATT&CK-like SoK | 7 (+ oss-bootloaders dataset) | 6 | UEFUZZER→FuzzUEr alias |
| linux-kernel-atlas | arXiv 2501.16165, 2502.13163 | ~30 | 15 | Hydra/MoonShine/USBFuzz… |
| iot-firmware-atlas | Fasano, Wright, Springer, Alrawi | 5 | deferred low-conf | FirmFuzz/BaseSAFE/DIANE… |
| mcu-firmware-atlas | MDPI 2025 (+ shared) | 13 | deferred | AIM/Hoedur/SEmu/Jetset… |
| rtos-firmware-atlas | thin from shared surveys | 0 | — | Hoedur already present |

Reports: `CROSSCHECK_{UEFI,LINUX,IOT_MCU}.md`, `gaps_*.jsonl`, per-repo `docs/SURVEY_GAP_FILL_2026-09-10.md`.
