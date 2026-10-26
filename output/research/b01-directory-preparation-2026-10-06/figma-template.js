// PREPARED ONLY. One individually approved B01 call is required before execution.
// Reuse existing foundations and stream instances; never rerun after uncertain writes.
const input = /*DIRECTORY_INPUT*/ null;
if (!input || input.product !== 'Hengshi Design v1' || input.frames.length !== 52) {
  throw Error('Missing exact prepared directory scope');
}
if (figma.editorType !== 'figma' || (figma.fileKey && figma.fileKey !== input.fileKey)) {
  throw Error('Wrong editor or file');
}
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE' || figma.root.children.length !== 1) throw Error('Changed page context');
await figma.setCurrentPageAsync(page);
const rootName = 'B01 / Directory search states / v1';
if (page.findOne(n => n.name === rootName) || page.findOne(n => n.name === input.sourcesName)) {
  throw Error('Existing or partial directory composition; inspect instead of duplicating');
}
const navigationRoot = await figma.getNodeByIdAsync('21:290');
const streamSet = await figma.getNodeByIdAsync('21:289');
if (!navigationRoot || navigationRoot.type !== 'FRAME' || navigationRoot.parent !== page ||
    !streamSet || streamSet.type !== 'COMPONENT_SET' || streamSet.children.length !== 16) {
  throw Error('The completed navigation checkpoint has changed');
}
const masters = new Map();
for (const record of input.streamMasters) {
  const node = await figma.getNodeByIdAsync(record.id);
  if (!node || node.type !== 'COMPONENT' || node.parent !== streamSet || node.name !== record.name) {
    throw Error('A required stream master has changed');
  }
  masters.set(record.state_id + '/' + record.stream_id, node);
}
const actionMaster = await figma.getNodeByIdAsync('14:18');
if (!actionMaster || actionMaster.type !== 'COMPONENT') throw Error('Missing inherited action');
const actionLabel = Object.keys(actionMaster.componentPropertyDefinitions).find(k => k.startsWith('Label#'));
if (!actionLabel) throw Error('Changed action label property');
const style = {};
const localStyles = await figma.getLocalTextStylesAsync();
for (const role of ['body','heading','meta']) {
  const matches = localStyles.filter(s => s.name === 'B01 reference / ' + role);
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited text style');
  style[role] = matches[0];
}
// Existing current fonts must be loaded before editing or instancing their text.
const fonts = [...Object.values(style).map(s => s.fontName),
  ...[actionMaster,...masters.values()].flatMap(master =>
    master.findAllWithCriteria({types:['TEXT']}).flatMap(node =>
      node.getStyledTextSegments(['fontName']).map(segment => segment.fontName)))];
