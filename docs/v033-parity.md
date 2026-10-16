# v0.3.3 workflow parity candidate (0.5.2)

Baseline: `1b0c604`. This is a Codex adaptation; Claude-specific APIs and private policy documents are excluded. JSON schemas, validators and verification gates are unchanged.

| Requirement IDs | Disposition | Evidence |
| --- | --- | --- |
| A1, A2, A3 | Already supported | root-cause-debugging: reproduce, single hypothesis/repair, no symptom masking, three-attempt stop |
| A4, A5 | Implemented together | orchestrate-work: inline handoff instructions, actual stage outputs in one diagnostic invocation; root-cause reference agrees |
| B1, B2, B3, B4, B5, B6, B7 | Already supported | execution-control: two-stage review, scope before quality, independent judgment, severity, bounded repairs, retained minor findings |
| C1, C2, C3 | Supported through native contract | execution-control: native status mapping and changed-prerequisite retry requirement; no new status values |
| D1, D2, D3, D4 | Already supported | execution-control: fresh evidence, artifact inspection, criterion matching and explicit uncertainty |
| E1 | Completed partial support | inline procedure/check fields in work/compute handoffs; reviewers receive two-stage/check instructions; lead references stay selective |
| E2, E3 | Implemented / completed partial support | batch independent reads/checks, inspect each result, keep adaptive steps sequential; focused reads and decisive excerpts with full logs |
| E4 | Completed partial support | full result/report files, compact return, selective narrative read; structured validation and final artifact inspection remain mandatory |
| E5, E6 | Implemented | existing goal/summary/evidence strings carry classification/paths; at most three independent low cards; per-card results/checks; clean review stages each one line |
| E7 | Implemented as a bundle | A4 + A5 + E2 shipped together; E1 does not stand alone |
| F1 | Implemented / existing suite retained | additional guidance tests fail on baseline and pass on candidate; run_checks.py includes all contract tests |
| F2, F3, F4, F5 | Behavior comparison | scenarios 06 and 07, isolated executions and separate blind substance scoring; measurements and adoption decision below |

Platform exclusions: Claude command/agent APIs, frontmatter model selection and private organizational policy text. Codex uses actual returned identities and native v0.3 statuses. Independent batching uses tool orchestration rather than shell chains; this preserves individual failures and observation-dependent decisions.

## Verification

- Guidance regression: 4 tests, 21 failing assertions on baseline, all 4 passing on candidate. These are wording guards, not behavioral proof.
- Full suite: 99 tests passed; frozen-install check passed. Assets and scripts unchanged from baseline.
- Independent implementation review: no blocking finding in the reviewed workflow scope. Final evidence and behavior outcomes are recorded below.

## Behavior comparison

Primary comparison: matched scenarios 06 and 07, one execution per version/scenario (four total). The first execution is serial; the remaining three are concurrent. All runs receive the same full-load document scope, so selective-loading savings and multi-card review savings are unmeasured. Substance scoring is performed by a separate fresh agent with version names/order/cost masked. Raw records are retained outside the distributable plugin.

Before receiving the candidate measurements, define "clearly reduced" for this small comparison as at least 10% less combined input+output tokens or summed execution wall time, with no lower substance score on either scenario. Cached input is part of input, not added twice. Parallel elapsed makespan is not per-run execution time. This is a local adoption gate, not evidence of a general speed/capability advantage; one matched pair per scenario cannot estimate run-to-run variance.

Execution measurements and independent anonymous substance scoring are complete. Scores were 8/8 on each scenario for both versions (16/16 → 16/16 total). Adoption fails the cost reduction gate.


### Observed cost (full-load, one pair per scenario)

| Scenario | Total tokens before → candidate | Seconds before → candidate | Tool calls before → candidate |
| --- | --- | --- | --- |
| 06 | 176,560 → 206,562 | 93.524 → 88.836 | 6 → 7 |
| 07 | 177,261 → 136,008 | 57.846 → 65.390 | 5 → 6 |
| Total | 353,821 → 342,570 (−3.18%) | 151.370 → 154.226 (+1.89%) | 11 → 13 |

The preregistered 10% reduction gate was not met. The candidate is retained on a separate branch and is **not adopted into main or installed**. The two earlier unpushed commits remain untouched. A4/A5/E2 and the other missing requirements are implemented in this reviewable candidate; effective cost reduction remains unproven. Lower uncached input alone (−31.08%) does not override the primary total-token criterion.

Executions used codex-cli 0.163.0, no model/effort override, fresh isolated fixture copies, and cumulative actual turn.completed usage. Concrete backend model/effort names were not exposed by that event stream; bundled system skills were generated automatically. Input includes cached input; cached tokens are not counted twice. No claim of matched backend routing or variance estimation is made. First execution was serial, the other three concurrent, so scheduling affects time. No monetary cost is inferred.

Selective loading (E1), file-handoff savings (E4), low-card multi-review savings (E5) and clean-review brevity savings (E6) were not isolated by these two worker scenarios. More repeated, realistic workflow comparisons would be needed before adopting on performance grounds. No extra samples were added after seeing a failed gate.


### Independent anonymous substance scores

| Scenario | Baseline | Candidate |
| --- | --- | --- |
| 06: code cause behind apparent environment failure | 8/8 | 8/8 |
| 07: stop after three failed repairs and inspect premise | 8/8 | 8/8 |
| Total | 16/16 | 16/16 |

The scorer was separate from implementation and execution and read only masked transcripts/artifacts in shuffled anonymous labels. It did not read version mapping or cost. Each item retains a pass/fail assessment and concrete evidence locators. Report format/status syntax was excluded. The earlier three failed repairs in scenario 07 are supplied history, not independently reproduced trials. No lost substance item was observed, so there is no loss attribution to a specific change. This does not demonstrate a substance improvement.

Disposition: retain a tested **candidate**, not an adopted performance upgrade. Next useful evaluation is a bounded selective-reference/file-handoff/multi-card workflow comparison with repeated matched runs and known model settings; this was not run to keep usage bounded.
