// PREPARED ONLY. A new, individually approved Figma call is required.
// Shared status specimens supplement host-template evidence; they cannot replace it.
const input = {"product":"Hengshi Design v1","status":"DOING","scope":"Prepared48 shared narrow grammar specimens plus five bundled native comparison captures; no external execution","template_id":"TPL-SYSTEM-RECOVERY","states":[{"id":"STATE-LOADING","title":"Loading optional information","body":"Confirmed page content remains readable in this fixture. Optional information is not ready.","truth":"Prior eligible public page only","action":"Continue reading","action_kind":"same_document_no_mutation"},{"id":"STATE-DEGRADED","title":"Some information is unavailable","body":"An optional part could not be shown. The current page and public navigation remain available.","truth":"Current confirmed public page; no stream change","action":"Open the directory","action_kind":"public_navigation"},{"id":"STATE-EMPTY","title":"No items in this view","body":"This is an approved empty view in the reference fixture, not an error or an invented case study.","truth":"Confirmed empty collection in the fixture","action":"Browse services","action_kind":"canonical_link"},{"id":"STATE-PENDING","title":"The outcome is not confirmed","body":"This request is still being checked. Do not repeat it as a new action until its existing outcome is reconciled.","truth":"Last confirmed record; pending is not success","action":"Check this request","action_kind":"same_operation_reconciliation_method_held"},{"id":"STATE-UNAVAILABLE","title":"This action is unavailable","body":"No new action was accepted in this fixture. Public information remains available.","truth":"Confirmed unavailability, not live staff status","action":"Browse services","action_kind":"canonical_link"},{"id":"STATE-OFFLINE","title":"Connection unavailable","body":"No fresh action or new content is confirmed while disconnected. The visible prior view makes no promise of offline storage.","truth":"Visible prior truth only; fresh availability unknown","action":"Check connection again","action_kind":"bounded_connectivity_read_no_redispatch"},{"id":"STATE-ERROR","title":"The action did not complete","body":"This fixture represents a confirmed failure before a business action was admitted; it is not an unknown outcome.","truth":"Prior authoritative state; no successful new action","action":"Return to the current page","action_kind":"same_document_no_mutation"},{"id":"STATE-PERMISSION-DENIED","title":"Private information is unavailable","body":"This access is not permitted. No private details or record-existence clues are shown.","truth":"Public location only; no permission grant","action":"Open the public website","action_kind":"canonical_link"},{"id":"STATE-SESSION-EXPIRED","title":"Private access has expired","body":"Public pages remain available. Opening retained private work requires current verified access; this fixture does not restore it.","truth":"Last confirmed public context; permitted private state follows its separate lifecycle","action":"Open the public website","action_kind":"canonical_link","held":"D-076 selects visitor access expiry after 30 minutes of inactivity or an authorized End, with no absolute conversation duration. Warning and More time remain required. Restoration mechanisms and complete-process accessibility evidence remain held; booking and staff clocks are separate. Do not invent a sign-in or restore mechanism."},{"id":"STATE-STALE","title":"This view is out of date","body":"The last confirmed information is labelled as earlier. Obtain the current eligible view before acting.","truth":"Earlier confirmed state, not current authority","action":"Check the current view","action_kind":"guarded_read_method_held"},{"id":"STATE-CONFLICT","title":"The information changed","body":"No new change is confirmed. Review the current authoritative version before deciding what to do.","truth":"Current/previous version distinction; no automatic overwrite or retry","action":"Review the current view","action_kind":"guarded_read_method_held"},{"id":"STATE-ASSET-FAILURE","title":"An optional visual could not load","body":"The relevant semantic information remains available in this fixture. The in-force delivery stream does not change silently.","truth":"Eligible public information; failed optional asset is not a closed service","action":"Open the semantic page","action_kind":"paired_canonical_link"},{"id":"STATE-CHECKSUM-MISMATCH","title":"New content was not verified","body":"The unverified replacement was not activated. This fixture keeps the prior complete eligible release without mixing content.","truth":"Prior confirmed release only; candidate remains inactive","action":"Continue with confirmed content","action_kind":"same_document_no_mutation"},{"id":"STATE-FOCUS","title":"Focus appearance requirement","body":"The recovery action needs a visible focus indicator and a text label. This specimen describes that requirement; it does not draw or execute a focus ring.","truth":"Focus requirement annotation only; no authored ring or action dispatch","action":"Open the directory","action_kind":"public_navigation"},{"id":"STATE-STREAM-CHANGED","title":"Presentation choice applied","body":"Use the exact accepted D-057 notice supplied by the inherited stream component; the location and open context remain.","truth":"Synthetic confirmed stream change; shared control carries accepted copy","action":"Continue reading","action_kind":"same_document_no_mutation"},{"id":"STATE-PREFERENCE-WRITE-FAILED","title":"Presentation applied for this session","body":"Use the exact accepted D-057 persistence notice supplied by the inherited stream component; saved preference is not confirmed.","truth":"Session choice applied; persistent write not confirmed","action":"Continue reading","action_kind":"same_document_no_mutation"}],"surfaces":[{"id":"light","mode":"MODE-STANDARD","reference_tokens":{"surface":"D035/palette/paper","text":"D035/palette/ink"}},{"id":"dark","mode":"MODE-STANDARD","reference_tokens":{"surface":"D035/palette/ink","text":"D035/palette/white"}},{"id":"forced-colours-specimen","mode":"MODE-FORCED-COLORS","implementation_roles":["Canvas","CanvasText","ButtonFace","ButtonText","LinkText","Highlight","HighlightText"],"limit":"Editable appearance and semantic role annotations only; actual OS/browser forced-colours mapping and behavior require later runtime evidence"}],"streams":[{"id":"S-HIGH","label":"Detailed 3D"},{"id":"S-MEDIUM","label":"Balanced 3D"},{"id":"S-LOW","label":"Simplified 3D"},{"id":"S-SEMANTIC","label":"Quick Access"}],"profile":{"profile_id":"SP-SYSTEM-RECOVERY","dimension":"state","applies_to":"Shared system status and recovery presentation","required_values":"STATE-LOADING;STATE-DEGRADED;STATE-EMPTY;STATE-PENDING;STATE-UNAVAILABLE;STATE-OFFLINE;STATE-ERROR;STATE-PERMISSION-DENIED;STATE-SESSION-EXPIRED;STATE-STALE;STATE-CONFLICT;STATE-ASSET-FAILURE;STATE-CHECKSUM-MISMATCH;STATE-FOCUS;STATE-STREAM-CHANGED;STATE-PREFERENCE-WRITE-FAILED","minimum_evidence":"Reusable focused frames for each class on light/dark/forced-color surfaces; route/flow host retains context","critical_distinct_frame_values":"STATE-PENDING;STATE-UNAVAILABLE;STATE-OFFLINE;STATE-ERROR;STATE-PERMISSION-DENIED;STATE-CHECKSUM-MISMATCH;STATE-STREAM-CHANGED;STATE-PREFERENCE-WRITE-FAILED","annotation_requirements":"What happened; what was preserved; authoritative state; smallest safe action; status semantics; no provider/secret/PII leakage","exception_rule":"This profile supplements rather than replaces a host template state profile","browser_profile":"BP-NFR-006","time_limit_branch":"TL-WARN-EXTEND"},"source_hashes":[{"path":"docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md","sha256":"fa3322d864dc8c29d2f7853d6dc9a961126f7a8aea2b575505997d05c3297064","matches_historical_fixture_input":true},{"path":"docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv","sha256":"deb91325e1c8a543878111883f5b1203ae9e5dc35c00e0d837e927786eaf47e2","matches_historical_fixture_input":false},{"path":"docs/phase-1-ui-reference-design/reference-template-inventory.csv","sha256":"62b11bf2ea7bd1f168ecaa01a0da5914107ba072670328f52c13c0fbdbb5bacb","matches_historical_fixture_input":true},{"path":"docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md","sha256":"88e573ff4d07dc1c3c257e05d537d6857a5940fb2fc6493a4cae787b1317252b","matches_historical_fixture_input":false},{"path":"docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md","sha256":"40a3779f56737725bb2c5e5d5a5ee34b44ad27030adc16cc374fdb9b04266a12","matches_historical_fixture_input":false},{"path":"docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md","sha256":"0bf065ae353f1d22c986501c624df46e4057d76ca06f71a35352360ac239a6b7","matches_historical_fixture_input":false},{"path":"output/research/b01-navigation-composition-2026-10-06/state-ledger.json","sha256":"f078e20b6fca5deec68a8876d83922d03064036aa797fb719cd6cae6d594da2b","matches_historical_fixture_input":true}],"external_calls":0,"limitations":["State language is proposed synthetic copy; no real service, record, staff availability, account existence, admission, cache, storage, retry, permission or restoration is claimed","Unknown/pending business outcomes must reconcile the same operation, not reuse a generic fresh retry","Anonymous recovery must not invent Microsoft/staff sign-in; accepted staff expiry remains a separate profile","Every class needs its own light/dark/forced-colour reference under the accepted profile; deduplication must name each applicable stream/profile without losing an obligation","Exact copy, token bindings, prototype, narrow/landscape/desktop/400% evidence, primitive states, independent review, export/restore/EXIT and founder pilot acceptance remain","Prepared successor only; source review and immediate scoped call permission/allowance required. No new Figma nodes claimed.","Historical fixture hashes are preserved separately. Current file identities do not establish independent re-review of all current source documents.","48 narrow shared grammar specimens supplement host coverage. Focus rings, forced-colours execution and complete-process behavior remain separate obligations."],"historical_fixture_source_hashes":[{"path":"docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md","sha256":"fa3322d864dc8c29d2f7853d6dc9a961126f7a8aea2b575505997d05c3297064"},{"path":"docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv","sha256":"6fa43937ae5e590b31e4fc21ea9e1209d3bfcdf145a6698d2429125213166dec"},{"path":"docs/phase-1-ui-reference-design/reference-template-inventory.csv","sha256":"62b11bf2ea7bd1f168ecaa01a0da5914107ba072670328f52c13c0fbdbb5bacb"},{"path":"docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md","sha256":"fafea73bdcedcf3057d504b98514f5796b331bf0184d30d10a165aae754e336f"},{"path":"docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md","sha256":"2b543fbf8c00e244f705d0931bacb76f8a2405d2bbb9bb4e1593a28fa86d87f8"},{"path":"docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md","sha256":"21833e0bf533d88243e3da34be6f7f2ca401c3401a907c719c58a4fcb2196fbf"},{"path":"output/research/b01-navigation-composition-2026-10-06/state-ledger.json","sha256":"f078e20b6fca5deec68a8876d83922d03064036aa797fb719cd6cae6d594da2b"}],"fileKey":"GOmLP6Cv96l768ueSrZ5Dg","streamMasters":[{"state_id":"STATE-PREFERENCE-WRITE-FAILED","stream_id":"S-SEMANTIC","selected_stream_id":"S-SEMANTIC","id":"21:204","name":"State=PREFERENCE-WRITE-FAILED, Stream=SEMANTIC"},{"state_id":"STATE-STREAM-CHANGED","stream_id":"S-SEMANTIC","selected_stream_id":"S-SEMANTIC","id":"21:272","name":"State=STREAM-CHANGED, Stream=SEMANTIC"}],"capture":{"planned_images":5,"tiles_per_sheet":[10,10,10,10,8],"scale":1,"max_width":3600,"max_height":2400,"max_created_nodes":5000,"max_receipt_utf8":19000,"actual_count_and_native_dimensions_require_result_inspection":true}};
if (!input || input.product !== 'Hengshi Design v1' || input.states.length !== 16 || input.surfaces.length !== 3) throw Error('Changed recovery scope');
if (figma.editorType !== 'figma' || (figma.fileKey && figma.fileKey !== input.fileKey)) throw Error('Wrong file/editor');
const page = await figma.getNodeByIdAsync('0:1');
if (!page || page.type !== 'PAGE' || figma.root.children.length !== 1) throw Error('Changed page context');
await figma.setCurrentPageAsync(page);
const rootName = 'B01 / Shared recovery specimens / v1';
if (page.findOne(n => n.name === rootName)) throw Error('Existing or partial recovery composition; inspect before any retry');
const navigation = await figma.getNodeByIdAsync('21:290');
const streamSet = await figma.getNodeByIdAsync('21:289');
const actionMaster = await figma.getNodeByIdAsync('14:18');
if (!navigation || navigation.type !== 'FRAME' || navigation.parent !== page ||
    !streamSet || streamSet.type !== 'COMPONENT_SET' || streamSet.children.length !== 16 ||
    !actionMaster || actionMaster.type !== 'COMPONENT' || actionMaster.parent?.type === 'COMPONENT_SET') throw Error('Changed inherited checkpoint');
