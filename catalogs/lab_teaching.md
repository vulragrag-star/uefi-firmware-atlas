# lab_teaching

_10 entries_

- **[uefi-rs](https://github.com/rust-osdev/uefi-rs)** ★1650 — Safe Rust UEFI API wrappers.  
  tags: `lab-usable, reference-impl, paper-repro`  
  smoke: Build UEFI apps in VM.

- **[DVUEFI](https://github.com/hacking-support/DVUEFI)** ★308 — Damn Vulnerable UEFI lab.  
  tags: `lab-usable, paper-repro, dataset`  
  smoke: Designed for lab use.

- **[edk2-test](https://github.com/tianocore/edk2-test)** ★105 — Test infrastructure and cases for EDK II based firmware.  
  tags: `lab-usable, paper-repro, reference-impl`  
  smoke: Host/firmware tests; separate from runtime_assess tools.

- **[edk2-pytool-extensions](https://github.com/tianocore/edk2-pytool-extensions)** ★77 — Plugin-based EDK2 build system extensions (Stuart et al.).  
  tags: `lab-usable, daily-ops, reference-impl`  
  smoke: Build orchestration on Linux VM; not a RE/parser.

- **[edk2-pytool-library](https://github.com/tianocore/edk2-pytool-library)** ★67 — Python library supporting UEFI/EDK2 development workflows.  
  tags: `lab-usable, daily-ops, reference-impl`  
  smoke: pip install; use with Stuart/CI — does not parse SPI dumps.

- **[containers](https://github.com/tianocore/containers)** ★37 — Official-ish EDK2 container images for builds.  
  tags: `lab-usable, daily-ops`  
  smoke: Docker build env on VM.

- **[edk2-edkrepo](https://github.com/tianocore/edk2-edkrepo)** ★31 — edkrepo utility to sync multi-repo EDK2 workspaces.  
  tags: `lab-usable, daily-ops`  
  smoke: Clone/sync workflows on VM.

- **[edk2-basetools](https://github.com/tianocore/edk2-basetools)** ★28 — EDK II BaseTools packaged as a Python/PIP module.  
  tags: `lab-usable, reference-impl`  
  smoke: Prefer matching edk2 revision; lab build aid.

- **[edk2-edkrepo-manifest](https://github.com/tianocore/edk2-edkrepo-manifest)** ★8 — Platform manifests consumed by edkrepo.  
  tags: `lab-usable, daily-ops`  
  smoke: Used with edkrepo; do not treat as a tool by itself.

- **[OVMF (OvmfPkg)](https://github.com/tianocore/edk2/tree/master/OvmfPkg)** ★? — QEMU virtual firmware package built from edk2 (OvmfPkg) — artifact layer.  
  tags: `lab-usable, paper-repro, reference-impl`  
  smoke: Build OvmfPkg from edk2 or use distro OVMF with QEMU; do not catalog as separate firmware project.
