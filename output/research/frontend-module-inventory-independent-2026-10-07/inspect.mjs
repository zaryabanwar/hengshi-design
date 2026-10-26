import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath, pathToFileURL} from 'node:url';
const out = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(out, '../../..');
const candidate = path.join(root, 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate');
const workspace = path.join(out, 'workspace');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const originalProtected = JSON.parse(await fs.readFile(path.join(root, 'output/research/frontend-module-inventory-2026-10-06/protected-before.json')));
async function verifyProtected() {
  for (const i of originalProtected) {
    const raw = await fs.readFile(path.join(root, i.path));
    if (raw.length !== i.bytes || sha(raw) !== i.sha256) throw Error('Protected identity drift: '+i.path);
  }
}
await verifyProtected();
await fs.mkdir(workspace);
for (const name of ['index.html','package.json','package-lock.json','vite.config.mjs','tsconfig.json','tsconfig.invalid.json','tsconfig.loader-control.json','src/fixture.tsx','src/fixture.css','src/invalid-control.tsx','src/loader-declaration-control.ts']) {
  const destination = path.join(workspace, name);
  await fs.mkdir(path.dirname(destination), {recursive:true});
  await fs.copyFile(path.join(candidate,name), destination);
}
await fs.mkdir(path.join(workspace,'node_modules'));
const junctions = [];
for (const entry of await fs.readdir(path.join(candidate,'node_modules'),{withFileTypes:true})) {
  if (entry.name.startsWith('.') || !entry.isDirectory()) continue;
  const source = path.join(candidate,'node_modules',entry.name);
  const target = path.join(workspace,'node_modules',entry.name);
  if (entry.name.startsWith('@')) {
    await fs.mkdir(target);
    for (const child of await fs.readdir(source,{withFileTypes:true})) {
      if (!child.isDirectory()) continue;
      const link = path.join(target,child.name), vendor = path.join(source,child.name);
      await fs.symlink(vendor,link,'junction'); junctions.push({link,vendor});
    }
  } else { await fs.symlink(source,target,'junction'); junctions.push({link:target,vendor:source}); }
}
const captures = [];
const observer = {name:'hsd-independent-boundary-observer',apply:'build',enforce:'post',generateBundle:{order:'post',handler(options,bundle,isWrite) {
  const graph = Array.from(this.getModuleIds(), id => {
    const info=this.getModuleInfo(id);
    if (!info) throw Error('Missing graph info');
    return {id,isEntry:info.isEntry,isExternal:info.isExternal,importedIds:info.importedIds,dynamicallyImportedIds:info.dynamicallyImportedIds,importers:info.importers,dynamicImporters:info.dynamicImporters};
  }).sort((a,b)=>a.id.localeCompare(b.id));
  captures.push({isWrite,graph,chunks:Object.values(bundle).filter(x=>x.type==='chunk').map(x=>({fileName:x.fileName,moduleIds:[...x.moduleIds],moduleKeys:Object.keys(x.modules)}))});
}}};
const {build}=await import(pathToFileURL(path.join(candidate,'node_modules/vite/dist/node/index.js')));
const result=await build({root:workspace,configFile:path.join(workspace,'vite.config.mjs'),plugins:[observer],build:{write:false,outDir:'not-written-dist'}});
const artifacts=[], chunks=[];
for (const r of Array.isArray(result)?result:[result]) for (const item of r.output) {
  const raw=Buffer.from(item.type==='chunk'?item.code:item.source);
  const original=await fs.readFile(path.join(candidate,'fixture-dist',item.fileName));
  artifacts.push({fileName:item.fileName,type:item.type,bytes:raw.length,sha256:sha(raw),originalEqual:raw.equals(original)});
  if(item.type==='chunk') chunks.push({fileName:item.fileName,moduleIds:[...item.moduleIds],modules:Object.entries(item.modules).map(([id,m])=>({id,renderedLength:m.renderedLength,renderedExports:m.renderedExports,renderedCodeSha256:m.code===null?null:sha(Buffer.from(m.code))}))});
}
const configuredOutDirExists=await fs.stat(path.join(workspace,'not-written-dist')).then(()=>true,e=>{if(e.code==='ENOENT')return false;throw e;});
await verifyProtected();
const record={node:process.version,workspace,captures,chunks,artifacts,configuredOutDirExists,protectedCount:originalProtected.length,protectedUnchanged:true,junctions};
await fs.writeFile(path.join(out,'observation.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});
if(captures.length!==1 || captures[0].isWrite || configuredOutDirExists || artifacts.length!==3 || artifacts.some(x=>!x.originalEqual))throw Error('Unexpected independent build boundary');
console.log(JSON.stringify({graphIds:new Set(captures.flatMap(x=>x.graph.map(x=>x.id))).size,outputIds:new Set(chunks.flatMap(x=>x.moduleIds)).size,artifacts,protectedUnchanged:true}));
