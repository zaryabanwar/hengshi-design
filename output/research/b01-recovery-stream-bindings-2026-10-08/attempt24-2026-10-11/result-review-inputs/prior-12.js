// PREPARED ONLY. A new, individually approved Figma call is required.
// Shared status specimens supplement host-template evidence; they cannot replace it.
const input = /*RECOVERY_INPUT*/ null;
if (!input || input.product !== 'Hengshi Design v1' || input.states.length !== 3 || input.surfaces.length !== 1 || input.streams.length !== 4 || input.planned_references.length !== 12) throw Error('Changed recovery scope');
if (figma.editorType !== 'figma' || (figma.fileKey && figma.fileKey !== input.fileKey)) throw Error('Wrong file/editor');
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE' || figma.root.children.length !== 1) throw Error('Changed page context');
await figma.setCurrentPageAsync(page);
const rootName = 'B01 / Shared recovery stream references / v1';
if (page.findOne(n => n.name === rootName)) throw Error('Existing or partial recovery composition; inspect before any retry');
const navigation = await figma.getNodeByIdAsync('21:290');
const streamSet = await figma.getNodeByIdAsync('21:289');
const actionMaster = await figma.getNodeByIdAsync('14:18');
if (!navigation || navigation.type !== 'FRAME' || navigation.parent !== page ||
    !streamSet || streamSet.type !== 'COMPONENT_SET' || streamSet.children.length !== 16 ||
    !actionMaster || actionMaster.type !== 'COMPONENT' || actionMaster.parent?.type === 'COMPONENT_SET') throw Error('Changed inherited checkpoint');
const actionLabel = Object.keys(actionMaster.componentPropertyDefinitions).find(k => k.startsWith('Label#'));
if (!actionLabel || actionMaster.componentPropertyDefinitions[actionLabel].type !== 'TEXT') throw Error('Missing inherited text action label');
const masters = new Map();
for (const record of input.streamMasters) {
  const node = await figma.getNodeByIdAsync(record.id);
  if (!node || node.type !== 'COMPONENT' || node.parent !== streamSet || node.name !== record.name) throw Error('Changed stream master');
  masters.set(record.stream_id+'|'+record.state_id, node);
}
if (masters.size !== 12 || input.streams.some(s => ['STATE-OPEN','STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED'].some(state => !masters.has(s.id+'|'+state)))) throw Error('Changed recovery stream scope');
const styles = {}, colours = {}, spaces = {};
const localStyles = await figma.getLocalTextStylesAsync();
for (const role of ['heading','body','meta']) {
  const matches = localStyles.filter(s => s.name === 'B01 reference / ' + role);
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited text style');
  styles[role] = matches[0];
}
const fontInputs = [...Object.values(styles).map(s => s.fontName),
  ...[actionMaster,...masters.values()].flatMap(m => m.findAllWithCriteria({types:['TEXT']}).flatMap(n => n.getStyledTextSegments(['fontName']).map(s => s.fontName)))];
for (const font of new Map(fontInputs.map(f => [f.family+'/'+f.style,f])).values()) await figma.loadFontAsync(font);
const localColours = await figma.variables.getLocalVariablesAsync('COLOR');
const localFloats = await figma.variables.getLocalVariablesAsync('FLOAT');
for (const name of ['ink','paper','white','mist']) {
  const matches = localColours.filter(v => v.name === 'D035/palette/' + name);
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited colour');
  colours[name] = matches[0];
}
for (const [number,value] of [4,8,12,16,24,32,48,64,96].entries()) {
  const matches = localFloats.filter(v => v.name === 'D035/space/' + (number+1));
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited spacing');
  spaces[value] = matches[0];
}
const collection = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.id === colours.ink.variableCollectionId);
if (!collection || Object.values(colours).some(v => v.variableCollectionId !== collection.id)) throw Error('Changed palette collection');
for (const v of Object.values(colours)) {
  const value = v.valuesByMode[collection.defaultModeId];
  if (!value || !['r','g','b'].every(k => Number.isFinite(value[k]) && value[k]>=0 && value[k]<=1)) throw Error('Invalid direct colour');
}
for (const [value,v] of Object.entries(spaces)) if (v.variableCollectionId !== collection.id || v.valuesByMode[collection.defaultModeId] !== Number(value)) throw Error('Changed spacing value');
// No canvas construction occurs before the guards above complete.
const rightEdge = Math.max(0,...page.children.map(n => n.x+n.width));
const paint = name => {
  const value = colours[name].valuesByMode[collection.defaultModeId];
  return figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:value.r,g:value.g,b:value.b}},'color',colours[name]);
};
function stack(parent,name,width,background) {
  const node = figma.createAutoLayout('VERTICAL'); node.name = name;
  node.resize(width,100); node.primaryAxisSizingMode='AUTO'; node.counterAxisSizingMode='FIXED'; node.clipsContent=false;
  node.fills=[paint(background)];
  for (const key of ['paddingTop','paddingRight','paddingBottom','paddingLeft']) {node[key]=24;node.setBoundVariable(key,spaces[24]);}
  node.itemSpacing=16; node.setBoundVariable('itemSpacing',spaces[16]);
  if (parent) parent.appendChild(node); else page.appendChild(node);
  return node;
}
async function text(parent,value,role='body',foreground='ink') {
  const node=figma.createText(); node.fontName=styles[role].fontName;
  await node.setTextStyleIdAsync(styles[role].id); node.characters=value; parent.appendChild(node);
  node.resize(Math.max(1,parent.width-parent.paddingLeft-parent.paddingRight),24);
  node.textAutoResize='HEIGHT'; node.layoutSizingHorizontal='FILL'; node.layoutSizingVertical='HUG';node.fills=[paint(foreground)];
  return node;
}
const root=stack(null,rootName,440,'mist');root.x=rightEdge+400;root.y=400;

