# TAXONOMY — firmware-atlas series (UEFI first)

## Series repos (separate, not kitchen sink)
1. uefi-firmware-atlas — PC/server platform firmware (UEFI/BIOS/PI + tightly coupled ACPI/TPM/LVFS)
2. linux-kernel-atlas — Linux kernel security research tooling (later)
3. iot-firmware-atlas — router/camera/NAS embedded Linux firmwares (later)
4. rtos-firmware-atlas — FreeRTOS/Zephyr/ThreadX/... (later)
5. mcu-firmware-atlas — bare-metal MCU/SoC firmware (later)

## Primary axis: research closed-loop stages
spec | acquire | parse | static_re | emulate_fuzz | runtime_assess | offense_poc | defend_harden | vuln_intel | dataset | paper_map | lab_teaching

## Secondary tags (orthogonal)
paper-repro | daily-ops | lab-usable | hw-required | dataset | reference-impl

## Completeness strategy
1. Harvest seed awesome lists
2. Expand via GitHub topic + keyword search
3. Expand via paper artifact links
4. Dedup; reject out-of-domain
5. Smoke-test lab-usable subset on Linux VM
