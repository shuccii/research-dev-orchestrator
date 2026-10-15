---
name: root-cause-debugging
description: Diagnose execution errors, failing tests, stalled work or unexpected numerical results before changing code, data or configuration. Use for NaN/inf, unstable fits, suspicious accuracy, unit mismatches and notebook execution problems.
---

# Root Cause Debugging

Adapted for Codex from mi-orchestrator v0.3.0 (`8235d7f`), which draws on Superpowers systematic-debugging. Use the available tools and the target project's constraints; no Superpowers installation is required.

## Reproduce before repairing

1. Read the full error and warnings. Record the command, input version, interpreter/environment, seed and notebook execution order needed to reproduce it. Reproduce in a disposable output area when possible; preserve the original data.
2. Inspect recent changes and compare a working example. Across a pipeline, inspect shape, columns, missing/non-finite counts, units and ranges at the boundaries (read → transform → fit → evaluate → plot) to locate the first invalid stage.
3. State one hypothesis and its evidence. Run the smallest probe that distinguishes it from an alternative; change one factor at a time. An unsuccessful probe is evidence to revise the hypothesis, not permission to accumulate speculative fixes.
4. Before the repair, retain a minimal reproducer that fails for the observed reason. Make one cause-directed repair, rerun the same check, then the relevant surrounding checks. Verify the original symptom, not just a successful exit code.

When reproduction is unavailable, record what is missing and gather evidence. Do not present a guessed change as a verified fix.

## Numerical and research failures

| Observation | First checks |
| --- | --- |
| NaN/inf or unstable matrices | Source row IDs, missingness, log/division domains, units, conditioning and precision |
| Unexpectedly good accuracy | Duplicates/groups across splits, preprocessing fit scope, target leakage and test-driven selection |
| Large seed-to-seed changes | Sample size, split balance, optimizer convergence and evaluation variance |
| Report differs from saved values | Artifact version, cell order, stale output, units and rounding |
| Missing module or runtime library | Intended interpreter, declared dependencies, lockfile and platform/runtime compatibility |

Do not silently drop invalid rows, replace NaN with zero, suppress warnings or choose a favorable seed to make a result look valid. If exclusions or a changed method are justified, record row IDs/counts, the rule, rationale and effect; resolve consequential choices under the applicable research contract before making scientific claims. A diagnostic fit remains provisional.

For scientific work, keep `research_strict`: a failed validity gate invalidates dependent outputs and claims. Debugging success does not restore scientific validity; rerun the affected checks and independent review. Do not weaken the research question or acceptance criteria to make a repair pass.

## Bound the repair loop

After three ineffective repair attempts, stop the current repair loop, preserve evidence and reconsider data definitions, model assumptions, task boundaries or architecture with the lead. A smaller manifest retry/compute budget takes precedence. Record attempted hypotheses and the decision needed before continuing. This is a worker handoff rule, not a declaration that the entire user's goal is blocked.

For a stalled agent or process, inspect its actual returned handle and state first. An observation timeout is not a terminal failure. Continue observing a live task rather than launching a duplicate. After confirmed termination or a missing handle, reduce/split the task or repair the prerequisite before retrying; repeated confirmed failures call for a minimal reproducer and a revised plan.

## Evidence to return

Include the failing reproducer/output, hypothesis, discriminating probe, repair diff, successful and failed checks, and remaining uncertainty. Record unexecuted checks as not run.

For a numerical handoff, first reopen each saved output with a readback command, then fill this evidence table from its output before composing the report. This includes diagnostic counts and null/blocked results, not just fitted metrics. Printing an in-memory object while writing it does not inspect the saved artifact.

| Saved artifact | Key/row | Executed readback command and observed value | Validity scope |
| --- | --- | --- | --- |
| Path of the actual output | Reported key or source row | Command that reopens the file, plus its returned value | Diagnostic, provisional or independently validated |

For JSON, a small Python command using `json.loads(Path(output_path).read_text())` and printing the reported keys is sufficient. Retain the actual command/output in the run evidence; this table is part of the readable handoff, not a new field in the JSON result contract.

When part of an orchestrated run, use the existing v0.3 result schema and the [execution-control status mapping](../orchestrate-work/references/execution-control.md); do not add new result enum values or infer independent review from a worker's own checks.
