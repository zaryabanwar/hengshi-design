// Local preparation. No execution authority. One approved call must combine
// source preflight,28 editable responsive references/annotations and five images.
const input = __INPUT__;
function packIds(ids) {
  const groups=new Map(),literalIds=[];
  for(const id of new Set(ids)) {
    const match=/^(.*:)(0|[1-9][0-9]*)$/.exec(id);
    if(!match||!Number.isSafeInteger(Number(match[2]))) {literalIds.push(id);continue;}
    if(!groups.has(match[1]))groups.set(match[1],[]);
    groups.get(match[1]).push(Number(match[2]));
  }
  const encoded=[...groups].map(([prefix,values])=>{
    values.sort((a,b)=>a-b);const ranges=[];
    for(const value of values){const last=ranges[ranges.length-1];
      if(last&&value===last[last.length-1]+1){if(last.length===1)last.push(value);else last[1]=value;}
      else ranges.push([value]);}
    return [prefix,ranges.map(r=>r.length===1?r[0]:r)];
  });
  const decoded=literalIds.slice();
  for(const [prefix,ranges] of encoded)for(const r of ranges){
    if(typeof r==='number')decoded.push(prefix+r);
    else for(let n=r[0];n<=r[1];n++)decoded.push(prefix+n);}
  const expected=[...new Set(ids)].sort();
  if(JSON.stringify(decoded.sort())!==JSON.stringify(expected))throw Error('ID codec mismatch');
  return {encoding:'prefix-inclusive-ranges-v1',count:expected.length,groups:encoded,literalIds};
}
const bytes=value=>encodeURIComponent(JSON.stringify(value)).match(/%[0-9A-F]{2}|[^%]/g).length;
const fingerprint=node=>JSON.stringify([node,...('findAll'in node?node.findAll(()=>true):[])].map((n,i)=>({
  type:n.type,name:n.name,visible:n.visible,opacity:n.opacity,x:i? n.x:null,y:i? n.y:null,
  width:n.width,height:n.height,rotation:n.rotation,text:n.type==='TEXT'?n.characters:null
})));
if(figma.editorType!=='figma'||(figma.fileKey&&figma.fileKey!==input.fileKey))throw Error('Wrong file/editor');
const page=await figma.getNodeByIdAsync('0:1');
if(!page||page.type!=='PAGE'||figma.root.children.length!==1)throw Error('Changed page context');
await figma.setCurrentPageAsync(page);
const rootName='B01 / Responsive viewport references / v1';
if(page.children.some(n=>n.name===rootName||n.name.startsWith('HSD_UIR_B01_TEMP_RESPONSIVE_')))
  throw Error('Existing or uncertain partial responsive result; inspect before separately approved retry');
if(input.references.length!==28||new Set(input.references.map(r=>r.name)).size!==28)throw Error('Changed28-view scope');
const originals=new Map();
for(const spec of input.sources){const node=await figma.getNodeByIdAsync(spec.id);
  if(!node||node.type!=='FRAME'||node.parent?.id!==spec.parentId||node.name!==spec.name||node.width!==spec.width||node.height!==spec.height)
    throw Error('Changed source '+spec.id);
  originals.set(spec.id,node);}
const styles=await figma.getLocalTextStylesAsync();
const metaMatches=styles.filter(s=>s.name==='B01 reference / meta');
if(metaMatches.length!==1)throw Error('Changed inherited meta style');
const meta=metaMatches[0];
const colourVariables=await figma.variables.getLocalVariablesAsync('COLOR');
const paperMatches=colourVariables.filter(v=>v.name==='D035/palette/paper');
const inkMatches=colourVariables.filter(v=>v.name==='D035/palette/ink');
if(paperMatches.length!==1||inkMatches.length!==1)throw Error('Changed inherited colour tokens');
const paint=variable=>{const collectionValue=Object.values(variable.valuesByMode)[0];
  if(!collectionValue||typeof collectionValue!=='object'||!('r'in collectionValue))throw Error('Changed colour value');
  return figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:collectionValue.r,g:collectionValue.g,b:collectionValue.b}},'color',variable);};
const fonts=new Map([[JSON.stringify(meta.fontName),meta.fontName]]);
for(const node of originals.values())for(const text of node.findAllWithCriteria({types:['TEXT']}))
  for(const run of text.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(run.fontName),run.fontName);
