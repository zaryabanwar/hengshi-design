"""Bounded public registry observations; no installation or selection."""
import concurrent.futures
import gzip
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from urllib.request import Request, urlopen

OUT = Path(__file__).resolve().parent
LIMIT = 8 * 1024 * 1024


def fetch(name):
    url = f"https://pypi.org/pypi/{name}/json"
    with urlopen(Request(url, headers={"User-Agent": "Hengshi-Phase1-Public-Research"}), timeout=20) as response:
        data = response.read(LIMIT + 1)
        if len(data) > LIMIT:
            raise ValueError("Public response exceeds research limit")
    target = OUT / f"{name}-project.json.gz"
    target.write_bytes(gzip.compress(data, mtime=0))
    obj = json.loads(data)
    info = obj["info"]
    return {"name": name, "url": url, "observed_utc": datetime.now(UTC).isoformat(),
            "raw_bytes": len(data), "raw_sha256": hashlib.sha256(data).hexdigest(),
            "snapshot": target.name, "snapshot_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            "observed_registry_version": info["version"], "requires_python": info["requires_python"],
            "requires_dist": info["requires_dist"], "project_urls": info["project_urls"],
            "classifiers": [x for x in info["classifiers"] if x.startswith("Development Status")],
            "selection": False}


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(fetch, ["msal", "authlib"]))
(OUT / "registry-observations.json").write_bytes((json.dumps(results, indent=2) + "\n").encode())
print(json.dumps(results, indent=2))
