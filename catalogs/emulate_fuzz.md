# emulate_fuzz

_9 entries_

- **[qiling](https://github.com/qilingframework/qiling)** ★6093 — Binary emulation framework with UEFI/DXE support  
  tags: `lab-usable, paper-repro, reference-impl`  
  smoke: Not UEFI-only but critical dependency

- **[tsffs](https://github.com/intel/tsffs)** ★331 — Snapshot/fuzz framework for SIMICS targeting firmware  
  tags: `lab-usable, paper-repro, reference-impl`  
  smoke: SIMICS-oriented; powerful but heavy setup

- **[efi_fuzz](https://github.com/Sentinel-One/efi_fuzz)** ★154 — Coverage-guided UEFI DXE protocol fuzzer (Qiling-based)  
  tags: `lab-usable, paper-repro`  
  smoke: Needs Qiling; good paper-repro target; ARCHIVED

- **[efi_dxe_emulator](https://github.com/assafcarlsbad/efi_dxe_emulator)** ★88 — Emulator for UEFI DXE modules  
  tags: `lab-usable, paper-repro`  
  smoke: Research emulator

- **[ebcvm](https://github.com/yabits/ebcvm)** ★82 — EFI Byte Code virtual machine  
  tags: `lab-usable`  
  smoke: Niche

- **[FuzzUEr](https://github.com/BreakingBoot/FuzzUEr)** ★19 — FuzzUEr / UEFUZZER — fuzz UEFI interfaces on EDK-2 (NDSS 2025).  
  tags: `paper-repro, lab-usable`  
  smoke: Needs EDK2/TSFFS-style setup; research.

- **[HBFA-FL](https://github.com/intel/HBFA-FL)** ★15 — HBFA-FL — host-based firmware analyzer lineage (public Intel path).  
  tags: `paper-repro, lab-usable`  
  smoke: Host-based; lab-usable with caveats.

- **[uefi_fuzzer](https://github.com/oscardagrach/uefi_fuzzer)** ★4 — UEFI fuzzer experiments  
  tags: `lab-usable`  
  smoke: Experimental

- **[smufuzz](https://github.com/wjqsec/smufuzz)** ★2 — SmuFuzz — deep SMM fuzzing in featured UEFI runtime (S&P 2026).  
  tags: `paper-repro`  
  smoke: Heavy deps (LibAFL/EDK2); research-only.