for(const font of fonts.values())await figma.loadFontAsync(font);
const inherited=page.children.slice(),before=inherited.map(fingerprint),positions=inherited.map(n=>[n.x,n.y]);
const pageOrder=inherited.map(n=>n.id).join('|');
const createdIds=[],frames=[],notes=[],units=[],boundsFindings=[];
function stack(parent,name,width,padding=0){const n=figma.createAutoLayout('VERTICAL');createdIds.push(n.id);
  n.name=name;n.resize(width,100);n.primaryAxisSizingMode='AUTO';n.counterAxisSizingMode='FIXED';
  n.paddingTop=n.paddingRight=n.paddingBottom=n.paddingLeft=padding;n.itemSpacing=16;n.clipsContent=false;
  n.fills=[paint(paperMatches[0])];parent.appendChild(n);return n;}
async function noteText(parent,copy){const n=figma.createText();createdIds.push(n.id);n.fontName=meta.fontName;
  await n.setTextStyleIdAsync(meta.id);n.characters=copy;n.fills=[paint(inkMatches[0])];parent.appendChild(n);
  n.resize(parent.width-parent.paddingLeft-parent.paddingRight,18);n.textAutoResize='HEIGHT';
  n.layoutSizingHorizontal='FILL';n.layoutSizingVertical='HUG';return n;}
function capChildren(parent){if(!('children'in parent))return;
  const available=parent.width-(parent.paddingLeft||0)-(parent.paddingRight||0);
  for(const child of parent.children){
    if(['FRAME','INSTANCE','TEXT'].includes(child.type)&&child.width>available&&available>0)child.resize(available,child.height);
    if(child.type==='FRAME')capChildren(child);
  }}
const root=stack(page,rootName,1488,24);root.x=Math.max(0,...inherited.map(n=>n.x+n.width))+400;root.y=400;
for(const record of input.references){
  const unit=stack(root,'EVIDENCE UNIT / '+record.name,record.width);units.push(unit);
  const source=originals.get(record.sourceId);if(!source)throw Error('Unresolved source');
  const frame=source.clone();createdIds.push(frame.id,...frame.findAll(()=>true).map(n=>n.id));unit.appendChild(frame);
  frame.name=record.name;frame.resize(record.width,frame.height);frame.layoutSizingHorizontal='FIXED';capChildren(frame);
  const note=stack(unit,'ANNOTATION / '+record.name,record.width,24);
  await noteText(note,'REFERENCE FIXTURE — NOT PUBLIC COPY');
  await noteText(note,record.viewportNote);
  await noteText(note,'Current stream '+record.streamId+'. Inherited content and controls; source '+record.sourceId+'. Profiles '+record.profiles.join(', ')+'.');
  await noteText(note,record.interactionNote);
  await noteText(note,'Design specimen only: no actual browser zoom, keyboard, screen-reader, safe-area, viewport occlusion, focus or action execution. Remaining modes, states and host/process evidence are not discharged.');
  frames.push(frame);notes.push(note);
  for(const n of frame.findAll(n=>n.type==='TEXT'||n.type==='INSTANCE')){
    if(![n.width,n.height].every(v=>Number.isFinite(v)&&v>0))boundsFindings.push([n.id,'invalid size']);
    const parent=n.parent;if(parent&&'width'in parent&&n.x+n.width>parent.width+1)boundsFindings.push([n.id,'horizontal overflow']);}
}
if(boundsFindings.length)throw Error('Responsive bounds finding; preserve partial result and inspect before any retry');
const unitsBefore=units.map(fingerprint),unitPositions=units.map(n=>[n.x,n.y]),rootOrder=root.children.map(n=>n.id).join('|');
const fontGroups=new Map();
for(const frame of frames)for(const text of frame.findAllWithCriteria({types:['TEXT']})){
  for(const run of text.getStyledTextSegments(['fontName'])){const key=JSON.stringify(run.fontName);
    if(!fontGroups.has(key))fontGroups.set(key,[]);fontGroups.get(key).push(text.id);}}
const base={createdNodeIds:packIds(createdIds),mutatedNodeIds:[page.id],createdComponentIds:[],createdVariableIds:[],createdStyleIds:[],
  rootId:root.id,frameFields:['id','inputIndex','width','height'],frames:frames.map((f,i)=>[f.id,i,f.width,f.height]),
  annotationIds:packIds(notes.map(n=>n.id)),unitFields:['id','inputIndex','width','height'],units:units.map((u,i)=>[u.id,i,u.width,u.height]),
  fontGroups:[...fontGroups].map(([font,ids])=>({font:JSON.parse(font),textIds:packIds(ids)})),
  boundsFindingCount:0,B01Complete:false,coveredScope:'28 responsive viewport design references only',limitations:input.limitations};
