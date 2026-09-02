---
name: orchestrate-work
description: Coordinate complex research, software, or job-search work with bounded parallel tasks, machine-readable evidence, independent review, and explicit approval boundaries.
---

# Orchestrate Work

Use this skill when a request has independent workstreams, a research-to-deliverable pipeline, or a meaningful review or approval boundary. Handle a simple question, one-file edit, or strictly sequential change directly.

## Choose the direct path first

For a small, mechanically verifiable operation with no dependencies, parallel work, semantic risk, or approval boundary, the lead performs and checks it directly. Do not create a manifest or result contract, read orchestration schemas, delegate a worker, or wait for a reviewer just to format a file or run an existing check. Report the checked artifact and finish. This path does not enter the structured integration workflow below.

Code changes and scientific or factual judgments are not mechanical operations merely because tests can run. Keep their semantic review gate, even when implementation is performed directly.

## Route the work

The lead owns the plan, final answer, validation rules, and integration. Delegate only bounded tasks with distinct outcomes and write scopes. Use at most three concurrent workers by default, and parallelize only when tasks have no dependency or write-scope conflict and coordination is likely to save time.

Give each worker its objective, inputs, permitted paths and tools, required artifacts and checks, stop condition, and output location. For code changes, use isolated worktrees or branches. A branch name alone is not isolation.

Treat delegation as started only after the spawn operation returns a concrete worker identity. Never wait without a known target, and never infer successful delegation or review from an attempted call. If spawning is unavailable or fails, attempt it only once. Continue safe implementation in the lead when useful, but record the distinct reviewer task as `blocked` with `blocked_reason: resource_unavailable`; do not attach that reason to a completed or needs-revision implementation result. Leave lead integration incomplete until an identifiable reviewer actually returns evidence.

Use a task manifest when a run has more than three tasks, delegated work, dependency ordering, parallel candidates, budgets, or approval-required operations. Read [the v0.2 contract](references/v0.2-contract.md) before creating or validating a manifest or result.

## Validate and integrate

Workers save structured results in the run directory. Validate a manifest before delegation, then validate each result against that same manifest. A completed result without a manifest is not integration-eligible.

Keep execution success separate from scientific, technical, or factual validity. Require independent semantic review for research conclusions, external facts, statistical design, data leakage, security-sensitive work, job claims, and implementation changes. A unit-test pass confirms the tested behavior; it does not establish that a code change preserves intent.

Give reviewers the run and task contracts, relevant diff, artifact and evidence indexes, and references needed for semantic judgment. Let them retrieve additional source material when required.

Integrate only results that pass the required checks and review. Report actual artifacts and checks, unresolved limitations, unavailable metrics, and approval-required next actions.

## Approval and budget boundaries

Classify operations as `read_only`, `reversible_write`, or `approval_required`. Treat submissions, messages, publication, deployment, spending, production-data changes, and material deletion as approval-required. A manifest is a preflight record; enforcement comes from the active Codex sandbox and approval controls.

Represent approval operations as tasks. User approval authorizes the operation but does not complete it; release dependent tasks only after the operation succeeds and its result is verified. Present independent ready approvals together when useful.

Do not substitute turn or tool counts for unavailable LLM-call counts. If a hard budget depends on an unobservable metric, stop with `blocked_reason: budget_unobservable`.
