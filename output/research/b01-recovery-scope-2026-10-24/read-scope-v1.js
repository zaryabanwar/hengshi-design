// Read-only B01 census: no node setters, creation, deletion, font or export calls.
if (figma.editorType !== 'figma' || figma.fileKey !== 'GOmLP6Cv96l768ueSrZ5Dg') throw Error('Wrong file/editor');
const page = await figma.getNodeByIdAsync('0:1');
if (page?.type !== 'PAGE' || page.name !== 'Page 1') throw Error('Wrong page');
await figma.setCurrentPageAsync(page);
figma.skipInvisibleInstanceChildren = false;
const section = await figma.getNodeByIdAsync('144:3197');
const set = await figma.getNodeByIdAsync('172:3740');
if (section?.type !== 'SECTION' || section.parent?.id !== page.id || section.name !== 'B01 / Four-stream three-host qualification / v1') throw Error('Wrong section');
if (set?.type !== 'COMPONENT_SET' || set.parent?.id !== section.id || set.name !== 'B01 qualification / RECOVERY / v1') throw Error('Wrong Recovery set');
const ids = ['172:3721','172:3702','172:3683','172:3664','172:3645','172:3626','172:3607','172:3588','172:3569','172:3550','172:3531','172:3512','172:3493','172:3474','172:3455','169:3402'];
if (set.children.length !== 16 || set.children.some(n=>!ids.includes(n.id))) throw Error('Recovery member drift');
const walk = n => [n,...('children' in n?n.children.flatMap(walk):[])];
const copy = x => JSON.parse(JSON.stringify(x));
const reactions = n => 'reactions' in n ? copy(n.reactions || []) : [];
const label = n => {
  if (n.type === 'TEXT') return n.characters;
  if (n.type !== 'INSTANCE') return null;
  const p = Object.entries(n.componentProperties).filter(([k,v])=>k.split('#')[0]==='Label' && v.type==='TEXT');
  return p.length===1?p[0][1].value:null;
};
const roots=[], recoveryReactions=[];
for (const root of set.children) {
  if (root.type !== 'COMPONENT') throw Error('Unexpected variant type');
  const v=root.variantProperties, descendants=walk(root);
  const context=root.children.find(n=>n.type==='TEXT' && n.name==='Context summary / fixed Services fixture');
  const menu=root.children.find(n=>n.name==='Menu action');
  const body=root.children.find(n=>n.type==='FRAME' && n.name==='PRIM-001 / Delivery stream control / B01 v1');
  if (!context || !menu || !body) throw Error('Missing Recovery anatomy '+root.id);
  const controls=[];
  for (const n of descendants) {
    const r=reactions(n); if(r.length) recoveryReactions.push([root.id,n.id,r]);
    if(n.name.startsWith('Native-radio appearance reference / S-')) controls.push([n.name.split('/ S-')[1],n.id,n.type,n.width,n.height,n.children.filter(c=>c.type==='TEXT').map(c=>c.characters)]);
    if(n.type==='INSTANCE' && label(n)==='Apply selection') controls.push(['APPLY',n.id,n.type,n.width,n.height,label(n)]);
  }
  roots.push([root.id,[v.Active,v.Pending,v.Disclosure],root.width,root.height,root.children.length,descendants.length,context.characters,[menu.id,menu.visible,label(menu)],[body.id,body.visible,body.children.length],controls]);
}
const frames=[];
for(const frame of section.children.filter(n=>n.type==='FRAME' && n.name.startsWith('ENQ_'))) {
  const children=[];
  for(const n of frame.children) {
    const main=n.type==='INSTANCE'?await n.getMainComponentAsync():null;
    const properties=n.type==='INSTANCE'?Object.entries(n.componentProperties).filter(([,v])=>v.type==='VARIANT').map(([k,v])=>[k,v.value]):[];
    children.push([n.id,n.type,n.name,n.visible,label(n),main?.id||null,main?.key||null,properties,reactions(n)]);
  }
  frames.push([frame.id,frame.name,frame.width,frame.height,frame.overflowDirection,children]);
}
const report={product:'Hengshi Design v1',scope:'Read-only Recovery variants/reactions and existing ENQ direct-child boundary census',section:section.id,set:set.id,rootFields:['id','tuple','width','height','directChildren','subtreeCount','context','menu[id,visible,label]','body[id,visible,children]','controls[role,id,type,width,height,label]'],roots,recoveryReactions,frameFields:['id','name','width','height','overflow','directChildren[id,type,name,visible,label,mainId,mainKey,variantProperties,reactions]'],frames,limits:'No node writes. Direct-child census only, not complete source equivalence, matching/restore qualification, browser behavior, accessibility or B01/Phase1 acceptance.'};
// Lossless string interning bounds repeated frame/control captions and metadata.
const strings=[], stringIds=new Map();
const pack=value=>typeof value==='string'?(()=>{if(!stringIds.has(value)){stringIds.set(value,strings.length);strings.push(value);}return '@'+stringIds.get(value);})():Array.isArray(value)?value.map(pack):value&&typeof value==='object'?Object.fromEntries(Object.entries(value).map(([k,v])=>[k,pack(v)])):value;
const packed=pack(report);
const envelope={result:'READ_ONLY_SCOPE',encoding:'interned-json-string; recursively replace @N values from strings[N]',data:JSON.stringify({strings,report:packed})};
const forms=[JSON.stringify(envelope),JSON.stringify(envelope,null,2),JSON.stringify(JSON.stringify(envelope))];
const bytes=s=>[...s].reduce((n,c)=>n+(c.codePointAt(0)<128?1:c.codePointAt(0)<2048?2:c.codePointAt(0)<65536?3:4),0);
if(Math.max(...forms.map(bytes))>=18000) return {result:'READ_ONLY_REPORT_TOO_LARGE',rootCount:roots.length,frameCount:frames.length,reactionCount:recoveryReactions.length,bytes:forms.map(bytes),mutatedNodeIds:[],createdNodeIds:[]};
return envelope;
