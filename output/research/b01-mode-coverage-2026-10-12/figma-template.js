// PREPARED ONLY: one separately approved call, no automatic retry.
const input = __INPUT__;
function packIds(ids){
  const groups=new Map(),literalIds=[];
  for(const id of new Set(ids)){const m=/^(.*:)(0|[1-9][0-9]*)$/.exec(id);
    if(!m||!Number.isSafeInteger(Number(m[2]))){literalIds.push(id);continue;}
    if(!groups.has(m[1]))groups.set(m[1],[]);groups.get(m[1]).push(Number(m[2]));}
  const encoded=[...groups].map(([prefix,values])=>{values.sort((a,b)=>a-b);const spans=[];
    for(const value of values){const last=spans[spans.length-1];if(last&&value===last[last.length-1]+1){if(last.length===1)last.push(value);else last[1]=value;}else spans.push([value]);}
    return [prefix,spans.map(s=>s.length===1?s[0]:s)];});
  const decoded=literalIds.slice();for(const [p,spans] of encoded)for(const s of spans){if(typeof s==='number')decoded.push(p+s);else for(let n=s[0];n<=s[1];n++)decoded.push(p+n);}
  const expected=[...new Set(ids)].sort();if(JSON.stringify(decoded.sort())!==JSON.stringify(expected))throw Error('ID codec mismatch');
  return {encoding:'prefix-inclusive-ranges-v1',count:expected.length,groups:encoded,literalIds};
}
const bytes=v=>encodeURIComponent(JSON.stringify(v)).match(/%[0-9A-F]{2}|[^%]/g).length;
const repairIds=new Set(input.nameRepairs.map(r=>r.node_id));
const descendants=n=>[n,...('findAll'in n?n.findAll(()=>true):[])];
const fingerprint=n=>JSON.stringify(descendants(n).map((v,i)=>({type:v.type,name:repairIds.has(v.id)?null:v.name,
  visible:v.visible,opacity:v.opacity,x:i?v.x:null,y:i?v.y:null,width:v.width,height:v.height,rotation:v.rotation,
  text:v.type==='TEXT'?v.characters:null,fills:'fills'in v&&v.fills!==figma.mixed?v.fills:null,
  strokes:'strokes'in v?v.strokes:null,effects:'effects'in v?v.effects:null,
  fontRuns:v.type==='TEXT'?v.getStyledTextSegments(['fontName','fontSize','fills']):null})));
if(figma.editorType!=='figma'||(figma.fileKey&&figma.fileKey!==input.fileKey))throw Error('Wrong file/editor');
const page=await figma.getNodeByIdAsync('0:1');
if(!page||page.type!=='PAGE'||figma.root.children.length!==1)throw Error('Changed page context');
await figma.setCurrentPageAsync(page);
if(page.children.some(n=>n.name===input.rootName||n.name.startsWith('HSD_UIR_B01_TEMP_MODE_')))throw Error('Existing or uncertain partial mode composition; inspect before new approval');
if(input.references.length!==48||input.nameRepairs.length!==8||new Set(input.references.map(r=>r.name)).size!==48)throw Error('Changed scope');
const sources=new Map(),controls=new Map(),cloneParents=new Set(),repairs=[];
for(const spec of input.sources){const node=await figma.getNodeByIdAsync(spec.id);
  if(!node||node.type!=='FRAME'||node.parent?.id!==spec.parentId||node.name!==spec.name||node.width!==spec.width||node.height!==spec.height)throw Error('Changed source '+spec.id);
  if(descendants(node).some(n=>'fills'in n&&Array.isArray(n.fills)&&n.fills.some(p=>p.type==='IMAGE')))throw Error('Unreviewed source image');
  sources.set(spec.id,node);cloneParents.add(spec.parentId);
  const master=input.masters.find(m=>m.stream_id===spec.streamId);if(!master)throw Error('Missing control master');
  const matches=[];for(const inst of node.findAllWithCriteria({types:['INSTANCE']})){
    const component=await inst.getMainComponentAsync();if(component?.id===master.id)matches.push(inst);}
  if(matches.length!==1||!matches[0].parent)throw Error('Changed source stream control '+spec.id);
  controls.set(spec.id,matches[0]);cloneParents.add(matches[0].parent.id);
  const rendered=node.findAllWithCriteria({types:['TEXT']}).map(n=>n.characters).join('\n');
  const label=input.labels.find(l=>l.id===spec.streamId)?.label;
  if(!label||!rendered.includes('Delivery stream — currently '+label)||!rendered.includes(input.copy.apply)||!rendered.includes(input.copy.advisement))throw Error('Changed inherited control copy');
}
for(const spec of input.nameRepairs){const node=await figma.getNodeByIdAsync(spec.node_id);
  if(!node||node.type!=='FRAME'||node.name!==spec.expected_current_name||node.width!==spec.width||node.height!==spec.height)throw Error('Changed repair source '+spec.node_id);
  let parent=node.parent;while(parent&&parent.id!==spec.ancestorId)parent=parent.parent;
  if(!parent)throw Error('Changed repair ancestry');repairs.push({node,spec});}
