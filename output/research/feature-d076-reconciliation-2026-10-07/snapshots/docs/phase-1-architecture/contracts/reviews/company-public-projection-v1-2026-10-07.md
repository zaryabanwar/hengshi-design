# Independent company public-projection review — v1

Date: 2026-10-07. Status: DOING; uncommitted, commits remain deferred.
Independent reviewer: `/root/review_visitor_lifetime_controls_current`.
Verdict: **bounded PASS for the D-076 company public-projection definition and schema seam**.
Material findings: none established. No legal clearance, runtime or founder acceptance.
This is separate from the visitor-lifetime review. The frozen packet's BLOCKED entry preserves earlier unavailable capability evidence; this review completed without that failure.

## Exact inspected inputs

The [13-input manifest](../../../../output/research/company-public-projection-2026-10-07/review-inputs.json) has SHA-256
`153c02c8e11d42ee383f1f8f2b7cad2eefb460075ed7e00f5fb6df4f8d03b3c4`.
All 13 frozen snapshot hashes and byte counts matched, including final verification.
Evidence below uses the manifest's snapshots, not moving current-source authority.
Later receipt, reference, manifest or state edits are outside the inspected bytes.

## Returned disposition

- Frozen [company-facts.schema.json](../../../../output/research/company-public-projection-2026-10-07/review-inputs/docs/phase-1-architecture/contracts/company-facts.schema.json):6–38 retains private address, opaque string identifiers, month validity and purpose-labelled contacts. Removing only the added definition at :41–52 reproduces the earlier private-schema SHA-256 `4c3162f19483563b88c1ef6beed4055a7acb9c608a947b0707d9aaa39e9f0695`, recorded at frozen [company-facts-shape-2026-10-04.md](../../../../output/research/company-public-projection-2026-10-07/review-inputs/docs/phase-1-architecture/contracts/reviews/company-facts-shape-2026-10-04.md):54–57. This is artifact-integrity evidence, not persistence/source-fidelity proof.
- The same schema snapshot:41–51 requires explicit `#/$defs/public_projection` validation and allows only schema version, legal name, registration jurisdiction and closed purpose-labelled contacts. Registration/address/validity and workflow fields are excluded. Its closure matches [JSON Schema additional-properties guidance](https://json-schema.org/understanding-json-schema/reference/object#additionalproperties); closure does not establish content eligibility.
- Frozen [PUBLICATION_CONTRACT.md](../../../../output/research/company-public-projection-2026-10-07/review-inputs/docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md):936–951 prohibits whole-private-object serialization and disguising excluded facts within permitted strings, copy, annotations, embedded JSON, media metadata or AI passages. Allowed values retain verification, eligibility, resource and safe-output requirements.
- The same publication snapshot:961–968 requires projection before public derivative generation or AI extraction, with every derivative consuming the same immutable eligible projection/current publication identity. Unknown projection or eligibility holds the candidate. Later inclusion requires separate explicit disclosure approval, reviewed representation and fresh candidate review; an admin/client flag cannot enable it.
- The same publication snapshot:953–959 and frozen [06-entity-and-public-contact.md](../../../../output/research/company-public-projection-2026-10-07/review-inputs/docs/software-definition/06-entity-and-public-contact.md):117–131,147–170 separate Contact/privacy/security facts from ownership, delivery, monitoring and operational claims. Dedicated-alias owners remain undecided. Mandatory operator/contact notice assessment remains required; the projection does not automatically expose the supplied address or grant legal clearance.
- The same publication snapshot:970–975 and frozen [content spec](../../../../output/research/company-public-projection-2026-10-07/review-inputs/specs/004-design-services-content/spec.md):33–47,276–277 quarantine fictional local fixtures from production/indexable output. Fixtures cannot establish company facts, verified work, live staff or contact operation.

## Independent reproduction

Executed from the frozen snapshot root using its schema and tests:

```text
C:/Python314/python.exe -B -m unittest scripts.validation.test_company_facts_schema scripts.validation.test_company_public_projection_schema
```

Result: **four methods PASS**, exit 0; elapsed test time **0.061 seconds**.
These establish validator-boundary behavior only. Frozen [test_company_public_projection_schema.py](../../../../output/research/company-public-projection-2026-10-07/review-inputs/scripts/validation/test_company_public_projection_schema.py):68–74 explicitly demonstrates that allowed strings can still carry excluded information or non-operational contact text. Semantic preparation must enforce those restrictions later.

## Held limits

This verdict does not authenticate company facts, verify registration or source month order, clear legal disclosure, activate contacts, assign alias ownership or establish safe rendering. Authorization, persistence, approval invalidation, synthetic quarantine, per-derivative exclusion, AI indexing, publication/withdrawal enforcement, accessibility and readiness remain unproven. Semantic/field/record/transport resource policies, actual integration/browser evidence, legal/mandatory-notice assessment, operational contact verification, full compatible graph and integrated/founder acceptance remain held.
The scope is the exact frozen proposal/representation seam. It grants no admin feature, application development, public fact/copy approval, contact operation, publication, Figma, Git or deployment authority. The review changed no files or external systems; subsequent authorized preservation creates this one uncommitted receipt only.
