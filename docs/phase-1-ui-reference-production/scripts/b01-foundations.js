// Proposed first foundation construction, not executed; no contracted frame or B01 exit.
// Require verified HSD_UIR_B01_PRE plus editable archive and immediate call approval.
// Follow figma-use,figma-generate-library. Fonts/styles must pass the read-only preflight.
if (figma.editorType !== 'figma' || figma.root.name !== 'Hengshi Design v1 — UI References') {
  throw new Error('Expected the single approved Hengshi v1 Design file');
}
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE') throw new Error('Expected Page 1');
await figma.setCurrentPageAsync(page);
if (page.children.length !== 0) throw new Error('Canvas changed: inspect before any construction/retry');
if ((await figma.getLocalPaintStylesAsync()).length || (await figma.getLocalTextStylesAsync()).length) {
  throw new Error('Styles already exist: inspect before any construction/retry');
}
const fonts = await figma.listAvailableFontsAsync();
const regular = {family:'Arial', style:'Regular'};
const bold = {family:'Arial', style:'Bold'};
for (const font of [regular, bold]) {
  if (!fonts.some(item => item.fontName.family === font.family && item.fontName.style === font.style)) {
    throw new Error('Approved Arial fallback unavailable: stop without downloading/substituting a font');
  }
  await figma.loadFontAsync(font);
}
const palette = [{"name": "ink", "hex": "#0B0F14", "role": "primary dark canvas and dark text"}, {"name": "graphite", "hex": "#161D26", "role": "raised dark surface"}, {"name": "slate", "hex": "#2A3542", "role": "border and secondary dark surface"}, {"name": "stone", "hex": "#D8D3C8", "role": "warm structural neutral"}, {"name": "mist", "hex": "#F3F1EA", "role": "soft light surface"}, {"name": "paper", "hex": "#FAF9F6", "role": "primary light canvas"}, {"name": "white", "hex": "#FFFFFF", "role": "high contrast text and print field"}, {"name": "signal/cyan/onDark", "hex": "#00D4FF", "role": "primary action and active connection"}, {"name": "signal/cyan/onLight", "hex": "#006D82", "role": "primary action and active connection"}, {"name": "signal/amber/onDark", "hex": "#FFB000", "role": "attention and conditional state"}, {"name": "signal/amber/onLight", "hex": "#8A5600", "role": "attention and conditional state"}, {"name": "signal/lime/onDark", "hex": "#B6F36B", "role": "verified state and data series"}, {"name": "signal/lime/onLight", "hex": "#4F7D18", "role": "verified state and data series"}, {"name": "signal/violet/onDark", "hex": "#A98CFF", "role": "demonstration state and spatial resonance"}, {"name": "signal/violet/onLight", "hex": "#6D52B5", "role": "demonstration state and spatial resonance"}];
const createdNodeIds = [];
const createdStyleIds = [];
const rgb = hex => ({r:parseInt(hex.slice(1,3),16)/255, g:parseInt(hex.slice(3,5),16)/255, b:parseInt(hex.slice(5,7),16)/255});
const paint = hex => ({type:'SOLID',color:rgb(hex)});
const paintStyles = [];
for (const token of palette) {
  const style = figma.createPaintStyle();
  style.name = 'D035/palette/' + token.name;
  style.description = token.role + '; approved source palette, not a theme or authority state.';
  style.paints = [paint(token.hex)];
  paintStyles.push({id:style.id, name:style.name, hex:token.hex});
  createdStyleIds.push(style.id);
}
const typeStyles = [];
for (const [name, font, size, lineHeight] of [
  ['body',regular,16,24], ['caption',regular,12,18], ['heading',bold,32,32]
]) {
  const style = figma.createTextStyle();
  style.name = 'D035/type/' + name;
  style.fontName = font;
  style.fontSize = size;
  style.lineHeight = {unit:'PIXELS',value:lineHeight};
  style.description = 'Arial system-stack fallback; no font file or hosted asset. Reference sizing only.';
  typeStyles.push({id:style.id, name:style.name});
  createdStyleIds.push(style.id);
}
const frame = figma.createAutoLayout('VERTICAL');
createdNodeIds.push(frame.id);
frame.name = 'B01 CONSTRUCTION — D035 foundations — NOT CONTRACTED EVIDENCE';
frame.x = 400; frame.y = 400;
frame.paddingTop = frame.paddingBottom = frame.paddingLeft = frame.paddingRight = 32;
frame.itemSpacing = 16;
frame.fills = [paint('#FAF9F6')];
frame.clipsContent = false;
const text = (parent, content, size=16, font=regular) => {
  const node = figma.createText();
  createdNodeIds.push(node.id);
  node.fontName = font;
  node.fontSize = size;
  node.lineHeight = {unit:'PIXELS',value:size === 32 ? 32 : size * 1.5};
  node.characters = content;
  node.textAutoResize = 'WIDTH_AND_HEIGHT';
  node.fills = [paint('#0B0F14')];
  parent.appendChild(node);
  return node;
};
text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY',12);
text(frame,'Hengshi Design v1 — foundation construction',32,bold);
text(frame,'Palette and typography only. No screen, live controls, staff availability or compliance claim.');
for (const token of palette) {
  const row = figma.createAutoLayout('HORIZONTAL');
  createdNodeIds.push(row.id);
  row.fills = []; row.itemSpacing = 16;
  row.counterAxisAlignItems = 'CENTER';
  frame.appendChild(row);
  const swatch = figma.createRectangle();
  createdNodeIds.push(swatch.id);
  swatch.resize(48,48);
  swatch.fills = [paint(token.hex)];
  swatch.strokes = [paint('#2A3542')]; swatch.strokeWeight = 1;
  row.appendChild(swatch);
  text(row,token.name + '  ' + token.hex + '  —  ' + token.role);
}
return {
  createdNodeIds, mutatedNodeIds:[], createdStyleIds,
  pageId:page.id, frameId:frame.id, paintStyles, typeStyles,
  bounds:{x:frame.x,y:frame.y,width:frame.width,height:frame.height},
  contractedEvidenceCreated:false, B01Complete:false,
  remaining:'Semantic alias/variable bindings, PRIM families, full template/state/viewport/mode/stream coverage, exports and independent reviews'
};
