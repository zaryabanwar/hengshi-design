# Backend compatibility evidence refresh

Status: DOING. Observed 2026-10-04. This metadata/resolver supplement preserves the July
inventory and current requirements/environment; no dependency, lock, Python,
database, authentication or cloud version is selected or changed.

## Review coverage

The [later backend review](reviews/refresh-backend-2026-10-04.md#later-disposition-windows-resolver-and-pydantic-source-channel)
records bounded PASS for the Windows resolver and Pydantic source-channel
follow-up at its exact listed hashes. Those
[reviewed producer bytes](../../output/research/contract-review-reference-reconciliation-2026-10-04/backend-evidence.pre-status.md)
are preserved; this page's later reference update does not replace that identity.
The original 19-package snapshot review retains its separate earlier scope.
Neither receipt proves imports/native ABI, complete platform compatibility,
distribution provenance, licence clearance or a selected production lock.

The separate [current evidence reconciliation](reviews/compatibility-evidence-reconciliation-v1-2026-10-05.md)
records bounded PASS after correction 1 for the current studies and authority
wording. Its [corrected producer bytes](../../output/research/compatibility-evidence-reconciliation-2026-10-05/correction-1/backend-evidence.corrected.md)
are preserved: production provider/OS/packaging evidence is conditional on D-068
planning, with the separately approved Entra and Azure EU private-AI constraints
retained. This reference addition is outside the exact inspected bytes; no full
stable graph, native runtime, legal clearance or MA-013 acceptance follows.

## Observations and source

[PyPI snapshot](backend-candidates-2026-10-04.json) records 19 packages, exact
observed versions, complete Requires-Dist strings, Python requirements, development
classifiers, license metadata and distribution filenames/hashes/yanked flags.
It also records the input requirements hash and current API virtualenv metadata.
The current API virtualenv uses Python 3.14.5. Installed metadata is an observation,
not proof of imports, test success, runtime health or reproducibility.

| Package family | Installed API virtualenv | PyPI candidate |
|---|---|---|
| FastAPI / Starlette | 0.138.0 / 1.3.1 | 0.142.2 / 1.7.0 |
| Pydantic / core | 2.13.4 / 2.46.4 | 2.13.5 / independently latest core 2.49.0 |
| Uvicorn | 0.49.0 | 0.54.0 |
| SQLAlchemy / Alembic | 2.0.51 / 1.18.4 | 2.1.3 / 1.20.0 |
| Psycopg / binary companion | 3.3.4 / 3.3.4 | 3.3.6 / 3.3.6 |
| bcrypt / PyJWT | 5.0.0 / 2.13.0 | 5.0.0 / 2.15.1 |
| HTTPX / pytest | 0.28.1 / 9.1.1 | 0.28.1 / 9.1.1 |
| pytest-asyncio | Not installed in this virtualenv | 1.4.0 |
| email-validator / python-dotenv | 2.3.0 / 1.2.2 | 2.3.0 / 1.2.4 |
| AnyIO / typing-extensions / greenlet | 4.14.0 / 4.15.0 / 3.5.2 | 4.15.1 / 4.16.0 / 3.5.6 |

Current `apps/api/requirements.txt:1-13` is unbounded or lower-bounded rather than
a deterministic production lock. It names pytest-asyncio even though this observed
virtualenv lacks its metadata. This slice installs nothing and infers no test
failure or live-server failure from that absence alone.

## Windows resolver dry run, 2026-10-04

An isolated [requirements study](../../output/research/compatibility-resolution-2026-10-04/backend-windows/requirements-study.txt)
pins the twelve existing requirements families to the observed candidates, keeping
the existing Uvicorn standard and Psycopg binary extras. It does not override
Starlette or Pydantic core independently. The current API Python 3.14.5 and pip
26.1.1 ran the documented
[pip dry-run/report mechanism](https://pip.pypa.io/en/stable/cli/pip_install/):

```powershell
.\apps\api\.venv\Scripts\python.exe -m pip --isolated install --dry-run --ignore-installed --only-binary=:all: --no-cache-dir --disable-pip-version-check --progress-bar off --index-url https://pypi.org/simple --report output/research/compatibility-resolution-2026-10-04/backend-windows/pip-report.json -r output/research/compatibility-resolution-2026-10-04/backend-windows/requirements-study.txt
```

Exit 0 resolves a wheel-eligible Windows CPython graph without installing packages
or executing source builds. The [pip report](../../output/research/compatibility-resolution-2026-10-04/backend-windows/pip-report.json)
contains artifact URLs/hashes, distribution metadata, environment and requested
extras. The resolved Pydantic 2.13.5 uses **core 2.46.5**, not independently newest
core 2.49.0. Active Requires-Dist clauses were inspected using the recorded Windows
markers and propagated extras; none had a missing or out-of-range target. These
are dependency-resolution observations, not import/native-library/database/API tests
or a production lock. Linux, other Python versions and future auth/telemetry extras
have separate graphs; this study cannot prove them.

None of the resolved versions is marked prerelease/dev or yanked in the report.
Several project maturity classifiers still say Alpha/Beta, including core,
Starlette, FastAPI and Uvicorn. Those labels are not the same field as a release
prerelease flag and must not be silently relabeled or treated as resolved stability
evidence. Official GitHub release metadata reports Uvicorn 0.54.0 and Pydantic
2.13.5 as non-draft/non-prerelease. The earlier core `v2.46.5` release lookup
returned 404 in the archived standalone repository. The source-channel follow-up
below establishes its monorepo tag and coupled source versions; it preserves that
404 and does not infer a GitHub release object, signed tag or verified wheel build.
Support/channel evidence for the complete final graph remains a review obligation.

The [combined analysis](../../output/research/compatibility-resolution-2026-10-04/resolution-analysis.json)
retains range checks, maturity labels, host context and protected-input hashes;
[release-channel observations](../../output/research/compatibility-resolution-2026-10-04/release-channel-checks.json)
preserve the actual results. Root/web manifests and locks plus API requirements
match before/after hashes. No application tests ran and no native database changed.
The earlier independent backend refresh review covers its older hashes, not this
new dry-run section. The later bounded review identified above covers that evidence;
no MA-013 acceptance or full
Phase 1 approval follows from successful resolution.

## Coupling and stability findings

- Pydantic 2.13.5 requires **pydantic-core==2.46.5**, so independently choosing
  latest core 2.49.0 violates its exact range. The snapshot separately includes
  official metadata/files for constrained core 2.46.5; this is a graph observation,
  not approval to install it. Core's latest metadata also carries an Alpha
  development classifier despite a non-prerelease version identifier. The exact
  coupled source and maintainer version-policy evidence below now contextualize
  core 2.46.5. The classifier is retained accurately; neither a package label nor
  this source association alone accepts the stable-only production graph.
- FastAPI's observed candidate advertises Starlette >=0.46.0 and Pydantic >=2.9.0.
  Advertised ranges admit the candidate versions but do not prove application
  compatibility. Context7 `/websites/fastapi_tiangolo` and the official
  [version guidance](https://fastapi.tiangolo.com/deployment/versions/) advise
  resolving Starlette through FastAPI. A generated transitive exact lock must obey
  that graph, rather than independently override Starlette. Exact tested FastAPI
  selection is still required.
- [SQLAlchemy 2.1 migration guidance](https://docs.sqlalchemy.org/en/21/changelog/migration_21.html)
  identifies Python >=3.11, changed default PostgreSQL driver, asyncio extra and
  autoflush/mapping behavior. Review the existing explicit Psycopg dialect,
  transaction/unit-of-work semantics and Alembic comparison before a separate wave.
  No asynchronous SQLAlchemy migration is selected by this evidence.
- Psycopg's binary extra requires the matching binary companion release. Observed
  3.3.6 Windows x64 CPython 3.14 files exist, but filename/hash metadata does not
  prove loading or libpq/OpenSSL capability. Its official
  [installation guidance](https://www.psycopg.org/psycopg3/docs/basic/install.html)
  distinguishes self-contained binary development from locally linked production
  builds; its current documentation header is a development release, so exact
  selected-release behavior and production packaging still need evidence.
- [bcrypt 5.0.0 release notes](https://pypi.org/project/bcrypt/5.0.0/) say inputs
  over 72 bytes raise ValueError. Future credential validation/error handling must
  preserve the approved random 24+ character emergency credential policy without
  silent truncation, unreviewed prehashing or a replacement password algorithm.
- pytest-asyncio 1.4.0 requires pytest >=8.4,<10; the observed pytest candidate is
  within that range. Windows dependency markers and chosen extras do not establish
  the graph for any separately selected production OS and extras. Production OS
  and packaging remain unselected under D-068. The snapshot's edge flags evaluate
  only the observed Windows runtime with no extras and are deliberately not a full
  resolver.

## Pydantic source-channel follow-up, 2026-10-04

Context7 `/pydantic/pydantic` led to the official
[tagging policy](https://pydantic.dev/docs/validation/latest/get-started/version-policy/#tagging-conventions):
since Pydantic 2.13, core is a workspace member of the Pydantic repository and its
published-version tags use `core-vx.y.z`. The standalone repository is archived.
The current policy was captured at an immutable source commit alongside a
separately retained `v2.13.5` copy. Both policy copies have identical bytes; no
policy change between those source identities is asserted.

The [exact source-channel receipt](../../output/research/compatibility-resolution-2026-10-04/backend-windows/pydantic-source-channel-evidence.json)
retains URLs, timestamps, status/errors, raw source filenames and SHA-256 hashes.
The corrected monorepo release-object endpoint also returns 404, while its
`core-v2.46.5` Git reference exists. After peeling annotated tags, both that core
tag and Pydantic `v2.13.5` point to commit
`001dea020e0809844e5b17666432c9135a976f46`.

At that source identity, Pydantic's
[pyproject](https://github.com/pydantic/pydantic/blob/001dea020e0809844e5b17666432c9135a976f46/pyproject.toml)
declares exactly `pydantic-core==2.46.5`; core's
[Cargo manifest](https://github.com/pydantic/pydantic/blob/001dea020e0809844e5b17666432c9135a976f46/pydantic-core/Cargo.toml)
declares version 2.46.5. This closes the missing source-location/version association
for the previously resolved pair, not the complete distribution provenance gate.
The core tag annotation says 2.46.3 despite the tag name and source version being
2.46.5. Both tag-object responses report `verification.verified: false`; no
signature verification or wheel-to-source attestation is claimed.

The exact core pyproject retains its Alpha development classifier. Pydantic's
pyproject declares Production/Stable and requires that exact core. Its official
version policy aims to preserve the public V2 API across minor releases, while
allowing documented validation-error and internal core-schema changes. Experimental
features have separate, changeable APIs and remain excluded as production
requirements by this project's governance. These facts distinguish the coupled
maintained public API from a standalone core maturity label without hiding the
label, selecting an experimental API or promising application compatibility.

Only metadata/source text was fetched and inspected: no package install, import,
source build, database operation, provider selection or application change.
Native ABI, actual FastAPI/Pydantic request and serialization behavior, clean
locked installation, advisory/licence and distribution-provenance evidence,
other target-platform graphs and complete independent compatibility acceptance
remain required. The earlier backend review covers its original hashes only;
this follow-up and the dry-run section have the separate bounded review identified
above. Neither receipt establishes full compatibility or implementation readiness.

## Required selection and rollback evidence

Choose only non-preview supported releases under the approved families, resolve
chosen extras and every transitive dependency for the actual target runtime, and
record a reproducible hash-locked install, SBOM/license/advisory and build evidence.
Finish Python support/ABI, JWT crypto, Uvicorn extras and database/libpq evidence
for the actual target runtime. Hosting-specific GA and production OS/packaging
graphs are conditional on the later approved target when D-068 planning resumes;
Azure and AWS remain candidates, with no hosting provider, production OS or
container requirement selected. Retain immutable-artifact and image-digest controls
where applicable to that eventual packaging. Entra staff identity and the separately
approved Azure EU route for personal/confidential AI data remain constraints.
SQLAlchemy, Pydantic and native wheels require focused
behavior tests plus one relevant suite in their separately reversible backend wave.

The requirements, application, native services and database are unchanged here.
An authorized rollback must restore the previous coherent environment/source/lock
and repeat affected evidence; no live rollback or installation was performed.
MA-013, exact production selection and complete Phase 1 acceptance remain open.

## Current registry and coupled Windows study — 2026-10-08

Status: DOING. [The bounded independent review](../../output/research/backend-current-review-2026-10-08/independent-review-backend-current-v1.json)
passes for 132 frozen inputs covering this study and the release/source follow-up
below. It reproduces metadata closure and migration-claim accuracy only; runtime,
supply-chain qualification, selection and integrated acceptance remain held. These
later review-reference edits are outside its frozen bytes.
The October 4 graph remains preserved as dated evidence; it is not silently
relabelled as the latest candidate or an accepted production lock.

The [registry recheck](../../output/research/backend-hash-inputs-2026-10-08/completed-registry-recheck.json)
matches all forty old wheel names, URLs and SHA-256 declarations against official
PyPI metadata. It preserves the initial eight-MiB receive-cap failure for the
large pydantic-core project response and its separate sixteen-MiB recovery.
The [old-graph hash-pinned derivative](../../output/research/backend-hash-inputs-2026-10-08/windows-study-hashed-requirements.txt)
is research input only. Metadata digest agreement does not independently verify
wheel content, signatures, provenance or licences.

Six newer non-preview, non-yanked releases were observed. One fresh, isolated,
wheel-only [resolver dry run](../../output/research/backend-hash-inputs-2026-10-08/latest-coupled-resolution/receipt.json)
uses the same twelve direct package families and existing Uvicorn standard and
Psycopg binary extras. It changes only observed direct candidate pins, leaving
transitive choice to the coupled resolver. No package was installed.

| Package | October 4 resolved study | October 8 resolved candidate |
|---|---|---|
| FastAPI | 0.142.2 | 0.143.0 |
| SQLAlchemy | 2.1.3 | 2.1.4 |
| Pydantic | 2.13.5 | 2.14.0 |
| pydantic-core | 2.46.5 | 2.50.0 |
| OpenTelemetry API | 1.45.0 | 1.45.1 |
| iniconfig | 2.3.0 | 2.3.1 |

Exit zero produces forty wheel records for the recorded Windows AMD64 CPython
3.14.5 environment. The [replayable metadata inspection](../../output/research/backend-hash-inputs-2026-10-08/latest-coupled-resolution/inspect_resolution.py)
checks marker clauses with propagated extras, active dependency ranges, Python
requirements, local wheel tags and saved registry hashes. Its
[observations](../../output/research/backend-hash-inputs-2026-10-08/latest-coupled-resolution/closure-observations.json)
record forty-five active dependency edges and unchanged protected application
manifests, locks, API requirements and virtualenv configuration. This demonstrates
resolution and metadata closure, not native imports, API/database behaviour or
application compatibility. No source builds, runtime upgrades or database work ran.

The [new hash-pinned research derivative](../../output/research/backend-hash-inputs-2026-10-08/latest-coupled-resolution/windows-study-hashed-requirements.txt)
retains this exact Windows mixed runtime/test graph. It is not a portable
production lock; a separately authorised replay must enforce hashes and wheels.
The [pip report format](https://pip.pypa.io/en/stable/reference/installation-report/)
itself is not a lockfile. The bounded review above is complete; full maintained-
release-channel and supply-chain qualification, native/request/serialization tests
and MA-013 selection remain pending. Earlier source-channel evidence for Pydantic 2.13.5/core 2.46.5
does not qualify the new pair. Production provider/OS planning remains deferred
under D-068. Adoption and rollback remain separately approved future work; the
current application and earlier reviewed evidence are unchanged.

## Current candidate release channels and migration obligations — 2026-10-08

Status: DOING. The bounded review above covers these source observations and
migration recommendations at their frozen bytes, without runtime or adoption
acceptance. The
[primary release/source observations](../../output/research/backend-hash-inputs-2026-10-08/source-channel-followup/source-observations.json)
retain non-draft/non-prerelease GitHub release objects for FastAPI 0.143.0,
Pydantic 2.14.0 and SQLAlchemy 2.1.4. The separate core-v2.50.0 tag and its two
raw-source lookups returned 404; those responses remain preserved. No release
object, signed tag or core-specific provenance is inferred from package numbers.

The [pinned Pydantic source inspection](../../output/research/backend-hash-inputs-2026-10-08/source-channel-followup/pinned-source-observations.json)
resolves its annotated release tag to commit
`fcdefa7198c4fc94a22eecf1a5b7926e20b9fc8a`. At that immutable commit the Pydantic
version is 2.14.0, its exact requirement is pydantic-core 2.50.0 and the core
Cargo package version is 2.50.0. The Pydantic pyproject matches the previously
fetched tag source. GitHub reports the tag unsigned. Pydantic retains its
Production/Stable classifier and core its Alpha classifier; neither is hidden.
This supports coupled source identity, not verification of the downloaded wheels.

Required focused behaviour checks for a separately authorised backend wave:

- [FastAPI 0.143.0](https://github.com/fastapi/fastapi/releases/tag/0.143.0) makes
  automatic telemetry exporter setup opt-in. Check the intended explicit
  instrumentation and export policy with synthetic requests: approved signals
  arrive, private payloads remain excluded and no unintended exporter activates.
  The protected prototype's sole application constructor at `app/main.py:17`
  contains no explicit telemetry configuration; this source observation does not
  inspect or change machine settings or select a future telemetry provider.
- [Pydantic 2.14.0](https://github.com/pydantic/pydantic/releases/tag/v2.14.0)
  changes validation/serialization details and drops Python 3.9 support. Exercise
  the intended request/error/response boundary, strict input rejection, timestamp
  serialization and generated schemas. Its [version policy](https://pydantic.dev/docs/validation/latest/get-started/version-policy/)
  permits changes to error details and internal core schemas within minor releases.
  Preserve stable public error projections; do not expose raw diagnostics or rely
  on experimental APIs or undocumented core internals.
- [SQLAlchemy 2.1.4](https://docs.sqlalchemy.org/en/21/changelog/changelog_21.html#change-2.1.4)
  fixes cursor/result and rollback connection cleanup. Check transaction rollback,
  resource return after failure and schema/type round trips with the selected
  Psycopg/PostgreSQL combination in isolated synthetic integration scenarios.
  Release-note fixes are not proof that Hengshi's pool or database behaves correctly.

These checks supplement the existing graph, provenance, licence, security and
rollback obligations. No tests of a new runtime ran in this slice. No application
install, dependency/lock/database/settings change, production selection or provider
choice follows. Earlier reviews retain their exact earlier scope. The bounded
review above passes for these source and migration claims only; complete graph
qualification and integrated/founder acceptance remain separate.

## Asymmetric JWT dependency closure and proposed native qualification — 2026-10-08

Status: DOING. The staff sign-in mediation proposal requires verification of the
provider token's signature, issuer, audience, validity and nonce. The earlier
40-package Windows study requests plain PyJWT and contains no cryptography
package. PyJWT's [pinned installation documentation](https://github.com/jpadilla/pyjwt/blob/2.15.1/docs/installation.rst)
requires cryptography for RSA/ECDSA and recommends the crypto extra. This is a
missing research coupling, not evidence of a running staff sign-in defect.
The [saved primary sources](../../output/research/backend-crypto-graph-2026-10-08/primary-docs/sources.json)
retain the exact source bytes and observation dates; no source signature or wheel
attestation is inferred.

The [research roots](../../output/research/backend-crypto-graph-2026-10-08/candidate-roots.txt)
change only `pyjwt==2.15.1` to `pyjwt[crypto]==2.15.1`. A wheel-only isolated
[dry-run receipt](../../output/research/backend-crypto-graph-2026-10-08/receipt.json)
records exit0 and no installation. The resulting
[43-package report](../../output/research/backend-crypto-graph-2026-10-08/pip-report.json)
adds cryptography50.0.2, cffi2.1.1 and pycparser3.1. The previous40 records retain
identical versions, distribution metadata and artifact associations; Uvicorn
standard and Psycopg binary extras remain. Saved Windows markers/extras produce48
active dependency edges with no missing/out-of-range target. The three added
packages' exact PyPI declarations and artifact identities match the report;
filenames intersect the observed Windows CPython3.14.5 tags. These observations
do not prove wheel contents, native ABI/import behavior or a supported release
channel. Cryptography and pycparser carry Production/Stable classifiers; cffi
has no development-status classifier. None of the three versions is a prerelease
or yanked in the saved metadata. Complete release/support evidence remains held.

The [metadata observations and research hash pins](../../output/research/backend-crypto-graph-2026-10-08/closure-observations.json)
record six unchanged protected project inputs. The pins are a platform-specific
evaluation input, not a selected production lock or an independently newest
whole-graph result. Earlier40-package source/review receipts retain their exact
scope. The [79-input initial review](../../output/research/backend-crypto-graph-2026-10-08/review/independent-review-crypto-graph-v1.json)
independently reproduced the metadata closure and requested a footprint-plan
correction. The [ten-input correction1 review](../../output/research/backend-crypto-graph-2026-10-08/review/correction-1/independent-review-correction-1-v1.json)
records PASS for the prospective admission/reservation repair only. Its inspected
inputs remain frozen; these later receipt references are outside those bytes.
No installation, native qualification or production acceptance follows.
Asymmetric JWT primitives do not supply a complete maintained OIDC/PKCE client.
That adapter, its graph, current staff mapping/session checks and actual Entra
qualification are still unselected/unimplemented.

The [proposed native qualification plan](../../output/research/backend-crypto-graph-2026-10-08/qualification-plan.json)
uses a new pip-less research virtualenv, exact hash-checked binary wheels and
offline installation through pip's documented `--python` support. Metadata totals
18,107,329 compressed archive bytes, not installed footprint. The proposed256MiB
admission/stop budget retains1GiB free disk. Before downloads/venv creation, reserve
that full allowance. Before installation, match actual wheel sizes/hashes, inspect
ZIP entry sizes without extraction and require measured retained output plus twice
the expanded contents plus64MiB installer/output allowance to fit the budget and
free-disk reserve. Refuse when it does not fit. Measure before/after each command
and stop on over-budget/reserve loss, preserving failures. This is a conservative
admission calculation, not an OS-enforced hard quota during installer/native
execution. Refuse an existing target, source builds or changed protected inputs. Existing
API/frontend environments, manifests and locks stay protected. No Docker,
database, server, account, credential or provider operation is part of the trial.
Execution requires applicable founder authorization; this plan executes nothing.
There is no automatic deletion or production dependency adoption.

The trial would exercise public-library boundaries with synthetic RSA rejection
cases, strict request/response validation, SQLite transaction rollback, offline
PostgreSQL DDL generation, binary libpq import/version reporting, bcrypt boundary
inputs, Uvicorn configuration without a listener and an actual pytest async case.
SQLite/offline SQL/native imports are distinct observations, not real PostgreSQL,
Hengshi HTTP/auth, deployment, concurrency or load assurance. Exact adapter and
full graph selection, release/provenance/licence/advisory evidence, actual
application qualification and integrated/founder acceptance remain separate gates.

## Maintained staff identity client comparison — 2026-10-08

Status: DOING. Recommend evaluating Authlib's async Starlette/HTTPX OIDC integration
as the leading staff sign-in candidate; MSAL plus a separately qualified verifier
is an alternative. This selects neither package nor adapter and changes no accepted
identity, session, API, provider or role boundary. The existing
[staff mediation proposal](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#staff-sign-in-mediation-proposal)
requires a maintained client, server-held state/nonce/PKCE credentials, token
verification and current Hengshi eligibility; the library does not own grants.
The [dated registry observations](../../output/research/staff-identity-client-options-2026-10-08/registry-observations.json)
and [immutable source associations](../../output/research/staff-identity-client-options-2026-10-08/primary-sources.json)
preserve exact inputs. Tags resolve to recorded commits, not proven wheel builds.
Both release objects are non-draft/non-prerelease; both registry classifiers say
Production/Stable. This is not full support, licence, advisory or runtime evidence.

| Candidate observation | Fit and extra work |
|---|---|
| MSAL1.39.0; Python>=3.9; requests<3, PyJWT[crypto]<3 and cryptography<51 | Microsoft's confidential client supports code-flow state, PKCE and nonce protection. Its current token acquisition decodes ID-token claims without signature/issuer/audience/expiry validation; the legacy decoder is deprecated and is no substitute. Hengshi would need a separately qualified maintained verifier. The default added offline-access scope needs explicit exclusion; no Graph/broker or durable provider-token cache is implied. Its default Requests path also needs bounded blocking-work isolation in FastAPI. |
| Authlib1.8.0; Python>=3.10; cryptography>=45.0.1 and joserfc>=1.6.1 | Native async framework integration uses the retained HTTPX family, with documented S256 configuration and an ID-token signature/claims validation path. An async server cache can hold temporary flow data while the browser session retains a correlation marker. This avoids copying provider secrets into the signed browser session, but does not establish atomic consumption, policy compliance or runtime compatibility. |

These ranges are registry declarations, not complete lower bounds or resolved
graphs; the frozen registry contains every exact Requires-Dist clause. Neither
candidate is installed, resolved together with the complete graph or included in
the separately prepared43-package native trial. Adding an adapter later requires
its own full coupled evaluation, qualification and integrated acceptance.

The recommendation follows the existing requirement to use a maintained client
and verifier, rather than hand-building OAuth. Research used Context7 MSAL and
Authlib identifiers, [Microsoft's acquisition guidance](https://learn.microsoft.com/en-us/entra/msal/python/getting-started/acquiring-tokens),
[Authlib's async framework guidance](https://docs.authlib.org/en/stable/oauth2/client/web/starlette.html)
and its [S256 configuration](https://docs.authlib.org/en/stable/oauth2/client/web/index.html#oauth-2-0-code-challenge).
The version-pinned source exposes defaults that illustrative examples omit:

- Authlib's cache path requires a browser-session marker. Its cache get/delete
  are separate calls; they do not prove the required one-time, expiring transaction
  claim under concurrent callbacks. The adapter must provide that guarantee.
- Without a server cache, the framework stores temporary flow data in the session.
  A signed cookie is readable; do not use that path to carry nonce/verifier or
  provider tokens. Do not copy the example's browser-session ID-token storage.
- Automatic ID-token parsing is conditional on both ID-token and stored nonce
  presence. Require the expected token/nonce explicitly before any staff grant.
  The generic parser permits `nonce_supported=false` to disable its nonce check;
  Hengshi must retain its mandatory nonce requirement and reject that bypass.
- Algorithms are taken from discovery metadata (default RS256), expiry leeway
  defaults to120seconds, and custom claim options can replace the default issuer
  options. None is an approved Hengshi policy. Configure and qualify explicit
  permitted issuer/tenant, audience, algorithms, time bounds and nonce checks
  without losing any guard when options change.
- Discovery/JWKS refresh needs the existing origin, bounded fetch/work and
  key-rotation controls. Local session issuance/current role checks and Hengshi
  logout remain owned by the backend, independently of provider logout.

Required later synthetic qualification covers wrong issuer/audience/key/algorithm,
missing or bypassed nonce, expiry, swapped token kind, browser mismatch, concurrent
or expired transaction use, missing/rotated keys, bounded network failure and
unchanged local logout/eligibility. These are retained requirement oracles, not
executed tests. Exact graph, storage/transaction/transport bindings, account
registration, legal/security qualification and integrated/founder acceptance
remain held. The [38-input independent review](../../output/research/staff-identity-client-options-2026-10-08/review/independent-review-identity-client-options-v1.json)
records bounded PASS for source/registry associations and this unselected comparison,
including the scoped map additions. Its frozen inputs remain preserved; these
later receipt references are outside inspected bytes. It selects no client or
graph and proves no actual identity/security, native or integrated conformance.

## Staff identity candidate dependency closure — 2026-10-08

Status: DOING. Following the separately reviewed unselected client comparison,
the [research roots](../../output/research/staff-identity-graph-2026-10-08/candidate-roots.txt)
add only Authlib1.8.0 to the preceding12-root crypto study. A wheel-only isolated
[dry-run receipt](../../output/research/staff-identity-graph-2026-10-08/receipt.json)
records exit0 after28.57seconds, no installation and unchanged six protected project
inputs. The [45-package report](../../output/research/staff-identity-graph-2026-10-08/pip-report.json)
adds Authlib1.8.0 and joserfc1.7.5. All43 preceding versions, distribution metadata
and artifact associations are unchanged. Active Windows markers/extras reproduce51
dependency edges without missing/out-of-range targets. The prior PyJWT crypto,
Uvicorn standard and Psycopg binary extras remain; joserfc's optional `drafts`
extra is absent and brings in no pycryptodome package. This does not certify all
algorithms a library exposes as approved production algorithms.

The [saved closure observations](../../output/research/staff-identity-graph-2026-10-08/closure-observations.json)
bind exact registry/Python/wheel-tag/hash/yank checks and evaluation hash pins.
Both added exact-version PyPI dependency declarations match the report; their
wheel tags and Python>=3.10 requirements admit the observed Windows CPython3.14.5
host. The joserfc [release observations](../../output/research/staff-identity-graph-2026-10-08/joserfc-release-observations.json)
retain the `v1.7.5`404 and actual `1.7.5` non-draft/non-prerelease release object.
Its registry classifier says Production/Stable. Earlier source/registry reviews
retain their exact scope; no source-to-wheel provenance is inferred. Total
registry-declared compressed wheel download size is18,439,402bytes, not installed footprint.
The evaluation pins are not a portable/selected production lock or proof that
every independent newest release was evaluated together.

This closes a saved metadata-coupling question, not OIDC verification, callback
atomicity, bounded JWKS fetching, current staff eligibility, native compatibility,
licence/advisory clearance or actual sign-in. Context7 joserfc guidance and its
[official JWT guide](https://jose.authlib.org/en/guide/jwt/) distinguish signature
decoding from subsequent claim validation; the previously documented mandatory
issuer/audience/time/nonce/algorithm guards still apply. No lower-level verifier
or client behavior was imported or exercised here. This45-package candidate is
separate from the pending43-package native-trial request and does not expand its
permission or change its reviewed plan. Complete graph/platform qualification,
applicable execution authorization and integrated/founder acceptance remain.
The [82-input independent review](../../output/research/staff-identity-graph-2026-10-08/review/independent-review-identity-graph-v1.json)
passes its saved metadata replay; its distribution-size wording finding is
resolved by the separate [eight-input correction review](../../output/research/staff-identity-graph-2026-10-08/review/correction-1/independent-review-correction-1-v1.json).
Frozen reviewed bytes remain preserved; these later receipt links are outside
those inputs. Neither receipt supplies native, OIDC or integrated acceptance.

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

The [29-input independent distribution review](../../output/research/staff-identity-distribution-2026-10-09/independent-review-distributions-v1.json)
passes the exact saved two-wheel/licence/publishing observations and appendix.
Its [frozen reviewed document](../../output/research/staff-identity-distribution-2026-10-09/backend.proposed.md)
remains preserved. This later reference is outside those inputs; no signature,
complete-candidate licence, legal, native, sign-in or integrated acceptance follows.

## Isolated native library qualification — 2026-10-09

Status: DOING. The founder approved the existing 43-package frozen trial in
“approve all three and resume”. Exact hashed binary wheels were downloaded once
and installed offline into a separate pip-less research environment. All 43
normalized package names and exact versions match; pip check reports no broken
requirements. The [original stopped receipt](../../output/research/backend-crypto-graph-2026-10-08/native-trial/receipt.json)
is retained: the harness initially compared lowercased names without Python's
required separator normalization. The [explicit correction](../../output/research/backend-crypto-graph-2026-10-08/native-trial/continuation-correction.json)
applies the [PyPA name rule](https://packaging.python.org/en/latest/specifications/name-normalization/)
to both inventories and rejects collisions or any real name/version difference.
Only the remaining approved probes continued; no download or install repeated.

The [14 public-library probes](../../output/research/backend-crypto-graph-2026-10-08/native-trial/library-probes.xml)
pass with zero failures/errors/skips. They exercise RSA token rejection, strict
synthetic HTTP input/output, SQLite rollback/reuse, offline Alembic PostgreSQL
DDL, bcrypt boundaries, Uvicorn configuration and the actual async pytest plugin.
Psycopg reports binary client implementation and build/runtime libpq 180004;
no database connection, actual Hengshi route, Entra/OIDC or provider was exercised.
The [continuation receipt](../../output/research/backend-crypto-graph-2026-10-08/native-trial/continuation-receipt.json)
records 81,648,527 retained trial bytes and 5,390,553,088 free disk bytes at its
measurement, within the 256 MiB admission budget/1 GiB floor. These are dated
observations, not current free space or an OS hard quota. Six protected inputs
remain unchanged; Authlib/joserfc were not part of this 43-package execution.

One warning remains: Starlette 1.7.0 TestClient's HTTPX 0.28.1 fallback is
deprecated. The [saved installed/tagged source and registry observation](../../output/research/backend-crypto-graph-2026-10-08/native-result-review/test-client-observation.json)
identify the coupling question; passing probes do not approve this path for the
selected test-tool graph. No HTTPX2 package, warning suppression or exception
was added. Evaluate the mutually compatible stable graph before adoption.
Independent native-result review, full candidate licences/provenance/advisories,
reproducible locks and integrated/founder acceptance remain required. This
qualification selects no production package and authorizes no application upgrade.