for (const font of new Map(fonts.map(f => [f.family + '/' + f.style,f])).values()) await figma.loadFontAsync(font);
const colour = {}, space = {};
const colours = await figma.variables.getLocalVariablesAsync('COLOR');
const floats = await figma.variables.getLocalVariablesAsync('FLOAT');
for (const name of ['ink','paper','mist','cyan-light']) {
  const matches = colours.filter(v => v.name === 'D035/palette/' + name);
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited palette');
  colour[name] = matches[0];
}
for (const [index,value] of [4,8,12,16,24,32,48,64,96].entries()) {
  const matches = floats.filter(v => v.name === 'D035/space/' + (index + 1));
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited spacing');
  space[value] = matches[0];
}
const collection = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.id === colour.ink.variableCollectionId);
if (!collection || Object.values(colour).some(v => v.variableCollectionId !== collection.id)) throw Error('Changed palette collection');
for (const v of Object.values(colour)) {
  const value = v.valuesByMode[collection.defaultModeId];
  if (!value || !['r','g','b'].every(k => Number.isFinite(value[k]))) throw Error('Changed direct palette value');
}
for (const [number,v] of Object.entries(space)) {
  if (v.valuesByMode[collection.defaultModeId] !== Number(number)) throw Error('Changed spacing value');
}
// All guards run before this first construction. Do not change existing drafts or masters.
const rightEdge = Math.max(0,...page.children.map(n => n.x + n.width));
const paint = name => {
  const value = colour[name].valuesByMode[collection.defaultModeId];
  return figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:value.r,g:value.g,b:value.b}},'color',colour[name]);
};
const roots = [];
function configure(node,width,padding=16,background='paper') {
  node.resize(width,100); node.primaryAxisSizingMode = 'AUTO'; node.counterAxisSizingMode = 'FIXED';
  node.clipsContent = false; node.fills = background ? [paint(background)] : [];
  for (const key of ['paddingTop','paddingRight','paddingBottom','paddingLeft']) {
    node[key] = padding; node.setBoundVariable(key,space[padding]);
  }
  node.itemSpacing = 16; node.setBoundVariable('itemSpacing',space[16]);
  return node;
}
function stack(parent,name,width,padding=16,background='paper') {
  const node = configure(figma.createAutoLayout('VERTICAL'),width,padding,background); node.name = name;
  if (parent) parent.appendChild(node); else {page.appendChild(node); roots.push(node);}
  return node;
}
async function text(parent,characters,role='body',link=false) {
  const node = figma.createText(); node.fontName = style[role].fontName;
  await node.setTextStyleIdAsync(style[role].id); node.characters = characters; parent.appendChild(node);
  node.resize(Math.max(1,parent.width-parent.paddingLeft-parent.paddingRight),24);
  node.textAutoResize = 'HEIGHT'; node.layoutSizingHorizontal = 'FILL'; node.layoutSizingVertical = 'HUG';
  node.fills = [paint('ink')]; if (link) node.textDecoration = 'UNDERLINE';
  return node;
}
function action(parent,label) {
  const node = actionMaster.createInstance(); parent.appendChild(node); node.setProperties({[actionLabel]:label});
  return node;
}
function component(parent,name,description) {
  const node = figma.createComponent(); node.layoutMode = 'VERTICAL'; configure(node,272,16,'mist');
  node.name = name; node.description = description; parent.appendChild(node); return node;
}
const source = stack(null,input.sourcesName,520,24,'mist'); source.x = rightEdge + 400; source.y = 400;
await text(source,'B01 FILE-LOCAL DIRECTORY SOURCES — v1','meta');
const inputMaster = component(source,'PRIM-019 / Directory search input / base',
  'Editable reference for a native labelled search input, not an implemented text field. Value is an explicit synthetic fixture. Native HTML label/name, autocomplete, input, focus and clearing remain implementation obligations.');
const labelProperty = inputMaster.addComponentProperty('Label','TEXT','Search the directory');
const valueProperty = inputMaster.addComponentProperty('Value','TEXT','Enter a search term');
const inputLabel = await text(inputMaster,'Search the directory');
inputLabel.componentPropertyReferences = {characters:labelProperty};
const inputValue = await text(inputMaster,'Enter a search term');
inputValue.componentPropertyReferences = {characters:valueProperty};
inputMaster.minHeight = 88;
const resultMaster = component(source,'PRIM-005 / Directory canonical result / base',
  'Editable result-link reference. Label and destination come from the canonical route inventory; this synthetic fixture neither activates a route nor claims published work or search ranking.');
