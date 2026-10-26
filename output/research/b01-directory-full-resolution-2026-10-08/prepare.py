from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
report=json.loads((root/'output/research/b01-directory-call19-2026-10-08/decoded-design-result.json').read_text(encoding='utf-8'))
expected=[{'id':f['id'],'name':f['reference']['name'],'width':f['width'],'height':f['height']} for f in report['frames']]
assert len(expected)==52
codec=(root/'output/research/b01-directory-return-recovery-2026-10-08/codec.js').read_text(encoding='utf-8')
code='// Prepared only: one approved future comparison export of all52 original references.\nconst expected='+json.dumps(expected,separators=(',',':'))+';\n'+codec+r'''
if(figma.editorType!=='figma'||(figma.fileKey&&figma.fileKey!=='GOmLP6Cv96l768ueSrZ5Dg'))throw Error('Wrong file/editor');
const page=await figma.getNodeByIdAsync('0:1');
if(!page||page.type!=='PAGE')throw Error('Missing page');
await figma.setCurrentPageAsync(page);
const originalParent=await figma.getNodeByIdAsync('27:381');
if(!originalParent||originalParent.type!=='FRAME'||originalParent.name!=='B01 / Directory search states / v1')throw Error('Changed directory root');
if(page.children.some(n=>n.name.startsWith('HSD_UIR_B01_TEMP_DIRECTORY_PIXELS_')))throw Error('Prior temporary directory export present; inspect before retry');
const originals=[];
for(const item of expected){
 const node=await figma.getNodeByIdAsync(item.id);
 if(!node||node.type!=='FRAME'||node.parent!==originalParent||node.name!==item.name||node.width!==item.width||node.height!==item.height)throw Error('Changed source '+item.id);
 originals.push(node);
}
const fingerprint=node=>JSON.stringify([node,...node.findAll(()=>true)].map((n,i)=>({
 type:n.type,name:n.name,visible:n.visible,opacity:n.opacity,
 x:i===0?null:n.x,y:i===0?null:n.y,width:n.width,height:n.height,rotation:n.rotation,
 text:n.type==='TEXT'?n.characters:null
})));
const before=originals.map(fingerprint);
const positions=originals.map(n=>({x:n.x,y:n.y}));
const parents=[page,originalParent];
const parentOrder=parents.map(p=>p.children.map(c=>c.id).join('|'));
const fonts=new Map();
for(const node of originals)for(const text of node.findAll(n=>n.type==='TEXT'))
 for(const segment of text.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(segment.fontName),segment.fontName);
for(const font of fonts.values())await figma.loadFontAsync(font);
const sheets=[],copies=[],createdIds=[],tiles=[];
let exportCompleted=false,reportData=null;
try{
 const right=Math.max(0,...page.children.filter(n=>'x'in n&&'width'in n).map(n=>n.x+n.width));
 const narrow=originals.map((n,i)=>({n,i})).filter(x=>x.n.width===320);
 const wide=originals.map((n,i)=>({n,i})).filter(x=>x.n.width===1440);
 const batches=[narrow.slice(0,12),narrow.slice(12,24),narrow.slice(24,36),narrow.slice(36,48),wide];
 if(batches.map(b=>b.length).join(',')!=='12,12,12,12,4')throw Error('Unexpected sheet allocations');
 for(let s=0;s<batches.length;s++){
  const sheet=figma.createAutoLayout('VERTICAL');sheets.push(sheet);createdIds.push(sheet.id);
  sheet.name='HSD_UIR_B01_TEMP_DIRECTORY_PIXELS_'+(s+1)+'_V01';sheet.itemSpacing=24;
  sheet.paddingTop=24;sheet.paddingBottom=24;sheet.paddingLeft=24;sheet.paddingRight=24;
  sheet.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];page.appendChild(sheet);
  sheet.x=right+400+s*2400;sheet.y=400;
  let row=null;
  for(let j=0;j<batches[s].length;j++){
   const {n:original,i}=batches[s][j];
   if(s<4&&j%6===0){row=figma.createAutoLayout('HORIZONTAL');row.itemSpacing=24;row.name='Temporary full-resolution row';createdIds.push(row.id);sheet.appendChild(row);}
   const copy=original.clone();copies.push(copy);createdIds.push(copy.id,...copy.findAll(()=>true).map(n=>n.id));
   (s<4?row:sheet).appendChild(copy);copy.name=original.name;
   copy.resize(original.width,original.height);copy.layoutSizingHorizontal='FIXED';copy.layoutSizingVertical='FIXED';
   if(fingerprint(copy)!==before[i])throw Error('Copy geometry/text mismatch '+original.id);
  }
 }
 // Capture bounds after every row is complete; auto-layout can change earlier positions.
 for(let i=0;i<copies.length;i++){
  const copy=copies[i],sheetIndex=Math.min(4,Math.floor(i/12)),sheet=sheets[sheetIndex];
  const b=copy.absoluteBoundingBox;
  if(!b)throw Error('Missing tile bounds');
  const itemIndex=i<48?i:48+(i-48);
  // Original input order is narrow first and four wide last, checked by allocations.
  const original=originals[itemIndex];
  if(copy.name!==original.name)throw Error('Unexpected tile order');
  tiles.push([original.id,copy.id,sheetIndex,b.x-sheet.x,b.y-sheet.y,b.width,b.height]);
 }
 const sheetBounds=sheets.map(s=>[s.width,s.height]);
 if(sheetBounds.some(([w,h])=>w>2400||h>8000||w<=0||h<=0)||createdIds.length>4000)throw Error('Export exceeds finite source/sheet limits');
 if(!originals.every((n,i)=>fingerprint(n)===before[i]&&n.x===positions[i].x&&n.y===positions[i].y))throw Error('Original geometry/text or positions changed');
 if(originalParent.children.map(c=>c.id).join('|')!==parentOrder[1])throw Error('Original parent order changed');
 reportData={createdNodeIds:packIds(createdIds),mutatedNodeIds:parents.map(p=>p.id),
  tileFields:['sourceId','cloneId','imageIndex','x','y','width','height'],tiles,sheetBounds,
  originalFrameCount:52,plannedImageCount:5,
  limitations:'Static pixel export only; no original correction or native exports/restore/EXIT, interaction, full profile coverage, independent review or acceptance.'};
 const bytes=encodeURIComponent(JSON.stringify(reportData)).match(/%[0-9A-F]{2}|[^%]/g).length;
 if(bytes>18000)throw Error('Comparison receipt exceeds18000-byte pre-export guard');
 for(const sheet of sheets)await sheet.screenshot({scale:1});
 exportCompleted=true;
}finally{
 for(const copy of copies)if(!copy.removed)copy.remove();
 for(const sheet of sheets)if(!sheet.removed)sheet.remove();
}
const originalGeometryTextUnchanged=originals.every((n,i)=>fingerprint(n)===before[i]);
const originalPositionsRestored=originals.every((n,i)=>n.x===positions[i].x&&n.y===positions[i].y);
const parentOrderRestored=parents.every((p,i)=>p.children.map(c=>c.id).join('|')===parentOrder[i]);
const allCreatedNodesRemoved=copies.every(n=>n.removed)&&sheets.every(n=>n.removed);
if(!originalGeometryTextUnchanged||!originalPositionsRestored||!parentOrderRestored||!allCreatedNodesRemoved)throw Error('Source restoration or cleanup failed');
return {...reportData,exportCompleted,originalGeometryTextUnchanged,originalPositionsRestored,parentOrderRestored,allCreatedNodesRemoved,removedCreatedNodeCount:reportData.createdNodeIds.count};
'''
target=out/'figma-call.js'
assert not target.exists()
target.write_text(code,encoding='utf-8',newline='')
meta={'product':'Hengshi Design v1','status':'TODO','external_calls':0,
 'scope':'One proposed comparison export of all52 existing directory views at scale1; five temporary clone sheets removed in finally; no original correction',
 'script_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'source_result_sha256':hashlib.sha256((root/'output/research/b01-directory-call19-2026-10-08/decoded-design-result.json').read_bytes()).hexdigest(),
 'images':5,'views':52,'sheet_allocations':[12,12,12,12,4],
 'finite_limits':'Each sheet<=2400x8000; created IDs<=4000; report<=18000 UTF8 bytes before export',
 'original_checks':'IDs names widths heights parent, geometry/text/positions and parent-order restoration; not exhaustive appearance fingerprint',
 'call_counts_if_approved':'October attempt20 conservative metered17; actual quota unknown; fresh per-call approval required',
 'limits':'Prepared only; no Figma execution or guarantee of renderer output or image delivery; full B01 coverage/runtime/native restore/acceptance remain held'}
(out/'preparation.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
print(json.dumps(meta))
