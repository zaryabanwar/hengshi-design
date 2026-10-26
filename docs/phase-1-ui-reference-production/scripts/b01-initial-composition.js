// PREPARED, NOT EXECUTED. Proposed Figma-only Inter fallback requires founder approval.
// One productive call: fonts/empty-file guards + tokens/components + six draft views + evidence.
// Not full B01 coverage/exit, a production screen, public copy or application implementation.
// Requires native HSD_UIR_B01_PRE archive aea663332bc62ba412e6c02477f7faa63f1f7f176bd11a16733d9b06d86cf272.
// Follow figma-use, figma-generate-library, figma-generate-design; no external library imports.
const expectedKey = 'GOmLP6Cv96l768ueSrZ5Dg';
if (figma.editorType !== 'figma') throw new Error('Expected approved Design editor');
if (figma.fileKey && figma.fileKey !== expectedKey) throw new Error('Wrong file identity');
// Native title/URL verified in paired PRE evidence; this host returned generic Document.
if (!['Document', 'Hengshi Design v1 — UI References'].includes(figma.root.name)) {
  throw new Error('Unexpected document identity: stop before construction');
}
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE' || figma.root.children.length !== 1) throw new Error('Unexpected page');
await figma.setCurrentPageAsync(page);
if (page.children.length || (await figma.getLocalPaintStylesAsync()).length ||
    (await figma.getLocalTextStylesAsync()).length ||
    (await figma.variables.getLocalVariableCollectionsAsync()).length) {
  throw new Error('Not the reviewed empty baseline: inspect changed content, do not overwrite');
}
const available = await figma.listAvailableFontsAsync();
const fonts = {body:{family:'Inter',style:'Regular'}, heading:{family:'Inter',style:'Bold'},
               meta:{family:'Cascadia Mono',style:'Regular'}};
for (const font of Object.values(fonts)) {
  if (!available.some(item => item.fontName.family === font.family && item.fontName.style === font.style)) {
    throw new Error('Proposed exact font/style unavailable: no silent substitution');
  }
  await figma.loadFontAsync(font);
}
const rgb = hex => ({r:parseInt(hex.slice(1,3),16)/255,g:parseInt(hex.slice(3,5),16)/255,b:parseInt(hex.slice(5,7),16)/255});
const createdStyleIds = [], createdVariableIds = [], createdCollectionIds = [], topLevels = [];
const collection = figma.variables.createVariableCollection('B01 / D035 reference colours');
createdCollectionIds.push(collection.id);
const vars = {};
// Exact D035 inherited palette. One default mode; full light/dark state matrix still required.
for (const [name,hex] of [['ink','#0B0F14'],['slate','#2A3542'],['stone','#D8D3C8'],
                         ['paper','#FAF9F6'],['mist','#F3F1EA'],['white','#FFFFFF'],
                         ['cyan-light','#006D82'],['cyan-dark','#00D4FF']]) {
  const variable = figma.variables.createVariable('D035/palette/' + name, collection, 'COLOR');
  variable.scopes = ['FRAME_FILL','SHAPE_FILL','TEXT_FILL','STROKE_COLOR'];
  variable.setValueForMode(collection.defaultModeId,rgb(hex));
  createdVariableIds.push(variable.id); vars[name] = {variable,hex};
}
const fill = name => figma.variables.setBoundVariableForPaint(
  {type:'SOLID',color:rgb(vars[name].hex)},'color',vars[name].variable);
