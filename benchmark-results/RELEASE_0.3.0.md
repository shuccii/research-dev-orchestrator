# Research Dev Orchestrator 0.3.0

Version 0.3.0 adds a strict, auditable research assurance profile while preserving the lightweight standard path for ordinary software and job-search work.

## Research assurance

- Research, analysis, machine learning, statistics, scientific interpretation, optimization, and research reporting route to `research_strict`.
- Stable sample/group split assignments and per-transform fit scopes make common leakage mechanisms machine-checkable.
- Resampling and synthetic parents must remain within training data; final test data cannot select labels, K, features, thresholds, models, or hyperparameters.
- Data-derived targets record their exact fit samples. Nominal class numbers cannot be treated as ordinal optimization distances.
- Repeated evaluation, distinct seeds, uncertainty, baselines, raw predictions, data-quality checks, and reproduction evidence are required for predictive completion.
- Optimization and prospective claims require feasibility, applicability-domain, training-overlap, prior-art, and experimental-validation evidence.
- Failed validity gates propagate through the declared product dependency graph and invalidate dependent metrics, interpretations, optimization outputs, figures, and claims.
- Completion requires claim-level evidence and full-scope independent review with distinct observed worker and reviewer identities.

## Verification

`python3 scripts/run_checks.py` is the deterministic verification command. The release includes strict research negative fixtures and a public behavioral benchmark covering leakage, circular targets, selection bias, invalid optimization, missing uncertainty, consequential imputation, physical impossibility, category duplication, extrapolation, retrospective rediscovery, and downstream invalidity.

The validators demonstrate compliance with declared contracts and retained evidence; they do not claim to prove scientific truth. Domain-semantic omissions remain subject to independent review, and unavailable reviewer identity prevents strict research completion.