const resultLabelProperty = resultMaster.addComponentProperty('Label','TEXT',input.routes[0].label);
const resultPathProperty = resultMaster.addComponentProperty('Destination','TEXT',input.routes[0].path);
const resultLabel = await text(resultMaster,input.routes[0].label,'body',true);
resultLabel.componentPropertyReferences = {characters:resultLabelProperty};
const resultPath = await text(resultMaster,input.routes[0].path,'meta');
resultPath.componentPropertyReferences = {characters:resultPathProperty};
await text(resultMaster,'Service department · semantic page','meta'); resultMaster.minHeight = 88;
const composition = stack(null,rootName,1800,24,'mist');
composition.x = source.x + source.width + 400; composition.y = 400;
const frames = [], annotationIds = [];
for (const record of input.frames) {
  const frame = stack(composition,record.name,record.width,24,'paper'); frame.layoutSizingHorizontal = 'FIXED';
  await text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta');
  await text(frame,'Hengshi Design','heading');
  await text(frame,'Skip to main content','body',true);
  await text(frame,'Services — current / Directory open','body',true);
  action(frame,'Book a conversation');
  await text(frame,'Directory','heading');
  await text(frame,'Browse departments or search published information.');
  action(frame,'Close directory');
  const field = inputMaster.createInstance(); frame.appendChild(field);
  field.resize(record.width - 48,Math.max(1,field.height));
  field.setProperties({[labelProperty]:'Search the directory',[valueProperty]:record.query || 'Enter a search term'});
  action(frame,'Search');
  if (record.query) action(frame,'Clear search');
  const state = input.states.find(s => s.id === record.state_id);
  if (!state) throw Error('Missing prepared state');
  await text(frame,state.heading,'heading'); await text(frame,state.message);
  if (state.results) {
    for (const route of input.routes.slice(0,state.results)) {
      const result = resultMaster.createInstance(); frame.appendChild(result);
      result.resize(record.width-48,Math.max(1,result.height));
      result.setProperties({[resultLabelProperty]:route.label,[resultPathProperty]:route.path});
    }
  }
  if (state.browse) {
    const browse = stack(frame,'Static semantic directory / no live index required',record.width-48,16,'mist');
    browse.layoutSizingHorizontal = 'FILL'; await text(browse,'Browse service departments');
    for (const route of input.routes) await text(browse,route.label,'body',true);
  }
  if (state.retry) action(frame,'Try search again');
  const streamState = ['STATE-PREFERENCE-READ-FAILED','STATE-PREFERENCE-WRITE-FAILED','STATE-STREAM-CHANGED'].includes(record.state_id)
    ? record.state_id : 'STATE-OPEN';
  const streamMaster = masters.get(streamState+'/'+record.stream_id);
  const streamInstance = streamMaster.createInstance(); frame.appendChild(streamInstance);
  streamInstance.resize(record.width===320 ? 272 : 640,Math.max(1,streamInstance.height));
  await text(frame,'Privacy and storage / Credits','body',true);
  frames.push(frame);
  const note = stack(composition,'ANNOTATION / '+record.name,Math.min(record.width,640),16,'paper');
  await text(note,record.state_id+' / '+record.stream_id,'meta');
  await text(note,'Synthetic directory fixture in the Services shell. Route labels/paths are planned canonical identities; no route publication, real result ranking or live index is claimed.','meta');
  await text(note,'Proposed nonmodal disclosure: keyboard activation opens Directory and focuses its heading; Close or Escape returns focus to the invoker. No focus trap. Empty fields show placeholder appearance, not a submitted value. Reading order: heading, Close, labelled search field, Search, Clear when populated, status/results or browse links, stream group, Apply, privacy.','meta');
  await text(note,'Search results are canonical semantic links. Query stays in transient form state, never an invented URL parameter, analytics/log event or saved preference. Native label/name, result link targets, polite status, pointer-up cancellation and keyboard/screen-reader operation require separate implementation evidence.','meta');
  await text(note,'Stream control inherits D-057 wording/current/pending distinction. Choice alone never applies; the separate Apply action preserves Services, the open directory, scroll and permitted query context. A state label is not storage or announcement proof.','meta');
  await text(note,'This light MODE-KEYBOARD reference is one profile intersection. Landscape/400% content stress, remaining modes and primitives, interaction/prototype, independent reviews, native exports/restore/EXIT and pilot acceptance remain. Ceiling-refusal fixtures are separately held.','meta');
  annotationIds.push(note.id);
}
const boundsFindings = [];
for (const frame of frames) {
  for (const node of frame.findAll(n => n.type==='TEXT'||n.type==='INSTANCE')) {
    if (![node.width,node.height].every(v=>Number.isFinite(v)&&v>0)) boundsFindings.push({id:node.id,issue:'invalid bounds'});
    const parent = node.parent;
    if (parent && 'width' in parent && node.x+node.width>parent.width+1) boundsFindings.push({id:node.id,issue:'horizontal overflow',parentId:parent.id});
  }
}
const createdNodeIds = [...new Set(roots.flatMap(root=>[root.id,...root.findAll(()=>true).map(n=>n.id)]))];
await frames.find((node,index)=>input.frames[index].state_id==='STATE-RESULTS' && node.width===320).screenshot();
await frames.find(node=>node.width===1440).screenshot();
return {createdNodeIds,mutatedNodeIds:[page.id],createdVariableIds:[],createdStyleIds:[],
  sourceId:source.id,compositionId:composition.id,componentIds:[inputMaster.id,resultMaster.id],
  frames:frames.map(n=>({id:n.id,name:n.name,width:n.width,height:n.height})),annotationIds,boundsFindings,
  B01Complete:false,coveredScope:'48 narrow directory state/stream references and four wide open references',
  limitations:input.limitations};
