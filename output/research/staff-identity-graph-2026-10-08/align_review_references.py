"""Link actual scoped review receipts without modifying frozen review inputs."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
initial = HERE / "review/independent-review-identity-graph-v1.json"
correction = HERE / "review/correction-1/independent-review-correction-1-v1.json"
if not correction.is_file():
    raise SystemExit("Independent correction receipt must exist first")
verdict = json.loads(correction.read_bytes())
if verdict.get("verdict") != "PASS":
    raise SystemExit("Correction has not independently passed")
alignment = HERE / "review/reference-alignment"
if alignment.exists():
    raise SystemExit("References already aligned; do not overwrite")
changes = [
    ("docs/phase-1-compatibility/backend-evidence-2026-10-04.md",
     b"Independent review of this new metadata appendix is pending; earlier receipts\ndo not cover its report or observations.",
     b"The [82-input independent review](../../output/research/staff-identity-graph-2026-10-08/review/independent-review-identity-graph-v1.json)\npasses its saved metadata replay; its distribution-size wording finding is\nresolved by the separate [eight-input correction review](../../output/research/staff-identity-graph-2026-10-08/review/correction-1/independent-review-correction-1-v1.json).\nFrozen reviewed bytes remain preserved; these later receipt links are outside\nthose inputs. Neither receipt supplies native, OIDC or integrated acceptance."),
    ("docs/software-definition/04-reconciliation-map.md",
     b"This new metadata study awaits independent review and supplies no native/OIDC qualification or expanded trial permission.",
     b"Its [82-input independent metadata replay](../../output/research/staff-identity-graph-2026-10-08/review/independent-review-identity-graph-v1.json) passes, with its sole size-label finding resolved by a separate [eight-input correction PASS](../../output/research/staff-identity-graph-2026-10-08/review/correction-1/independent-review-correction-1-v1.json). These bounded receipts supply no native/OIDC qualification or expanded trial permission."),
]
prepared = []
for rel, old, new in changes:
    raw = (ROOT / rel).read_bytes()
    if raw.count(old) != 1:
        raise SystemExit(f"Expected exact unique segment in {rel}")
    prepared.append((rel, raw, raw.replace(old, new, 1)))
alignment.mkdir()
results = []
for rel, before, after in prepared:
    (alignment / (Path(rel).name + ".before")).write_bytes(before)
    (ROOT / rel).write_bytes(after)
    results.append({"path": rel, "before_sha256": hashlib.sha256(before).hexdigest(),
                    "after_sha256": hashlib.sha256(after).hexdigest(),
                    "scope": "Receipt reference segment only"})
output = {"status": "DOING", "scope": "Later navigation references outside frozen review inputs",
          "initial_review_sha256": hashlib.sha256(initial.read_bytes()).hexdigest(),
          "correction_review_sha256": hashlib.sha256(correction.read_bytes()).hexdigest(),
          "changes": results}
(alignment / "reference-update.json").write_bytes((json.dumps(output, indent=2) + "\n").encode())
print(json.dumps(output))
