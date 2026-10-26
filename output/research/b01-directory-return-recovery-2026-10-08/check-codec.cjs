const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const assert=require('node:assert/strict');
const codec=fs.readFileSync(path.join(__dirname,'codec.js'),'utf8');
const context=vm.createContext({});vm.runInContext(codec,context);
function decode(packed) {
  const ids=Array.from(packed.literalIds);
  for(const [prefix,ranges] of packed.groups)
    for(const r of ranges) {
      if(typeof r==='number') ids.push(prefix+r);
      else for(let n=r[0];n<=r[1];n++)ids.push(prefix+n);
    }
  return ids;
}
const root=path.resolve(__dirname,'../../..');
const packets=[
  'output/research/b01-navigation-composition-2026-10-06/provider-result.json',
  'output/research/b01-navigation-recovery-2026-10-07/provider-result.json'
];
const results=[];
for(const file of packets) {
  const provider=JSON.parse(fs.readFileSync(path.join(root,file),'utf8'));
  const text=provider.content.find(c=>c.type==='text'&&c.text.startsWith('{'));
  const receipt=JSON.parse(text.text),ids=receipt.createdNodeIds;
  assert(Array.isArray(ids));
  const packed=context.packIds(ids);
  assert.deepEqual(decode(packed).sort(),[...new Set(ids)].sort());
  results.push({file,ids:ids.length,rawBytes:Buffer.byteLength(JSON.stringify(ids)),packedBytes:Buffer.byteLength(JSON.stringify(packed)),roundTrip:true});
}
const synthetic=[];
for(let instance=0;instance<160;instance++)
  for(let child=0;child<25;child++)synthetic.push(`I39:${100+instance};21:${child*2+1}`);
synthetic.push('39:1','39:2','39:4','39:001','unusual-node','39:9007199254740992','39:4');
const packed=context.packIds(synthetic);
assert.deepEqual(decode(packed).sort(),[...new Set(synthetic)].sort());
results.push({case:'4000 compound instance IDs plus gaps duplicates and literal fallbacks',ids:synthetic.length,rawBytes:Buffer.byteLength(JSON.stringify(synthetic)),packedBytes:Buffer.byteLength(JSON.stringify(packed)),roundTrip:true});
const AsyncFunction=Object.getPrototypeOf(async function(){}).constructor;
new AsyncFunction(fs.readFileSync(path.join(__dirname,'figma-call.js'),'utf8'));
const result={product:'Hengshi Design v1',status:'DOING',checks:results,scriptSyntax:true,
  limits:'Local codec conservation and syntax only; no Figma API execution or actual52-view receipt-size/visual assertion'};
fs.writeFileSync(path.join(__dirname,'codec-check.json'),JSON.stringify(result,null,2)+'\n');
process.stdout.write(JSON.stringify(result)+'\n');