const styles=await figma.getLocalTextStylesAsync(),roleStyles={};
for(const role of ['heading','body','meta']){const found=styles.filter(s=>s.name==='B01 reference / '+role);if(found.length!==1)throw Error('Changed text style '+role);roleStyles[role]=found[0];}
const variables=await figma.variables.getLocalVariablesAsync('COLOR'),colours={};
for(const name of ['paper','ink','white']){const found=variables.filter(v=>v.name==='D035/palette/'+name);if(found.length!==1)throw Error('Changed colour token');colours[name]=found[0];}
const floats=await figma.variables.getLocalVariablesAsync('FLOAT'),spacing={};
for(const [value,suffix] of [[16,4],[24,5]]){const found=floats.filter(v=>v.name==='D035/space/'+suffix);if(found.length!==1||!Object.values(found[0].valuesByMode).includes(value))throw Error('Changed spacing token');spacing[value]=found[0];}
const available=await figma.listAvailableFontsAsync();
if(!available.some(f=>f.fontName.family===input.fallbackFont.family&&f.fontName.style===input.fallbackFont.style))throw Error('Unavailable reviewed fallback');
const fonts=new Map([[JSON.stringify(input.fallbackFont),input.fallbackFont]]);
for(const style of Object.values(roleStyles))fonts.set(JSON.stringify(style.fontName),style.fontName);
for(const source of sources.values())for(const text of source.findAllWithCriteria({types:['TEXT']}))for(const run of text.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(run.fontName),run.fontName);
for(const font of fonts.values())await figma.loadFontAsync(font);
const inherited=page.children.slice(),before=inherited.map(fingerprint),positions=inherited.map(n=>[n.x,n.y]),pageOrder=inherited.map(n=>n.id).join('|');
const createdIds=[],frames=[],annotations=[],units=[],bounds=[];
const paint=name=>{const value=Object.values(colours[name].valuesByMode)[0];
  if(!value||typeof value!=='object'||!('r'in value))throw Error('Changed direct token value');
  return figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:value.r,g:value.g,b:value.b}},'color',colours[name]);};
function stack(parent,name,width,padding=24){const n=figma.createAutoLayout('VERTICAL');createdIds.push(n.id);n.name=name;n.resize(width,100);
  n.primaryAxisSizingMode='AUTO';n.counterAxisSizingMode='FIXED';n.clipsContent=false;n.itemSpacing=16;n.setBoundVariable('itemSpacing',spacing[16]);
  for(const key of ['paddingTop','paddingRight','paddingBottom','paddingLeft']){n[key]=padding;if(padding===24)n.setBoundVariable(key,spacing[24]);}
  n.fills=[paint('paper')];parent.appendChild(n);return n;}
