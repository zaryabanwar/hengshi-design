// Report-only lossless encoding. Every node ID is represented; no canvas mutation here.
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