const actionLabel = Object.keys(actionMaster.componentPropertyDefinitions).find(k => k.startsWith('Label#'));
if (!actionLabel || actionMaster.componentPropertyDefinitions[actionLabel].type !== 'TEXT') throw Error('Missing inherited text action label');
const masters = new Map();
for (const record of input.streamMasters) {
  const node = await figma.getNodeByIdAsync(record.id);
  if (!node || node.type !== 'COMPONENT' || node.parent !== streamSet || node.name !== record.name) throw Error('Changed stream master');
  masters.set(record.state_id, node);
}
if (masters.size !== 2 || !masters.has('STATE-STREAM-CHANGED') || !masters.has('STATE-PREFERENCE-WRITE-FAILED')) throw Error('Changed recovery stream scope');
const styles = {}, colours = {}, spaces = {};
const localStyles = await figma.getLocalTextStylesAsync();
for (const role of ['heading','body','meta']) {
  const matches = localStyles.filter(s => s.name === 'B01 reference / ' + role);
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited text style');
  styles[role] = matches[0];
}
const fontInputs = [...Object.values(styles).map(s => s.fontName),
  ...[actionMaster,...masters.values()].flatMap(m => m.findAllWithCriteria({types:['TEXT']}).flatMap(n => n.getStyledTextSegments(['fontName']).map(s => s.fontName)))];
