# 002 — Behavior evidence, monitoring and recovery — v1

Status: DOING. [Proposed feature specification](spec.md) exists; no accepted plan,
executable tasks, running monitor or product test evidence is created by it.

The specification binds required behavior boundaries to the canonical QA matrix,
preserves approved numerical targets and distinguishes real integration/browser
evidence from artifact guards, schema fixtures and mocks. Its [independent review](reviews/qa-feature-v1-2026-10-04.md)
is REVISE: the dated addendum supersedes the original PASS because FQA-N06 counts
browser families instead of accepted release coverage. The exact one-word repair
is prepared; applying and re-reviewing it awaits a founder exception to the
exhausted two-cycle limit. Exact measurement/SLI/retention/provider contracts and
approved isolated test scope remain inputs. Do not implement this feature until
the feature artifacts and complete Phase 1 package have their required approvals.

Use the proposed [QA/recovery definition](../../docs/phase-1-architecture/contracts/QA_RECOVERY.md)
and [acceptance matrix](../../docs/phase-1-architecture/contracts/acceptance-matrix.csv)
as product-level inputs. They preserve accepted load, monthly availability,
performance and recovery targets; TODO rows are required future evidence, not
executed test results. The bounded feature must refine these contracts rather
than duplicate or downgrade their constraints.
