from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parent
original = root / 'output/research/b01-directory-preflight-refresh-2026-10-07/figma-call.js'
raw = original.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '4c811c9122bc049af4b5a01561a97b563c5eed849e9fab20809cdb54b67b62b8'
text = raw.decode('utf-8')
marker = 'await frames.find((node,index)=>input.frames[index].state_id'
prefix, tail = text.split(marker, 1)
assert tail.count('return {createdNodeIds,') == 1
codec = r'''// Report-only lossless encoding. Every node ID is represented; no canvas mutation here.
function packIds(ids) {
  const byPrefix = new Map(), literalIds = [];
  for (const id of [...new Set(ids)]) {
    const match = /^(.*:)(0|[1-9][0-9]*)$/.exec(id);
    if (!match || !Number.isSafeInteger(Number(match[2]))) { literalIds.push(id); continue; }
    if (!byPrefix.has(match[1])) byPrefix.set(match[1], []);
    byPrefix.get(match[1]).push(Number(match[2]));
  }
  const groups = [...byPrefix.entries()].map(([prefix, suffixes]) => {
    suffixes.sort((a,b)=>a-b);
    const ranges = [];
    for (const suffix of suffixes) {
      const last = ranges[ranges.length-1];
      if (last && suffix === last[last.length-1]+1) {
        if (last.length===1) last.push(suffix); else last[1]=suffix;
      } else ranges.push([suffix]);
    }
    return [prefix,ranges.map(r=>r.length===1?r[0]:r)];
  });
  const decoded = literalIds.slice();
  for (const [prefix,ranges] of groups)
    for (const range of ranges) {
      if (typeof range==='number') decoded.push(prefix+range);
      else for (let n=range[0];n<=range[1];n++) decoded.push(prefix+n);
    }
  const expected = [...new Set(ids)].sort();
  if (JSON.stringify(decoded.sort())!==JSON.stringify(expected)) throw Error('Lossless ID report mismatch');
  return {encoding:'prefix-inclusive-ranges-v1',count:expected.length,groups,literalIds};
}
const groupedBounds = new Map();
for (const finding of boundsFindings) {
  const key = JSON.stringify([finding.issue,finding.parentId??null]);
  if (!groupedBounds.has(key)) groupedBounds.set(key,[]);
  groupedBounds.get(key).push(finding.id);
}
const report = {
  createdNodeIds:packIds(createdNodeIds),mutatedNodeIds:[page.id],
  createdVariableIds:[],createdStyleIds:[],sourceId:source.id,compositionId:composition.id,
  componentIds:[inputMaster.id,resultMaster.id],
  frameFields:['id','inputIndex','width','height'],
  frames:frames.map((n,i)=>[n.id,i,n.width,n.height]),annotationIds:packIds(annotationIds),
  boundsFindingCount:boundsFindings.length,
  boundsFindings:[...groupedBounds.entries()].map(([key,ids])=>({context:JSON.parse(key),nodeIds:packIds(ids)})),
  B01Complete:false,coveredScope:'48 narrow directory state/stream references and four wide open references',
  limitations:input.limitations.filter(s=>!s.startsWith('Prepared only;')),
  reportOnlyChange:true
};
// Exact UTF-8 byte count without relying on an unavailable host TextEncoder.
const reportBytes = encodeURIComponent(JSON.stringify(report)).match(/%[0-9A-F]{2}|[^%]/g).length;
if (reportBytes>19000) throw Error('Compact report '+reportBytes+' bytes exceeds local 19000-byte guard; do not commit canvas edits');
await frames.find((node,index)=>input.frames[index].state_id==='STATE-RESULTS' && node.width===320).screenshot();
await frames.find(node=>node.width===1440).screenshot();
return report;
'''
target = out / 'figma-call.js'
assert not target.exists(), 'Preserve prior preparation'
target.write_text(prefix+codec, encoding='utf-8', newline='')
(out / 'codec.js').write_text(codec.split('const groupedBounds',1)[0], encoding='utf-8', newline='')
meta = {'product':'Hengshi Design v1','status':'TODO','external_calls':0,
 'scope':'Same 52 views and two components; only returned report encoding changes',
 'base_script_sha256':hashlib.sha256(raw).hexdigest(),
 'script_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'unchanged_construction_prefix_sha256':hashlib.sha256(prefix.encode()).hexdigest(),
 'unchanged_construction_prefix_bytes':len(prefix.encode()),
 'all_ids':'Lossless prefix and inclusive numeric suffix ranges with in-call round-trip equality; literal fallback',
 'frames':'Each tuple contains id/inputIndex/width/height; exact names/state/stream resolve from unchanged input ordinal',
 'bounds':'Every finding represented by issue/parent and lossless node IDs; none sampled or omitted',
 'return_budget':'19000-byte UTF-8 pre-return guard under observed20480-byte limit; future actual result unknown',
 'previews':'Same two native screenshots; no separate inspection call',
 'authorization':'Prepared only; fresh one-call approval required; prior retry permission consumed'}
(out / 'preparation.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
print(json.dumps(meta))
