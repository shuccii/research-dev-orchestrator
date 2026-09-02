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
