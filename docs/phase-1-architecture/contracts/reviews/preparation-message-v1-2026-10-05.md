# Private preparation messages — independent v1 review

Date: 2026-10-05. Reviewer: `review_semantic_preparation_v1`, independent of
the producer. Verdict: **PASS for the bounded proposal and schema tooling**.
Task status: DOING; no commit, founder acceptance or implementation is implied.

## Exact inspected inputs

| Input | Verified SHA-256 |
|---|---|
| [Private message schema](../publication-preparation.schema.json) | `23c3569baa844a542dd8f7a283af87f50b93dfa1fdf3ccef2c401136c8acc2ac` |
| [Publication contract](../PUBLICATION_CONTRACT.md), new message/acceptance section | `c5b2d1ea531fba329959889ccda55191e604a465f9c7bf7e425541331a7488fc` |
| [Interface catalogue](../INTERFACE_CATALOG.md), preparation boundary refinement | `8795d3114531596203a7f59545e74a86d77322c53e437719bfbc6d225867119b` |
| [New shape-test source](../../../../scripts/validation/test_publication_preparation_schema.py) | `5b4fb2c75230cb0df73a47c96eda8ed2eed1105fe2ea0b58c866ca9925bd639f` |
| [Reused public envelope schema](../publication-manifest.schema.json) | `d3620c8326246bc34040188de610c5823f1013936572d3ffb63a5eb350bc3852` |
| [Reused synthetic envelope fixture source](../../../../scripts/validation/test_publication_manifest_schema.py) | `b8464d4a67d9c8c2f46d4583cf09a6f816661fdf65fd1cce20568d60fe5a78b4` |

Checked all six hashes before review. Read current governance, accepted PUB-001–006,
SEC-001/002 and DATA-001/010, logical data/security authority, publication lifecycle,
serving and withdrawal obligations, and the preceding semantic review. This is
new scope outside that receipt. Supporting records were inspected for alignment;
their unrelated historical contents are not exhaustively re-reviewed here.

## Findings and authority assessment

No actionable material finding within this bounded scope.

- `prepare`, `prepared` and `failed` are mutually exclusive closed variants;
  nested bindings/plans/failures are closed and the public envelope/route/artifact
  shapes are reused through fixed local references. The messages add no public
  API, queue, permission grant or automatically trusted result.
- Input identities bind candidate revision, public snapshot, route/derivative
  plans, renderer/client/toolchain/configuration and limits profile. Plans and
  snapshot have defined digest subjects; final artifact and manifest checksums
  are produced afterward. The public checksum remains outside its nested manifest,
  avoiding self-hashing; this proposal introduces no prerequisite for a worker to
  obtain approval of a not-yet-produced final envelope.
- Coordinator admission verifies exact current approval/eligibility and approved
  immutable inputs; workers receive only the permitted public projection and
  isolated staging scope. Receipt verification authenticates origin, checks current
  binding/generation and independently verifies bytes/content/plan/envelope agreement.
  Preparation never becomes approval, verified readiness merely by declaration,
  active-pointer authority or confirmation of an external business operation.
- Changed binding creates new preparation identity; unchanged-input retries use
  separately admitted increasing attempts. Duplicate effects, conflicting results,
  delayed writers, cancellation/revocation and unknown termination have explicit
  refusal/fencing/reconciliation obligations. Immutable attempt namespaces and
  final-byte checks do not silently substitute for physical enforcement.
- Failed results contain closed codes and optional planned-artifact identity,
  excluding raw diagnostics and retry grants. Cleanup/retention requires separate
  authorized policy; no failure code authorizes deletion or a new retention clock.
  Prior eligible release and truthful recovery remain governed by publication.

## Executed definition-level checks

Ran `python -B scripts/validation/test_publication_preparation_schema.py`:
all four unittest methods passed. Both schema resources passed Draft 2020-12
schema checking under the installed definition tooling.

For the main independent probe batch, constructed synthetic request/result/failure messages from the
contract, rather than introspecting the schema or importing producer fixture
helpers. Separate probes checked every required root/binding field, unknown
authority/private fields, invalid numeric revisions, UUID casing/end anchoring,
invalid UTC/calendar/hash values, route/plan closure, unsupported failure variants,
empty stream/duplicate dependency values and reused-envelope private-field denial.
Expected valid shapes and expected rejections behaved as specified.
A supplemental duplicate-stream rejection check used the existing synthetic fixture
and installed validator; it remained a schema-only check.

Additional probes deliberately confirmed that shape-valid documents can still
contain duplicate plan identities, seven copies of one derivative kind, a dot
segment in a key, unresolved dependencies, a different envelope release identity
or a different timestamp representation. These remain the explicitly documented
semantic/coordinator checks, not failures silently accepted as readiness. Digests,
actual bytes, origin, current authorization and cross-message state were not
verified by these probes. Strict raw JSON duplicate-property/Unicode/JCS parsing
is a separate implementation obligation; Python object fixtures do not exercise it.

Checked [JSON Schema validation semantics](https://json-schema.org/draft/2020-12/json-schema-validation),
[python-jsonschema local registry guidance](https://python-jsonschema.readthedocs.io/en/stable/referencing/)
and [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785) on 2026-10-05. Format
assertion and fixed resource resolution are appropriate; schema shape alone cannot
establish operational authorization or canonicalization. Current documentation
does not select the installed tooling as a complete production graph.

## Remaining gates and exclusions

PASS is proposal/schema evidence only. Exact worker identity/grants, isolated
process/storage scope, transaction/fencing mechanics, limits/timeouts/concurrency,
diagnostic and artifact retention, raw JSON acceptance and current eligibility
mechanisms remain reviewed implementation inputs. Actual worker/coordinator/
activation concurrency, replay, cancellation, partial/late writes, public-field
disclosure, failed preparation and recovery require boundary tests after approval.

No application handler, worker, database, dependency, lock, setting, provider or
producer input was changed. No runtime security/correctness, complete stable
compatibility graph, physical resource enforcement, release acceptance or integrated
Phase 1 acceptance follows. Only this review receipt was written.
