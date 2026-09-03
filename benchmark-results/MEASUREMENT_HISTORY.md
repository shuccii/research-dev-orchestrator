# Measurement history

These are diagnostic records, not a successful v0.2 release claim. The installed plugin remains v0.1.0.

## Preliminary baseline

`baseline/metrics.jsonl` contains one full six-case v0.1 pilot and one earlier formatting smoke run. This is not a three-repetition baseline. The complete pilot passed the then-current artifact checks; independent semantic adjudication was not completed. Only a fresh paired session can provide final release measurements.

## Interrupted and rejected sessions

- `primary-20260902` and `primary-20260902b`: manually interrupted before any complete measured row, while correcting benchmark integrity issues.
- `primary-20260902c`: stopped after the Codex account usage limit caused three consecutive failed attempts for format pair 2. It has only two valid pairs and is insufficient measurement. No reset credit was redeemed.
- `primary-20260903`: format completed three valid pairs. Ratios were 0.3861, 1.5259, and 4.9013, giving a median of 1.5259, above the task-level limit of 1.15. Remaining cases were stopped because this candidate could not pass the speed gate. This is not a full six-case quality evaluation.

The 176.28-second v0.2 formatting run created orchestration records and issued six collaboration wait calls with empty receiver lists. Worker/reviewer activity was claimed in messages, but actual worker spawn was not established by the retained events. The earlier event adapter only recognized `collab_agent_tool_call` and missed the observed `collab_tool_call` variant. Its zero subagent-event count must not be interpreted as proof that no collaboration occurred.

## Corrective changes

The skill now explicitly completes small mechanical tasks in the lead without manifest, result-contract, worker, or reviewer overhead. The event adapter recognizes both observed collaboration event variants and reports observed spawn calls separately, while total subagent and reviewer counts remain unavailable. Formatting now has a host-observed zero-collaboration critical check. These changes require a new frozen evaluation session; earlier sessions are retained unchanged and cannot be promoted to release evidence.

## Post-correction focused diagnostic

`diagnostic-format-20260903` ran three fresh paired executions against the corrected direct path. All critical and noncritical items passed, both versions had zero observed collaboration and spawn calls, and the paired active-time ratios had a median of 0.2589. This scoped result validates the regression fix but cannot unlock holdout or release; a new full six-case primary comparison is still required.

## First post-correction full attempt

`primary-postfix-20260903` reproduced the formatting improvement, then produced three consecutive 300-second timeouts for the v0.2 independent-module run. The outputs passed the artifact-only checks but did not yield a completed turn, so all three rows are invalid measurements and the session is blocked as `external_dependency`. Retained events show repeated waits without a concrete receiver plus prose assertions of worker/reviewer activity. The candidate therefore failed evidence integrity as well as measurement sufficiency.

The subsequent correction requires a concrete spawned identity before waiting, allows one failed spawn attempt before direct fallback, leaves independent review explicitly outstanding, records independent write scopes as a critical manifest criterion, and makes unbound waits a critical failure. Another frozen session is required to test this behavior.

`diagnostic-independent-20260903` did not test that correction: the Codex usage limit interrupted the initial v0.1 run and both replacements, so it is retained only as another `external_dependency` record. The limit later reset without redeeming the available reset credit.

Before another attempt, the conformance gate was tightened further: v0.2 needs integration-eligible semantic-review results for both implementation scopes, with reviewer identity bound to an agent identifier observed by the host. A fast direct fallback with review still outstanding cannot pass the release rubric.