for (const font of new Map(fontInputs.map(f => [f.family+'/'+f.style,f])).values()) await figma.loadFontAsync(font);
const localColours = await figma.variables.getLocalVariablesAsync('COLOR');
const localFloats = await figma.variables.getLocalVariablesAsync('FLOAT');
for (const name of ['ink','paper','white','mist']) {
  const matches = localColours.filter(v => v.name === 'D035/palette/' + name);
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited colour');
  colours[name] = matches[0];
}
for (const [number,value] of [4,8,12,16,24,32,48,64,96].entries()) {
  const matches = localFloats.filter(v => v.name === 'D035/space/' + (number+1));
  if (matches.length !== 1) throw Error('Missing or ambiguous inherited spacing');
  spaces[value] = matches[0];
}
const collection = (await figma.variables.getLocalVariableCollectionsAsync()).find(c => c.id === colours.ink.variableCollectionId);
if (!collection || Object.values(colours).some(v => v.variableCollectionId !== collection.id)) throw Error('Changed palette collection');
for (const v of Object.values(colours)) {
  const value = v.valuesByMode[collection.defaultModeId];
  if (!value || !['r','g','b'].every(k => Number.isFinite(value[k]) && value[k]>=0 && value[k]<=1)) throw Error('Invalid direct colour');
}
for (const [value,v] of Object.entries(spaces)) if (v.variableCollectionId !== collection.id || v.valuesByMode[collection.defaultModeId] !== Number(value)) throw Error('Changed spacing value');
if(page.children.some(n=>n.name.startsWith('HSD_UIR_B01_TEMP_GRAMMAR_CAPTURE_')))throw Error('Previous temporary grammar sheet remains; inspect before retry');
const preservationFingerprint=node=>JSON.stringify([node,...('findAll' in node?node.findAll(()=>true):[])].map((n,i)=>({type:n.type,name:n.name,visible:n.visible,opacity:n.opacity,x:i===0?null:n.x,y:i===0?null:n.y,width:n.width,height:n.height,rotation:n.rotation,text:n.type==='TEXT'?n.characters:null})));
const inheritedNodes=page.children.slice();
const inheritedBefore=inheritedNodes.map(preservationFingerprint);
const inheritedPositions=inheritedNodes.map(n=>[n.x,n.y]);
const inheritedPageOrder=page.children.map(n=>n.id).join('|');
// No canvas construction occurs before the guards above complete.
const rightEdge = Math.max(0,...page.children.map(n => n.x+n.width));
const paint = name => {
  const value = colours[name].valuesByMode[collection.defaultModeId];
  return figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:value.r,g:value.g,b:value.b}},'color',colours[name]);
};
function stack(parent,name,width,background) {
  const node = figma.createAutoLayout('VERTICAL'); node.name = name;
  node.resize(width,100); node.primaryAxisSizingMode='AUTO'; node.counterAxisSizingMode='FIXED'; node.clipsContent=false;
  node.fills=[paint(background)];
  for (const key of ['paddingTop','paddingRight','paddingBottom','paddingLeft']) {node[key]=24;node.setBoundVariable(key,spaces[24]);}
  node.itemSpacing=16; node.setBoundVariable('itemSpacing',spaces[16]);
  if (parent) parent.appendChild(node); else page.appendChild(node);
  return node;
}
async function text(parent,value,role='body',foreground='ink') {
  const node=figma.createText(); node.fontName=styles[role].fontName;
  await node.setTextStyleIdAsync(styles[role].id); node.characters=value; parent.appendChild(node);
  node.resize(Math.max(1,parent.width-parent.paddingLeft-parent.paddingRight),24);
  node.textAutoResize='HEIGHT'; node.layoutSizingHorizontal='FILL'; node.layoutSizingVertical='HUG';node.fills=[paint(foreground)];
  return node;
}
const root=stack(null,rootName,440,'mist');root.x=rightEdge+400;root.y=400;
await text(root,'SHARED RECOVERY GRAMMAR — v1','heading');
await text(root,'REFERENCE FIXTURES — NOT PUBLIC COPY. Sixteen shared states on three annotated surfaces; not complete pages or full stream/profile coverage.','meta');
const frames=[],annotations=[];
for (const surface of input.surfaces) {
  const dark=surface.id==='dark'; const background=dark?'ink':surface.id==='forced-colours-specimen'?'white':'paper'; const foreground=dark?'white':'ink';
  for (const state of input.states) {
    const frame=stack(root,'B01 shared recovery / '+state.id+' / '+surface.id+' / v1',320,background);
    await text(frame,'REFERENCE FIXTURE — NOT PUBLIC COPY','meta',foreground);
    await text(frame,state.title,'heading',foreground);await text(frame,state.body,'body',foreground);
    const action=actionMaster.createInstance();frame.appendChild(action);action.setProperties({[actionLabel]:state.action});
    if (['STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED'].includes(state.id)) {
      const instance=masters.get(state.id).createInstance();frame.appendChild(instance);instance.resize(272,Math.max(1,instance.height));
    }
    frames.push({node:frame,state,surface});
    const note=stack(root,'ANNOTATION / '+state.id+' / '+surface.id,320,'paper');
    await text(note,'Preserved truth: '+state.truth,'meta');
    await text(note,'Smallest safe action: '+state.action_kind+'. Appearance only; no route, request, permission, retry, storage or sign-in is executed.','meta');
    await text(note,'Shared grammar applies to '+input.streams.map(s => s.id).join(', ')+'. Each host still needs its own contracted stream/state, context, input, focus, viewport and complete-process evidence. No evidence obligation is deduplicated by this specimen.','meta');
    await text(note,'Status announcement semantics, live-region urgency and focus restoration require host-specific reference and browser evidence. These visual specimens do not execute announcements or move focus.','meta');
    if (state.held) await text(note,state.held,'meta');
    if (surface.id==='forced-colours-specimen') await text(note,'OS system roles: '+surface.implementation_roles.join(', ')+'. This editable token-colour specimen does not execute forced-colours or bind OS colours. Later host/browser evidence must prove actual system roles and visibility.','meta');
    if (state.id==='STATE-FOCUS') await text(note,'The label is an annotation; an actual focus-visible ring, keyboard activation and focus order remain separate host/primitive evidence. This frame is not counted as executed focus coverage.','meta');
    if (['STATE-STREAM-CHANGED','STATE-PREFERENCE-WRITE-FAILED'].includes(state.id)) await text(note,'Inherited Quick Access stream instance carries accepted D-057 notice copy. Other stream host instances and their preserved context remain separate; selection alone never applies.','meta');
    annotations.push(note.id);
  }
}
const boundsFindings=[];
for (const {node:frame} of frames) for (const node of frame.findAll(n => n.type==='TEXT'||n.type==='INSTANCE')) {
  if (![node.width,node.height].every(v => Number.isFinite(v)&&v>0)) boundsFindings.push({id:node.id,issue:'invalid bounds'});
  const parent=node.parent;
  if (parent && 'width' in parent && node.x+node.width>parent.width+1) boundsFindings.push({id:node.id,issue:'horizontal overflow',parentId:parent.id});
}
// Report-only lossless encoding. Every node ID is represented; no canvas mutation here.
function packIds(ids) {
  const byPrefix = new Map(), literalIds = [];
  for (const id of [...new Set(ids)]) {
    const match = /^(.*:)(0|[1-9][0-9]*)$/.exec(id);
    if (!match || !Number.isSafeInteger(Number(match[2]))) { literalIds.push(id); continue; }
    if (!byPrefix.has(match[1])) byPrefix.set(match[1], []);
    byPrefix.get(match[1]).push(Number(match[2]));
  }
  const groups = [...byPrefix.entries()].map(([prefix, suffixes]) => {
    suffixes.sort((a,b)=>a-b);
    const ranges = [];
    for (const suffix of suffixes) {
      const last = ranges[ranges.length-1];
      if (last && suffix === last[last.length-1]+1) {
        if (last.length===1) last.push(suffix); else last[1]=suffix;
      } else ranges.push([suffix]);
    }
    return [prefix,ranges.map(r=>r.length===1?r[0]:r)];
  });
  const decoded = literalIds.slice();
  for (const [prefix,ranges] of groups)
    for (const range of ranges) {
      if (typeof range==='number') decoded.push(prefix+range);
      else for (let n=range[0];n<=range[1];n++) decoded.push(prefix+n);
    }
  const expected = [...new Set(ids)].sort();
  if (JSON.stringify(decoded.sort())!==JSON.stringify(expected)) throw Error('Lossless ID report mismatch');
  return {encoding:'prefix-inclusive-ranges-v1',count:expected.length,groups,literalIds};
}

