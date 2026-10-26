"""Freeze the bounded compatibility proposal; no installation or app mutation."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    path.write_bytes((json.dumps(value, indent=2) + "\n").encode())


plan = {
    "status": "TODO", "execution_authorized": False,
    "scope": "Proposed isolated Windows library qualification, not Hengshi feature implementation or stack adoption",
    "candidate": "candidate-hashed-requirements.txt",
    "candidate_sha256": sha((HERE / "candidate-hashed-requirements.txt").read_bytes()),
    "archive_bytes_from_registry": 18107329,
    "target": "output/research/backend-crypto-graph-2026-10-08/native-trial",
    "limits": {
        "new_output_budget_bytes": 268435456,
        "minimum_free_disk_bytes": 1073741824,
        "command_deadline_seconds": 180,
        "no_source_builds": True,
        "no_existing_environment_changes": True,
        "no_database_or_provider_connection": True,
        "no_automatic_cleanup": True
    },
    "steps": [
        "Require applicable founder authorization before creating or installing into the new research environment; independently review this proposal first.",
        "Recheck frozen inputs, current native Python/pip identity, free disk and exact candidate hashes; refuse an existing target or incompatible host.",
        "Use native Python venv --without-pip for the new target. Existing pip is the recorded bootstrap tool, not a newly selected production toolchain.",
        "Download only the 43 exact hashed binary wheels with --require-hashes --only-binary=:all: --no-deps --no-cache-dir into the dedicated wheelhouse; enforce budget before offline installation.",
        "Use existing pip --python <new-environment-python> with --no-index --find-links <wheelhouse> --require-hashes --only-binary=:all: --no-deps --no-cache-dir to install only into that new environment. No source build or dependency re-resolution.",
        "Run pip check and the synthetic public-library probes below with bytecode disabled, no application import or server/listener and no real tokens, accounts or data.",
        "Measure retained output size and verify protected inputs unchanged; stop on failure. Preserve errors rather than reinterpret or silently retry. Deletion needs separate approval."
    ],
    "probes": [
        {"boundary": "PyJWT + cryptography", "cases": "Locally generated RSA key: valid RS256 token with explicit algorithm, issuer and audience succeeds; wrong key, wrong audience, expired token and disallowed algorithm fail. No Entra token or live JWKS.", "limit": "Primitive coupling only; no OIDC/PKCE/nonce discovery client, identity grant or Hengshi session enforcement."},
        {"boundary": "FastAPI + Pydantic + HTTPX TestClient", "cases": "Strict integer plus extra-forbid request accepts a valid integer and rejects coercible text/unknown fields; explicit response model returns expected UTC serialization.", "limit": "In-process synthetic library fixture, no actual Hengshi route, socket, security or production serialization coverage."},
        {"boundary": "SQLAlchemy", "cases": "In-memory SQLite transaction rollback leaves no committed row after an intentional failure; subsequent transaction remains usable.", "limit": "No PostgreSQL/Psycopg persistence, network pool or concurrency assurance."},
        {"boundary": "Alembic", "cases": "Public offline PostgreSQL dialect context emits DDL for a synthetic table without a database connection.", "limit": "No migration run, real schema or rollback exercise."},
        {"boundary": "Psycopg binary", "cases": "Import public pq API; record implementation/build/runtime libpq versions without connecting.", "limit": "Native import only, no database protocol, authentication or driver transaction assurance."},
        {"boundary": "bcrypt", "cases": "Synthetic short password verifies; incorrect password fails; 73-byte input raises the version's documented length error.", "limit": "No production password policy, emergency access or password storage adoption."},
        {"boundary": "Uvicorn", "cases": "Load a synthetic ASGI application configuration without running or binding the server.", "limit": "No actual listener, websocket, shutdown, load or deployment proof."},
        {"boundary": "pytest + pytest-asyncio", "cases": "Run an actual async synthetic test through the installed plugin and report package identities and failures.", "limit": "Test tooling coupling only, not application coverage."}
    ],
    "official_patterns": [
        "https://pip.pypa.io/en/stable/topics/python-option/",
        "https://pip.pypa.io/en/stable/topics/secure-installs/",
        "https://fastapi.tiangolo.com/tutorial/testing/",
        "https://docs.sqlalchemy.org/en/21/core/connections.html",
        "https://alembic.sqlalchemy.org/en/latest/api/runtime.html",
        "https://www.psycopg.org/psycopg3/docs/api/pq.html"
    ],
    "remaining": [
        "Whole-graph newest-compatible recheck, production tools/platform selection and reproducible final lock",
        "Supported release channel, provenance/attestations, full licence and advisory review",
        "Maintained OIDC/PKCE adapter selection and its complete extra graph",
        "Approved actual identity/API/database/authorization/recovery behavior and named environment qualification",
        "Independent results review and integrated/founder acceptance; no dependency adoption implied"
    ]
}
write_json(HERE / "qualification-plan.json", plan)

backend = ROOT / "docs/phase-1-compatibility/backend-evidence-2026-10-04.md"
index = ROOT / "docs/phase-1-compatibility/README.md"
before = HERE / "before"
before.mkdir(exist_ok=True)
for path in (backend, index):
    (before / path.name).write_bytes(path.read_bytes())

appendix = '''
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
scope; the three additions and this appendix require separate independent review.
Asymmetric JWT primitives do not supply a complete maintained OIDC/PKCE client.
That adapter, its graph, current staff mapping/session checks and actual Entra
qualification are still unselected/unimplemented.

The [proposed native qualification plan](../../output/research/backend-crypto-graph-2026-10-08/qualification-plan.json)
uses a new pip-less research virtualenv, exact hash-checked binary wheels and
offline installation through pip's documented `--python` support. Metadata totals
18,107,329 archive bytes; the proposed new-output budget is256MiB with at least1GiB
free disk retained. Preflight and measured footprint checks precede installation;
refuse an existing target, source builds or changed protected inputs. Existing
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
'''
backend.write_bytes(backend.read_bytes() + appendix.encode())
entry = '''
The [asymmetric JWT closure and proposed native qualification](backend-evidence-2026-10-04.md#asymmetric-jwt-dependency-closure-and-proposed-native-qualification--2026-10-08)
adds a research PyJWT crypto extra:43 Windows package records and48 active edges,
with the previous40 metadata/artifacts unchanged. No packages were installed and
no complete OIDC client is selected. The bounded native trial is prepared, not
authorized or executed; earlier receipts do not review the three additions.
Independent review, full graph selection and integrated acceptance remain held.

'''
raw = index.read_bytes()
anchor = b"## Current authority and dated evidence\r\n"
assert raw.count(anchor) == 1
index.write_bytes(raw.replace(anchor, anchor + entry.encode(), 1))

packet = HERE / "review"
packet.mkdir(exist_ok=True)
files = [
    "AGENTS.md", ".specify/memory/constitution.md", "PROJECT.md", "DECISIONS.md",
    "PROJECT_STATE.yaml", "TASKS.md", "docs/software-definition/README.md",
    "docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md",
    "specs/001-platform-security-hardening/spec.md",
    "docs/phase-1-compatibility/backend-evidence-2026-10-04.md",
    "docs/phase-1-compatibility/README.md",
    "output/research/backend-current-review-2026-10-08/independent-review-backend-current-v1.json",
    "output/research/backend-hash-inputs-2026-10-08/latest-coupled-resolution/pip-report.json"
]
files += list(json.loads((HERE / "proposal.json").read_bytes())["protected_inputs_before"])
files += [p.relative_to(ROOT).as_posix() for p in HERE.rglob("*")
          if p.is_file() and "review" not in p.relative_to(HERE).parts]
observations = json.loads((HERE / "closure-observations.json").read_bytes())
files += [x["registry_snapshot"] for x in observations["package_records"]]
inputs = []
for number, rel in enumerate(dict.fromkeys(files), 1):
    source = ROOT / rel
    raw = source.read_bytes()
    target = packet / "inputs" / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    inputs.append({"path": rel, "snapshot": target.relative_to(ROOT).as_posix(),
                   "bytes": len(raw), "sha256": sha(raw)})
write_json(packet / "review-inputs.json", {
    "status": "DOING", "scope": "Crypto metadata closure plus proposed bounded native trial, no execution or adoption",
    "inputs": inputs, "revision_cycle": 0,
    "review_receipt_target": "independent-review-crypto-graph-v1.json"
})
print(json.dumps({"inputs": len(inputs), "manifest_sha256": sha((packet / "review-inputs.json").read_bytes()),
                  "canonical": {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in (backend, index)}}))
