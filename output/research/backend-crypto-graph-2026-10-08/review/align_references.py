"""Link scoped receipts without changing frozen reviewed inputs."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE / "reference-alignment"
OUT.mkdir(exist_ok=True)
backend = ROOT / "docs/phase-1-compatibility/backend-evidence-2026-10-04.md"
index = ROOT / "docs/phase-1-compatibility/README.md"
changes = []


def update(path, old, new):
    raw = path.read_bytes()
    assert raw.count(old.encode()) == 1
    (OUT / path.name).write_bytes(raw)
    result = raw.replace(old.encode(), new.encode(), 1)
    path.write_bytes(result)
    changes.append({"path": path.relative_to(ROOT).as_posix(),
                    "before_sha256": hashlib.sha256(raw).hexdigest(),
                    "after_sha256": hashlib.sha256(result).hexdigest()})


update(backend,
       "scope; the three additions and this appendix require separate independent review.",
       """scope. The [79-input initial review](../../output/research/backend-crypto-graph-2026-10-08/review/independent-review-crypto-graph-v1.json)
independently reproduced the metadata closure and requested a footprint-plan
correction. The [ten-input correction1 review](../../output/research/backend-crypto-graph-2026-10-08/review/correction-1/independent-review-correction-1-v1.json)
records PASS for the prospective admission/reservation repair only. Its inspected
inputs remain frozen; these later receipt references are outside those bytes.
No installation, native qualification or production acceptance follows.""")
update(index,
       """authorized or executed; earlier receipts do not review the three additions.
Independent review, full graph selection and integrated acceptance remain held.""",
       """authorized or executed. The [79-input review](../../output/research/backend-crypto-graph-2026-10-08/review/independent-review-crypto-graph-v1.json)
reproduced the metadata closure and requested a footprint repair; the separate
[ten-input correction1 review](../../output/research/backend-crypto-graph-2026-10-08/review/correction-1/independent-review-correction-1-v1.json)
passes the prospective admission/overhead plan. Later receipt references are
outside inspected inputs. Native execution/qualification, full graph selection
and integrated acceptance remain held.""")
(OUT / "reference-update.json").write_bytes((json.dumps({
    "status": "DOING", "scope": "Scoped receipt references only; not a new review or changed reviewed input",
    "changes": changes, "application_changed": False, "installation_performed": False
}, indent=2) + "\n").encode())
print(json.dumps(changes))