if(bytes(base)>19000)throw Error('Complete responsive receipt exceeds finite guard; inspect partial result');
const sheets=[],rows=[],copies=[],tempIds=[],tiles=[],cleanupFailures=[];let report=null;
try{
  for(let s=0;s<input.capture.groups.length;s++){
    const group=input.capture.groups[s],sheet=figma.createAutoLayout('VERTICAL');sheets.push(sheet);tempIds.push(sheet.id);
    sheet.name='HSD_UIR_B01_TEMP_RESPONSIVE_'+s+'_V01';sheet.paddingTop=sheet.paddingRight=sheet.paddingBottom=sheet.paddingLeft=24;
    sheet.itemSpacing=24;sheet.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];page.appendChild(sheet);
    sheet.x=root.x+root.width+400+s*4000;sheet.y=400;
    for(let offset=0;offset<group.indices.length;offset+=group.columns){const row=figma.createAutoLayout('HORIZONTAL');
      rows.push(row);tempIds.push(row.id);row.name='Temporary responsive comparison row';row.itemSpacing=24;sheet.appendChild(row);
      for(const index of group.indices.slice(offset,offset+group.columns)){
        const copy=units[index].clone();copies.push({node:copy,index,sheet:s});tempIds.push(copy.id,...copy.findAll(()=>true).map(n=>n.id));
        row.appendChild(copy);copy.resize(units[index].width,units[index].height);copy.layoutSizingHorizontal='FIXED';copy.layoutSizingVertical='FIXED';
        if(fingerprint(copy)!==unitsBefore[index])throw Error('Responsive clone mismatch');}}
  }
  for(const item of copies){const b=item.node.absoluteBoundingBox,sheet=sheets[item.sheet];if(!b)throw Error('Missing tile bounds');
    const geometry=[b.x-sheet.x,b.y-sheet.y,b.width,b.height];
    if(!geometry.every(Number.isInteger)||geometry[0]<0||geometry[1]<0||geometry[0]+geometry[2]>sheet.width||geometry[1]+geometry[3]>sheet.height)
      throw Error('Invalid responsive tile');
    tiles.push([units[item.index].id,item.node.id,item.index,item.sheet,...geometry]);}
  const sheetBounds=sheets.map(s=>[s.width,s.height]);
  if(copies.length!==28||sheetBounds.some(([w,h])=>w<=0||h<=0||w>3600||h>4800)||createdIds.length+tempIds.length>8000)
    throw Error('Finite responsive capture limit exceeded');
  report={...base,createdNodeIds:packIds([...createdIds,...tempIds]),temporaryNodeIds:packIds(tempIds),removedTemporaryNodeIds:packIds(tempIds),
    tileFields:['unitId','cloneId','inputIndex','imageIndex','x','y','width','height'],tiles,sheetBounds,plannedImageCount:5,requestedScale:1,
    allTemporaryNodesRemoved:true,originalGeometryTextUnchanged:true,originalPositionsUnchanged:true,originalPageOrderPreserved:true,
    newUnitsGeometryTextUnchanged:true,newUnitsPositionsUnchanged:true,newRootOrderPreserved:true};
  if(bytes(report)>19000)throw Error('Complete capture receipt exceeds finite guard');
  for(const sheet of sheets)await sheet.screenshot({scale:1});
}finally{for(const node of [...copies.map(c=>c.node),...rows,...sheets]){
  try{if(!node.removed)node.remove();}catch(_){cleanupFailures.push(node.id);}}
  if(cleanupFailures.length)throw Error('Responsive cleanup failed; inspect before separately approved retry');}
report.allTemporaryNodesRemoved=[...copies.map(c=>c.node),...rows,...sheets].every(n=>n.removed);
report.originalGeometryTextUnchanged=inherited.every((n,i)=>fingerprint(n)===before[i]);
report.originalPositionsUnchanged=inherited.every((n,i)=>n.x===positions[i][0]&&n.y===positions[i][1]);
report.originalPageOrderPreserved=page.children.filter(n=>n!==root).map(n=>n.id).join('|')===pageOrder;
report.newUnitsGeometryTextUnchanged=units.every((n,i)=>fingerprint(n)===unitsBefore[i]);
report.newUnitsPositionsUnchanged=units.every((n,i)=>n.x===unitPositions[i][0]&&n.y===unitPositions[i][1]);
report.newRootOrderPreserved=root.children.map(n=>n.id).join('|')===rootOrder;
for(const key of ['allTemporaryNodesRemoved','originalGeometryTextUnchanged','originalPositionsUnchanged','originalPageOrderPreserved','newUnitsGeometryTextUnchanged','newUnitsPositionsUnchanged','newRootOrderPreserved'])
  if(report[key]!==true)throw Error('Responsive preservation failed '+key+'; inspect before separately approved retry');
if(bytes(report)>19000)throw Error('Final complete receipt exceeds finite guard');
return report;
