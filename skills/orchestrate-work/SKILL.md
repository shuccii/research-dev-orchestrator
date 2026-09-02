---
name: orchestrate-work
description: Coordinate complex research, software, or job-search work by decomposing it into safe parallel tasks, capturing evidence, reviewing outputs, and integrating only verified results.
---

# Orchestrate Work

Use this skill for work that has two or more independent workstreams, requires a research-to-deliverable pipeline, or needs a durable review and approval boundary. Work directly for a simple question, single-file edit, or strictly sequential task.

## 1. Establish the run contract

Before delegation, state the requested outcome, artefacts, validation criteria, editable paths, and any external side effects. Create a run directory under the current project at `runs/<YYYY-MM-DD>-<short-slug>/`. Do not create it outside the project.

Classify every requested operation as one of:

- `read_only`: inspect, search, analyse, or draft.
- `reversible_write`: create a branch, draft, local file, or uncommitted change.
- `approval_required`: submit an application, send a message, publish, deploy, spend money, change production data, or delete material data.

Never perform an `approval_required` operation. Prepare a verified handoff describing the exact target, current state, and next click or command, then wait for explicit approval.

## 2. Decompose and assign

Use a central manager pattern: the lead agent owns the user-facing result, task plan, validation rules, and integration. Delegate a bounded task only when it has a distinct outcome, inputs, and write scope.

Delegate independent tasks in parallel only if all of the following are true:

1. Neither task depends on the other task's result.
2. Their write scopes do not overlap.
3. Each task can return an auditable result without access to another worker's hidden reasoning.
4. The expected gain exceeds the coordination cost.

For code changes, assign each implementation task an isolated Git worktree or branch. Do not let multiple workers edit the same file. Research and review workers should be read-only unless their deliverable explicitly requires a separate draft file.

Use at most three concurrent workers by default. Give every worker: objective, supplied inputs, permitted tools and paths, required artefacts, validation command or method, stop condition, and the result contract below.

## 3. Require an auditable result

Every worker must save `result.json` in its assigned run subdirectory and return a concise summary. Use the schema in `assets/task-result.schema.json`; validate it with `scripts/validate_task_result.py` before integration.

The result must distinguish:

- what completed from what merely was attempted;
- execution success from scientific, technical, or factual validity;
- direct evidence from inference;
- unresolved risks from accepted limitations.

If any required field is missing, evidence is absent, or validation fails, set the task to `needs_revision`; do not silently promote it to complete.

## 4. Review gate and integration

Assign a reviewer when work changes code, derives a research conclusion, uses external facts, or affects an application. The reviewer checks the deliverable against the run contract and may not approve its own implementation without a separate validation method.

Only integrate results after the review gate passes. The lead then records an `integration.md` containing: included artefacts, verification evidence, excluded or unresolved items, and any approval-required next action.

## 5. Report clearly

Lead with the delivered outcome. Name the artefacts, commands or checks actually run, material limitations, and any handoff awaiting the user's approval. Do not claim completion for a task that only executed without passing its validation criteria.
