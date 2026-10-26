// Prepared read-only PNG-byte return; requires fresh immediate call approval.
const expected=[{"id":"21:517","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":320},{"id":"21:556","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_READ_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":320},{"id":"21:595","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","width":320},{"id":"21:634","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","width":320},{"id":"21:673","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":320},{"id":"21:712","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_PREFERENCE_WRITE_FAILED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":320},{"id":"21:751","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_HIGH_V01","width":320},{"id":"21:790","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_LOW_V01","width":320},{"id":"21:829","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":320},{"id":"21:868","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_STREAM_CHANGED_VP_320_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":320},{"id":"21:938","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_LOW_V01","width":1440},{"id":"21:969","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_MEDIUM_V01","width":1440},{"id":"21:1000","name":"HSD_UIR_B01_TPL_GLOBAL_NAVIGATION_REF_STATE_OPEN_VP_DESKTOP_MODE_KEYBOARD_STREAM_SEMANTIC_V01","width":1440}];
if(figma.editorType!=='figma'||(figma.fileKey&&figma.fileKey!=='GOmLP6Cv96l768ueSrZ5Dg'))throw Error('Wrong file/editor');
const page=await figma.getNodeByIdAsync('0:1');
if(!page||page.type!=='PAGE')throw Error('Missing page');
await figma.setCurrentPageAsync(page);
const exports=[];
for(const record of expected){
 const node=await figma.getNodeByIdAsync(record.id);
 if(!node||node.type!=='FRAME'||node.name!==record.name||node.width!==record.width)throw Error('Changed frame '+record.id);
 const bytes=await node.exportAsync({format:'PNG',constraint:{type:'SCALE',value:1}});
 exports.push({id:node.id,name:node.name,width:node.width,height:node.height,mimeType:'image/png',pngBase64:figma.base64Encode(bytes)});
}
return {createdNodeIds:[],mutatedNodeIds:[],exports,limitations:'Static node PNG exports only. No prototype, conformance, full coverage or acceptance.'};
