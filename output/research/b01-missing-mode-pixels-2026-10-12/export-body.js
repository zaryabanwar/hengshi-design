// PREPARED ONLY. One separately reviewed and approved existing-unit export.
function packIds(ids) {
  const groups = new Map(), literalIds = [];
  for (const id of new Set(ids)) {
    const m = /^(.*:)(0|[1-9][0-9]*)$/.exec(id);
    if (!m || !Number.isSafeInteger(Number(m[2]))) { literalIds.push(id); continue; }
    if (!groups.has(m[1])) groups.set(m[1], []);
    groups.get(m[1]).push(Number(m[2]));
  }
  const packed = [...groups].map(([prefix, values]) => {
    values.sort((a,b) => a-b);
    const ranges = [];
    for (const v of values) {
      const last = ranges[ranges.length-1];
      if (last && v === last[last.length-1]+1) {
        if (last.length === 1) last.push(v); else last[1] = v;
      } else ranges.push([v]);
    }
    return [prefix, ranges.map(r => r.length === 1 ? r[0] : r)];
  });
  const decoded = literalIds.slice();
  for (const [prefix, ranges] of packed) for (const r of ranges) {
    if (typeof r === 'number') decoded.push(prefix+r);
    else for (let i=r[0]; i<=r[1]; i++) decoded.push(prefix+i);
  }
  const unique = [...new Set(ids)].sort();
  if (JSON.stringify(decoded.sort()) !== JSON.stringify(unique)) throw Error('Lossless ID mismatch');
  return {encoding:'prefix-inclusive-ranges-v1',count:unique.length,groups:packed,literalIds};
}


const descendants=n=>[n,...n.findAll(()=>true)];
const bytes=v=>encodeURIComponent(JSON.stringify(v)).match(/%[0-9A-F]{2}|[^%]/g).length;
const fingerprint=n=>JSON.stringify(descendants(n).map((v,i)=>({type:v.type,name:v.name,visible:v.visible,opacity:v.opacity,x:i?v.x:null,y:i?v.y:null,width:v.width,height:v.height,rotation:v.rotation,text:v.type==='TEXT'?v.characters:null,fills:'fills'in v?v.fills:null,strokes:'strokes'in v?v.strokes:null,font:v.type==='TEXT'?v.getStyledTextSegments(['fontName','fontSize','lineHeight','letterSpacing']):null})));
if(figma.editorType!=='figma'||(figma.fileKey&&figma.fileKey!==input.fileKey))throw Error('Wrong file/editor');
if(input.expected.length!==11||new Set(input.expected.map(e=>e.unitId)).size!==11||input.rootChildIds.length!==48)throw Error('Changed export scope');
const page=await figma.getNodeByIdAsync(input.pageId);
if(!page||page.type!=='PAGE'||figma.root.children.length!==1)throw Error('Changed page');
await figma.setCurrentPageAsync(page);
if(page.children.some(n=>n.name===input.tempName))throw Error('Prior temporary export remains; inspect before retry');
const root=await figma.getNodeByIdAsync(input.rootId);
if(!root||root.type!=='FRAME'||root.parent!==page||root.name!==input.rootName||JSON.stringify(root.children.map(n=>n.id))!==JSON.stringify(input.rootChildIds))throw Error('Changed mode root');
const originals=[];
for(const e of input.expected){const unit=await figma.getNodeByIdAsync(e.unitId),frame=await figma.getNodeByIdAsync(e.frameId);
 if(!unit||unit.type!=='FRAME'||unit.parent!==root||unit.name!==e.unitName||unit.width!==e.width||unit.height!==e.height||!frame||frame.type!=='FRAME'||frame.parent!==unit||frame.name!==e.frameName||frame.width!==e.frameWidth||frame.height!==e.frameHeight)throw Error('Changed source unit '+e.unitId);
 originals.push(unit);}
