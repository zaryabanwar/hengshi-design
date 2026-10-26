# Independent backend compatibility-refresh review

Date: 2026-10-04. Reviewer: `review_publication_contract`; independent of producer.
Result: PASS. Open actionable findings: 0. No producer revision required.
Scope: nineteen-package PyPI observation, constrained core observation and evidence.

Independently fetched official PyPI latest and exact-version metadata for all
nineteen candidates, plus exact core 2.46.5 metadata. Recorded latest versions,
Requires-Python, complete Requires-Dist, available classifiers/license expressions,
distribution filenames/counts, SHA-256 and yanked flags match. Registry hashes
are observations; distribution contents/signatures were not downloaded or audited.

All forty-three recorded range/marker flags reproduce for CPython 3.14.5 on
Windows with no extras. Pydantic 2.13.5's exact core 2.46.5 edge rejects independently
latest core 2.49.0; the constrained alternative remains an observation, not a lock.
Every table entry matches snapshot and current virtualenv metadata. The observed
Python version/prefix and unchanged requirements hash match; pytest-asyncio metadata
is absent as described. No application imports or runtime tests were inferred.

Official [FastAPI version guidance](https://fastapi.tiangolo.com/deployment/versions/)
supports letting FastAPI resolve Starlette and testing a pinned compatible version.
[SQLAlchemy 2.1 migration guidance](https://docs.sqlalchemy.org/en/21/changelog/migration_21.html)
supports the Python floor, default PostgreSQL-driver and asyncio/autoflush cautions.
[bcrypt 5.0.0 notes](https://pypi.org/project/bcrypt/5.0.0/) explicitly describe
the over-72-byte ValueError; the evidence does not replace credential policy.

[Psycopg installation guidance](https://www.psycopg.org/psycopg3/docs/basic/install.html)
currently identifies itself as 3.3.7.dev1. It prefers locally linked C installation
for production, while offering binary installation when build prerequisites are
unavailable; this is guidance, not a categorical ban on binary production packages.
The evidence appropriately leaves selected-release behavior and packaging unresolved.
The Windows CPython 3.14 binary filename is present, without proving load or libpq ABI.

Non-prerelease version syntax does not settle production stability. Both observed
core versions and Starlette carry Alpha classifiers; FastAPI, Uvicorn and HTTPX
carry Beta classifiers. Exact maintainer support/release evidence remains required
under the stated stable-only gate; no candidate is approved by this review.

## Exact reviewed bytes

SHA-256:

- `backend-evidence-2026-10-04.md`: `806DD2F2D60DA1360708689771DACA5490982991283E4F6DE28150F63863AD26`
- `backend-candidates-2026-10-04.json`: `A9E5485AEB506A8746787B77C2510DA00983D4AD26DA146790BF3A7187008BC0`
- `apps/api/requirements.txt`: `B99F98E119CB6653F38B19D1EE83CC7F33D92A699083645CA19369A8912E89BD`

PASS means bounded evidence consistency, not complete graph compatibility, security,
license clearance, production selection or Phase 1 approval. Extras/transitives,
actual target OS/ABI, clean hash-locked installation, integration tests, JWT crypto,
cloud/database GA evidence and rollback proof remain required. No producer file,
dependency, lock, application, installed environment or service was changed.


## Later disposition: Windows resolver and Pydantic source channel

Date: 2026-10-04. Independent reviewer: `review_publication_contract`.
Result: PASS for this bounded evidence follow-up. Open actionable findings: 0.
The original report above remains unchanged and applies only to its original hashes.
A factual clarification was inspected: tag/current policy copies have identical
bytes; the revised producer text no longer implies a policy change between them.

Recomputed active Requires-Dist from the raw pip report using its recorded Windows
CPython 3.14.5 markers and fixed-point propagated extras. Forty resolved wheel
records cover twelve requested families; Uvicorn standard and Psycopg binary are
the active extras. All forty-five active clauses and Requires-Python ranges pass,
and the combined analysis agrees. Core resolves to 2.46.5; no preview/dev or yanked
record appears. Exit/output agree with resolution, not installed runtime behavior.
Official pip documentation and installed pip's dry-run return path support the
no-install mechanism; the reviewer did not rerun the resolver or candidates.
The protected-input receipt and combined hashes match current protected files.

All twelve local source-response files match receipt byte lengths and SHA-256.
Fresh primary fetches match seven source texts byte-for-byte and the significant
API ref/tag fields. Both annotated refs peel to the same recorded commit; pinned
Pydantic requires core 2.46.5 and its pinned Cargo version is 2.46.5. Both tag
objects remain unsigned/unverified; the core annotation's 2.46.3 discrepancy is
retained. Standalone repository archival and both release-object 404 observations
are confirmed; a 404 does not deny the independently established monorepo tag.
Uvicorn/Pydantic release draft/prerelease fields match their primary API records.
The public version policy contextualizes tags, minor-release guarantees and their
exceptions; core Alpha classification remains visible. No experimental API,
signed tag, wheel-to-source build attestation or complete stable graph is approved.

Exact SHA-256 (research paths relative to `output/research/compatibility-resolution-2026-10-04/`):

- Current `docs/phase-1-compatibility/backend-evidence-2026-10-04.md`: `4D500C5C398722BC8E68447044F4C07A9402F2DFF6BDE926A239E293C129C153`
- Unchanged `backend-candidates-2026-10-04.json`: `A9E5485AEB506A8746787B77C2510DA00983D4AD26DA146790BF3A7187008BC0`
- `backend-windows/requirements-study.txt`: `2D588F1262F7C04D8BAA100E18BFD6AAB903C501E7B5408FCF2D298FD469FCAE`
- `backend-windows/pip-report.json`: `B9A135FA96EE978AF2011EA4E4B8F848FD44235DB46349CAED74CC61ECC2C8F6`
- `backend-windows/resolver-output.txt`: `E55ED332DA06A98619C29D7C7D4DBD5BB12941EE552A332631BA67E55A24FAE5`
- `backend-windows/resolver-exit-code.txt`: `13BF7B3039C63BF5A50491FA3CFD8EB4E699D1BA1436315AEF9CBE5711530354`
- `backend-windows/pydantic-source-channel-evidence.json`: `A6EB0C83A2431F0BAAE0242AA63ED07F55E28558C8638BEEF2A4AAEB2392DD89` (binds all twelve raw source files and their individual hashes)
- `resolution-analysis.json`: `8F08D32270DFBF06ED11BF72C5639ACF0FA08E07E1DFC28567CC9FDD50A994D0`
- `release-channel-checks.json`: `6E42A028D39A9286490AD7F19D730C989A160E27CF32514EC59FCB8C1CB68813`
- `protected-input-hashes.json`: `8F15A53BC1BF2C0CB92F536624E955B06725BC31B5BFF3007D8B2729527A0661`

PASS establishes evidence consistency and source-location/version association,
not imports, native ABI, clean locked installation, database/API behavior,
distribution attestation, advisory/license clearance, final platform graph,
MA-013 or Phase 1 acceptance. Prior native/inventory/QA review scopes remain;
the QA exception is not accepted here. No producer, application, service,
credential, migration or external write was changed by this review.
