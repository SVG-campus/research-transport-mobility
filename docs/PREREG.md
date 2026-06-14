# Preregistration — `research-transport-mobility`
 
**Pillar:** `research-transport-mobility`  
**Title:** Transit Frequency and Delay Causality (ECT-2026-004)
**Date:** 2026-06-14  
**ORCID Identifier:** `0009-0004-9601-5617`

## Charter (one paragraph)

Model movement, logistics, and emissions trade-offs with pinned streams and preregistered KPIs. This study investigates the causal flow between urban transit vehicle Headway and total Passenger Delay, validating that OCCA's Peter-Clark constraint-based DAG recovery correctly captures that increased headway causes increased delay under temporal priority rules while filtering out passenger flow volume confounders.

## Primary question (Layer A)

- **Question:** Does scheduled transit vehicle headway (headway_minutes) cause a change in average passenger delay (delay_minutes)?
- **Expected DAG:** `headway_minutes -> delay_minutes`
- **Primary metric:** Directed edges count and information coefficient.
- **Direction / threshold:** $\alpha = 0.05$ for PC algorithm. The discovered headway-to-delay edge must be directed from headway to delay and have a positive path coefficient. The absolute correlation/information coefficient must exceed the phase-shuffled Spectral MC null ($p < 0.05$).

## Null / negative controls

- **Null model:** Phase-shuffled Spectral Monte Carlo (FFT surrogate paths).
- **Caps:** Capped at $N = 25$ runs for local smokes (`runs/smoke.yaml`); $N = 1000$ for full remote promotion validation with run ID `charter_transport_mobility_headway_run_01`.

## Truth scope & ethics

- **Scope:** Observational transit and network datasets under the **ECT-2026** standard.
- **Data rights:** Utilizes GTFS and transit schedule statistics as a proxy.

## Promotion rules

Numbers enter `BEST_ANSWERS_OVERVIEW` (meta) only after `methodology_preamble.assert_run_card` passes in the same environment that produced the artifact. Follow the meta checklist [PROMOTION_CHECKLIST.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) before editing canonical summaries.
