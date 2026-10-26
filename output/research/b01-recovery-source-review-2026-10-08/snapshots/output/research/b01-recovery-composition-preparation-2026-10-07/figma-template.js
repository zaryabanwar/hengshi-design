// PREPARED ONLY. A new, individually approved Figma call is required.
// Shared status specimens supplement host-template evidence; they cannot replace it.
const input = /*RECOVERY_INPUT*/ null;
if (!input || input.product !== 'Hengshi Design v1' || input.states.length !== 16 || input.surfaces.length !== 3) throw Error('Changed recovery scope');
if (figma.editorType !== 'figma' || (figma.fileKey && figma.fileKey !== input.fileKey)) throw Error('Wrong file/editor');
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE' || figma.root.children.length !== 1) throw Error('Changed page context');
await figma.setCurrentPageAsync(page);
const rootName = 'B01 / Shared recovery specimens / v1';
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
  masters.set(record.state_id, node);
}
if (masters.size !== 2 || !masters.has('STATE-STREAM-CHANGED') || !masters.has('STATE-PREFERENCE-WRITE-FAILED')) throw Error('Changed recovery stream scope');
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
await text(root,'SHARED RECOVERY GRAMMAR — v1','heading');
await text(root,'REFERENCE FIXTURES — NOT PUBLIC COPY. Sixteen shared states on three annotated surfaces; not complete pages or full stream/profile coverage.','meta');
const frames=[],annotations=[];
for (const surface of input.surfaces) {
  const dark=surface.id==='dark'; const background=dark?'ink':surface.id==='forced-colours-specimen'?'white':'paper'; const foreground=dark?'white':'ink';
  for (const state of input.states) {
    const frame=stack(root,'B01 shared recovery / '+state.id+' / '+surface.id+' / v1',320,background);
    await text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta',foreground);
    await text(frame,state.title,'heading',foreground);await text(frame,state.body,'body',foreground);
    const action=actionMaster.createInstance();frame.appendChild(action);action.setProperties({[actionLabel]:state.action});
    if (['STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED'].includes(state.id)) {
      const instance=masters.get(state.id).createInstance();frame.appendChild(instance);instance.resize(272,Math.max(1,instance.height));
    }
    frames.push({node:frame,state,surface});
    const note=stack(root,'ANNOTATION / '+state.id+' / '+surface.id,320,'paper');
    await text(note,'Preserved truth: '+state.truth,'meta');
    await text(note,'Smallest safe action: '+state.action_kind+'. Appearance only; no route, request, permission, retry, storage or sign-in is executed.','meta');
    await text(note,'Shared grammar applies to '+input.streams.map(s => s.id).join(', ')+'. Each host still needs its own contracted stream/state, context, input, focus, viewport and complete-process evidence. No evidence obligation is deduplicated by this specimen.','meta');
    await text(note,'Status announcement semantics, live-region urgency and focus restoration require host-specific reference and browser evidence. These visual specimens do not execute announcements or move focus.','meta');
    if (state.held) await text(note,state.held,'meta');
    if (surface.id==='forced-colours-specimen') await text(note,'OS system roles: '+surface.implementation_roles.join(', ')+'. This editable token-colour specimen does not execute forced-colours or bind OS colours. Later host/browser evidence must prove actual system roles and visibility.','meta');
    if (state.id==='STATE-FOCUS') await text(note,'The label is an annotation; an actual focus-visible ring, keyboard activation and focus order remain separate host/primitive evidence. This frame is not counted as executed focus coverage.','meta');
    if (['STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED'].includes(state.id)) await text(note,'Inherited Quick Access stream instance carries accepted D-057 notice copy. Other stream host instances and their preserved context remain separate; selection alone never applies.','meta');
    annotations.push(note.id);
  }
}
const boundsFindings=[];
for (const {node:frame} of frames) for (const node of frame.findAll(n => n.type==='TEXT'||n.type==='INSTANCE')) {
  if (![node.width,node.height].every(v => Number.isFinite(v)&&v>0)) boundsFindings.push({id:node.id,issue:'invalid bounds'});
  const parent=node.parent;
  if (parent && 'width' in parent && node.x+node.width>parent.width+1) boundsFindings.push({id:node.id,issue:'horizontal overflow',parentId:parent.id});
}
await frames.find(f => f.state.id==='STATE-PENDING'&&f.surface.id==='light').node.screenshot();
await frames.find(f => f.state.id==='STATE-PERMISSION-DENIED'&&f.surface.id==='dark').node.screenshot();
return {createdNodeIds:[root.id,...root.findAll(()=>true).map(n=>n.id)],mutatedNodeIds:[page.id],createdComponentIds:[],createdVariableIds:[],createdStyleIds:[],rootId:root.id,
  frames:frames.map(f=>({id:f.node.id,name:f.node.name,state:f.state.id,surface:f.surface.id,width:f.node.width,height:f.node.height})),annotationIds:annotations,boundsFindings,
  B01Complete:false,coveredScope:'48 shared narrow recovery grammar specimens only',limitations:input.limitations};
