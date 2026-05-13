# Run configuration

`smoke.yaml` caps stochastic budgets for **local smoke** and CI-friendly notebooks. Full archival runs override via env or a `runs/full.yaml` (add when ready) and must log seeds.

`ci_notebooks.yaml` lists notebooks executed headlessly in GitHub Actions after `pytest` (see `scripts/ci_execute_smoke_nb.py`).

On **CI failure**, GitHub Actions uploads `notebooks/`, `runs/`, and `scripts/ci_execute_smoke_nb.py` as a downloadable artifact for debugging.

Optional rows may set `enabled: false` so future charter notebooks stay listed without running in CI until they are stable headless.

**`notebooks/CHARTER_SHELL.ipynb`** (minimal preamble + run card) runs in CI **after** the three `SMOKE_*.ipynb` notebooks (see [`ci_notebooks.yaml`](ci_notebooks.yaml) for order) and **before** `CHARTER_EXTENDED_LIGHT`, **`CHARTER_LAYER_A_MULTIDRAW_SMOKE`**, and the domain stream charter—extend it as the charter grows.

**`notebooks/CHARTER_EXTENDED_LIGHT.ipynb`** (synthetic mean + run card) runs next as a light Layer A–shaped check.

**`notebooks/CHARTER_LAYER_A_MULTIDRAW_SMOKE.ipynb`** — synthetic two-sample pooled-label **permutation** null (Hub-free), capped by `runs/smoke.yaml`; runs **before** the domain stream charter row in [`ci_notebooks.yaml`](ci_notebooks.yaml).

**`notebooks/CHARTER_MOBILITY_NEWS_PROXY_STREAM_SMOKE.ipynb`** runs next: small streaming slice of `fancyzhx/ag_news` + y-shuffle null + run card (NLP proxy until OD data pins).

**`FUTURE_CHARTER_SLOT.ipynb`** is listed disabled with **no** committed file: replace that row with a real path when you add a heavier charter notebook, verify headless execution locally, then set `enabled: true`.

## Next validation (honest)

- Treat progress on the **domain data** axis as unsubstantiated until a domain-native pin (for example licensed GTFS/static route graphs, probe counts, or comparable mobility tables) ships with a passing domain stream smoke in CI—not the news proxy alone.
- Flip **`FUTURE_CHARTER_SLOT`** to `enabled: true` only after a real notebook path exists and runs headless locally (and in CI when ready).
- Meta promotion should carry an archived run card plus **commit SHA** per the meta [`PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research/blob/main/docs/PROMOTION_CHECKLIST.md), not narrative-only claims.
- **`CHARTER_LAYER_A_MULTIDRAW_SMOKE`** and the domain stream charter are **sanity** checks for wiring and null/UI patterns—they are not identification of real-world mobility effects.

## Promotion audit (canonical numbers)

Template: [`runs/promotion_audit.example.yaml`](promotion_audit.example.yaml) — copy the `example_entry` shape when recording a promotion; fill **`commit_sha`** (`github.sha` in Actions, `git rev-parse HEAD` locally) and optional **`ci_run_url`**. Full gate: [meta `PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research/blob/main/docs/PROMOTION_CHECKLIST.md).
