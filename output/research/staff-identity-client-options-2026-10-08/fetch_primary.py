"""Freeze pinned official client source for comparison; never import it."""
import concurrent.futures
import gzip
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

OUT = Path(__file__).resolve().parent
LIMIT = 2 * 1024 * 1024


def get(url, target):
    item = {"url": url, "observed_utc": datetime.now(UTC).isoformat()}
    try:
        with urlopen(Request(url, headers={"User-Agent": "Hengshi-Phase1-Public-Research"}), timeout=20) as response:
            raw = response.read(LIMIT + 1)
            item["http_status"] = response.status
        if len(raw) > LIMIT:
            raise ValueError("Response exceeds bounded research limit")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(gzip.compress(raw, mtime=0))
        item.update({"raw_bytes": len(raw), "raw_sha256": hashlib.sha256(raw).hexdigest(),
                     "snapshot": target.relative_to(OUT).as_posix(),
                     "snapshot_sha256": hashlib.sha256(target.read_bytes()).hexdigest()})
        return item, raw
    except HTTPError as error:
        item["http_status"] = error.code
        return item, None


def family(name, repo, tag, files):
    records = []
    prefix = f"https://api.github.com/repos/{repo}"
    record, raw = get(f"{prefix}/git/ref/tags/{tag}", OUT / name / "tag-ref.json.gz")
    records.append(record)
    if raw is None:
        return {"name": name, "records": records, "source_commit": None}
    obj = json.loads(raw)["object"]
    if obj["type"] == "tag":
        record, raw = get(obj["url"], OUT / name / "annotated-tag.json.gz")
        records.append(record)
        if raw is None:
            return {"name": name, "records": records, "source_commit": None}
        obj = json.loads(raw)["object"]
    if obj["type"] != "commit":
        raise ValueError("Tag did not resolve to a source commit")
    commit = obj["sha"]
    record, release = get(f"{prefix}/releases/tags/{tag}", OUT / name / "release.json.gz")
    records.append(record)
    for path in files:
        record, _ = get(f"https://raw.githubusercontent.com/{repo}/{commit}/{path}",
                        OUT / name / "source" / (path + ".gz"))
        records.append(record)
    return {"name": name, "tag": tag, "source_commit": commit, "records": records,
            "wheel_provenance": False, "installation": False}


families = [
    ("msal", "AzureAD/microsoft-authentication-library-for-python", "1.39.0", [
        "msal/__init__.py", "msal/application.py", "msal/oauth2cli/oidc.py",
        "msal/oauth2cli/oauth2.py", "msal/token_cache.py", "docs/index.rst"
    ]),
    ("authlib", "authlib/authlib", "v1.8.0", [
        "authlib/__init__.py", "authlib/integrations/starlette_client/apps.py",
        "authlib/integrations/starlette_client/integration.py",
        "authlib/integrations/base_client/async_openid.py",
        "authlib/integrations/base_client/framework_integration.py",
        "docs/oauth2/client/web/starlette.rst"
    ])
]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(lambda args: family(*args), families))
(OUT / "primary-sources.json").write_bytes((json.dumps(results, indent=2) + "\n").encode())
print(json.dumps([{k: value for k, value in row.items() if k != "records"}
                  | {"responses": [(x["http_status"], x["url"]) for x in row["records"]]}
                 for row in results], indent=2))
