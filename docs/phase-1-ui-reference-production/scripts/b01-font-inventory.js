// Prepared read-only call, not executed. Fresh CB-06/CB-07 approval required.
// No font installation, loading, substitution, node/style creation or sharing change.
if (figma.editorType !== 'figma') throw new Error('Expected a Figma Design file');
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE') throw new Error('Expected previously inspected Page 1');
const fonts = await figma.listAvailableFontsAsync();
const names = fonts.map(item => item.fontName).sort((a, b) =>
  a.family.localeCompare(b.family) || a.style.localeCompare(b.style));
const families = [...new Set(names.map(font => font.family))];
const documentedNames = new Set([
  'Segoe UI', 'Arial', 'Helvetica', 'Cascadia Mono', 'Segoe UI Mono', 'Consolas'
]);
const documentedCandidates = names.filter(font => documentedNames.has(font.family));
return {
  fileName: figma.root.name,
  pageId: page.id,
  pageName: page.name,
  fontCount: names.length,
  familyCount: families.length,
  documentedCandidates: documentedCandidates.slice(0, 64),
  documentedCandidatesTruncated: documentedCandidates.length > 64,
  families: families.slice(0, 120),
  familiesTruncated: families.length > 120,
  createdNodeIds: [],
  mutatedNodeIds: []
};
