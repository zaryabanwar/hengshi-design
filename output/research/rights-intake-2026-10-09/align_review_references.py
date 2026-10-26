"""Link existing bounded review receipts outside their frozen inputs."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
initial = HERE / "review/independent-review-rights-intake-v1.json"
correction = HERE / "review/correction-1/independent-review-correction-1-v1.json"
if not correction.exists() or json.loads(correction.read_bytes()).get("verdict") != "PASS":
    raise SystemExit("Correction must independently pass first")
target = HERE / "review/reference-alignment"
if target.exists():
    raise SystemExit("Preserve existing alignment")
changes = [
    ("docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md",
     b"preserve raw and compressed identities. Independent review of this addition is\npending; no legal clearance, mailbox verification or runtime assurance is claimed.",
     b"preserve raw and compressed identities. The [28-input independent review](../../../output/research/rights-intake-2026-10-09/review/independent-review-rights-intake-v1.json)\nverified source/definition consistency except its mixed-data finding, resolved by\nthe separate [eight-input correction PASS](../../../output/research/rights-intake-2026-10-09/review/correction-1/independent-review-correction-1-v1.json).\nThese later receipt links are outside frozen reviewed bytes. No legal clearance,\nmailbox verification, adoption or runtime assurance is claimed."),
    ("docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md",
     b"The proposal needs independent/integrated acceptance; no adapter is implemented.",
     b"The [28-input independent review](../../../output/research/rights-intake-2026-10-09/review/independent-review-rights-intake-v1.json) and separate [eight-input correction PASS](../../../output/research/rights-intake-2026-10-09/review/correction-1/independent-review-correction-1-v1.json)\ncover their exact logical/source consistency scopes; later receipt links remain\noutside those frozen inputs. Operating/legal and integrated/founder acceptance\nremain required; no adapter is implemented."),
]
prepared = []
for rel, old, new in changes:
    before = (ROOT / rel).read_bytes()
    if before.count(old) != 1:
        raise SystemExit(f"Exact unique reference missing: {rel}")
    prepared.append((rel, before, before.replace(old, new, 1)))
target.mkdir()
results = []
for rel, before, after in prepared:
    (target / (Path(rel).name + ".before")).write_bytes(before)
    (ROOT / rel).write_bytes(after)
    results.append({"path": rel, "before_sha256": hashlib.sha256(before).hexdigest(),
                    "after_sha256": hashlib.sha256(after).hexdigest()})
record = {"status": "DOING", "scope": "Later receipt references only",
          "initial_review_sha256": hashlib.sha256(initial.read_bytes()).hexdigest(),
          "correction_review_sha256": hashlib.sha256(correction.read_bytes()).hexdigest(),
          "changes": results}
(target / "reference-update.json").write_bytes((json.dumps(record, indent=2) + "\n").encode())
print(json.dumps(record))
