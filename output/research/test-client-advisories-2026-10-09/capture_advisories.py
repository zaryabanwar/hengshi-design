"""Read-only OSV queries for a frozen candidate; no install or package execution."""
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import re
import urllib.parse
import urllib.request

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GRAPH = ROOT / 'output/research/test-client-graph-2026-10-09/closure-observations.json'
RECEIPT = HERE / 'receipt.json'
if RECEIPT.exists() or (HERE / 'request-1.json').exists():
    raise SystemExit('Refuse repeating captured advisory query')
raw = GRAPH.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'f979543df57552aac1c08dd61ac3f1322e3629777dfc10229e6ff976b5c47f1f'
graph = json.loads(raw)
packages = graph['package_records']
assert len(packages) == 48
protected = json.loads((ROOT / 'output/research/test-client-graph-2026-10-09/receipt.json').read_bytes())['protected_inputs_before']
sha = lambda value: hashlib.sha256(value).hexdigest()
def unchanged():
    return all(sha((ROOT / path).read_bytes()) == value for path, value in protected.items())
assert unchanged()
def write(name, value):
    (HERE / name).write_bytes((json.dumps(value, indent=2) + '\n').encode())
def fetch(url, body=None):
    request = urllib.request.Request(url, data=body, headers={
        'User-Agent': 'Hengshi-Phase1-readonly-advisory-evidence/1',
        'Content-Type': 'application/json', 'Accept': 'application/json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read(8 * 1024 * 1024 + 1)
        assert len(data) <= 8 * 1024 * 1024
        return data, {'url': url, 'http_status': response.status,
                      'captured_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                      'bytes': len(data), 'sha256': sha(data)}
result = {'product_release': 'v1', 'status': 'DOING', 'observation': 'not_finished',
          'candidate_sha256': sha(raw), 'package_count': 48,
          'scope': 'Exact PyPI-name/version OSV advisory lookup, not security clearance or embedded/native coverage',
          'limits': ['No-match is only the database response at capture time, not absence of vulnerabilities.',
                     'PyPI queries do not identify all embedded/native libraries, OS dependencies, application defects or exploitability.',
                     'No package selection, exception, ignore rule, production change or complete advisory clearance follows.']}
try:
    docs = []
    for filename in ('post-v1-querybatch.md', 'get-v1-vulns.md'):
        data, source = fetch('https://raw.githubusercontent.com/google/osv.dev/master/docs/api/' + filename)
        (HERE / (filename + '.gz')).write_bytes(gzip.compress(data, mtime=0))
        docs.append({**source, 'saved': filename + '.gz'})
    write('primary-guidance.json', docs)
    base = [{'package': {'ecosystem': 'PyPI', 'name': p['name']}, 'version': p['version']} for p in packages]
    pending = list(enumerate(base))
    matches = [[] for _ in packages]
    requests = []
    seen_tokens = set()
    page = 0
    while pending:
        page += 1
        if page > 5:
            raise RuntimeError('Pagination capture admission limit exceeded; incomplete query')
        request = {'queries': [query for index, query in pending]}
        write('request-' + str(page) + '.json', request)
        data, capture = fetch('https://api.osv.dev/v1/querybatch', json.dumps(request).encode())
        (HERE / ('response-' + str(page) + '.json')).write_bytes(data)
        response = json.loads(data)
        assert isinstance(response.get('results'), list) and len(response['results']) == len(pending)
        requests.append({**capture, 'page': page, 'query_indexes': [index for index, query in pending]})
        next_pending = []
        for (index, query), entry in zip(pending, response['results']):
            assert isinstance(entry, dict) and 'error' not in entry
            vulns = entry.get('vulns', [])
            assert isinstance(vulns, list)
            for vuln in vulns:
                assert isinstance(vuln.get('id'), str) and vuln['id']
            matches[index].extend(vulns)
            token = entry.get('next_page_token')
            if token:
                assert (index, token) not in seen_tokens
                seen_tokens.add((index, token))
                next_pending.append((index, {**base[index], 'page_token': token}))
        pending = next_pending
    write('query-captures.json', requests)
    ids = sorted({v['id'] for entries in matches for v in entries})
    details = []
    (HERE / 'advisories').mkdir()
    for identifier in ids:
        assert re.fullmatch(r'[A-Za-z0-9._-]+', identifier)
        data, capture = fetch('https://api.osv.dev/v1/vulns/' + urllib.parse.quote(identifier))
        detail = json.loads(data)
        assert detail.get('id') == identifier
        (HERE / 'advisories' / (identifier + '.json')).write_bytes(data)
        details.append({**capture, 'id': identifier, 'withdrawn': detail.get('withdrawn'),
                        'summary': detail.get('summary'), 'aliases': detail.get('aliases', []),
                        'severity': detail.get('severity', []),
                        'saved': 'advisories/' + identifier + '.json'})
    write('advisory-details.json', details)
    mappings = [{'package': p['name'], 'version': p['version'], 'matches': entries}
                for p, entries in zip(packages, matches)]
    write('package-results.json', mappings)
    result.update({'observation': 'complete_saved_OSV_query', 'pagination_exhausted': True,
                   'request_count': page, 'unique_advisory_count': len(ids),
                   'matching_package_count': sum(bool(x) for x in matches),
                   'unmatched_package_count': sum(not x for x in matches),
                   'advisory_ids': ids})
except Exception as error:
    result.update({'status': 'BLOCKED', 'observation': 'incomplete_stopped_on_error',
                   'error': type(error).__name__ + ': ' + str(error)})
finally:
    result['protected_inputs_unchanged'] = unchanged()
    write('receipt.json', result)
    print(json.dumps(result, indent=2))
if result['observation'] != 'complete_saved_OSV_query' or not result['protected_inputs_unchanged']:
    raise SystemExit(1)
