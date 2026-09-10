# EDK2 stack hierarchy (do not flatten)

This atlas keeps the **Tianocore EDK2 orbit** as one named `stack: edk2` with explicit `stack_role`s.
Closed-loop `closed_loop_stage` still answers *where in research/ops the artifact sits*;
`stack_role` answers *where it sits inside EDK2* so build tools never look like firmware parsers.

```text
edk2                          [core]           ← only root reference implementation
├── edk2-platforms            [platforms]
├── OvmfPkg → OVMF            [qemu_artifact]  ← built FROM edk2; distro ovmf packages = builds
├── edk2-libc                 [runtime_lib]
├── edk2-staging / edk2-non-osi [satellite]
├── build_tool layer
│   ├── edk2-pytool-library
│   ├── edk2-pytool-extensions   (Stuart / plugins; depends on library)
│   ├── edk2-basetools
│   ├── edk2-edkrepo (+ edk2-edkrepo-manifest)
│   └── tianocore/containers
└── edk2-test                 [test]           ← NOT CHIPSEC / runtime_assess
```

## Mixing rules
| Wrong | Right |
|---|---|
| Treat OVMF as a second “core” next to edk2 | `stack_role: qemu_artifact`, parent `tianocore_edk2` |
| List pytool-* beside UEFITool under “parse tools” | `stack_role: build_tool`; stage stays build/lab, not `parse` |
| Equate edk2-test with CHIPSEC | edk2-test = EDK2 SCT/host tests; CHIPSEC = `runtime_assess` outside this stack |
| Dump every `tianocore/*` repo in | Skip mirrors, deprecated BaseTools win32, review-sandbox, openssl fork, etc. |

See also `data/rejected.jsonl` for explicit anti-mix notes.
