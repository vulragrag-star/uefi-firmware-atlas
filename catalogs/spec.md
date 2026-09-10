# spec

_12 entries_

- **[edk2](https://github.com/tianocore/edk2)** ★6238 — QEMU virtual firmware package built from edk2 (OvmfPkg) — artifact layer.  
  tags: `lab-usable, paper-repro, reference-impl`  
  smoke: Build OvmfPkg from edk2 or use distro OVMF with QEMU; do not catalog as separate firmware project.

- **[coreboot](https://github.com/coreboot/coreboot)** ★2788 — coreboot — open host firmware (non-EDK2 path).  
  tags: `reference-impl, lab-usable`  
  smoke: Build select boards; fringe.

- **[oreboot](https://github.com/oreboot/oreboot)** ★1797 — Pure-Rust boot firmware.  
  tags: `reference-impl, lab-usable`  
  smoke: Limited boards.

- **[uefi-rs](https://github.com/rust-osdev/uefi-rs)** ★1650 — Idiomatic Rust UEFI bindings and apps  
  tags: `reference-impl, lab-usable`  
  smoke: Reference for writing EFI apps

- **[mu](https://github.com/microsoft/mu)** ★658 — Project Mu - Microsoft UEFI modern fork/ecosystem  
  tags: `reference-impl`  
  smoke: mu_basecore ecosystem

- **[edk2-platforms](https://github.com/tianocore/edk2-platforms)** ★655 — Platform packages for EDK II.  
  tags: `reference-impl, lab-usable`  
  smoke: Some QEMU platforms buildable.

- **[slimbootloader](https://github.com/slimbootloader/slimbootloader)** ★468 — Intel Slim Bootloader minimal firmware.  
  tags: `reference-impl, lab-usable`  
  smoke: Select targets buildable.

- **[edk2-staging](https://github.com/tianocore/edk2-staging)** ★180 — Staging area for new EDK II features before mainline.  
  tags: `reference-impl`  
  smoke: Track features; prefer edk2 main for baselines.

- **[edk2-libc](https://github.com/tianocore/edk2-libc)** ★136 — libc port and apps for EDK II.  
  tags: `reference-impl, lab-usable`  
  smoke: Build with edk2 workspace.

- **[uefi](https://github.com/yabits/uefi)** ★110 — Small UEFI-related project from yabits  
  tags: `lab-usable`  
  smoke: Small; ARCHIVED

- **[edk2-non-osi](https://github.com/tianocore/edk2-non-osi)** ★91 — Non-OSI licensed content used with some EDK2 platforms.  
  tags: `reference-impl`  
  smoke: License-constrained; not for redistribution experiments.

- **[UEFI Specification](https://uefi.org/specifications)** ★? — Official UEFI Forum specifications.  
  tags: `reference-impl, daily-ops, paper-repro`  
  smoke: PDF only.