async function text(parent,copy,role='body'){const n=figma.createText();createdIds.push(n.id);n.fontName=roleStyles[role].fontName;
  await n.setTextStyleIdAsync(roleStyles[role].id);n.characters=copy;n.fills=[paint('ink')];parent.appendChild(n);
  n.resize(parent.width-parent.paddingLeft-parent.paddingRight,24);n.textAutoResize='HEIGHT';n.layoutSizingHorizontal='FILL';n.layoutSizingVertical='HUG';return n;}
function trackClone(node){createdIds.push(...descendants(node).map(n=>n.id));return node;}
function cap(parent){if(!('children'in parent))return;const available=parent.width-(parent.paddingLeft||0)-(parent.paddingRight||0);
  for(const child of parent.children){if(['FRAME','INSTANCE','TEXT'].includes(child.type)&&child.width>available&&available>0)child.resize(available,child.height);if(child.type==='FRAME')cap(child);}}
function adapt(frame,mode){
  for(const n of descendants(frame)){
    if(mode==='MODE-UNAVAILABLE-FONT'&&n.type==='TEXT'){n.fontName=input.fallbackFont;n.textAutoResize='HEIGHT';}
    if(mode==='MODE-GRAYSCALE')for(const key of ['fills','strokes'])if(key in n&&Array.isArray(n[key]))n[key]=n[key].map(p=>{
      if(p.type!=='SOLID')return p;const v=.2126*p.color.r+.7152*p.color.g+.0722*p.color.b;
      const copy={...p,color:{r:v,g:v,b:v}};delete copy.boundVariables;return copy;});
    if(mode==='MODE-FORCED-COLORS'){
      if('fills'in n&&Array.isArray(n.fills)&&n.fills.length)n.fills=[paint(n.type==='TEXT'||['VECTOR','LINE','ELLIPSE'].includes(n.type)?'ink':'white')];
      if('strokes'in n&&n.strokes.length)n.strokes=[paint('ink')];
      if(['FRAME','INSTANCE'].includes(n.type)&&n!==frame){n.strokes=[paint('ink')];n.strokeWeight=1;}
      if('effects'in n)n.effects=[];
    }
  }
  cap(frame);
}
const root=stack(page,input.rootName,420);root.x=Math.max(0,...inherited.map(n=>n.x+n.width))+400;root.y=400;
for(const record of input.references){
  const unit=stack(root,'EVIDENCE UNIT / '+record.name,320,0);units.push(unit);
  const source=sources.get(record.sourceId);if(!source)throw Error('Unresolved source');
  let frame;
  if(record.kind==='FRAME'){frame=trackClone(source.clone());unit.appendChild(frame);frame.name=record.name;frame.resize(320,frame.height);frame.layoutSizingHorizontal='FIXED';}
  else{
    frame=stack(unit,record.name,320);await text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta');await text(frame,'Hengshi Design','heading');
    await text(frame,'Services / '+(record.templateId==='TPL-DIRECTORY-SEARCH'?'Directory open':record.templateId==='TPL-GLOBAL-NAVIGATION'?'Navigation open':'Recovery: confirmed error'),'meta');
    const label=input.labels.find(l=>l.id===record.streamId).label;await text(frame,'In force: '+label,'body');
    if(record.modeId==='MODE-PRINT'){
      await text(frame,'Printable reference summary','heading');await text(frame,'Current presentation: Quick Access. Selected next option: Detailed 3D — not applied.');
      await text(frame,record.templateId==='TPL-SYSTEM-RECOVERY'?'Confirmed pre-admission error; prior eligible Services content remains. No business action completed.':'Services remains the current location. Directory/navigation context is represented; no live results or publication is established.');
      await text(frame,'Online actions: /services · /book. Open the online page to navigate, change presentation or book. This printed summary has no active controls.','body');
    }else{
      if(record.modeId==='MODE-UNAVAILABLE-IMAGE-ASSET')await text(frame,'Optional brand mark omitted. Full company name above remains readable.','body');
      const control=trackClone(controls.get(record.sourceId).clone());frame.appendChild(control);control.resize(272,control.height);control.layoutSizingHorizontal='FIXED';
      if(record.modeId==='MODE-SCREEN-READER')await text(frame,'Semantic order: host heading → context/status → delivery fieldset/legend → labelled options → Apply → safe recovery/links.','meta');
      if(record.templateId==='TPL-SYSTEM-RECOVERY')await text(frame,'Confirmed pre-admission error. Prior eligible Services content remains; safe recovery: open the directory. No successful mutation is inferred.','body');
    }
  }
  adapt(frame,record.modeId);frames.push(frame);
  const note=stack(unit,'ANNOTATION / '+record.name,320);annotations.push(note);
  await text(note,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta');
  await text(note,record.kind+' · '+record.modeId+' · '+record.streamId+' · source '+record.sourceId,'meta');
  await text(note,input.hostNotes[record.templateId],'meta');await text(note,input.modeNotes[record.modeId],'meta');
  await text(note,'Design specimen only. No actual browser, OS palette, font/image failure, screen reader, print, focus or action execution. Full profiles, prototypes, exports and acceptance remain.','meta');
  for(const n of descendants(unit))if(['TEXT','INSTANCE'].includes(n.type)){
    if(![n.width,n.height].every(v=>Number.isFinite(v)&&v>0))bounds.push([n.id,'invalid size']);
    const p=n.parent;if(p&&'width'in p&&n.x+n.width>p.width+1)bounds.push([n.id,'horizontal overflow']);}
}
if(bounds.length)throw Error('Mode bounds findings; inspect partial composition before separately approved retry');
// Only these eight exact existing frame names may change; all appearance is retained.
for(const {node,spec} of repairs)node.name=spec.proposed_name;
const unitBefore=units.map(fingerprint),unitPositions=units.map(n=>[n.x,n.y]),rootOrder=root.children.map(n=>n.id).join('|');
const fontGroups=new Map();for(const frame of frames)for(const n of frame.findAllWithCriteria({types:['TEXT']}))for(const run of n.getStyledTextSegments(['fontName'])){
  const key=JSON.stringify(run.fontName);if(!fontGroups.has(key))fontGroups.set(key,[]);fontGroups.get(key).push(n.id);}
const base={createdNodeIds:packIds(createdIds),mutatedNodeIds:[...new Set([page.id,...cloneParents,...repairIds])],createdComponentIds:[],createdVariableIds:[],createdStyleIds:[],rootId:root.id,
  frameFields:['id','inputIndex','width','height'],frames:frames.map((f,i)=>[f.id,i,f.width,f.height]),annotationIds:packIds(annotations.map(n=>n.id)),
  unitFields:['id','inputIndex','width','height'],units:units.map((u,i)=>[u.id,i,u.width,u.height]),
  nameRepairs:repairs.map(({node,spec})=>[node.id,spec.expected_current_name,node.name]),
  fontGroups:[...fontGroups].map(([font,ids])=>({font:JSON.parse(font),textIds:packIds(ids)})),boundsFindingCount:0,B01Complete:false,
  coveredScope:input.scope,limitations:input.limitations};
if(bytes(base)>input.capture.maxReceiptBytes)throw Error('Mode report exceeds finite guard');
const sheets=[],rows=[],copies=[],temporaryIds=[],tiles=[],cleanupFailures=[];let report=null;
try{
  for(let s=0;s<input.capture.groups.length;s++){
    const sheet=figma.createAutoLayout('HORIZONTAL');sheets.push(sheet);temporaryIds.push(sheet.id);sheet.name='HSD_UIR_B01_TEMP_MODE_'+s+'_V01';
    sheet.paddingTop=sheet.paddingRight=sheet.paddingBottom=sheet.paddingLeft=24;sheet.itemSpacing=24;sheet.fills=[paint('white')];page.appendChild(sheet);sheet.x=root.x+root.width+400+s*5200;sheet.y=400;
    for(const index of input.capture.groups[s]){const copy=units[index].clone();copies.push({node:copy,index,sheet:s});temporaryIds.push(...descendants(copy).map(n=>n.id));
      sheet.appendChild(copy);copy.resize(units[index].width,units[index].height);copy.layoutSizingHorizontal='FIXED';copy.layoutSizingVertical='FIXED';
      if(fingerprint(copy)!==unitBefore[index])throw Error('Mode capture clone mismatch');}
  }
  for(const item of copies){const b=item.node.absoluteBoundingBox,sheet=sheets[item.sheet];if(!b)throw Error('Missing mode tile bounds');
    const geometry=[b.x-sheet.x,b.y-sheet.y,b.width,b.height];if(!geometry.every(Number.isInteger)||geometry[0]<0||geometry[1]<0||geometry[0]+geometry[2]>sheet.width||geometry[1]+geometry[3]>sheet.height)throw Error('Invalid mode tile');
    tiles.push([units[item.index].id,item.node.id,item.index,item.sheet,...geometry]);}
  const sheetBounds=sheets.map(s=>[s.width,s.height]);
  if(copies.length!==48||sheetBounds.some(([w,h])=>w<=0||h<=0||w>input.capture.maxWidth||h>input.capture.maxHeight)||createdIds.length+temporaryIds.length>input.capture.maxTrackedCreatedIds)throw Error('Finite mode capture limit');
  report={...base,createdNodeIds:packIds([...createdIds,...temporaryIds]),temporaryNodeIds:packIds(temporaryIds),removedTemporaryNodeIds:packIds(temporaryIds),
    tileFields:['unitId','cloneId','inputIndex','imageIndex','x','y','width','height'],tiles,sheetBounds,plannedImageCount:5,requestedScale:1,
    allTemporaryNodesRemoved:true,originalDescriptorUnchangedExceptApprovedNames:true,originalPositionsUnchanged:true,originalPageOrderPreserved:true,
    newUnitsDescriptorUnchanged:true,newUnitsPositionsUnchanged:true,newRootOrderPreserved:true,eightExactNamesRepaired:true};
  if(bytes(report)>input.capture.maxReceiptBytes)throw Error('Complete mode capture report exceeds finite guard');
  for(const sheet of sheets)await sheet.screenshot({scale:1});
}finally{
  for(const node of [...copies.map(c=>c.node),...rows,...sheets])try{if(!node.removed)node.remove();}catch(_){cleanupFailures.push(node.id);}
  if(cleanupFailures.length)throw Error('Mode cleanup failed; inspect partial composition before separately approved retry');
}
report.allTemporaryNodesRemoved=[...copies.map(c=>c.node),...sheets].every(n=>n.removed);
report.originalDescriptorUnchangedExceptApprovedNames=inherited.every((n,i)=>fingerprint(n)===before[i]);
report.originalPositionsUnchanged=inherited.every((n,i)=>n.x===positions[i][0]&&n.y===positions[i][1]);
report.originalPageOrderPreserved=page.children.filter(n=>n!==root).map(n=>n.id).join('|')===pageOrder;
report.newUnitsDescriptorUnchanged=units.every((n,i)=>fingerprint(n)===unitBefore[i]);
report.newUnitsPositionsUnchanged=units.every((n,i)=>n.x===unitPositions[i][0]&&n.y===unitPositions[i][1]);
report.newRootOrderPreserved=root.children.map(n=>n.id).join('|')===rootOrder;
report.eightExactNamesRepaired=repairs.every(({node,spec})=>node.name===spec.proposed_name);
for(const key of ['allTemporaryNodesRemoved','originalDescriptorUnchangedExceptApprovedNames','originalPositionsUnchanged','originalPageOrderPreserved','newUnitsDescriptorUnchanged','newUnitsPositionsUnchanged','newRootOrderPreserved','eightExactNamesRepaired'])if(report[key]!==true)throw Error('Mode preservation failed '+key);
if(bytes(report)>input.capture.maxReceiptBytes)throw Error('Final mode report exceeds finite guard');
return report;