const styles = {};
for (const [role,size,height] of [['body',16,24],['heading',32,40],['meta',12,18]]) {
  const style = figma.createTextStyle();
  style.name = 'B01 reference / ' + role; style.fontName = fonts[role];
  style.fontSize = size; style.lineHeight = {unit:'PIXELS',value:height};
  style.description = role === 'meta' ? 'D035 documented system monospace reference.' :
    'Founder-selected Figma-only fallback. No website font or redistributed font asset.';
  createdStyleIds.push(style.id); styles[role] = style;
}
const layout = (parent,name,width,background='paper') => {
  const node = figma.createAutoLayout('VERTICAL'); node.name = name;
  node.fills = background ? [fill(background)] : []; node.clipsContent = false;
  node.itemSpacing = 16; node.paddingTop = node.paddingBottom = 24;
  node.paddingLeft = node.paddingRight = 24; node.resize(width,100);
  node.primaryAxisSizingMode = 'AUTO'; node.counterAxisSizingMode = 'FIXED';
  if (parent) parent.appendChild(node); else {page.appendChild(node);topLevels.push(node);}
  return node;
};
const text = async (parent,content,role='body',colour='ink') => {
  const node = figma.createText(); node.fontName = fonts[role];
  await node.setTextStyleIdAsync(styles[role].id); node.characters = content;
  node.textAutoResize = 'HEIGHT'; node.resize(Math.max(1,parent.width-48),20);
  node.fills = [fill(colour)]; parent.appendChild(node); return node;
};
const source = layout(null,'B01 CONSTRUCTION / file-local PRIM sources',520,'mist');
source.x = 400; source.y = 400;
await text(source,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta');
await text(source,'Hengshi Design v1','heading');
await text(source,'Initial composition only. Full variants, stream/mode/state coverage and independent reviews remain.');
const button = figma.createComponent(); button.name = 'PRIM-015 / General action button / base';
button.description = 'Draft file-local action. Label is instance text; other states and interactive evidence remain required.';
button.layoutMode = 'VERTICAL'; button.resize(220,56); button.primaryAxisSizingMode = 'AUTO';
button.counterAxisSizingMode = 'FIXED'; button.paddingTop = button.paddingBottom = 16;
button.paddingLeft = button.paddingRight = 24; button.fills = [fill('cyan-light')];
source.appendChild(button);
const label = await text(button,'Book a conversation','body','white');
label.componentPropertyReferences = {characters:button.addComponentProperty('Label','TEXT','Book a conversation')};
const action = (parent,caption) => {
  const instance = button.createInstance(); parent.appendChild(instance);
  const property = Object.keys(button.componentPropertyDefinitions).find(key=>key.startsWith('Label#'));
  if (!property) throw new Error('Missing action label property');
  instance.setProperties({[property]:caption}); return instance;
};
const controls = async parent => {
  const control = layout(parent,'PRIM-001 / delivery stream control / reference',parent.width-48,'mist');
  await text(control,'Delivery stream — in force: Quick Access');
  for (const label of ['Detailed 3D','Balanced 3D','Simplified 3D','Quick Access']) {
    await text(control,(label === 'Quick Access' ? '● ' : '○ ') + label);
  }
  await text(control,'Every option offers the same destinations and core journeys. The 3D options differ in visual detail. Quick Access presents the journey without a 3D scene.');
  await text(control,'Selecting an option does not change your experience. Apply selection re-enters the experience only when you choose a different option, keeping your current location where available. If that location has no match, you will arrive at the nearest available parent destination and be told where you are. Applying the current option makes no change.');
  action(control,'Apply selection');
  await text(control,'Visual reference only. Native fieldset/radios, names and interactions require separate evidence.','meta');
};
const frames = [];
for (const [template,width,column] of [
  ['TPL-GLOBAL-NAVIGATION',1440,0],['TPL-GLOBAL-NAVIGATION',390,1],
  ['TPL-DIRECTORY-SEARCH',1440,2],['TPL-DIRECTORY-SEARCH',390,3],
  ['TPL-SYSTEM-RECOVERY',1440,4],['TPL-SYSTEM-RECOVERY',390,5]]) {
  const frame = layout(null,'B01 DRAFT / ' + template + ' / ' + width,width);
  frame.x = 1040 + column*1560; frame.y = 400;
  await text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta');
  await text(frame,'Hengshi Design','heading');
  await text(frame,'Skip to main content','meta');
  await text(frame,width>600 ? 'Services    Evidence    About    Contact' : 'Menu   ·   collapsed navigation');
  action(frame,'Book a conversation');
  await text(frame,'Home / Services','meta');
  if (template === 'TPL-GLOBAL-NAVIGATION') {
    await text(frame,'Choose how you explore','heading');
    await controls(frame);
  } else if (template === 'TPL-DIRECTORY-SEARCH') {
    await text(frame,'Explore our capabilities','heading');
    const input = layout(frame,'PRIM-004 / search field / fixture',width-48,'mist');
    await text(input,'Search services'); await text(input,'[ Example query ]'); action(input,'Search');
    await text(frame,'Example results — synthetic fixture','meta');
    await text(frame,'Strategy & Transformation'); await text(frame,'Digital Products & Growth');
    await text(frame,'AI, Data & Automation'); await text(frame,'Immersive & Creative');
    await text(frame,'Cloud, Reliability & Trust');
    await text(frame,'Static directory remains reachable when search is unavailable.','meta');
  } else {
    await text(frame,'Continue from here','heading');
    const state = layout(frame,'PRIM-058 / unavailable / reference fixture',width-48,'mist');
    await text(state,'Example unavailable state');
    await text(state,'This is a recovery-layout fixture, not an actual error or approved legal/security message.');
    action(state,'Browse the directory'); action(state,'Contact');
    await text(frame,'Preserve current location and process truth. Never treat a timeout as a confirmed failure.','meta');
  }
  await text(frame,'Initial light-mode composition. Hover/focus/disabled, narrow disclosure, transactional variants, dark mode and complete contracted coverage remain.','meta');
  frames.push(frame);
}
const createdNodeIds = [...new Set(topLevels.flatMap(node=>[node.id,...node.findAll(()=>true).map(child=>child.id)]))];
await frames[0].screenshot();
return {createdNodeIds,mutatedNodeIds:[],createdStyleIds,createdVariableIds,createdCollectionIds,
  pageId:page.id,componentIds:[button.id],fonts,firstCompositionOnly:true,B01Complete:false,
  frames:frames.map(frame=>({id:frame.id,name:frame.name,width:frame.width,height:frame.height})),
  remaining:'Full contracted PRIM/state/viewport/mode/stream matrix, exports, inspection, independent reviews and founder pilot acceptance'};
