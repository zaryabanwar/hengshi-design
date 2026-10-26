// PREPARED ONLY. Build inputs with b01-prepare-navigation.ps1; obtain fresh call approval.
// One existing-page B01 composition: inherited foundations, local stream variants,
// 320px/desktop references, returned IDs/bounds and two previews. No library publication.
// The four ceiling-refusal references remain held; no device capability fact is invented.
// Follow figma-use, figma-generate-library and figma-generate-design.
const input = /*B01_NAVIGATION_INPUTS*/ null;
if (!input || input.product !== 'Hengshi Design v1' || input.frames.length !== 20 || input.controls.length !== 16) {
  throw new Error('Missing reviewed preparation inputs');
}
if (figma.editorType !== 'figma' || (figma.fileKey && figma.fileKey !== input.fileKey)) {
  throw new Error('Wrong editor/file; no mutation');
}
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE' || figma.root.children.length !== 1) throw new Error('Unexpected page');
await figma.setCurrentPageAsync(page);
const rootName = 'B01 / Navigation stream states / v1';
if (page.findOne(node => node.name === rootName) || page.findOne(node => node.name === input.componentSetName)) {
  throw new Error('This composition exists or partially exists; inspect it before retrying');
}
for (const id of ['14:20','14:41','14:62','14:84','14:106','14:124']) {
  const node = await figma.getNodeByIdAsync(id);
  if (!node || node.type !== 'FRAME' || node.parent !== page || !node.name.startsWith('B01 DRAFT / ')) {
    throw new Error('Initial draft checkpoint changed');
  }
}
const actionMaster = await figma.getNodeByIdAsync('14:18');
if (!actionMaster || actionMaster.type !== 'COMPONENT' || actionMaster.parent?.type === 'COMPONENT_SET') {
  throw new Error('Expected existing action master');
}
const actionProperty = Object.keys(actionMaster.componentPropertyDefinitions).find(key => key.startsWith('Label#'));
if (!actionProperty) throw new Error('Missing existing action property');
const styles = await figma.getLocalTextStylesAsync();
const style = {};
for (const role of ['body','heading','meta']) {
  const match = styles.filter(item => item.name === 'B01 reference / ' + role);
  if (match.length !== 1) throw new Error('Missing or ambiguous existing text style');
  style[role] = match[0];
}
const currentFonts = [...Object.values(style).map(item => item.fontName),
  ...actionMaster.findAllWithCriteria({types:['TEXT']}).flatMap(node =>
    node.getStyledTextSegments(['fontName']).map(segment => segment.fontName))];
