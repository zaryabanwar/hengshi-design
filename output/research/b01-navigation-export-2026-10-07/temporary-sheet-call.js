// Founder-approved single temporary comparison-sheet export and cleanup, 2026-10-07.
const expected=[{"id":"21:517","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":320},{"id":"21:556","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":320},{"id":"21:595","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","width":320},{"id":"21:634","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","width":320},{"id":"21:673","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":320},{"id":"21:712","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":320},{"id":"21:751","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","width":320},{"id":"21:790","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","width":320},{"id":"21:829","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":320},{"id":"21:868","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":320},{"id":"21:938","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_LOW_V01","width":1440},{"id":"21:969","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":1440},{"id":"21:1000","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":1440}];
if(figma.editorType!=='figma'||(figma.fileKey&&figma.fileKey!=='GOmLP6Cv96l768ueSrZ5Dg'))throw Error('Wrong file/editor');
const page=await figma.getNodeByIdAsync('0:1');
if(!page||page.type!=='PAGE')throw Error('Missing page');
await figma.setCurrentPageAsync(page);
const originals=[];
for(const item of expected){
 const node=await figma.getNodeByIdAsync(item.id);
 if(!node||node.type!=='FRAME'||node.name!==item.name||node.width!==item.width)throw Error('Changed source '+item.id);
 originals.push(node);
}
const fingerprint=node=>JSON.stringify([node,...node.findAll(()=>true)].map((n,i)=>({
 type:n.type,name:n.name,visible:n.visible,opacity:n.opacity,
 x:i===0?null:n.x,y:i===0?null:n.y,width:n.width,height:n.height,rotation:n.rotation,
 text:n.type==='TEXT'?n.characters:null
})));
const before=originals.map(fingerprint);
const originalPositions=originals.map(n=>({x:n.x,y:n.y}));
const parents=[...new Set(originals.map(n=>n.parent))];
const parentChildren=parents.map(n=>n.children.map(c=>c.id).join('|'));
const fonts=new Map();
for(const node of originals)for(const text of node.findAll(n=>n.type==='TEXT')){
 for(const segment of text.getStyledTextSegments(['fontName']))fonts.set(JSON.stringify(segment.fontName),segment.fontName);
}
for(const font of fonts.values())await figma.loadFontAsync(font);
const createdNodeIds=[];const cloneHandles=[];const mutatedNodeIds=[page.id,...parents.map(n=>n.id)];
let sheet=null;const tiles=[];let sheetBounds=null;let originalIntegrity=false;let exportCompleted=false;let executionError=null;
try{
 const rightEdge=Math.max(0,...page.children.filter(n=>'x' in n&&'width' in n).map(n=>n.x+n.width));
 sheet=figma.createAutoLayout('VERTICAL');sheet.name='HSD_UIR_B01_TEMP_NAVIGATION_EXPORT_SHEET_V01';sheet.itemSpacing=24;
 createdNodeIds.push(sheet.id);page.appendChild(sheet);sheet.x=rightEdge+400;sheet.y=400;
 sheet.paddingTop=24;sheet.paddingBottom=24;sheet.paddingLeft=24;sheet.paddingRight=24;
 sheet.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];
 let row=null;let narrowCount=0;
 for(let index=0;index<originals.length;index++){
  const original=originals[index];
  if(original.width===320){
   if(narrowCount%5===0){row=figma.createAutoLayout('HORIZONTAL');row.name='Temporary narrow-view row';row.itemSpacing=24;createdNodeIds.push(row.id);sheet.appendChild(row);}
   narrowCount++;
  }
  const copy=original.clone();cloneHandles.push(copy);
  createdNodeIds.push(copy.id,...copy.findAll(()=>true).map(n=>n.id));
  (original.width===320?row:sheet).appendChild(copy);copy.name=original.name;
  copy.resize(original.width,original.height);copy.layoutSizingHorizontal='FIXED';copy.layoutSizingVertical='FIXED';
  if(fingerprint(copy)!==before[index])throw Error('Clone content/layout mismatch '+original.id);
  const bounds=copy.absoluteBoundingBox;
  if(!bounds)throw Error('Missing export tile bounds');
  tiles.push({sourceId:original.id,name:original.name,cloneId:copy.id,x:bounds.x-sheet.x,y:bounds.y-sheet.y,width:bounds.width,height:bounds.height});
 }
 originalIntegrity=originals.every((node,i)=>fingerprint(node)===before[i])&&parents.every((p,i)=>p.children.map(c=>c.id).join('|')===parentChildren[i]);
 if(!originalIntegrity)throw Error('Original source or parent order changed');
 sheetBounds={width:sheet.width,height:sheet.height};
 if(sheet.width>8000||sheet.height>12000||createdNodeIds.length>3000)throw Error('Export sheet exceeds prepared finite bounds');
 // One native image block avoids relying on multiple inline previews or PNG bytes in returned JSON text.
 await sheet.screenshot({scale:1});
}finally{
 // Only nodes created by this invocation are removed; no original is removed or edited.
 for(const copy of cloneHandles)if(!copy.removed)copy.remove();
 if(sheet&&!sheet.removed)sheet.remove();
}
const restored=originals.every((node,i)=>fingerprint(node)===before[i])&&parents.every((p,i)=>p.children.map(c=>c.id).join('|')===parentChildren[i]);
const originalPositionsRestored=originals.every((node,i)=>node.x===originalPositions[i].x&&node.y===originalPositions[i].y);
const allCopiesRemoved=cloneHandles.every(n=>n.removed)&&(!sheet||sheet.removed);
if(!restored||!originalPositionsRestored||!allCopiesRemoved)executionError='Source restoration or cleanup check failed';
return {createdNodeIds:[...new Set(createdNodeIds)],removedCreatedNodeCount:allCopiesRemoved?[...new Set(createdNodeIds)].length:null,allCreatedNodesRemoved:allCopiesRemoved,mutatedNodeIds,
 sourceFramesUnchanged:restored,originalPositionsRestored,parentOrderRestored:restored,exportCompleted,executionError,tiles,sheetBounds,
 limitations:'Static copies for producer pixel inspection only; no original correction, interaction evidence, independent review or acceptance.'};