const groups=new Map();
for(const finding of boundsFindings){
 const context=JSON.stringify([finding.issue,finding.parentId??null]);
 if(!groups.has(context))groups.set(context,[]);
 groups.get(context).push(finding.id);
}
const report={
 createdNodeIds:packIds([root.id,...root.findAll(()=>true).map(n=>n.id)]),
 mutatedNodeIds:[page.id],createdComponentIds:[],createdVariableIds:[],createdStyleIds:[],rootId:root.id,
 frameFields:['id','stateIndex','surfaceIndex','width','height'],
 frames:frames.map(f=>[f.node.id,input.states.indexOf(f.state),input.surfaces.indexOf(f.surface),f.node.width,f.node.height]),
 annotationIds:packIds(annotations),boundsFindingCount:boundsFindings.length,
 boundsFindings:[...groups].map(([key,ids])=>({context:JSON.parse(key),nodeIds:packIds(ids)})),
 B01Complete:false,coveredScope:'48 shared narrow recovery grammar specimens only',limitations:input.limitations,
 reportFormat:'recovery-ordinals-and-lossless-ids-v1'
};
const reportBytes=encodeURIComponent(JSON.stringify(report)).match(/%[0-9A-F]{2}|[^%]/g).length;
if(reportBytes>19000)throw Error('Recovery report '+reportBytes+' bytes exceeds local19000-byte guard; inspect any uncertain partial canvas before retry');
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
