# Agent behavior checks

These four fixture tasks adapt the scenarios added by mi-orchestrator v0.3.0 (commit 8235d7f). They test the consuming agent, not phrases in a SKILL.md.

1. Freeze the original and candidate skill files/commit hashes. Start a fresh agent for each version with the same model, tools and input-only `cases.json`. Copy each fixture to a disposable directory. Keep `rubric.md` and expected outcomes out of the worker context.
2. Load only relevant skills from that version. Let the worker act within fixture-only write scopes and retain actual commands, outputs, artifacts and final replies. The blocked-routing case is decision-only: no installation or real delegation.
3. An independent reviewer reads the traces and artifacts, then scores `rubric.md`, recording evidence per item and unassessed items honestly. Preserve safety and scope findings even if a numerical score is high.
4. Compare matched cases, including extra steps, questions, failures and unnecessary delegation. A single pair of runs is a smoke test; repeat independent runs before claiming reduced failures, latency or cost. Do not claim improvement from structural checks or matching prose.

These exercises are plugin-behavior tests, not scientific experiments. A scientific use of their sample data still requires the normal research_strict gates before scientific claims. No provider API, external service or optional numeric/plotting dependency is needed.
