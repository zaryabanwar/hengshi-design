"""Frozen metadata replay only. Writes reviewer results, never producer inputs."""
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit
from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name as canonical, parse_wheel_filename
from packaging.version import Version

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT = HERE / "inputs"
BASE = INPUT / "output/research/backend-crypto-graph-2026-10-08"
sha = lambda b: hashlib.sha256(b).hexdigest()
read_json = lambda p: json.loads(p.read_text(encoding="utf-8"))
sys.stdout.reconfigure(encoding="utf-8")

raw = (HERE / "review-inputs.json").read_bytes()
assert sha(raw) == "0ee12b239f49ee02c1ae8868c8d0c02a2d9561c854f89c83e24271b0e2b8ad57"
manifest = json.loads(raw)
for item in manifest["inputs"]:
    b = (ROOT / item["snapshot"]).read_bytes()
    assert len(b) == item["bytes"] and sha(b) == item["sha256"], item["path"]
    assert (ROOT / item["path"]).read_bytes() == b, item["path"]

proposal = read_json(BASE / "proposal.json")
plan = read_json(BASE / "qualification-plan.json")
producer = read_json(BASE / "closure-observations.json")
receipt = read_json(BASE / "receipt.json")
report_raw = (BASE / "pip-report.json").read_bytes()
report = json.loads(report_raw)
assert sha(report_raw) == receipt["report_sha256"] == producer["report_sha256"]
assert receipt["exit_code"] == 0 and receipt["installation_performed"] is False
assert "--dry-run" in receipt["command"] and "--only-binary=:all:" in receipt["command"]
old_raw = (INPUT / proposal["basis_report"]).read_bytes()
assert sha(old_raw) == proposal["basis_report_sha256"]
old_report = json.loads(old_raw)
records = {canonical(r["metadata"]["name"]): r for r in report["install"]}
old = {canonical(r["metadata"]["name"]): r for r in old_report["install"]}
assert len(records) == len(report["install"]) == 43 and len(old) == 40
assert set(records) - set(old) == {"cryptography", "cffi", "pycparser"}
for n, r in old.items():
    assert records[n]["metadata"] == r["metadata"], n
    assert records[n]["download_info"] == r["download_info"], n
env = report["environment"]
host = default_environment()
assert all(host[k] == v for k, v in env.items())

roots_raw = (BASE / "candidate-roots.txt").read_bytes()
assert sha(roots_raw) == proposal["root_requirements_sha256"]
root_reqs = [Requirement(line) for line in roots_raw.decode().splitlines() if line and not line.startswith("#")]
root_map = {canonical(r.name): r for r in root_reqs}
assert len(root_map) == len(root_reqs) == 12
assert set(root_map) == {n for n, r in records.items() if r["requested"]}
assert set(root_map) == {n for n, r in old.items() if r["requested"]}
extras = {n: set() for n in records}
for n, r in root_map.items():
    assert r.url is None and r.specifier == SpecifierSet("==" + records[n]["metadata"]["version"])
    previous = set(old[n].get("requested_extras", []))
    assert set(r.extras) == (previous | {"crypto"} if n == "pyjwt" else previous)
    assert set(r.extras) == set(records[n].get("requested_extras", []))
    extras[n].update(r.extras)

edges = set()
changed = True
while changed:
    changed = False
    for n, record in records.items():
        for declaration in record["metadata"].get("requires_dist", []):
            req = Requirement(declaration)
            if req.marker and not any(req.marker.evaluate({**env, "extra": e}) for e in extras[n] | {""}):
                continue
            target = canonical(req.name)
            assert target in records and req.url is None, (n, declaration)
            assert req.specifier.contains(records[target]["metadata"]["version"], prereleases=False)
            edges.add((n, target, declaration))
            if set(req.extras) - extras[target]:
                extras[target].update(req.extras)
                changed = True
assert len(edges) == 48 and sorted(map(list, edges)) == producer["active_edges"]
reachable = set(root_map)
while True:
    expanded = reachable | {b for a, b, _ in edges if a in reachable}
    if expanded == reachable:
        break
    reachable = expanded
assert reachable == set(records)