const fonts=new Map();for(const u of originals)for(const t of u.findAllWithCriteria({types:['TEXT']}))for(const run of t.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(run.fontName),run.fontName);
for(const f of fonts.values())await figma.loadFontAsync(f);
const before=originals.map(fingerprint),positions=originals.map(n=>[n.x,n.y]),rootBefore=fingerprint(root),pageOrder=page.children.map(n=>n.id).join('|'),rootOrder=root.children.map(n=>n.id).join('|');
const copies=[],created=[],cleanupFailures=[];let sheet=null,report=null;
try{
 sheet=figma.createAutoLayout('HORIZONTAL');created.push(sheet.id);sheet.name=input.tempName;sheet.paddingTop=sheet.paddingRight=sheet.paddingBottom=sheet.paddingLeft=24;sheet.itemSpacing=24;sheet.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];
 const right=Math.max(0,...page.children.filter(n=>n!==sheet&&'x'in n&&'width'in n).map(n=>n.x+n.width));page.appendChild(sheet);sheet.x=right+400;sheet.y=400;
 for(let i=0;i<originals.length;i++){const copy=originals[i].clone();copies.push(copy);created.push(...descendants(copy).map(n=>n.id));sheet.appendChild(copy);copy.resize(originals[i].width,originals[i].height);copy.layoutSizingHorizontal='FIXED';copy.layoutSizingVertical='FIXED';if(fingerprint(copy)!==before[i])throw Error('Changed export clone');}
 const tiles=copies.map((c,i)=>{const b=c.absoluteBoundingBox;if(!b)throw Error('Missing tile bounds');const values=[b.x-sheet.x,b.y-sheet.y,b.width,b.height];if(!values.every(Number.isInteger)||values[0]<0||values[1]<0||values[0]+values[2]>sheet.width||values[1]+values[3]>sheet.height)throw Error('Invalid tile bounds');return[originals[i].id,c.id,input.expected[i].inputIndex,0,...values];});
 if(sheet.width>input.maxWidth||sheet.height>input.maxHeight||sheet.width<=0||sheet.height<=0||new Set(created).size>input.maxTrackedIds)throw Error('Export finite bound');
 if(originals.some((n,i)=>fingerprint(n)!==before[i]||n.x!==positions[i][0]||n.y!==positions[i][1])||root.children.map(n=>n.id).join('|')!==rootOrder)throw Error('Source changed before capture');
 report={createdNodeIds:packIds(created),mutatedNodeIds:[page.id,root.id],sourceFields:['unitId','inputIndex','frameId','width','height'],sources:input.expected.map(e=>[e.unitId,e.inputIndex,e.frameId,e.width,e.height]),tileFields:['unitId','cloneId','inputIndex','imageIndex','x','y','width','height'],tiles,sheetBounds:[[sheet.width,sheet.height]],requestedScale:1,plannedImageCount:1,originalDescriptorUnchanged:true,originalPositionsUnchanged:true,rootDescriptorUnchanged:true,parentOrdersPreserved:true,allTemporaryNodesRemoved:true,removedTemporaryNodeIds:packIds(created),fonts:[...fonts.values()],limitations:input.limits};
 if(bytes(report)>input.maxReceiptBytes)throw Error('Finite report guard');
 await sheet.screenshot({scale:1});
}finally{
 for(const n of [...copies,...(sheet?[sheet]:[])])try{if(!n.removed)n.remove();}catch(_){cleanupFailures.push(n.id);}
 if(cleanupFailures.length)throw Error('Temporary cleanup failed; inspect before any separately approved retry');
}
report.allTemporaryNodesRemoved=copies.every(n=>n.removed)&&sheet.removed;report.originalDescriptorUnchanged=originals.every((n,i)=>fingerprint(n)===before[i]);report.originalPositionsUnchanged=originals.every((n,i)=>n.x===positions[i][0]&&n.y===positions[i][1]);report.rootDescriptorUnchanged=fingerprint(root)===rootBefore;report.parentOrdersPreserved=page.children.map(n=>n.id).join('|')===pageOrder&&root.children.map(n=>n.id).join('|')===rootOrder;
for(const k of ['allTemporaryNodesRemoved','originalDescriptorUnchanged','originalPositionsUnchanged','rootDescriptorUnchanged','parentOrdersPreserved'])if(!report[k])throw Error('Export preservation failed '+k);if(bytes(report)>input.maxReceiptBytes)throw Error('Final report guard');return report;
