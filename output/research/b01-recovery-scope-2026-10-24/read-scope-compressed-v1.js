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

function encodeScope(text) {
  const bytes=[];
  for(const c of text){const x=c.codePointAt(0); if(x<128)bytes.push(x);else if(x<2048)bytes.push(192|(x>>6),128|(x&63));else if(x<65536)bytes.push(224|(x>>12),128|((x>>6)&63),128|(x&63));else bytes.push(240|(x>>18),128|((x>>12)&63),128|((x>>6)&63),128|(x&63));}
  let dict=new Map(Array.from({length:256},(_,i)=>[String.fromCharCode(i),i])),next=256,w='';const codes=[];
  for(const b of bytes){const c=String.fromCharCode(b),wc=w+c;if(dict.has(wc))w=wc;else{codes.push(dict.get(w));if(next<4096)dict.set(wc,next++);else{dict=new Map(Array.from({length:256},(_,i)=>[String.fromCharCode(i),i]));next=256;}w=c;}}
  if(w)codes.push(dict.get(w));
  const raw=codes.flatMap(n=>[n>>8,n&255]),alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';let result='';
  for(let i=0;i<raw.length;i+=3){const a=raw[i],b=raw[i+1],c=raw[i+2],n=(a<<16)|((b||0)<<8)|(c||0);result+=alphabet[(n>>>18)&63]+alphabet[(n>>>12)&63]+(b===undefined?'=':alphabet[(n>>>6)&63])+(c===undefined?'=':alphabet[n&63]);}
  return result;
}
const data=encodeScope(JSON.stringify(report));
if(data.length>17500)return {result:"READ_ONLY_REPORT_TOO_LARGE",bytes:data.length,mutatedNodeIds:[],createdNodeIds:[]};
return {result:"READ_ONLY_SCOPE",encoding:"LZW-UTF8-u16be-base64-reset4096",data};
