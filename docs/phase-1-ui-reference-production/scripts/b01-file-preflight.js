// Proposed read-only use_figma call, not executed. Immediate CB-06/CB-07 approval required.
// Follow figma-use; this inventories only the single approved file, not team libraries.
if (figma.editorType !== 'figma') throw new Error('Expected a Figma Design file');
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE') throw new Error('Expected the previously inspected Page 1');
await figma.setCurrentPageAsync(page);
const paintStyles = await figma.getLocalPaintStylesAsync();
const textStyles = await figma.getLocalTextStylesAsync();
const fonts = await figma.listAvailableFontsAsync();
return {
  fileName: figma.root.name,
  editorType: figma.editorType,
  pageId: page.id,
  pageName: page.name,
  pageCount: figma.root.children.length,
  canvasChildCount: page.children.length,
  paintStyleCount: paintStyles.length,
  textStyleCount: textStyles.length,
  paintStyles: paintStyles.slice(0, 50).map(style => ({id:style.id, name:style.name})),
  textStyles: textStyles.slice(0, 50).map(style => ({id:style.id, name:style.name})),
  styleInventoryTruncated: paintStyles.length > 50 || textStyles.length > 50,
  arialRegularAvailable: fonts.some(item => item.fontName.family === 'Arial' && item.fontName.style === 'Regular'),
  arialBoldAvailable: fonts.some(item => item.fontName.family === 'Arial' && item.fontName.style === 'Bold'),
  topLevelNodes: page.children.slice(0, 30).map(node => ({id: node.id, type: node.type, name: node.name})),
  inventoryTruncated: page.children.length > 30,
  createdNodeIds: [],
  mutatedNodeIds: []
};
