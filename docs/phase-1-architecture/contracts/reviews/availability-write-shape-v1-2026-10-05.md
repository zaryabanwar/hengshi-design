# Staff availability write shape — independent review v1

Reviewed 2026-10-05. **Iteration-0 verdict: REVISE**, one medium finding. Scope is only the new IF-STAFF-09 directional schema, local fixtures, additive “Directional shape encoding proposal” and illustrative operation-ID repair. The prior HTTP review retains its exact original scope; no wire freeze or implementation acceptance follows.

## Exact evidence

Packet: `output/research/availability-write-shape-2026-10-05/review-inputs.json`, SHA256 `e57991546f350a380c5f517fc05fcb15c433d4475eb12984a7e3965c3517689a`. Independently verified all 20 frozen size/hash identities and correspondence to current sources before correction, plus 12 protected-input hashes.

| Producer | Bytes | SHA256 |
| --- | ---: | --- |
| `docs/phase-1-architecture/contracts/availability-write.schema.json` | 5,132 | `cfdb1a940113ce43630bc16e9bad423abb7884c389616d34e19aab897109f911` |
| `scripts/validation/test_availability_write_schema.py` | 8,447 | `0b1fdb3fa2fc3f32167cbc90b5c883f4bfc68c226885880438dec8b138b3bc4a` |
| `docs/phase-1-architecture/contracts/AVAILABILITY_WRITE_HTTP.md` | 20,988 | `34db8ee2f6590b52842b097f702741d8eb01aa282650b60ff88abb9195fd5a6e` |

The prior 17,992-byte HTTP body, SHA256 `ecbe82a65d739857b78621a7800e11330b8f03dd464807dd36fe5920ab3dacc8`, is preserved after exactly one 33-to-32-character example repair; the remainder is the appended section. Schema/tooling links resolve. Current governance, security/availability/data/catalogue authority and earlier receipt were inspected as context, without reaccepting their full contents.

## Finding

**AWS-MED-001 — canonical schema registration cannot resolve the shared department definition.** At `availability-write.schema.json:8`, the relative `availability-read.schema.json#/$defs/departmentKey` reference is incompatible with registering the schemas only under their declared URN `$id` values. Independently registering both frozen schemas by those canonical IDs and validating an otherwise valid withdrawn response produces `_WrappedReferencingError: Unresolvable: availability-read.schema.json#/$defs/departmentKey`. The fixture setup registers only file-URI aliases, masking this failure. Replace the reference with the read schema's canonical identifier and exercise both canonical-ID registration and supported file aliases through the real validator. No remote retrieval or new dependency is needed.

## Inspection and verification

Independent original-byte reproduction, exit 0:

- `python -B -m unittest discover -s scripts/validation -p test_availability_write_schema.py -v`: **4 methods pass**, under file-URI registration.
- `python -B -m unittest discover -s scripts/validation -p 'test_*schema.py'`: **38 methods pass**, once, with the same registration limitation.

Additional arithmetic probes independently compared 3,355 values with `1 <= value <= 2**64 - 1`, including each ceiling digit with extreme suffixes and deterministic samples inside/outside the range. Unicode digits, line terminators, NUL, whitespace, signs, noncanonical zeroes, numeric/boolean values and malformed identities reject. Syntax-valid all-zero identities accept, appropriately without entropy/issuance claims.

Commands and responses are directional; none/current bindings and declared/withdrawn/pending correlations match the preceding HTTP tables. All code/recovery combinations were independently challenged; only `stale_binding` permits and requires `current`. Minimal errors remain closed, with no diagnostic projection. Canonical wing selectors reuse the unchanged read definition. Otherwise valid stale, unissued or uncorrelated records can pass shape checks; an ordinary duplicate-key JSON parse can also produce a valid dictionary. These are expressly held parser/authority/state limitations, not additional findings.

Primary [JSON Schema string guidance](https://json-schema.org/understanding-json-schema/reference/string), [combination guidance](https://json-schema.org/understanding-json-schema/reference/combining) and [jsonschema referencing documentation](https://python-jsonschema.readthedocs.io/en/stable/referencing/) were independently consulted for pattern/composition and controlled resource registration. They do not select a library release or production parser. Producer source identities alone were not taken as independent verification.

## Limits and held gates

Strict raw decoding and duplicate-member rejection, decoded path/HTTP status/header/error precedence, actual identity generation/issuance and scoped uniqueness, current grants/delegate scope, authorized disclosure, mutation/replay/concurrency/fencing, expiry/timing/retention/restore policy, browser correlation/live-state behavior, complete compatible stable graph, implementation evidence and integrated/founder acceptance remain held. No new route, grant, numeric service policy, database type or persistence mechanism is selected. Tests validate schema/tooling only. No production/security/runtime certification, full Phase 1 acceptance, campus/model or QA revision is implied. Only this receipt was authored.

## Correction-1 disposition — superseding bounded PASS

Reviewed 2026-10-05. **PASS for the corrected encoding slice; AWS-MED-001 closed. No remaining actionable findings.** The iteration-0 REVISE and all its evidence above are preserved; the original receipt prefix SHA256 is `ceffe618ddb489d9e72e28d5b14198917e01b2718f50e5962e728a0cc8b41273`.

Correction packet: `output/research/availability-write-shape-2026-10-05/correction-1/review-inputs.json`, SHA256 `a63ebea45fb5f15011b500448a2a6074085245849019566231b37e03f8221e02`. All 20 corrected snapshot/current-source sizes and hashes independently match; the original manifest and all 20 original snapshots remain intact.

| Corrected producer | Bytes | SHA256 |
| --- | ---: | --- |
| `availability-write.schema.json` | 5,135 | `f6d18639e28f517c7d950cfee3c33795a41f31ce972cac810ca98edb2d398004` |
| `test_availability_write_schema.py` | 8,986 | `79274e7eda092dfea5284edb56102e93b237908d5f0efdb46e89df32b0233253` |
| `AVAILABILITY_WRITE_HTTP.md` | 21,261 | `2b91f0f4164527c5a2ffae3cd28a39c1261f0a79d182d7ad5e487c95ebf46d51` |

The exact correction changes only the shared department reference to `urn:hengshi:v1:availability-read#/$defs/departmentKey`, fixture registration/validation through canonical identifiers and file aliases, and the corresponding explanatory paragraph. Sixteen other context/guard inputs are byte-identical across packets; the suite transcript was regenerated. All 12 protected-input guard hashes still match. No prior HTTP requirement, range, response alternative or grant changes.

Independently reproduced the corrected four focused methods, exit 0. Separate probes using a registry containing **only the two canonical URN identifiers**, with no file aliases or retrieval callback, validate commands, declared/withdrawn/pending and stale-binding responses; unknown wings and responses supplied as commands reject. The file-URI entry aliases also validate with the corrected registry. This resolves the original portability failure. The 38-method suite above was independently run on iteration-0 bytes; correction-1's 38-method passing suite is producer evidence, not an additional independent broad rerun. No broader rerun was needed for this reference-only repair after focused reproduction and exact-diff inspection.

All scope limits and remaining gates above continue unchanged. This superseding PASS establishes only corrected definition/shape/tooling coherence, not runtime authorization, state correctness, production selection or integrated/founder acceptance.
