# defend_harden

_20 entries_

- **[u-root](https://github.com/u-root/u-root)** ★3071 — Go userland for LinuxBoot-style boot.  
  tags: `lab-usable, reference-impl`  
  smoke: Build on VM.

- **[sbctl](https://github.com/Foxboron/sbctl)** ★2256 — User-friendly Secure Boot key manager  
  tags: `daily-ops, lab-usable`  
  smoke: Pairs with shim/systemd-boot

- **[lanzaboote](https://github.com/nix-community/lanzaboote)** ★1837 — Secure Boot & Measured Boot for NixOS (uki/stub)  
  tags: `daily-ops, lab-usable, reference-impl`  
  smoke: UKI/systemd-boot

- **[heads](https://github.com/linuxboot/heads)** ★1590 — Secure/measured coreboot+LinuxBoot firmware distribution  
  tags: `hw-required, lab-usable, reference-impl`  
  smoke: Board-specific; HW required

- **[shim](https://github.com/rhboot/shim)** ★1103 — First-stage UEFI bootloader for Secure Boot (distro signed)  
  tags: `reference-impl, daily-ops`  
  smoke: Distro Secure Boot root

- **[linuxboot](https://github.com/linuxboot/linuxboot)** ★955 — Linux as firmware (replace DXE with Linux/u-root)  
  tags: `reference-impl, lab-usable`  
  smoke: Research & production niches

- **[dropWPBT](https://github.com/Jamesits/dropWPBT)** ★447 — Disable/remove Windows Platform Binary Table abuse  
  tags: `lab-usable, daily-ops`  
  smoke: Defense

- **[mortar](https://github.com/noahbliss/mortar)** ★277 — Secure Boot automation frameworks  
  tags: `lab-usable`  
  smoke: Ops

- **[Mosby](https://github.com/pbatard/Mosby)** ★268 — Secure Boot enrollment helper (Mosby)  
  tags: `lab-usable`  
  smoke: Secure Boot

- **[sbupdate](https://github.com/andreyv/sbupdate)** ★223 — Sign and manage Secure Boot kernels/uki  
  tags: `daily-ops`  
  smoke: Ops; ARCHIVED

- **[arch-secure-boot](https://github.com/max-baz/arch-secure-boot)** ★146 — UEFI Secure Boot for Arch Linux + btrfs snapshot recovery  
  tags: `lab-usable`  
  smoke: Metadata-only; smoke not run in this crawl

- **[efibootguard](https://github.com/siemens/efibootguard)** ★133 — Simple UEFI bootloader focused on robustness  
  tags: `reference-impl`  
  smoke: Bootloader

- **[pesign](https://github.com/rhboot/pesign)** ★126 — Tool for signing PE/COFF binaries for Secure Boot  
  tags: `daily-ops, lab-usable`  
  smoke: Secure Boot signing

- **[bootguard](https://github.com/flothrone/bootguard)** ★120 — Intel BootGuard related research/tools  
  tags: `lab-usable, hw-required`  
  smoke: Platform root of trust

- **[fwupd-efi](https://github.com/fwupd/fwupd-efi)** ★65 — EFI binary helpers for fwupd capsule updates  
  tags: `reference-impl`  
  smoke: Pairs with fwupd

- **[meta-secure-core](https://github.com/Wind-River/meta-secure-core)** ★38 — Yocto meta layer for secure boot/core  
  tags: `reference-impl`  
  smoke: Borderline embedded but SB relevant

- **[UEFI-SecureBoot-SignTool](https://github.com/aneesh-neelam/UEFI-SecureBoot-SignTool)** ★31 — UEFI Secure Boot signing tool  
  tags: `lab-usable`  
  smoke: Signing

- **[secure_boot_manager](https://github.com/corthon/secure_boot_manager)** ★5 — Secure Boot management utility  
  tags: `lab-usable`  
  smoke: Ops

- **[GRUB](https://git.savannah.gnu.org/git/grub.git)** ★? — GNU GRUB2 OS bootloader on Secure Boot path (savannah git)  
  tags: `paper-repro, reference-impl`  
  smoke: Type-2 bootloader; Secure Boot / BootHole relevance

- **[rustBoot](https://github.com/nihalpasham/rustBoot)** ★? — Pure-Rust secure bootloader cited in SoK github list  
  tags: `paper-repro, reference-impl`  
  smoke: 
