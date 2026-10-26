# Recovery measurement — independent definition review

Status: DOING. Producer preserved review by
`/root/review_directory_references_v1`. No commit, implementation or adoption.

## Initial disposition — REVISE

The [twelve-input manifest](../../../../output/research/recovery-measurement-2026-10-08/review-inputs.json)
SHA256 remained `9cf7828b0b80a13b450749744b9a2444712a5c2c122de2ebce5de7cce849fab2`.
All twelve live/snapshot hashes and sizes matched initially and finally.
The preceding22,651 QA bytes were preserved; only QA-RECOVERY.unresolved_input
changed in the acceptance matrix. The reviewer made no file/runtime/provider changes.

1. RC-01: earliest plausible interruption maximizes recovery duration but minimizes
   data-loss exposure. The original combined uncertainty rule could falsely pass
   a possible25hour exposure against24hours. Use separate conservative bounds;
   recovery-point validity and completeness cannot be assumed.
2. RC-02: the latest historical boundary pass does not establish complete recovery
   after another boundary regresses. Require current valid passing evidence across
   every required affected boundary at completion, retaining the original start.

Other target/risk, privacy, credential, ephemeral-data and uncertain-operation
safeguards were coherent within scope. The proposal distinguishes its accounting
from NIST guidance and authorizes no backup/restore activity, hosting or retention.

## Correction 1 — superseding bounded PASS

Producer changes separate the worst-case RPO/RTO bounds and require current valid
coverage at completion. Known regression/expiry/incompatible state invalidates
older passes. Two arithmetic examples explain the changes without claiming a
real drill. Original REVISE and snapshots remain preserved. Exact recovery-profile/storage/provider/privacy bindings, actual drill evidence
and integrated founder acceptance remain required.

The independent reviewer confirms RC-01 and RC-02 closed with no consequential
remaining finding in this definition scope. All twelve live/snapshot hashes and
sizes matched initially and finally at the [correction-1 manifest](../../../../output/research/recovery-measurement-2026-10-08/correction-1/review-inputs.json),
SHA256 `9f075cd135d0cbd3fc975a0faeccf5034dc0aef35af76c160043f5743e37d47f`.
Corrected QA SHA256: `1469d2cd8c0c32c1ff10103dcc0ee2b73bbf52d4de9d1490c7bf77e521fcba74`.
Only the two intended replacements changed; the matrix and other eleven inputs
remain unchanged. The initial manifest and pre-correction QA remain preserved.
This PASS establishes definition coherence, not measured recovery, monitoring,
provider/restore activity, policy adoption or Phase 1 acceptance. No drill was run.
