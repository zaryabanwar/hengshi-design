"""Associate selected archive notices with an official immutable source commit."""
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import tarfile
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0"

def sha(data):
    return hashlib.sha256(data).hexdigest().upper()

def save(name, data):
    path = OUT / name
    if path.exists():
        raise RuntimeError(f"Evidence already exists: {name}")
    path.write_bytes(data)
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "bytes": len(data), "sha256": sha(data)}

def fetch(url, name):
    with urlopen(Request(url, headers={"User-Agent": "Hengshi-candidate-notice-inspection/1.0"}), timeout=25) as response:
        raw = response.read()
        receipt = {"requested_url": url, "final_url": response.url, "status": response.status,
                   "observed_at": datetime.now(timezone.utc).isoformat()}
    return raw, {**receipt, **save(name, raw)}

inspection_raw = (OUT / "inspection.json").read_bytes()
inspection = json.loads(inspection_raw)
archive_raw = (OUT / "gsap-3.15.0.tgz").read_bytes()
assert sha(archive_raw) == inspection["archive"]["sha256"]
assert not inspection["git_head"], "This study assumes no npm gitHead"
tag_raw, tag_receipt = fetch("https://api.github.com/repos/greensock/GSAP/git/ref/tags/3.15.0", "official-tag.json")
tag = json.loads(tag_raw)
assert tag["ref"] == "refs/tags/3.15.0"
assert tag["object"]["type"] == "commit", "Resolve annotated tags explicitly before comparison"
commit = tag["object"]["sha"]
comparisons = []
with tarfile.open(fileobj=io.BytesIO(archive_raw), mode="r:gz") as archive:
    for source_path in ["README.md", "src/gsap-core.js", "dist/gsap.js", "dist/gsap.min.js"]:
        packed = archive.extractfile("package/" + source_path).read()
        source, receipt = fetch(f"https://raw.githubusercontent.com/greensock/GSAP/{commit}/{source_path}",
                                "source-" + source_path.replace("/", "--"))
        comparison = {"archive_path": "package/" + source_path, "archive_sha256": sha(packed),
                      "official_source": receipt, "bytes_equal": packed == source}
        if source_path == "README.md":
            comparison["archive_readme"] = save("archive-README.md", packed)
        comparisons.append(comparison)
report = {"status": "DOING", "date": "2026-10-04", "scope": "Selected notice-bearing files only; no source-build attestation or licence clearance",
          "prior_inspection_sha256": sha(inspection_raw), "official_tag": tag_receipt,
          "tag_commit": commit, "npm_git_head_absent": True, "comparisons": comparisons,
          "archive_integrity_rechecked": True, "downloaded_code_executed": False,
          "production_selected": False}
receipt = save("source-association.json", (json.dumps(report, indent=2) + "\n").encode("utf-8"))
print(json.dumps({"receipt": receipt, "commit": commit,
                  "comparisons": [{"path": row["archive_path"], "bytes_equal": row["bytes_equal"]} for row in comparisons]}, indent=2))
