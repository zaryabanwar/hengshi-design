"""Document the unselected metadata experiment and freeze its review inputs."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
backend = ROOT / "docs/phase-1-compatibility/backend-evidence-2026-10-04.md"
mapping = ROOT / "docs/software-definition/04-reconciliation-map.md"
before = HERE / "before"
before.mkdir(exist_ok=True)
for p in (backend, mapping):
    (before / p.name).write_bytes(p.read_bytes())

appendix = '''
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
compressed registry archive size is18,439,402bytes, not installed footprint.
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
Independent review of this new metadata appendix is pending; earlier receipts
do not cover its report or observations.
'''
backend.write_bytes(backend.read_bytes()+appendix.encode())
raw = mapping.read_bytes()
old = b"Neither client nor its graph is selected or included in the43-package trial."
new = b"Neither client nor its graph is selected or included in the43-package trial. A later [45-package Authlib candidate dry run](../phase-1-compatibility/backend-evidence-2026-10-04.md#staff-identity-candidate-dependency-closure--2026-10-08) adds only Authlib/joserfc with all43 prior metadata/artifact associations unchanged. This new metadata study awaits independent review and supplies no native/OIDC qualification or expanded trial permission."
assert raw.count(old) == 1
mapping.write_bytes(raw.replace(old, new, 1))

packet = HERE / "review"
packet.mkdir(exist_ok=True)
paths = ["AGENTS.md", ".specify/memory/constitution.md", "PROJECT.md", "DECISIONS.md",
         "PROJECT_STATE.yaml", "TASKS.md", "docs/software-definition/README.md",
         "docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md",
         "specs/001-platform-security-hardening/spec.md",
         "docs/phase-1-compatibility/backend-evidence-2026-10-04.md",
         "docs/software-definition/04-reconciliation-map.md",
         "output/research/backend-crypto-graph-2026-10-08/pip-report.json",
         "output/research/backend-crypto-graph-2026-10-08/closure-observations.json",
         "output/research/backend-crypto-graph-2026-10-08/candidate-roots.txt",
         "output/research/backend-crypto-graph-2026-10-08/qualification-plan.json",
         "output/research/staff-identity-client-options-2026-10-08/review/independent-review-identity-client-options-v1.json"]
paths += [p.relative_to(ROOT).as_posix() for p in HERE.rglob("*")
          if p.is_file() and "review" not in p.relative_to(HERE).parts]
observations = json.loads((HERE / "closure-observations.json").read_bytes())
paths += [x["registry_snapshot"] for x in observations["package_records"]]
receipt = json.loads((HERE / "receipt.json").read_bytes())
paths += list(receipt["protected_inputs_before"])
inputs = []
for rel in dict.fromkeys(paths):
    p = ROOT / rel
    raw = p.read_bytes()
    target = packet / "inputs" / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    inputs.append({"path": rel, "snapshot": target.relative_to(ROOT).as_posix(),
                   "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
(packet / "review-inputs.json").write_bytes((json.dumps({"status": "DOING", "revision_cycle": 0,
    "scope": "Unselected Windows Authlib candidate metadata closure and scoped navigation addition only",
    "inputs": inputs}, indent=2)+"\n").encode())
print(json.dumps({"inputs": len(inputs), "manifest_sha256": hashlib.sha256((packet / "review-inputs.json").read_bytes()).hexdigest()}))
