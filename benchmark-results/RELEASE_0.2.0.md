# Research Dev Orchestrator 0.2.0 release decision

Released by explicit user decision with one accepted environment limitation: `codex exec --ephemeral --json` in Codex CLI 0.152.1 did not expose a verifiable spawn/reviewer identity. The v0.2 contract remains fail-closed: when no identifiable independent reviewer is available, semantic tasks stay unreviewed and integration is incomplete rather than being falsely marked complete.

The deterministic contract, manifest, approval, telemetry, benchmark, and security checks passed. Formatting direct-path performance passed its three-pair diagnostic. The incomplete full public benchmark and independent-review limitation remain documented in `V0.2_EXPERIMENTAL_REPORT.md`; this release does not relabel those measurements as passing.

Operational use in the Codex app may use app-native subagents. For independently reviewed completion, preserve the returned reviewer identity in result records. When using ephemeral CLI sessions without observable identities, treat the reviewer task as blocked with `resource_unavailable`.
