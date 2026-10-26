
## Staff identity distribution licences and publishing evidence — 2026-10-09

Status: DOING. The [exact artifact observations](../../output/research/staff-identity-distribution-2026-10-09/observations.json)
inspect only Authlib 1.8.0 and joserfc 1.7.5 from the existing unselected 45-package
candidate. Both downloaded wheel byte lengths and SHA-256 digests match the frozen
resolver/registry identities. ZIP contents were read in memory, with complete
RECORD member/hash/length checks; neither package was installed or imported.
These are artifact-consistency observations, not native or sign-in tests.

| Exact candidate | Licence file in the wheel | Retained notice |
|---|---|---|
| Authlib 1.8.0 | [BSD-3-Clause text](../../output/research/staff-identity-distribution-2026-10-09/authlib/licenses/LICENSE), matching LICENSE at the previously recorded source commit | Copyright 2017 Hsiaoming Yang, conditions and disclaimer. |
| joserfc 1.7.5 | [BSD-3-Clause text](../../output/research/staff-identity-distribution-2026-10-09/joserfc/licenses/LICENSE), matching LICENSE at the recorded 1.7.5 tag commit | Copyright 2023 Hsiaoming Yang, conditions and disclaimer. |

For these two licence texts, a later source distribution must retain copyright,
conditions and disclaimer; a later binary distribution must reproduce them in
the supplied documentation/materials. Do not imply endorsement by the holders or
contributors. Carry the exact applicable notices into the eventual release
inventory and its delivery mechanism; a registry classifier or this table is not
that delivered notice bundle. This observation selects no paid support plan and
does not clear all transitive/embedded code or settle the project's legal review.

PyPI's Integrity API returned 200 provenance objects for both exact wheel filenames.
The returned GitHub publisher fields name `authlib/authlib` and `authlib/joserfc`,
respectively, with `pypi.yml` in `pypi-release`. Their decoded publish statements
name the corresponding exact wheel digest. **These statements are unverified**:
no signature, certificate identity or transparency-proof verification ran. Use
[PyPI's documented verification procedure](https://docs.pypi.org/attestations/consuming-attestations/)
with an independently expected repository when the verification environment is
qualified. Reading publisher fields, comparing a subject digest, checking RECORD
or matching one source licence does not prove publisher authenticity, reproducible
build provenance or equality of the complete wheel to the tagged source.

The [captured primary guidance](../../output/research/staff-identity-distribution-2026-10-09/primary-docs.json)
distinguishes wheel self-consistency from cryptographic attestation verification.
The six protected project inputs remain unchanged. This read-only inspection
does not execute or expand the separately pending 43-package native trial.
Complete candidate licences/notices, provenance verification, advisories, native
qualification, current latest-compatible graph/locks and integrated/founder
acceptance remain. Independent review of this new appendix and its exact artifact
inputs is required; earlier receipts retain their own frozen scope.