for (const font of [...new Map(currentFonts.map(item => [item.family + '/' + item.style,item])).values()]) {
  await figma.loadFontAsync(font);
}
const colours = await figma.variables.getLocalVariablesAsync('COLOR');
const palette = {};
for (const name of ['ink','paper','mist','cyan-light']) {
  const match = colours.filter(item => item.name === 'D035/palette/' + name);
  if (match.length !== 1) throw new Error('Missing or ambiguous inherited palette');
  palette[name] = match[0];
}
const collections = await figma.variables.getLocalVariableCollectionsAsync();
const collection = collections.find(item => item.id === palette.ink.variableCollectionId);
if (!collection || Object.values(palette).some(item => item.variableCollectionId !== collection.id)) {
  throw new Error('Inherited palette collection changed');
}
for (const variable of Object.values(palette)) {
  const value = variable.valuesByMode[collection.defaultModeId];
  if (!value || !['r','g','b'].every(channel => Number.isFinite(value[channel]))) {
    throw new Error('Expected direct inherited colour value');
  }
}
const floats = await figma.variables.getLocalVariablesAsync('FLOAT');
if (floats.some(item => item.name.startsWith('D035/space/'))) {
  throw new Error('Spacing foundations already exist; inspect and reuse instead of duplicating');
}
// Every guard above runs before the first mutation. A partial failed write requires inspection.
const rightEdge = Math.max(0,...page.children.map(node => node.x + node.width));
const createdVariableIds = [];
const spaces = {};
for (const [index,value] of [4,8,12,16,24,32,48,64,96].entries()) {
  const variable = figma.variables.createVariable('D035/space/' + (index + 1),collection,'FLOAT');
  variable.scopes = ['GAP']; variable.setValueForMode(collection.defaultModeId,value);
  variable.setVariableCodeSyntax('WEB','var(--hd-space-' + (index + 1) + ')');
  spaces[value] = variable; createdVariableIds.push(variable.id);
}
const paint = name => {
  const value = palette[name].valuesByMode[collection.defaultModeId];
  return figma.variables.setBoundVariableForPaint(
    {type:'SOLID',color:{r:value.r,g:value.g,b:value.b}},'color',palette[name]);
};
const roots = [];
const trackRoot = node => {page.appendChild(node); roots.push(node); return node;};
const stack = (parent,name,width,padding=24,background='paper') => {
  const node = figma.createAutoLayout('VERTICAL'); node.name = name;
  node.resize(width,100); node.primaryAxisSizingMode = 'AUTO'; node.counterAxisSizingMode = 'FIXED';
  node.clipsContent = false; node.fills = background ? [paint(background)] : [];
  for (const field of ['paddingTop','paddingRight','paddingBottom','paddingLeft']) {
    node[field] = padding; node.setBoundVariable(field,spaces[padding]);
  }
  node.itemSpacing = 16; node.setBoundVariable('itemSpacing',spaces[16]);
  if (parent) parent.appendChild(node); else trackRoot(node);
  return node;
};
const text = async (parent,characters,role='body',link=false) => {
  const node = figma.createText(); node.fontName = style[role].fontName;
  await node.setTextStyleIdAsync(style[role].id); node.characters = characters;
  parent.appendChild(node); node.resize(Math.max(1,parent.width-parent.paddingLeft-parent.paddingRight),24);
  node.textAutoResize = 'HEIGHT'; node.layoutSizingHorizontal = 'FILL'; node.layoutSizingVertical = 'HUG';
  node.fills = [paint('ink')]; if (link) node.textDecoration = 'UNDERLINE';
  return node;
};
const action = (parent,label) => {
  const instance = actionMaster.createInstance(); parent.appendChild(instance);
  instance.setProperties({[actionProperty]:label}); return instance;
};
const labelFor = id => input.labels.find(item => item.id === id).label;
const cards = [];
const byKey = new Map();
for (const record of input.controls) {
  const component = figma.createComponent();
  component.name = 'State=' + record.state_id.replace('STATE-','') + ', Stream=' + record.stream_id.replace('S-','');
  component.description = 'PRIM-001 delivery-stream control reference. Native HTML radios/fieldset and Apply semantics are implementation targets; this editable Figma component is not an executed control or accessibility proof.';
  component.layoutMode = 'VERTICAL'; component.resize(272,100);
  component.primaryAxisSizingMode = 'AUTO'; component.counterAxisSizingMode = 'FIXED';
  component.clipsContent = false; component.fills = [paint('mist')];
  component.paddingTop = component.paddingBottom = component.paddingLeft = component.paddingRight = 16;
  for (const field of ['paddingTop','paddingRight','paddingBottom','paddingLeft']) component.setBoundVariable(field,spaces[16]);
  component.itemSpacing = 16; component.setBoundVariable('itemSpacing',spaces[16]);
  trackRoot(component); cards.push(component);
  const active = labelFor(record.stream_id);
  const selected = labelFor(record.selected_stream_id);
  await text(component,input.copy.legend.replace('{active_label}',active));
  for (const option of input.labels) {
    const row = stack(component,'Native-radio appearance reference / ' + option.id,240,4,null);
    row.minHeight = 44; row.layoutSizingHorizontal = 'FILL';
    await text(row,(option.id === record.selected_stream_id ? '● ' : '○ ') + option.label);
  }
  await text(component,input.copy.peer_explanation);
  await text(component,input.copy.advisement);
  action(component,input.copy.apply);
  // Copy is extracted from the accepted D-057 table, not paraphrased from implementation.
  if (record.state_id !== 'STATE-OPEN') {
    const message = input.copy[record.state_id]
      .replaceAll('{active_label}',active).replaceAll('{selected_label}',selected)
      .replaceAll('{destination}','Services');
    const status = stack(component,'PRIM-057 / polite persistent page status reference',240,4,null);
    status.layoutSizingHorizontal = 'FILL'; await text(status,message);
  }
  await text(component,input.copy.privacy,'body',true);
  byKey.set(record.state_id + '/' + record.stream_id,component);
}
const componentSet = figma.combineAsVariants(cards,page);
componentSet.name = input.componentSetName;
componentSet.description = 'B01 local PRIM-001 stream-control references: four streams and four selected states. Ceiling-refusal facts remain unresolved. D-057 wording is inherited. No published library, application behavior or conformance is asserted.';
componentSet.x = rightEdge + 400; componentSet.y = 400;
for (const [index,component] of cards.entries()) {
  component.x = 24 + (index % 4)*320;
  component.y = 24 + Math.floor(index/4)*2400;
}
componentSet.resize(1328,Math.max(...cards.map(node => node.y+node.height))+24);
const composition = stack(null,rootName,1800,24,'mist');
composition.x = componentSet.x + componentSet.width + 400; composition.y = 400;
const frames = [];
const annotations = [];
for (const record of input.frames) {
  const frame = stack(composition,record.name,record.width,24);
  frame.layoutSizingHorizontal = 'FIXED';
  await text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta');
  await text(frame,'Hengshi Design','heading');
  await text(frame,'Skip to main content','body',true);
  if (record.width === 320) {
    action(frame,'Close menu');
    const nav = stack(frame,'PRIM-002 / expanded narrow navigation',272,4,null);
    for (const item of ['Services — current','Evidence','About','Contact']) await text(nav,item,'body',true);
  } else {
    await text(frame,'Services — current     Evidence     About     Contact','body',true);
  }
  action(frame,'Book a conversation');
  await text(frame,'Home / Services','body',true);
  await text(frame,'Choose how you explore','heading');
  const master = byKey.get(record.state_id + '/' + record.stream_id);
  const instance = master.createInstance(); frame.appendChild(instance);
  instance.resize(record.width === 320 ? 272 : 640,Math.max(1,instance.height));
  await text(frame,'Privacy and storage   ·   Credits','body',true);
  frames.push(frame);
  const annotation = stack(composition,'ANNOTATION / ' + record.name,Math.min(record.width,640),16);
  await text(annotation,'REFERENCE EVIDENCE — ' + record.state_id + ' / ' + record.stream_id,'meta');
  await text(annotation,input.fixture,'meta');
  await text(annotation,record.state_id === 'STATE-OPEN'
    ? 'Pending radio selection differs from the in-force legend. Selecting changes only checked state; application waits for explicit Apply or same-form Enter submission.'
    : 'State fixture represents an authoritative outcome supplied by the system. Neither a screenshot nor these static symbols establish storage success, live announcements or actual application behavior.');
  await text(annotation,'Keyboard target: skip link; navigation; Book; breadcrumb; stream group; Apply; Privacy and storage; Credits. Radio arrows select only; Tab leaves the group; Apply remains separate. Advisement precedes Apply and must be associated with both fieldset and Apply.','meta');
  await text(annotation,'Native radio appearance is illustrative; production retains native inputs. Interaction, focus-return, 400% zoom, forced-colors, screen-reader, unavailable-assets and complete B01 coverage remain.','meta');
  annotations.push(annotation);
}
const overflow = [];
for (const frame of frames) {
  for (const child of frame.findAll(node => node.type === 'TEXT' || node.type === 'INSTANCE')) {
    if (child.width <= 0 || child.height <= 0 || !Number.isFinite(child.width) || !Number.isFinite(child.height)) {
      overflow.push({id:child.id,issue:'invalid bounds'});
    }
    const parent = child.parent;
    if (parent && 'width' in parent && child.x + child.width > parent.width + 1) {
      overflow.push({id:child.id,issue:'horizontal overflow',parentId:parent.id});
    }
  }
}
const createdNodeIds = [...new Set([composition,componentSet].flatMap(root =>
  [root.id,...root.findAll(() => true).map(node => node.id)]))];
// Return IDs and bounds even if visual evidence identifies a defect; never claim completion.
await frames.find(node => node.width === 320).screenshot();
await frames.find(node => node.width === 1440).screenshot();
return {createdNodeIds,mutatedNodeIds:[page.id],createdVariableIds,mutatedCollectionIds:[collection.id],
  componentSetId:componentSet.id,componentIds:cards.map(node => node.id),
  frames:frames.map(node => ({id:node.id,name:node.name,width:node.width,height:node.height})),
  annotationIds:annotations.map(node => node.id),overflow,
  B01Complete:false,coveredScope:'16 narrow navigation stream/state references plus four desktop open references',
  held:input.held,remaining:'Other contracted navigation states and profiles; search/recovery templates; full PRIM matrix; interaction evidence; exports; independent review; restore/EXIT and founder acceptance'};
