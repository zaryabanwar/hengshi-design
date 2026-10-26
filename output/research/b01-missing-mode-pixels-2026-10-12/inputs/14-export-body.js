// Local preparation only. Requires independent review and one scoped call approval.
// `expected` and `parentSpecs` are embedded by prepare; never evaluate external source.
function packIds(ids) {
  const groups = new Map(), literalIds = [];
  for (const id of new Set(ids)) {
    const m = /^(.*:)(0|[1-9][0-9]*)$/.exec(id);
    if (!m || !Number.isSafeInteger(Number(m[2]))) { literalIds.push(id); continue; }
    if (!groups.has(m[1])) groups.set(m[1], []);
    groups.get(m[1]).push(Number(m[2]));
  }
  const packed = [...groups].map(([prefix, values]) => {
    values.sort((a,b) => a-b);
    const ranges = [];
    for (const v of values) {
      const last = ranges[ranges.length-1];
      if (last && v === last[last.length-1]+1) {
        if (last.length === 1) last.push(v); else last[1] = v;
      } else ranges.push([v]);
    }
    return [prefix, ranges.map(r => r.length === 1 ? r[0] : r)];
  });
  const decoded = literalIds.slice();
  for (const [prefix, ranges] of packed) for (const r of ranges) {
    if (typeof r === 'number') decoded.push(prefix+r);
    else for (let i=r[0]; i<=r[1]; i++) decoded.push(prefix+i);
  }
  const unique = [...new Set(ids)].sort();
  if (JSON.stringify(decoded.sort()) !== JSON.stringify(unique)) throw Error('Lossless ID mismatch');
  return {encoding:'prefix-inclusive-ranges-v1',count:unique.length,groups:packed,literalIds};
}

if (figma.editorType !== 'figma' || (figma.fileKey && figma.fileKey !== 'GOmLP6Cv96l768ueSrZ5Dg')) throw Error('Wrong file/editor');
if (expected.length !== 15 || new Set(expected.map(e => e.id)).size !== 15 || parentSpecs.length !== 2) throw Error('Changed fifteen-view scope');
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE') throw Error('Missing page');
await figma.setCurrentPageAsync(page);
if (page.children.some(n => n.name.startsWith('HSD_UIR_B01_TEMP_REMAINING_PIXELS_'))) throw Error('Previous temporary sheet remains; inspect before retry');
const sourceParents = [];
for (const spec of parentSpecs) {
  const parent = await figma.getNodeByIdAsync(spec.id);
  if (!parent || parent.type !== 'FRAME' || parent.parent !== page || parent.name !== spec.name) throw Error('Changed source parent '+spec.id);
  sourceParents.push(parent);
}
const originals = [];
for (const item of expected) {
  const node = await figma.getNodeByIdAsync(item.id);
  if (!node || node.type !== 'FRAME' || node.parent?.id !== item.parentId || node.name !== item.name || node.width !== item.width || node.height !== item.height) throw Error('Changed source '+item.id);
  originals.push(node);
}
const fingerprint = node => JSON.stringify([node,...node.findAll(()=>true)].map((n,i)=>({
  type:n.type,name:n.name,visible:n.visible,opacity:n.opacity,
  x:i===0?null:n.x,y:i===0?null:n.y,width:n.width,height:n.height,rotation:n.rotation,
  text:n.type==='TEXT'?n.characters:null
})));
const before = originals.map(fingerprint);
const positions = originals.map(n=>({x:n.x,y:n.y}));
const parents = [page,...sourceParents];
const parentOrder = parents.map(p=>p.children.map(n=>n.id).join('|'));
const fonts = new Map();
for (const node of originals) for (const text of node.findAllWithCriteria({types:['TEXT']})) {
  for (const segment of text.getStyledTextSegments(['fontName'])) fonts.set(JSON.stringify(segment.fontName),segment.fontName);
}
for (const font of fonts.values()) await figma.loadFontAsync(font);

