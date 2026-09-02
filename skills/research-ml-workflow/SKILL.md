---
name: research-ml-workflow
description: Build, execute, validate, and communicate machine-learning research with separate data, modelling, validation, interpretation, and slide-preparation stages.
---

# Research ML Workflow

Use this skill when the user asks for machine-learning research, experiment execution, result validation, interpretation, figures, or slides.

Start from a written run contract: research question, target variable, sample unit, allowed data sources, success metrics, split strategy, compute budget, and final deliverable. Do not infer an unsupported causal claim from predictive performance.

## Recommended task graph

1. **Data auditor**: profile sources, sample counts, units, missingness, duplicates, leakage risks, and permitted transformations.
2. **Modeller**: implement a reproducible baseline and candidate models with fixed configuration files and seeds.
3. **Experiment runner**: execute only the approved configurations; retain commands, environment, logs, raw metrics, and generated figures.
4. **Validation reviewer**: independently check splits, leakage, fit scope, metric definitions, uncertainty, and reproducibility. Execution completion is not evidence of numerical validity.
5. **Interpreter**: compare verified results with the research question, state alternative explanations and limitations, and identify the next discriminating experiment.
6. **Presentation writer**: create figures and slides only from reviewed metrics and interpretations. Mark preliminary results and missing validation explicitly.

Run data auditing independently from literature or domain-context research. Do not start model comparison before the target and evaluation scheme are defined. Parallelise models only when they share a frozen dataset version and evaluation protocol.

## Required validation

- Confirm the split unit prevents information leakage; do not use random pixel splits when independent samples or regions are required.
- Fit preprocessing within each training fold only.
- Retain raw predictions or sufficient arrays to recompute reported metrics.
- Report variation across folds, seeds, or independent repeats where the design allows it.
- Separate predictive association from causal interpretation.
- Record any unavailable raw data or unexecuted calculation as a limitation, not a result.

Use `semantic_review_required` for research conclusions, statistical design, data leakage, and interpretation. Follow `orchestrate-work` for task manifests, structured results, review gates, and approval boundaries.
