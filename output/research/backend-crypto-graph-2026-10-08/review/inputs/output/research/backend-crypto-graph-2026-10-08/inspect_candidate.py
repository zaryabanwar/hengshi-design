"""Saved metadata inspection only; no installation or production selection."""
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name, parse_wheel_filename
from packaging.version import Version

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = ROOT / "output/research/backend-hash-inputs-2026-10-08"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def inspect():
    report_bytes = (HERE / "pip-report.json").read_bytes()
    report = json.loads(report_bytes)
    receipt = json.loads((HERE / "receipt.json").read_bytes())
    assert receipt["exit_code"] == 0 and not receipt["installation_performed"]
    assert digest(report_bytes) == receipt["report_sha256"]
    environment = report["environment"]
    host = default_environment()
    assert all(host[key] == value for key, value in environment.items())
    records = {canonicalize_name(x["metadata"]["name"]): x for x in report["install"]}
    assert len(records) == len(report["install"]) == 43
    old_raw = (BASE / "latest-coupled-resolution/pip-report.json").read_bytes()
    proposal = json.loads((HERE / "proposal.json").read_bytes())
    assert digest(old_raw) == proposal["basis_report_sha256"]
    old = {canonicalize_name(x["metadata"]["name"]): x
           for x in json.loads(old_raw)["install"]}
    assert set(records) - set(old) == {"cryptography", "cffi", "pycparser"}
    for name, previous in old.items():
        current = records[name]
        assert current["metadata"] == previous["metadata"], name
        assert current["download_info"] == previous["download_info"], name
    extras = {name: set(x.get("requested_extras", [])) for name, x in records.items()}
    assert extras["pyjwt"] == {"crypto"}
    assert extras["uvicorn"] == {"standard"} and extras["psycopg"] == {"binary"}
    edges = set()
    changed = True
    while changed:
        changed = False
        for name, record in records.items():
            for declaration in record["metadata"].get("requires_dist", []):
                req = Requirement(declaration)
                active = not req.marker or any(
                    req.marker.evaluate({**environment, "extra": extra})
                    for extra in {""} | extras[name])
                if not active:
                    continue
                target = canonicalize_name(req.name)
                assert req.url is None and target in records, (name, declaration)
                assert req.specifier.contains(records[target]["metadata"]["version"],
                                              prereleases=False), (name, declaration)
                edges.add((name, target, declaration))
                added = set(req.extras) - extras[target]
                if added:
                    extras[target].update(added)
                    changed = True
    compatible = set(sys_tags())
    observations, pins, total_bytes = [], [], 0
    for name, record in sorted(records.items()):
        version = Version(record["metadata"]["version"])
        assert not version.is_prerelease and not version.is_devrelease
        assert not record["is_yanked"]
        requires_python = record["metadata"].get("requires_python")
        assert not requires_python or SpecifierSet(requires_python).contains(
            environment["python_full_version"])
        url = record["download_info"]["url"]
        parts = urlsplit(url)
        assert parts.scheme == "https" and parts.hostname == "files.pythonhosted.org"
        filename = unquote(parts.path.rsplit("/", 1)[1])
        wheel_name, wheel_version, _, tags = parse_wheel_filename(filename)
        assert canonicalize_name(wheel_name) == name and wheel_version == version
        assert tags & compatible, filename
        archive_hash = record["download_info"]["archive_info"]["hashes"]["sha256"]
        if name in old:
            source = BASE / ("core-recovery/pydantic-core-project.json.gz"
                             if name == "pydantic-core" else f"primary/{name}-project.json.gz")
            registry = json.loads(gzip.decompress(source.read_bytes()))
            files = registry["releases"][str(version)]
        else:
            source = HERE / f"new-registry/{name}-exact.json.gz"
            registry = json.loads(gzip.decompress(source.read_bytes()))
            assert canonicalize_name(registry["info"]["name"]) == name
            assert registry["info"]["version"] == str(version)
            assert sorted(str(Requirement(x)) for x in registry["info"].get("requires_dist") or []) == sorted(
                str(Requirement(x)) for x in record["metadata"].get("requires_dist") or [])
            files = registry["urls"]
        matches = [x for x in files if x["filename"] == filename and x["url"] == url]
        assert len(matches) == 1 and matches[0]["digests"]["sha256"] == archive_hash
        assert matches[0]["packagetype"] == "bdist_wheel" and not matches[0]["yanked"]
        total_bytes += matches[0]["size"]
        token = name + ("[" + ",".join(sorted(extras[name])) + "]" if extras[name] else "")
        pins.append(f"{token}=={version} --hash=sha256:{archive_hash}")
        observations.append({"name": name, "version": str(version), "extras": sorted(extras[name]),
                             "wheel": filename, "sha256": archive_hash, "bytes": matches[0]["size"],
                             "registry_snapshot": source.relative_to(ROOT).as_posix(),
                             "registry_snapshot_sha256": digest(source.read_bytes())})
    current = {p: digest((ROOT / p).read_bytes()) for p in proposal["protected_inputs_before"]}
    assert current == proposal["protected_inputs_before"]
    requirement_bytes = ("# Research-only Windows graph with PyJWT crypto; not a production lock.\n"
                         "# Metadata hashes only; wheel contents and native compatibility unverified.\n"
                         + "\n".join(pins) + "\n").encode()
    (HERE / "candidate-hashed-requirements.txt").write_bytes(requirement_bytes)
    result = {"status": "DOING", "scope": "Saved Windows metadata closure only",
              "report_sha256": digest(report_bytes), "package_records": observations,
              "active_edges": [list(x) for x in sorted(edges)], "environment": environment,
              "previous_40_metadata_and_artifacts_unchanged": True,
              "added_packages": sorted(set(records) - set(old)),
              "archive_bytes": total_bytes, "protected_inputs_unchanged": True,
              "hashed_requirements_sha256": digest(requirement_bytes),
              "installation_performed": False, "wheel_content_verified": False,
              "native_runtime_verified": False, "production_selection": False,
              "independent_review": "pending",
              "limits": ["No full OIDC/PKCE client selected or identity/provider test",
                         "No actual install, signature/RSA/native/HTTP/database tests",
                         "No release-channel, provenance, licence/security or full-graph acceptance"]}
    (HERE / "closure-observations.json").write_bytes((json.dumps(result, indent=2) + "\n").encode())
    return {"packages": len(records), "active_edges": len(edges), "archive_bytes": total_bytes,
            "previous_40_unchanged": True, "native_runtime_verified": False}


if __name__ == "__main__":
    print(json.dumps(inspect(), indent=2))
