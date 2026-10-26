"""Read candidate archives as data; never install or execute downloaded code."""
import base64
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import tarfile
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "output/research/compatibility-resolution-2026-10-04/gsap-notice-3.15.0"
OUT.mkdir(exist_ok=True)
LOCK = ROOT / "output/research/compatibility-resolution-2026-10-04/native-lint-probe/package-lock.json"
PROTECTED = [
    "apps/web/package.json", "apps/web/package-lock.json", "apps/api/requirements.txt",
    "output/research/compatibility-resolution-2026-10-04/native-lint-probe/package.json",
    str(LOCK.relative_to(ROOT)).replace("\\", "/"),
]

def digest(data):
    return hashlib.sha256(data).hexdigest().upper()

def protected_hashes():
    return {name: digest((ROOT / name).read_bytes()) for name in PROTECTED}

def save(name, data):
    destination = OUT / name
    if destination.exists() and destination.read_bytes() != data:
        raise RuntimeError(f"Refusing to replace prior evidence: {name}")
    destination.write_bytes(data)
    return {"path": str(destination.relative_to(ROOT)).replace("\\", "/"),
            "bytes": len(data), "sha256": digest(data)}

def fetch(url, filename):
    request = Request(url, headers={"User-Agent": "Hengshi-candidate-notice-inspection/1.0"})
    with urlopen(request, timeout=25) as response:
        data = response.read()
        observation = {"requested_url": url, "final_url": response.url,
                       "status": response.status, "content_type": response.headers.get("Content-Type"),
                       "observed_at": datetime.now(timezone.utc).isoformat()}
    observation.update(save(filename, data))
    return data, observation

before = protected_hashes()
lock_data = json.loads(LOCK.read_text(encoding="utf-8"))
entry = lock_data["packages"]["node_modules/gsap"]
assert entry["version"] == "3.15.0", "Candidate identity changed"
metadata_raw, metadata_receipt = fetch("https://registry.npmjs.org/gsap/3.15.0", "registry.json")
metadata = json.loads(metadata_raw)
assert metadata["name"] == "gsap" and metadata["version"] == entry["version"]
assert metadata["dist"]["tarball"] == entry["resolved"]
assert metadata["dist"]["integrity"] == entry["integrity"]
archive_raw, archive_receipt = fetch(entry["resolved"], "gsap-3.15.0.tgz")
assert entry["integrity"].startswith("sha512-")
actual_integrity = "sha512-" + base64.b64encode(hashlib.sha512(archive_raw).digest()).decode("ascii")
assert actual_integrity == entry["integrity"], "Archive integrity mismatch"
inventory, notices, headers = [], [], []
with tarfile.open(fileobj=io.BytesIO(archive_raw), mode="r:gz") as archive:
    for member in archive.getmembers():
        if not member.isfile():
            continue
        content = archive.extractfile(member).read()
        inventory.append({"path": member.name, "bytes": len(content), "sha256": digest(content)})
        if member.name == "package/package.json":
            manifest = json.loads(content)
        if Path(member.name).name.lower() in {"license", "licence", "license.txt", "copying", "notice"}:
            notice_text = content.decode("utf-8")
            record = save("archive-" + Path(member.name).name, content)
            notices.append({"archive_path": member.name, "text": notice_text, **record})
        if member.name in {"package/dist/gsap.js", "package/dist/gsap.min.js", "package/src/gsap-core.js", "package/gsap-core.js"}:
            headers.append({"path": member.name, "sha256": digest(content),
                            "first_1200_characters": content.decode("utf-8")[:1200]})
assert manifest["name"] == "gsap" and manifest["version"] == "3.15.0"
source_receipts = []
for url, filename in [
    ("https://gsap.com/standard-license/", "official-standard-license.html"),
    ("https://webflow.com/legal/terms", "incorporated-webflow-terms.html"),
]:
    try:
        _, receipt = fetch(url, filename)
        source_receipts.append(receipt)
    except Exception as error:
        source_receipts.append({"requested_url": url, "error_type": type(error).__name__, "error": str(error)})
git_head = metadata.get("gitHead")
if git_head:
    try:
        source_bytes, receipt = fetch(f"https://raw.githubusercontent.com/greensock/GSAP/{git_head}/LICENSE", "pinned-source-LICENSE")
        source_receipts.append({**receipt, "matches_archive_license": any(source_bytes.decode("utf-8") == notice["text"] for notice in notices)})
    except Exception as error:
        source_receipts.append({"git_head": git_head, "error_type": type(error).__name__, "error": str(error)})
after = protected_hashes()
assert before == after, "Protected input changed during read-only inspection"
report = {
    "status": "DOING", "date": "2026-10-04", "scope": "Unselected candidate package notice evidence, not legal clearance, a build SBOM or production compatibility",
    "package": "gsap", "version": "3.15.0", "candidate_lock": str(LOCK.relative_to(ROOT)).replace("\\", "/"),
    "lock_entry": entry, "metadata": metadata_receipt, "archive": archive_receipt,
    "registry_license": metadata.get("license"), "archive_manifest_license": manifest.get("license"),
    "git_head": git_head, "archive_integrity_matches_lock_and_registry": True,
    "archive_files": inventory, "notice_files": notices, "selected_source_headers": headers,
    "official_sources": source_receipts, "protected_hashes_before": before, "protected_hashes_after": after,
    "downloaded_code_executed": False, "dependencies_installed": False, "production_selected": False,
}
receipt = save("inspection.json", (json.dumps(report, indent=2) + "\n").encode("utf-8"))
print(json.dumps({"inspection": receipt, "archive_regular_files": len(inventory),
                  "notice_files": [notice["archive_path"] for notice in notices],
                  "manifest_license": manifest.get("license"), "sources": source_receipts,
                  "protected_inputs_unchanged": before == after}, indent=2))