await text(root,'SHARED RECOVERY STREAM REFERENCES — v1','heading');
await text(root,'REFERENCE FIXTURES — NOT PUBLIC COPY. Twelve explicit stream/state references at320px; no whole-profile or complete B01 claim.','meta');
const frames=[],annotations=[];
for(const stream of input.streams)for(const state of input.states){
 const spec=input.planned_references.find(r=>r.stream_id===stream.id&&r.state_id===state.id);
 if(!spec)throw Error('Missing exact reference binding');
 const frame=stack(root,spec.planned_frame_name,320,'paper');
 await text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta');
 await text(frame,'Hengshi Design · Services','heading');
 await text(frame,'Services — current | Evidence | About | Contact');
 await text(frame,'Home / Services','meta');
 const control=masters.get(stream.id+'|'+spec.source_control_state).createInstance();frame.appendChild(control);control.resize(272,Math.max(1,control.height));
 await text(frame,state.title,'heading');await text(frame,state.body);
 const action=actionMaster.createInstance();frame.appendChild(action);action.setProperties({[actionLabel]:state.action});
 await text(frame,'Eligible public page content remains readable in this reference. No World entry, business action, permission or staff-presence claim is established.','meta');
 const note=stack(root,'ANNOTATION / '+spec.planned_frame_name,320,'paper');
 await text(note,'Host: TPL-SYSTEM-RECOVERY. Public context: Services. Represented in-force choice: '+stream.label+'. Current location/open context remains; no control or action is executed.','meta');
 await text(note,'Preserved truth: '+state.truth+'. Smallest safe action: '+state.action_kind+'. Error means confirmed pre-admission failure, not pending/unknown success.','meta');
 await text(note,'Inherited D-057 labels, order, current/pending and accepted notices remain editable component references. Keyboard/focus/announcement associations and host prototype behavior require separate inspection. MODE-KEYBOARD is an authored reference axis, not executed browser evidence.','meta');
 await text(note,'These twelve narrow light references do not replace other viewport/mode/state profiles, the48shared grammar specimens, the eight ceiling-refusal host bindings, complete-process proof or B01 EXIT.','meta');
 frames.push({node:frame,state,stream,spec});annotations.push(note.id);
}
const boundsFindings=[];
for(const {node:frame} of frames)for(const node of frame.findAll(n=>n.type==='TEXT'||n.type==='INSTANCE')){
 if(![node.width,node.height].every(v=>Number.isFinite(v)&&v>0))boundsFindings.push({id:node.id,issue:'invalid bounds'});
 const parent=node.parent;if(parent&&'width'in parent&&node.x+node.width>parent.width+1)boundsFindings.push({id:node.id,issue:'horizontal overflow',parentId:parent.id});
}
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

const groups=new Map();for(const finding of boundsFindings){const key=JSON.stringify([finding.issue,finding.parentId??null]);if(!groups.has(key))groups.set(key,[]);groups.get(key).push(finding.id);}
const report={createdNodeIds:packIds([root.id,...root.findAll(()=>true).map(n=>n.id)]),mutatedNodeIds:[page.id],createdComponentIds:[],createdVariableIds:[],createdStyleIds:[],rootId:root.id,
 frameFields:['id','inputIndex','width','height'],frames:frames.map(f=>[f.node.id,input.planned_references.indexOf(f.spec),f.node.width,f.node.height]),annotationIds:packIds(annotations),boundsFindingCount:boundsFindings.length,
 boundsFindings:[...groups].map(([key,ids])=>({context:JSON.parse(key),nodeIds:packIds(ids)})),B01Complete:false,coveredScope:'12 explicit shared recovery stream/state references only',limitations:input.limitations,reportFormat:'recovery-stream-ordinals-and-lossless-ids-v1'};
const reportBytes=encodeURIComponent(JSON.stringify(report)).match(/%[0-9A-F]{2}|[^%]/g).length;
if(reportBytes>19000)throw Error('Recovery report '+reportBytes+' bytes exceeds local19000-byte guard; inspect any uncertain partial canvas before retry');
await frames.find(f=>f.state.id==='STATE-ERROR'&&f.stream.id==='S-HIGH').node.screenshot();
await frames.find(f=>f.state.id==='STATE-PREFERENCE-WRITE-FAILED'&&f.stream.id==='S-SEMANTIC').node.screenshot();
return report;
