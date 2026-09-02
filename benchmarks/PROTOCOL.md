# Public evaluation protocol

The six primary cases in `cases.py` use only synthetic or frozen public fixtures. The two holdout cases are excluded from tuning and run only after the primary gate passes. Files named `benchmarks/private.local.*` are optional local regressions and are never part of the public release claim.

Run deterministic checks with `python3 scripts/run_checks.py`. Create preliminary v0.1 measurements with `python3 benchmarks/harness.py pilot --output baseline`. For a release comparison, use a fresh directory and run `python3 benchmarks/harness.py compare --output benchmark-results/<session>`. Each case gets three paired executions, with version order alternating. The harness invokes a fresh ephemeral Codex process, injects the selected frozen skill text, records host-side time and CLI events, and never imports or executes agent-generated code.

Generate `adjudications.template.jsonl` with the `adjudication-template` mode. An independent reviewer must inspect retained workspaces and replace every placeholder with a run-bound decision. `report` rejects missing, duplicate, cross-session, or malformed adjudications. Raw workspaces and events are local-only and gitignored.

Release requires all v0.2 critical checks, no noncritical-score regression against v0.1, accepted semantic adjudication for both versions, an overall median active-time ratio at most 0.90, and every case median at most 1.15. Infrastructure failures may be retried twice; fewer than three valid pairs is insufficient measurement. Holdout is then run once and independently reviewed. Any quality failure, speed failure, or insufficient measurement leaves v0.1.0 installed.

`active_wall_clock` currently equals child-process elapsed time because the noninteractive harness has no human approval channel; `approval_wait` is therefore zero with an explicit basis. LLM calls, reviewer count, subagent count, observed model identity, and cost remain null when the CLI does not expose them. They are never inferred from turn or tool counts.
