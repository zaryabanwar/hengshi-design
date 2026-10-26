const typeOf = (owner, name) => {
  try { return typeof owner[name]; }
  catch { return "not exposed"; }
};
return {
  editorType: figma.editorType,
  pages: figma.root.children.map(page => ({ id: page.id, name: page.name })),
  currentPage: {
    id: figma.currentPage.id,
    name: figma.currentPage.name,
    childCount: figma.currentPage.children.length
  },
  namedVersionApiType: typeOf(figma, "saveVersionHistoryAsync"),
  nodeExportApiType: typeOf(figma.currentPage, "exportAsync"),
  createdNodeIds: [],
  mutatedNodeIds: [],
  scope: "Read-only inventory and API-presence observation. Presence does not prove execution, private sharing or full editable-file archive support."
};
