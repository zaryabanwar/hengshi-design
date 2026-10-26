async function figmaToolScope(){
// Read-only combined inspection. Fresh call approval required; no canvas mutations.
const frames = [
  {
    "id": "21:291",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01",
    "width": 320,
    "height": 1562
  },
  {
    "id": "21:328",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_LOW_V01",
    "width": 320,
    "height": 1562
  },
  {
    "id": "21:365",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01",
    "width": 320,
    "height": 1562
  },
  {
    "id": "21:402",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01",
    "width": 320,
    "height": 1562
  },
  {
    "id": "21:439",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:478",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:517",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:556",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:595",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:634",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:673",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:712",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01",
    "width": 320,
    "height": 1730
  },
  {
    "id": "21:751",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01",
    "width": 320,
    "height": 1634
  },
  {
    "id": "21:790",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01",
    "width": 320,
    "height": 1634
  },
  {
    "id": "21:829",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01",
    "width": 320,
    "height": 1634
  },
  {
    "id": "21:868",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01",
    "width": 320,
    "height": 1634
  },
  {
    "id": "21:907",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_HIGH_V01",
    "width": 1440,
    "height": 1034
  },
  {
    "id": "21:938",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_LOW_V01",
    "width": 1440,
    "height": 1034
  },
  {
    "id": "21:969",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_MEDIUM_V01",
    "width": 1440,
    "height": 1034
  },
  {
    "id": "21:1000",
    "name": "HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_SEMANTIC_V01",
    "width": 1440,
    "height": 1034
  }
];
const page = await figma.getNodeByIdAsync('0:1');
if(!page || page.type !== 'PAGE' || figma.editorType !== 'figma') throw new Error('Wrong editor/page');
await figma.setCurrentPageAsync(page);
const roots=[]; const findings=[]; const observations=[];
for(const expected of frames){
 const node=await figma.getNodeByIdAsync(expected.id);
 if(!node || node.type !== 'FRAME' || node.name !== expected.name || node.width !== expected.width) throw new Error('Reference identity changed: '+expected.id);
 roots.push(node);
 const texts=node.findAllWithCriteria({types:['TEXT']});
 const instances=node.findAllWithCriteria({types:['INSTANCE']});
 const issues=[];
 for(const child of [...texts,...instances]){
  if(child.width<=0||child.height<=0) issues.push({id:child.id,issue:'invalid dimensions'});
  const parent=child.parent;
  if(parent && 'width' in parent && child.x+child.width>parent.width+1) issues.push({id:child.id,issue:'horizontal overflow'});
  if(child.type==='TEXT'){
   if(child.hasMissingFont) issues.push({id:child.id,issue:'missing font'});
   if(!child.textStyleId) issues.push({id:child.id,issue:'missing text style'});
   // Single-line inherited action text can use WIDTH_AND_HEIGHT; record wrapping without treating that as a defect.
   if(child.textAutoResize==='NONE' && child.height<=0) issues.push({id:child.id,issue:'invalid fixed text height'});
  }
 }
 observations.push({id:node.id,name:node.name,width:node.width,height:node.height,textCount:texts.length,instanceCount:instances.length,issues});
 findings.push(...issues);
}
const set=await figma.getNodeByIdAsync('21:289');
if(!set || set.type!=='COMPONENT_SET' || set.children.length!==16) throw new Error('Variant checkpoint changed');
const colourIds=new Set((await figma.variables.getLocalVariablesAsync('COLOR')).map(v=>v.id));
const spacing=(await figma.variables.getLocalVariablesAsync('FLOAT')).filter(v=>v.name.startsWith('D035/space/'));
const tokenEvidence=spacing.map(v=>({id:v.id,name:v.name,scopes:v.scopes,codeSyntax:v.codeSyntax,valuesByMode:v.valuesByMode}));
const variantEvidence=set.children.map(n=>({id:n.id,name:n.name,width:n.width,height:n.height}));
// Earlier open high narrow/wide pixels are already preserved. Inspect remaining 18 new views without another construction call.
for(const node of roots.filter(n=>!['21:291','21:907'].includes(n.id))) await node.screenshot({scale:1});
return {createdNodeIds:[],mutatedNodeIds:[],observations,findings,tokenEvidence,variantEvidence,renderedFrameIds:roots.filter(n=>!['21:291','21:907'].includes(n.id)).map(n=>n.id),limitations:'Read-only static references. No interaction/WCAG/physical-device/full-B01/Phase1 acceptance or runtime proof.'};

}
