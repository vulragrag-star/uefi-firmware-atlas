# Index-only / UNCERTAIN entries

Some rows are **bibliographic indexes**, not installable tools:

| `status` | Meaning |
|---|---|
| `INDEX` | Stable pointer (paper, dashboard, policy); not a build target |
| `UNCERTAIN` | Important in literature; public code/URL not confirmed |
| `LICENSE_BOUND` | Dataset exists but redistribution restricted |
| `GAP` | Explicit hole we are tracking |

Fields: `index_only: true` plus `status`. Rendered into `catalogs/` like other rows; smoke notes say do not claim lab success.
