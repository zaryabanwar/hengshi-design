// PREPARED ONLY. One individually approved B01 call is required before execution.
// Reuse existing foundations and stream instances; never rerun after uncertain writes.
const input = {"product":"Hengshi Design v1","fileKey":"GOmLP6Cv96l768ueSrZ5Dg","sourcesName":"B01 / Directory reusable sources / v1","streamMasters":[{"state_id":"STATE-OPEN","stream_id":"S-HIGH","selected_stream_id":"S-MEDIUM","id":"21:25","name":"State=OPEN, Stream=HIGH"},{"state_id":"STATE-OPEN","stream_id":"S-LOW","selected_stream_id":"S-SEMANTIC","id":"21:40","name":"State=OPEN, Stream=LOW"},{"state_id":"STATE-OPEN","stream_id":"S-MEDIUM","selected_stream_id":"S-LOW","id":"21:55","name":"State=OPEN, Stream=MEDIUM"},{"state_id":"STATE-OPEN","stream_id":"S-SEMANTIC","selected_stream_id":"S-HIGH","id":"21:70","name":"State=OPEN, Stream=SEMANTIC"},{"state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-HIGH","selected_stream_id":"S-HIGH","id":"21:85","name":"State=PREFERENCE-READ-FAILED, Stream=HIGH"},{"state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-LOW","selected_stream_id":"S-LOW","id":"21:102","name":"State=PREFERENCE-READ-FAILED, Stream=LOW"},{"state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-MEDIUM","selected_stream_id":"S-MEDIUM","id":"21:119","name":"State=PREFERENCE-READ-FAILED, Stream=MEDIUM"},{"state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-SEMANTIC","selected_stream_id":"S-SEMANTIC","id":"21:136","name":"State=PREFERENCE-READ-FAILED, Stream=SEMANTIC"},{"state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-HIGH","selected_stream_id":"S-HIGH","id":"21:153","name":"State=PREFERENCE-WRITE-FAILED, Stream=HIGH"},{"state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-LOW","selected_stream_id":"S-LOW","id":"21:170","name":"State=PREFERENCE-WRITE-FAILED, Stream=LOW"},{"state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-MEDIUM","selected_stream_id":"S-MEDIUM","id":"21:187","name":"State=PREFERENCE-WRITE-FAILED, Stream=MEDIUM"},{"state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-SEMANTIC","selected_stream_id":"S-SEMANTIC","id":"21:204","name":"State=PREFERENCE-WRITE-FAILED, Stream=SEMANTIC"},{"state_id":"STATE-STREAM-CHANGED","stream_id":"S-HIGH","selected_stream_id":"S-HIGH","id":"21:221","name":"State=STREAM-CHANGED, Stream=HIGH"},{"state_id":"STATE-STREAM-CHANGED","stream_id":"S-LOW","selected_stream_id":"S-LOW","id":"21:238","name":"State=STREAM-CHANGED, Stream=LOW"},{"state_id":"STATE-STREAM-CHANGED","stream_id":"S-MEDIUM","selected_stream_id":"S-MEDIUM","id":"21:255","name":"State=STREAM-CHANGED, Stream=MEDIUM"},{"state_id":"STATE-STREAM-CHANGED","stream_id":"S-SEMANTIC","selected_stream_id":"S-SEMANTIC","id":"21:272","name":"State=STREAM-CHANGED, Stream=SEMANTIC"}],"routes":[{"id":"ROUTE-WING-STRATEGY","label":"Strategy & Transformation","path":"/services/strategy-transformation"},{"id":"ROUTE-WING-DIGITAL","label":"Digital Products & Growth","path":"/services/digital-products-growth"},{"id":"ROUTE-WING-AI-DATA","label":"AI, Data & Automation","path":"/services/ai-data-automation"},{"id":"ROUTE-WING-IMMERSIVE","label":"Immersive & Creative","path":"/services/immersive-creative"},{"id":"ROUTE-WING-CLOUD-TRUST","label":"Cloud, Reliability & Trust","path":"/services/cloud-reliability-trust"}],"states":[{"id":"STATE-OPEN","heading":"Browse departments","message":"Choose a semantic department page.","query":"","results":0,"browse":true},{"id":"STATE-EMPTY-QUERY","heading":"Browse departments","message":"Enter a search term, or choose a department below.","query":"","results":0,"browse":true},{"id":"STATE-RESULTS","heading":"Search results","message":"Five synthetic results for this reference.","query":"design","results":5,"browse":false},{"id":"STATE-NO-RESULTS","heading":"No matching results","message":"Try another search term or browse departments.","query":"unmatched example","results":0,"browse":true},{"id":"STATE-LOADING","heading":"Searching the directory","message":"You can continue using the department links while search is pending.","query":"design","results":0,"browse":true},{"id":"STATE-DERIVED-INDEX-UNAVAILABLE","heading":"Search is unavailable","message":"The semantic department directory is available. Search has not returned a result.","query":"design","results":0,"browse":true,"retry":true},{"id":"STATE-OFFLINE","heading":"Connection unavailable","message":"This fixture makes no claim that a fresh result or department page is available offline. Keep the current view and retry when connected.","query":"design","results":0,"browse":false,"retry":true},{"id":"STATE-ERROR","heading":"Search did not complete","message":"No new result was confirmed. The department links remain available in this connected fixture.","query":"design","results":0,"browse":true,"retry":true},{"id":"STATE-STALE","heading":"Earlier results","message":"These reference results belong to an earlier completed query and are not current results for the edited term.","query":"updated example","results":2,"browse":true,"retry":true},{"id":"STATE-PREFERENCE-READ-FAILED","heading":"Browse departments","message":"Stored presentation choice could not be read; use the persistent selection control below.","query":"","results":0,"browse":true},{"id":"STATE-PREFERENCE-WRITE-FAILED","heading":"Browse departments","message":"The presentation is applied for this session; the accepted storage status is shown below.","query":"","results":0,"browse":true},{"id":"STATE-STREAM-CHANGED","heading":"Browse departments","message":"The presentation changed; the Services location and open directory remain.","query":"","results":0,"browse":true}],"frames":[{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-OPEN","stream_id":"S-HIGH","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-OPEN","stream_id":"S-MEDIUM","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-OPEN","stream_id":"S-LOW","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-OPEN","stream_id":"S-SEMANTIC","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_EMPTY_QUERY_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-EMPTY-QUERY","stream_id":"S-HIGH","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_EMPTY_QUERY_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-EMPTY-QUERY","stream_id":"S-MEDIUM","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_EMPTY_QUERY_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-EMPTY-QUERY","stream_id":"S-LOW","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_EMPTY_QUERY_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-EMPTY-QUERY","stream_id":"S-SEMANTIC","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_RESULTS_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-RESULTS","stream_id":"S-HIGH","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_RESULTS_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-RESULTS","stream_id":"S-MEDIUM","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_RESULTS_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-RESULTS","stream_id":"S-LOW","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_RESULTS_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-RESULTS","stream_id":"S-SEMANTIC","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_NO_RESULTS_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-NO-RESULTS","stream_id":"S-HIGH","width":320,"query":"unmatched example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_NO_RESULTS_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-NO-RESULTS","stream_id":"S-MEDIUM","width":320,"query":"unmatched example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_NO_RESULTS_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-NO-RESULTS","stream_id":"S-LOW","width":320,"query":"unmatched example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_NO_RESULTS_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-NO-RESULTS","stream_id":"S-SEMANTIC","width":320,"query":"unmatched example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_LOADING_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-LOADING","stream_id":"S-HIGH","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_LOADING_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-LOADING","stream_id":"S-MEDIUM","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_LOADING_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-LOADING","stream_id":"S-LOW","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_LOADING_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-LOADING","stream_id":"S-SEMANTIC","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_DERIVED_INDEX_UNAVAILABLE_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-DERIVED-INDEX-UNAVAILABLE","stream_id":"S-HIGH","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_DERIVED_INDEX_UNAVAILABLE_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-DERIVED-INDEX-UNAVAILABLE","stream_id":"S-MEDIUM","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_DERIVED_INDEX_UNAVAILABLE_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-DERIVED-INDEX-UNAVAILABLE","stream_id":"S-LOW","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_DERIVED_INDEX_UNAVAILABLE_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-DERIVED-INDEX-UNAVAILABLE","stream_id":"S-SEMANTIC","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OFFLINE_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-OFFLINE","stream_id":"S-HIGH","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OFFLINE_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-OFFLINE","stream_id":"S-MEDIUM","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OFFLINE_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-OFFLINE","stream_id":"S-LOW","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OFFLINE_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-OFFLINE","stream_id":"S-SEMANTIC","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_ERROR_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-ERROR","stream_id":"S-HIGH","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_ERROR_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-ERROR","stream_id":"S-MEDIUM","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_ERROR_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-ERROR","stream_id":"S-LOW","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_ERROR_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-ERROR","stream_id":"S-SEMANTIC","width":320,"query":"design"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STALE_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-STALE","stream_id":"S-HIGH","width":320,"query":"updated example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STALE_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-STALE","stream_id":"S-MEDIUM","width":320,"query":"updated example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STALE_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-STALE","stream_id":"S-LOW","width":320,"query":"updated example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STALE_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-STALE","stream_id":"S-SEMANTIC","width":320,"query":"updated example"},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-HIGH","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-MEDIUM","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-LOW","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-PREFERENCE-READ-FAILED","stream_id":"S-SEMANTIC","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-HIGH","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-MEDIUM","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-LOW","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-SEMANTIC","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-STREAM-CHANGED","stream_id":"S-HIGH","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-STREAM-CHANGED","stream_id":"S-MEDIUM","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-STREAM-CHANGED","stream_id":"S-LOW","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-STREAM-CHANGED","stream_id":"S-SEMANTIC","width":320,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_HIGH_V01","state_id":"STATE-OPEN","stream_id":"S-HIGH","width":1440,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_MEDIUM_V01","state_id":"STATE-OPEN","stream_id":"S-MEDIUM","width":1440,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_LOW_V01","state_id":"STATE-OPEN","stream_id":"S-LOW","width":1440,"query":""},{"name":"HSD_UIR_B01_TPL_DIRECTORY_SEARCH_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_SEMANTIC_V01","state_id":"STATE-OPEN","stream_id":"S-SEMANTIC","width":1440,"query":""}],"limitations":["Prepared only; no Figma call or external write performed","Synthetic state/result fixtures and proposed nonmodal focus contract are subject to design review and founder pilot acceptance","MODE-KEYBOARD naming is a reference specification, not actual native input, keyboard or screen-reader execution","Existing D057 master copy is reused; ceiling facts, other modes/profiles/primitives, prototype, independent reviews, exports/restore/EXIT and full pilot acceptance remain","All existing Figma content preserved; no new page, library publication, website font, route activation or application implementation"]};
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
const groupedBounds = new Map();
for (const finding of boundsFindings) {
  const key = JSON.stringify([finding.issue,finding.parentId??null]);
  if (!groupedBounds.has(key)) groupedBounds.set(key,[]);
  groupedBounds.get(key).push(finding.id);
}
const report = {
  createdNodeIds:packIds(createdNodeIds),mutatedNodeIds:[page.id],
  createdVariableIds:[],createdStyleIds:[],sourceId:source.id,compositionId:composition.id,
  componentIds:[inputMaster.id,resultMaster.id],
  frameFields:['id','inputIndex','width','height'],
  frames:frames.map((n,i)=>[n.id,i,n.width,n.height]),annotationIds:packIds(annotationIds),
  boundsFindingCount:boundsFindings.length,
  boundsFindings:[...groupedBounds.entries()].map(([key,ids])=>({context:JSON.parse(key),nodeIds:packIds(ids)})),
  B01Complete:false,coveredScope:'48 narrow directory state/stream references and four wide open references',
  limitations:input.limitations.filter(s=>!s.startsWith('Prepared only;')),
  reportOnlyChange:true
};
// Exact UTF-8 byte count without relying on an unavailable host TextEncoder.
const reportBytes = encodeURIComponent(JSON.stringify(report)).match(/%[0-9A-F]{2}|[^%]/g).length;
if (reportBytes>19000) throw Error('Compact report '+reportBytes+' bytes exceeds local 19000-byte guard; do not commit canvas edits');
await frames.find((node,index)=>input.frames[index].state_id==='STATE-RESULTS' && node.width===320).screenshot();
await frames.find(node=>node.width===1440).screenshot();
return report;
