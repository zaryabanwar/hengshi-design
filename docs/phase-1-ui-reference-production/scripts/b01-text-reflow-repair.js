// PREPARED ONLY. A fresh individual Figma call approval is required.
// Targeted repair for b01-initial-composition.js:67 and its actual overlap preview.
// Preserve existing IDs, copy, fonts, tokens and composition; create/delete nothing.
// Follow figma-use. Do not rerun the original empty-baseline construction script.
if (figma.editorType !== 'figma' || (figma.fileKey && figma.fileKey !== 'GOmLP6Cv96l768ueSrZ5Dg')) {
  throw new Error('Wrong editor or file: no repair');
}
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE') throw new Error('Missing approved page');
await figma.setCurrentPageAsync(page);
const frameIds = ['14:20','14:41','14:62','14:84','14:106','14:124'];
const frames = [];
for (const id of frameIds) {
  const frame = await figma.getNodeByIdAsync(id);
  if (!frame || frame.type !== 'FRAME' || frame.parent !== page ||
      !frame.name.startsWith('B01 DRAFT / ')) throw new Error('Changed draft: stop before mutation');
  frames.push(frame);
}
const component = await figma.getNodeByIdAsync('14:18');
if (!component || component.type !== 'COMPONENT' || component.parent?.type === 'COMPONENT_SET') {
  throw new Error('Changed action component');
}
// Repair the master once; leave instance text/property overrides intact.
const insideInstance = node => {
  for (let parent = node.parent; parent && parent.type !== 'PAGE'; parent = parent.parent) {
    if (parent.type === 'INSTANCE') return true;
  }
  return false;
};
const texts = [...new Map([component,...frames].flatMap(root =>
  root.findAllWithCriteria({types:['TEXT']}).filter(node => !insideInstance(node))
).map(node => [node.id,node])).values()];
const available = await figma.listAvailableFontsAsync();
for (const node of texts) {
  if (node.fontName === figma.mixed || !Number.isFinite(node.width) || node.width <= 0 ||
      !node.parent || !('layoutMode' in node.parent) || node.parent.layoutMode === 'NONE') {
    throw new Error('Unexpected text/font/layout: no silent correction');
  }
  if (!available.some(item => item.fontName.family === node.fontName.family &&
      item.fontName.style === node.fontName.style)) throw new Error('Current font unavailable');
  await figma.loadFontAsync(node.fontName);
}
const before = texts.map(node => ({id:node.id,width:node.width,height:node.height}));
for (const node of texts) {
  // resize resets sizing modes: set the intended wrapping/hug modes afterwards.
  node.resize(node.width,Math.max(24,node.height));
  node.textAutoResize = 'HEIGHT';
  node.layoutSizingHorizontal = 'FIXED';
  node.layoutSizingVertical = 'HUG';
}
const affectedIds = [...new Set([component.id,...frames.map(node => node.id),
  ...texts.map(node => node.id),...frames.flatMap(frame =>
    frame.findAllWithCriteria({types:['INSTANCE']}).map(node => node.id))])];
for (const frame of frames) await frame.screenshot();
return {createdNodeIds:[],mutatedNodeIds:affectedIds,before,
  textBounds:texts.map(node => ({id:node.id,width:node.width,height:node.height})),
  frames:frames.map(node => ({id:node.id,name:node.name,width:node.width,height:node.height})),
  B01Complete:false,remaining:'Inspect all six repaired views; complete contracted coverage, exports, independent review and founder acceptance'};
