// Capture all48 newly authored specimens without changing their permanent layout.
// Five ordered horizontal comparison sheets contain10/10/10/10/8 native tiles.
const specimenBefore=frames.map(f=>preservationFingerprint(f.node));
const specimenPositions=frames.map(f=>[f.node.x,f.node.y]);
const rootOrder=root.children.map(n=>n.id).join('|');
const permanentIds=[root.id,...root.findAll(()=>true).map(n=>n.id)];
const tempSheets=[],tempRows=[],tempCopies=[],temporaryIds=[],tiles=[],cleanupFailures=[];
let captureReport=null;
try {
  for(let s=0;s<5;s++) {
    const sheet=figma.createAutoLayout('VERTICAL');tempSheets.push(sheet);temporaryIds.push(sheet.id);
    sheet.name='HSD_UIR_B01_TEMP_GRAMMAR_CAPTURE_'+s+'_V01';
    sheet.paddingTop=24;sheet.paddingRight=24;sheet.paddingBottom=24;sheet.paddingLeft=24;
    sheet.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];page.appendChild(sheet);
    sheet.x=root.x+root.width+400+s*3800;sheet.y=400;
    const row=figma.createAutoLayout('HORIZONTAL');tempRows.push(row);temporaryIds.push(row.id);
    row.name='Temporary grammar comparison row';row.itemSpacing=24;sheet.appendChild(row);
    for(let j=0;j<10&&s*10+j<frames.length;j++) {
      const ordinal=s*10+j,source=frames[ordinal].node,copy=source.clone();
      tempCopies.push(copy);temporaryIds.push(copy.id,...copy.findAll(()=>true).map(n=>n.id));
      row.appendChild(copy);copy.resize(source.width,source.height);
      copy.layoutSizingHorizontal='FIXED';copy.layoutSizingVertical='FIXED';
      if(preservationFingerprint(copy)!==specimenBefore[ordinal])throw Error('Grammar clone geometry/text mismatch');
    }
  }
  for(let ordinal=0;ordinal<tempCopies.length;ordinal++) {
    const copy=tempCopies[ordinal],imageIndex=Math.floor(ordinal/10),sheet=tempSheets[imageIndex],bounds=copy.absoluteBoundingBox;
    if(!bounds)throw Error('Missing grammar tile bounds');
    const x=bounds.x-sheet.x,y=bounds.y-sheet.y,w=bounds.width,h=bounds.height;
    if(![x,y,w,h].every(Number.isInteger)||x<0||y<0||w<=0||h<=0||x+w>sheet.width||y+h>sheet.height)throw Error('Invalid grammar tile bounds');
    tiles.push([frames[ordinal].node.id,copy.id,imageIndex,x,y,w,h]);
  }
  const sheetBounds=tempSheets.map(s=>[s.width,s.height]);
  if(tiles.length!==48||sheetBounds.some(([w,h])=>w<=0||h<=0||w>3600||h>2400)||permanentIds.length+temporaryIds.length>5000)throw Error('Finite grammar export limit exceeded');
  captureReport={...report,createdNodeIds:packIds([...permanentIds,...temporaryIds]),
    temporaryNodeIds:packIds(temporaryIds),removedTemporaryNodeIds:packIds(temporaryIds),
    tileFields:['sourceId','cloneId','imageIndex','x','y','width','height'],tiles,sheetBounds,
    plannedImageCount:5,requestedScale:1,allTemporaryNodesRemoved:true,
    originalGeometryTextUnchanged:true,originalPositionsUnchanged:true,originalPageOrderPreserved:true,
    specimenGeometryTextUnchanged:true,specimenPositionsUnchanged:true,specimenChildOrderPreserved:true,
    captureLimitations:['Five screenshots requested; actual returned count/native dimensions require result inspection',
      'PNG-to-source mapping follows request order and tile records; image blocks have no independent source ID tag',
      'Geometry/text/visibility/opacity fingerprint only, not exhaustive paint/font/style appearance equality',
      'Cleanup is best-effort; permanent composition remains if capture fails; inspect before any separately approved retry']};
  const completeBytes=encodeURIComponent(JSON.stringify(captureReport)).match(/%[0-9A-F]{2}|[^%]/g).length;
  if(completeBytes>19000)throw Error('Complete grammar receipt exceeds19000-byte guard; inspect before separately approved retry');
  for(const sheet of tempSheets)await sheet.screenshot({scale:1});
} finally {
  for(const node of [...tempCopies,...tempRows,...tempSheets]) {
    try {if(!node.removed)node.remove();}catch(_){cleanupFailures.push('Temporary removal failed');}
  }
  if(cleanupFailures.length)throw Error('Grammar cleanup failed; inspect before any separately approved retry');
}
captureReport.allTemporaryNodesRemoved=[...tempCopies,...tempRows,...tempSheets].every(n=>n.removed);
captureReport.originalGeometryTextUnchanged=inheritedNodes.every((n,i)=>preservationFingerprint(n)===inheritedBefore[i]);
captureReport.originalPositionsUnchanged=inheritedNodes.every((n,i)=>n.x===inheritedPositions[i][0]&&n.y===inheritedPositions[i][1]);
captureReport.originalPageOrderPreserved=page.children.filter(n=>n.id!==root.id).map(n=>n.id).join('|')===inheritedPageOrder;
captureReport.specimenGeometryTextUnchanged=frames.every((f,i)=>preservationFingerprint(f.node)===specimenBefore[i]);
captureReport.specimenPositionsUnchanged=frames.every((f,i)=>f.node.x===specimenPositions[i][0]&&f.node.y===specimenPositions[i][1]);
captureReport.specimenChildOrderPreserved=root.children.map(n=>n.id).join('|')===rootOrder;
for(const key of ['allTemporaryNodesRemoved','originalGeometryTextUnchanged','originalPositionsUnchanged','originalPageOrderPreserved','specimenGeometryTextUnchanged','specimenPositionsUnchanged','specimenChildOrderPreserved'])if(captureReport[key]!==true)throw Error('Grammar preservation failed: '+key+'; inspect before separately approved retry');
const finalBytes=encodeURIComponent(JSON.stringify(captureReport)).match(/%[0-9A-F]{2}|[^%]/g).length;
if(finalBytes>19000)throw Error('Final grammar receipt exceeds finite guard; inspect before separately approved retry');
return captureReport;