const sheets = [], copies = [], rows = [], createdIds = [], tiles = [];
let exportCompleted = false, reportData = null;
try {
  const right = Math.max(0,...page.children.filter(n=>'x' in n && 'width' in n).map(n=>n.x+n.width));
  for (let s=0; s<5; s++) {
    const sheet = figma.createAutoLayout('VERTICAL'); sheets.push(sheet); createdIds.push(sheet.id);
    sheet.name = 'HSD_UIR_B01_TEMP_REMAINING_PIXELS_'+(s+1)+'_V01';
    sheet.paddingTop=24; sheet.paddingBottom=24; sheet.paddingLeft=24; sheet.paddingRight=24;
    sheet.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}]; page.appendChild(sheet);
    sheet.x=right+400+s*1400; sheet.y=400;
    const row = figma.createAutoLayout('HORIZONTAL'); rows.push(row); createdIds.push(row.id);
    row.name='Temporary full-resolution comparison row'; row.itemSpacing=24; sheet.appendChild(row);
    for (let j=0; j<3; j++) {
      const i=s*3+j, original=originals[i], copy=original.clone();
      copies.push(copy); createdIds.push(copy.id,...copy.findAll(()=>true).map(n=>n.id)); row.appendChild(copy);
      copy.resize(original.width,original.height); copy.layoutSizingHorizontal='FIXED'; copy.layoutSizingVertical='FIXED';
      if (fingerprint(copy)!==before[i]) throw Error('Copy geometry/text mismatch '+original.id);
    }
  }
  for (let i=0; i<copies.length; i++) {
    const copy=copies[i], sheetIndex=Math.floor(i/3), sheet=sheets[sheetIndex], b=copy.absoluteBoundingBox;
    if (!b || copy.name!==originals[i].name) throw Error('Missing or misordered tile');
    const x=b.x-sheet.x, y=b.y-sheet.y;
    if (![x,y,b.width,b.height].every(Number.isInteger) || x<0 || y<0 || x+b.width>sheet.width || y+b.height>sheet.height) throw Error('Invalid full-resolution tile');
    tiles.push([originals[i].id,copy.id,sheetIndex,x,y,b.width,b.height]);
  }
  const sheetBounds=sheets.map(s=>[s.width,s.height]);
  if (sheetBounds.some(([w,h])=>w>1200 || h>2400 || w<=0 || h<=0) || createdIds.length>1500) throw Error('Finite export limit exceeded');
  if (!originals.every((n,i)=>fingerprint(n)===before[i] && n.x===positions[i].x && n.y===positions[i].y)) throw Error('Original changed before export');
  if (!sourceParents.every((p,i)=>p.children.map(n=>n.id).join('|')===parentOrder[i+1])) throw Error('Source parent order changed');
  reportData={createdNodeIds:packIds(createdIds),mutatedNodeIds:parents.map(p=>p.id),
    sourceFields:['id','parentId','name','width','height'],sources:expected.map(e=>[e.id,e.parentId,e.name,e.width,e.height]),
    tileFields:['sourceId','cloneId','imageIndex','x','y','width','height'],tiles,sheetBounds,
    sourceFrameCount:15,plannedImageCount:5,requestedScale:1,
    limitations:['Only static pixels of twelve recovery frames and three remaining directory refusal frames',
      'Actual returned image count and PNG dimensions must be checked; requesting five images is not receipt proof',
      'Source fingerprint covers geometry/text/visibility/opacity only, not exhaustive appearance equality',
      'No keyboard, detector, accessibility, full B01, native restore/EXIT or founder acceptance proof',
      'Exception cleanup is best-effort; a throwing call may return no IDs and requires inspection before any approved retry']};
  const reportBytes=encodeURIComponent(JSON.stringify(reportData)).match(/%[0-9A-F]{2}|[^%]/g).length;
  if (reportBytes>18000) throw Error('Receipt exceeds finite UTF-8 guard');
  for (const sheet of sheets) await sheet.screenshot({scale:1});
  exportCompleted=true;
} finally {
  for (const copy of copies) if (!copy.removed) copy.remove();
  for (const sheet of sheets) if (!sheet.removed) sheet.remove();
}
const originalGeometryTextUnchanged=originals.every((n,i)=>fingerprint(n)===before[i]);
const originalPositionsRestored=originals.every((n,i)=>n.x===positions[i].x && n.y===positions[i].y);
const parentOrderRestored=parents.every((p,i)=>p.children.map(n=>n.id).join('|')===parentOrder[i]);
const allCreatedNodesRemoved=copies.every(n=>n.removed) && rows.every(n=>n.removed) && sheets.every(n=>n.removed);
if (!originalGeometryTextUnchanged || !originalPositionsRestored || !parentOrderRestored || !allCreatedNodesRemoved) throw Error('Source restoration or cleanup failed');
return {...reportData,exportCompleted,originalGeometryTextUnchanged,originalPositionsRestored,parentOrderRestored,
  allCreatedNodesRemoved,removedCreatedNodeIds:reportData.createdNodeIds,removedCreatedNodeCount:reportData.createdNodeIds.count};
