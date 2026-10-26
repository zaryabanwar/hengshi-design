from pathlib import Path
import hashlib
import json

root=Path.cwd();out=root/'output/research/booking-email-wire-2026-10-08';cor=out/'correction-1';cor.mkdir(exist_ok=False)
manifest_path=out/'review-inputs.json';m=json.loads(manifest_path.read_bytes())
for r in m['inputs']:
    raw=(root/r['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'],r['path']
    assert raw==(root/r['snapshot']).read_bytes()
initial=dict(result='REVISE',reviewer='/root/review_directory_references_v1',
    manifest_sha256='c5e80c526addfb6355c2fedd98db723befe4ac1fca64d5a2edb992b115bcec67',
    findings=[dict(id='EW01',reason='Reserved record slots alone cannot protect extensions from a full shared receive/fresh-mutation work pool.')],
    independent_evidence=dict(matching_initial_final_pairs=32,preserved_prefix_bytes=89006,validator_methods_passed=52),
    scope=m['scope'])
dest=out/'initial-independent-review.json';assert not dest.exists();dest.write_text(json.dumps(initial,indent=2)+'\n',encoding='utf-8')
p=root/'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md';raw=p.read_bytes();(cor/'INTERFACE_CATALOG.before-correction.md').write_bytes(raw)
a=('Recommend using the qualification profile\'s existing service-wide 48 receive/\nfresh-mutation and 16 receive/reconciliation slots as one shared pool across\nqualification and these two routes, not multiplying capacity per endpoint.\nCount draining/uncertain work until known release. Its five-second receive and\nten-second observation deadlines apply; observation expiry cannot abandon admitted\nwork or decide its outcome. Delivery workers are separately bounded private jobs,\nnot uncounted work hidden behind a completed HTTP request.').replace('\n','\r\n').encode()
b=('Recommend retaining one service-wide 48 receive/fresh-mutation slot budget across\nqualification and these routes, partitioned into 16 general and 32 protected\nchallenge-extension slots; retain the separate 16 receive/reconciliation budget.\nBefore issue/resend, also reserve one protected receive/work slot for that active\nchallenge, in addition to its operation records below. Refuse new challenge\nadmission before effects if that complete work/record reservation is unavailable.\nGeneral issue/resend/qualification/verification traffic cannot consume a protected\nslot, and one challenge cannot consume another challenge\'s allocation. One such\nreceive/extension job may be in flight per challenge; same-operation replay does\nnot create parallel extension work. Total active/reserved/draining protected slots\nnever exceeds 32, counted across workers, replacement challenges and processes.\n\nIngress must route a currently authorized own-process challenge-extension candidate\nto its protected receive slot before general-pool pressure can reject it. Require\nthe allowed Origin/method/media and current proof/CSRF scope; guessed selectors or\npublic requests cannot allocate that reservation. Decode the bounded body within\nthe existing five-second receive deadline. A candidate that is not the closed\nextend command cannot execute ordinary mutations in this lane: use general\nadmission or a safe refusal, without altering challenge clocks/counters. Exact\nproxy/receiver routing and malicious/incomplete-body qualification remain later\nimplementation obligations; an ordinary pool gate placed ahead of this lane would\nviolate the proposed protection.\n\nRelease the reserved extension slot only when no further extension is eligible\n(consumption, expiry, invalidation or the tenth extension), and its in-flight/\ndraining/uncertain work is known released. Replacement cannot forget or borrow an\nolder occupied slot. Its ten-second observation deadline is not work abandonment\nor proof of failure; reconcile the same uncertain operation before fresh extension.\nThis protects admission from unrelated general traffic, not network, clock/store/\nkey outages or an already-uncertain own operation. No guarantee of actual latency\nor complete timing accessibility follows before real-load/ingress qualification.\nDelivery workers remain separately bounded private jobs, not work hidden behind a\ncompleted HTTP response.').replace('\n','\r\n').encode()
assert raw.count(a)==1;raw=raw.replace(a,b)
a=('consume its unused reserved slots, so capacity alone cannot deny its promised\nten-extension route after admission.').replace('\n','\r\n').encode()
b=('consume its unused reserved record slots. This protects the ten-extension route\nfrom record-capacity exhaustion; the distinct protected work-admission profile\nabove addresses ordinary receive/mutation pool pressure.').replace('\n','\r\n').encode()
assert raw.count(a)==1;raw=raw.replace(a,b)
a=('projection. Later runtime qualification must cover loss/duplicate/stale/out-of-order\nresponses,').replace('\n','\r\n').encode()
b=('projection. Later runtime qualification must cover reserved-extension admission\nwhile the general pool is saturated/draining, no cross-challenge slot borrowing,\nincomplete/malicious-body bounds, atomic release/replacement and an uncertain own\nextension, plus loss/duplicate/stale/out-of-order responses,').replace('\n','\r\n').encode()
assert raw.count(a)==1;raw=raw.replace(a,b)
assert raw.startswith((root/m['prefix']['path']).read_bytes());p.write_bytes(raw)
snaps=cor/'snapshots';snaps.mkdir();rows=[]
for i,r in enumerate(m['inputs']):
    data=(root/r['path']).read_bytes()
    if r['path']!='docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md': assert hashlib.sha256(data).hexdigest()==r['sha256']
    s=snaps/f"{i:02d}-{Path(r['path']).name}";s.write_bytes(data)
    rows.append(dict(path=r['path'],snapshot=str(s.relative_to(root)).replace('\\','/'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
fixed=dict(scope=m['scope'],correction=1,inputs=rows,prefix=m['prefix'],findings_addressed=['EW01'])
data=(json.dumps(fixed,indent=2)+'\n').encode();(cor/'review-inputs.json').write_bytes(data)
print(json.dumps(dict(inputs=len(rows),manifest_sha256=hashlib.sha256(data).hexdigest(),catalogue_sha256=hashlib.sha256(raw).hexdigest(),other_initial_inputs_unchanged=31,prefix_bytes=m['prefix']['bytes'])))
