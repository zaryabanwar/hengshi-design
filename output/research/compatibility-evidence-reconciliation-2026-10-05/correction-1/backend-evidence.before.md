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
  within that range. Windows dependency markers and chosen extras are distinct
  from Linux production markers. The snapshot's edge flags evaluate only the
  observed Windows runtime with no extras and are deliberately not a full resolver.

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
Finish Python support/ABI, JWT crypto, Uvicorn extras, database/libpq, Azure GA and
production image/OS graphs. SQLAlchemy, Pydantic and native wheels require focused
behavior tests plus one relevant suite in their separately reversible backend wave.

The requirements, application, native services and database are unchanged here.
An authorized rollback must restore the previous coherent environment/source/lock
and repeat affected evidence; no live rollback or installation was performed.
MA-013, exact production selection and complete Phase 1 acceptance remain open.
