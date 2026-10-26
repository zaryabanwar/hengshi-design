# Monthly availability measurement — independent definition review

Status: DOING. Producer preserved the independent review from
`/root/review_directory_references_v1`. No commit, implementation or adoption.

## Initial disposition — REVISE

The initial thirteen-input manifest is
[review-inputs.json](../../../../output/research/availability-measurement-2026-10-08/review-inputs.json),
SHA256 `d76774868befd468271718ae10642a200c46a041c3bd05db692a171864779415`.
All thirteen snapshot/live sizes and hashes matched initially and finally.
The exact QA pre-edit prefix was retained; only the QA-PERFORMANCE row's
`unresolved_input` changed in the acceptance matrix.

1. AV-01: the original all-due-checks predicate could count an empty/no-traffic
   observation bin as good. Require affirmative nonempty coverage; absent coverage
   is unknown, while an observed service failure still takes precedence as bad.
2. AV-02: the original API row covered only public reads and private entry,
   narrowing NFR-004's separate API target. Include applicable catalogue operation
   families, including legitimate follow-up actions; unmeasured scope stays unknown.

The reviewer otherwise found four separate targets, G/B/U accounting,
monthly formulas/exclusions and privacy/authority restrictions coherent.
The 43.2-bin allowance/44-bin failure example is correct. Google SRE supports
user-outcome measurement and signal limitations, not Hengshi's specific bin policy.
No runtime/provider probe or file edit occurred in this initial review.

## Correction 1 — superseding bounded PASS

The API row now maps applicable catalogue operations, including follow-up actions,
and keeps unmeasured families unknown. Good bins explicitly require affirmative,
nonempty coverage; zero due checks/no traffic without sufficient approved evidence,
missing operation families and carry-forward success cannot certify them. Profile
revisions are prospective and cannot reset elapsed accounting. The independent
reviewer confirms AV-01 and AV-02 closed with no consequential remaining finding
in this definition scope. The initial REVISE is preserved.

Exact privacy/measurement/alert bindings, deployment choice, runtime evidence,
integrated founder acceptance remain required. No
production monitoring, data collection, service activation or public SLA follows.

The [correction-1 thirteen-input manifest](../../../../output/research/availability-measurement-2026-10-08/correction-1/review-inputs.json)
SHA256 is `713058b8f1815556bf402cd6879bae7ff04a6208225d34c14f820e114252ae37`.
All thirteen live/snapshot sizes and hashes matched initially/finally. The
pre-correction QA file matches the initial reviewed QA hash. Only the two specified
QA replacements changed; the matrix and other twelve inputs are unchanged.
Reviewed QA SHA256: `01bbaa92a3af4efc77717f7550a0c1015aadb9365deea7c1b22e8683253355a6`.

This PASS establishes bounded definition coherence only. It does not measure
availability, accept the sampling policy, prove concrete observation/admission
bindings or authorize monitoring, telemetry, provider/hosting activity, release,
full Phase 1 acceptance or runtime changes. No product tests were added for prose.

Receipt-status reconciliation after the separate visual review removes only the
stale pending-re-review phrase. The original and correction-1 contract snapshots
and the visual review input receipt remain preserved; no verdict is expanded to
new source bytes or runtime evidence.
