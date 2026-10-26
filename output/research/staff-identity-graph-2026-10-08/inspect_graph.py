"""Verify saved resolver/registry observations, not native or OIDC behavior."""
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name, parse_wheel_filename
from packaging.version import Version

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASIS = ROOT / "output/research/backend-crypto-graph-2026-10-08"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, value):
    path.write_bytes((json.dumps(value, indent=2) + "\n").encode())


report_raw = (HERE / "pip-report.json").read_bytes()
report = json.loads(report_raw)
receipt = json.loads((HERE / "receipt.json").read_bytes())
assert receipt["exit_code"] == 0 and not receipt["installation_performed"]
assert sha(report_raw) == receipt["report_sha256"]
old_raw = (BASIS / "pip-report.json").read_bytes()
assert sha(old_raw) == receipt["basis_report_sha256"]
records = {canonicalize_name(x["metadata"]["name"]): x for x in report["install"]}
old = {canonicalize_name(x["metadata"]["name"]): x for x in json.loads(old_raw)["install"]}
assert len(records) == len(report["install"]) == 45
assert set(records) - set(old) == {"authlib", "joserfc"}
for name, entry in old.items():
    assert records[name]["metadata"] == entry["metadata"], name
    assert records[name]["download_info"] == entry["download_info"], name
env = report["environment"]
host = default_environment()
assert all(host[k] == v for k, v in env.items())
extras = {n: set(x.get("requested_extras", [])) for n, x in records.items()}
assert extras["pyjwt"] == {"crypto"} and extras["uvicorn"] == {"standard"}
assert extras["psycopg"] == {"binary"}
assert not extras["authlib"] and not extras["joserfc"]
edges = set()
changed = True
while changed:
    changed = False
    for name, entry in records.items():
        for clause in entry["metadata"].get("requires_dist", []):
            req = Requirement(clause)
            active = not req.marker or any(req.marker.evaluate({**env, "extra": extra})
                                          for extra in {""} | extras[name])
            if not active:
                continue
            target = canonicalize_name(req.name)
            assert req.url is None and target in records
            assert req.specifier.contains(records[target]["metadata"]["version"], prereleases=False)
            edges.add((name, target, clause))
            new = set(req.extras) - extras[target]
            if new:
                extras[target].update(new)
                changed = True
assert "pycryptodome" not in records and not extras["joserfc"]
source_receipts = []
registries = {}
for name in ("authlib", "joserfc"):
    version = records[name]["metadata"]["version"]
    url = f"https://pypi.org/pypi/{name}/{version}/json"
    with urlopen(Request(url, headers={"User-Agent": "Hengshi-Phase1-Public-Research"}), timeout=20) as response:
        raw = response.read(8*1024*1024+1)
        assert len(raw) <= 8*1024*1024
    path = HERE / f"{name}-exact.json.gz"
    path.write_bytes(gzip.compress(raw, mtime=0))
    registry = json.loads(raw)
    assert canonicalize_name(registry["info"]["name"]) == name
    assert registry["info"]["version"] == version
    assert sorted(str(Requirement(x)) for x in registry["info"].get("requires_dist") or []) == sorted(
        str(Requirement(x)) for x in records[name]["metadata"].get("requires_dist") or [])
    registries[name] = (path, registry)
    source_receipts.append({"url": url, "raw_bytes": len(raw), "raw_sha256": sha(raw),
                            "snapshot": path.relative_to(ROOT).as_posix(), "snapshot_sha256": sha(path.read_bytes())})
write(HERE / "registry-sources.json", source_receipts)
old_closure = json.loads((BASIS / "closure-observations.json").read_bytes())
old_sources = {x["name"]: x for x in old_closure["package_records"]}
tags = set(sys_tags())
pins, observations, size = [], [], 0
for name, entry in sorted(records.items()):
    version = Version(entry["metadata"]["version"])
    assert not version.is_prerelease and not version.is_devrelease and not entry["is_yanked"]
    python = entry["metadata"].get("requires_python")
    assert not python or SpecifierSet(python).contains(env["python_full_version"])
    url = entry["download_info"]["url"]
    parsed = urlsplit(url)
    assert parsed.scheme == "https" and parsed.hostname == "files.pythonhosted.org"
    filename = unquote(parsed.path.rsplit("/", 1)[1])
    wheel_name, wheel_version, _, wheel_tags = parse_wheel_filename(filename)
    assert canonicalize_name(wheel_name) == name and wheel_version == version and wheel_tags & tags
    digest = entry["download_info"]["archive_info"]["hashes"]["sha256"]
    if name in old_sources:
        source_record = old_sources[name]
        source = ROOT / source_record["registry_snapshot"]
        assert sha(source.read_bytes()) == source_record["registry_snapshot_sha256"]
        registry = json.loads(gzip.decompress(source.read_bytes()))
        artifacts = registry["urls"] if "-exact" in source.name else registry["releases"][str(version)]
    else:
        source, registry = registries[name]
        artifacts = registry["urls"]
    matches = [x for x in artifacts if x["filename"] == filename and x["url"] == url]
    assert len(matches) == 1 and matches[0]["digests"]["sha256"] == digest
    artifact = matches[0]
    assert artifact["packagetype"] == "bdist_wheel" and not artifact["yanked"]
    size += artifact["size"]
    token = name + ("["+",".join(sorted(extras[name]))+"]" if extras[name] else "")
    pins.append(f"{token}=={version} --hash=sha256:{digest}")
    observations.append({"name": name, "version": str(version), "extras": sorted(extras[name]),
                         "wheel": filename, "sha256": digest, "bytes": artifact["size"],
                         "registry_snapshot": source.relative_to(ROOT).as_posix(),
                         "registry_snapshot_sha256": sha(source.read_bytes())})
assert all(sha((ROOT / p).read_bytes()) == h for p, h in receipt["protected_inputs_before"].items())
pins_raw = ("# Unselected Windows Authlib/backend research graph; not a production lock.\n"+
            "\n".join(pins)+"\n").encode()
(HERE / "candidate-hashed-requirements.txt").write_bytes(pins_raw)
result = {"status": "DOING", "scope": "Saved Windows metadata closure only",
          "report_sha256": sha(report_raw), "package_records": observations,
          "active_edges": [list(x) for x in sorted(edges)], "environment": env,
          "previous_43_metadata_and_artifacts_unchanged": True, "added_packages": ["authlib", "joserfc"],
          "optional_drafts_extra_selected": False, "archive_bytes": size,
          "hashed_requirements_sha256": sha(pins_raw), "protected_inputs_unchanged": True,
          "installation_performed": False, "native_runtime_verified": False,
          "oidc_security_qualified": False, "production_selection": False,
          "independent_review": "pending", "native_trial_permission_expanded": False}
write(HERE / "closure-observations.json", result)
print(json.dumps({"packages": len(records), "active_edges": len(edges), "archive_bytes": size,
                  "added": {n: records[n]["metadata"]["version"] for n in ("authlib", "joserfc")},
                  "previous_43_unchanged": True, "optional_drafts_extra_selected": False}))
