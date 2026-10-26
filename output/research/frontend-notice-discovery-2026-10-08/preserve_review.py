from pathlib import Path
import hashlib, json, shutil
root=Path(__file__).resolve().parents[3]
packet=Path(__file__).resolve().parent
manifest=packet/'review-inputs.json'
assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='4dc5d04d30d6a6c7e2b5139a217606e3c0082bea295e7da2f763c9e9f0620d6b'
items=json.loads(manifest.read_text(encoding='utf-8'))['inputs']
for item in items:
    for path in [root/item['source'],packet/item['snapshot']]:
        raw=path.read_bytes()
        assert len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],str(path)
prior=root/'docs/phase-1-compatibility/reviews/frontend-supply-chain-v1-2026-10-06.md'
before=packet/'frontend-supply-chain-review.before.md'
assert not before.exists()
shutil.copyfile(prior,before)
with prior.open('a',encoding='utf-8',newline='') as stream:
    stream.write('''

## Later bounded notice discovery — 2026-10-08

The [independent discovery receipt](installed-notice-discovery-v1-2026-10-08.md)
extends evidence for the eleven packages missed by the root-name-prefix collector:
394 own files, 356 eligible text files, 129 hit files and 281 retained excerpts.
It preserves eight exact input identities and reproduced installed-file identities.
The 38 outside-whitelist exclusions include 31 text JSON source maps; they are not
38 binary files. Prefixes, twelve-line caps, metadata-only hits and linked terms
leave applicable notices and attribution completeness unresolved. This later
accuracy PASS neither changes the preceding review's hashes/scope nor confers
licence/provenance clearance, deployed coverage or complete graph acceptance.
''')
assert prior.read_bytes().startswith(before.read_bytes())
print(json.dumps({'frozen_inputs_rechecked':len(items),'prior_receipt_prefix_preserved':True,'bounded_review':'PASS'}))