tags = set(sys_tags())
observations = []
pins = {}
archive_bytes = 0
new_classifiers = {}
for n, record in sorted(records.items()):
    metadata = record["metadata"]
    version = Version(metadata["version"])
    assert not version.is_prerelease and not version.is_devrelease and not record["is_yanked"]
    assert SpecifierSet(metadata.get("requires_python") or "").contains(env["python_full_version"])
    info = record["download_info"]
    url = urlsplit(info["url"])
    assert url.scheme == "https" and url.hostname == "files.pythonhosted.org"
    filename = unquote(url.path.rsplit("/", 1)[-1])
    wn, wv, _, wt = parse_wheel_filename(filename)
    assert canonical(wn) == n and wv == version and wt & tags
    if n in old:
        rel = "core-recovery/pydantic-core-project.json.gz" if n == "pydantic-core" else f"primary/{n}-project.json.gz"
        registry_path = "output/research/backend-hash-inputs-2026-10-08/" + rel
    else:
        registry_path = f"output/research/backend-crypto-graph-2026-10-08/new-registry/{n}-exact.json.gz"
    registry_bytes = (INPUT / registry_path).read_bytes()
    registry = json.loads(gzip.decompress(registry_bytes))
    assert canonical(registry["info"]["name"]) == n
    assert Version(registry["info"]["version"]) == version
    norm = lambda vals: sorted(str(Requirement(x)) for x in vals or [])
    assert norm(registry["info"].get("requires_dist")) == norm(metadata.get("requires_dist")), n
    assert SpecifierSet(registry["info"].get("requires_python") or "") == SpecifierSet(metadata.get("requires_python") or "")
    files = registry["releases"][str(version)] if n in old else registry["urls"]
    match = [f for f in files if f["filename"] == filename and f["url"] == info["url"]]
    assert len(match) == 1
    wheel = match[0]
    digest = info["archive_info"]["hashes"]["sha256"]
    assert wheel["digests"]["sha256"] == digest and wheel["packagetype"] == "bdist_wheel" and not wheel["yanked"]
    assert SpecifierSet(wheel.get("requires_python") or "").contains(env["python_full_version"])
    archive_bytes += wheel["size"]
    pins[n] = (str(version), sorted(extras[n]), digest)
    observations.append({"name": n, "version": str(version), "extras": sorted(extras[n]), "wheel": filename,
                         "sha256": digest, "bytes": wheel["size"], "registry_snapshot": registry_path,
                         "registry_snapshot_sha256": sha(registry_bytes)})
    if n not in old:
        new_classifiers[n] = [x for x in registry["info"]["classifiers"] if x.startswith("Development Status")]
assert observations == producer["package_records"]
assert archive_bytes == producer["archive_bytes"] == plan["archive_bytes_from_registry"] == 18107329
hash_raw = (BASE / "candidate-hashed-requirements.txt").read_bytes()
assert sha(hash_raw) == producer["hashed_requirements_sha256"] == plan["candidate_sha256"]
hash_pins = {}
for line in hash_raw.decode().splitlines():
    if not line or line.startswith("#"):
        continue
    requirement, hashpart = line.split(" --hash=sha256:")
    req = Requirement(requirement)
    assert req.url is None and req.marker is None
    n = canonical(req.name)
    assert n not in hash_pins
    hash_pins[n] = (next(iter(req.specifier)).version, sorted(req.extras), hashpart)
assert hash_pins == pins
assert len(proposal["protected_inputs_before"]) == 6
for path, digest in proposal["protected_inputs_before"].items():
    assert sha((INPUT / path).read_bytes()) == sha((ROOT / path).read_bytes()) == digest

source_count = 0
for file in ("new-registry/sources.json", "primary-docs/sources.json"):
    for source in read_json(BASE / file)["sources"]:
        packed = (INPUT / source["snapshot"]).read_bytes()
        original = gzip.decompress(packed)
        assert len(original) == source["raw_bytes"] and sha(original) == source["raw_sha256"]
        if "snapshot_sha256" in source:
            assert sha(packed) == source["snapshot_sha256"]
        assert source["status"] == 200
        source_count += 1

before = (BASE / "before/backend-evidence-2026-10-04.md").read_bytes()
after = (INPUT / "docs/phase-1-compatibility/backend-evidence-2026-10-04.md").read_bytes()
assert after.startswith(before)
old_readme = (BASE / "before/README.md").read_text(encoding="utf-8").splitlines(keepends=True)
new_readme = (INPUT / "docs/phase-1-compatibility/README.md").read_text(encoding="utf-8").splitlines(keepends=True)
changes = [x for x in difflib.SequenceMatcher(a=old_readme, b=new_readme, autojunk=False).get_opcodes() if x[0] != "equal"]
assert len(changes) == 1 and changes[0][0] == "insert"
assert plan["execution_authorized"] is False
result = {"status": "DOING", "replay_verdict": "PASS", "scope": "Metadata closure and artifact integrity only; prospective plan requires separate verdict",
          "manifest_sha256": sha(raw), "frozen_live_input_count": len(manifest["inputs"]), "package_count": len(records),
          "active_edge_count": len(edges), "root_count": len(root_map), "previous_40_metadata_download_info_unchanged": True,
          "added": sorted(set(records) - set(old)), "all_records_root_reachable": True, "archive_bytes": archive_bytes,
          "compressed_bytes_are_not_installed_footprint": True, "protected_input_count": 6,
          "exact_source_raw_hash_count": source_count, "new_development_classifiers": new_classifiers,
          "backend_prefix_preserved_bytes": len(before), "readme_diff": "one insertion only", "edges": sorted(map(list, edges)),
          "package_observations": observations, "reviewer_read_repair": "An exploratory read initially omitted UTF-8; retried explicitly without input changes.",
          "limits": "No network, installation, wheel contents/native API/ABI, release/provenance/licence/security review or production selection."}
(HERE / "independent-replay-results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("replay_verdict", "frozen_live_input_count", "package_count", "active_edge_count", "archive_bytes")}))
