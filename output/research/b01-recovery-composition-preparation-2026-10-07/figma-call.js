// PREPARED ONLY. A new, individually approved Figma call is required.
// Shared status specimens supplement host-template evidence; they cannot replace it.
const input = {"product": "Hengshi Design v1", "status": "DOING", "scope": "Prepared shared recovery composition only; no Figma execution", "template_id": "TPL-SYSTEM-RECOVERY", "states": [{"id": "STATE-LOADING", "title": "Loading optional information", "body": "Confirmed page content remains readable in this fixture. Optional information is not ready.", "truth": "Prior eligible public page only", "action": "Continue reading", "action_kind": "same_document_no_mutation"}, {"id": "STATE-DEGRADED", "title": "Some information is unavailable", "body": "An optional part could not be shown. The current page and public navigation remain available.", "truth": "Current confirmed public page; no stream change", "action": "Open the directory", "action_kind": "public_navigation"}, {"id": "STATE-EMPTY", "title": "No items in this view", "body": "This is an approved empty view in the reference fixture, not an error or an invented case study.", "truth": "Confirmed empty collection in the fixture", "action": "Browse services", "action_kind": "canonical_link"}, {"id": "STATE-PENDING", "title": "The outcome is not confirmed", "body": "This request is still being checked. Do not repeat it as a new action until its existing outcome is reconciled.", "truth": "Last confirmed record; pending is not success", "action": "Check this request", "action_kind": "same_operation_reconciliation_method_held"}, {"id": "STATE-UNAVAILABLE", "title": "This action is unavailable", "body": "No new action was accepted in this fixture. Public information remains available.", "truth": "Confirmed unavailability, not live staff status", "action": "Browse services", "action_kind": "canonical_link"}, {"id": "STATE-OFFLINE", "title": "Connection unavailable", "body": "No fresh action or new content is confirmed while disconnected. The visible prior view makes no promise of offline storage.", "truth": "Visible prior truth only; fresh availability unknown", "action": "Check connection again", "action_kind": "bounded_connectivity_read_no_redispatch"}, {"id": "STATE-ERROR", "title": "The action did not complete", "body": "This fixture represents a confirmed failure before a business action was admitted; it is not an unknown outcome.", "truth": "Prior authoritative state; no successful new action", "action": "Return to the current page", "action_kind": "same_document_no_mutation"}, {"id": "STATE-PERMISSION-DENIED", "title": "Private information is unavailable", "body": "This access is not permitted. No private details or record-existence clues are shown.", "truth": "Public location only; no permission grant", "action": "Open the public website", "action_kind": "canonical_link"}, {"id": "STATE-SESSION-EXPIRED", "title": "Private access has expired", "body": "Public pages remain available. Opening retained private work requires current verified access; this fixture does not restore it.", "truth": "Last confirmed public context; permitted private state follows its separate lifecycle", "action": "Open the public website", "action_kind": "canonical_link", "held": "Exact anonymous restoration, accessible continuation and duration remain held; do not display a fictitious sign-in or restore mechanism"}, {"id": "STATE-STALE", "title": "This view is out of date", "body": "The last confirmed information is labelled as earlier. Obtain the current eligible view before acting.", "truth": "Earlier confirmed state, not current authority", "action": "Check the current view", "action_kind": "guarded_read_method_held"}, {"id": "STATE-CONFLICT", "title": "The information changed", "body": "No new change is confirmed. Review the current authoritative version before deciding what to do.", "truth": "Current/previous version distinction; no automatic overwrite or retry", "action": "Review the current view", "action_kind": "guarded_read_method_held"}, {"id": "STATE-ASSET-FAILURE", "title": "An optional visual could not load", "body": "The relevant semantic information remains available in this fixture. The in-force delivery stream does not change silently.", "truth": "Eligible public information; failed optional asset is not a closed service", "action": "Open the semantic page", "action_kind": "paired_canonical_link"}, {"id": "STATE-CHECKSUM-MISMATCH", "title": "New content was not verified", "body": "The unverified replacement was not activated. This fixture keeps the prior complete eligible release without mixing content.", "truth": "Prior confirmed release only; candidate remains inactive", "action": "Continue with confirmed content", "action_kind": "same_document_no_mutation"}, {"id": "STATE-FOCUS", "title": "Recovery action in focus", "body": "The action has a visible focus indicator and a text label. This appearance is not executed keyboard evidence.", "truth": "Focus appearance only; no action dispatch", "action": "Open the directory", "action_kind": "public_navigation"}, {"id": "STATE-STREAM-CHANGED", "title": "Presentation choice applied", "body": "Use the exact accepted D-057 notice supplied by the inherited stream component; the location and open context remain.", "truth": "Synthetic confirmed stream change; shared control carries accepted copy", "action": "Continue reading", "action_kind": "same_document_no_mutation"}, {"id": "STATE-PREFERENCE-WRITE-FAILED", "title": "Presentation applied for this session", "body": "Use the exact accepted D-057 persistence notice supplied by the inherited stream component; saved preference is not confirmed.", "truth": "Session choice applied; persistent write not confirmed", "action": "Continue reading", "action_kind": "same_document_no_mutation"}], "surfaces": [{"id": "light", "mode": "MODE-STANDARD", "reference_tokens": {"surface": "D035/palette/paper", "text": "D035/palette/ink"}}, {"id": "dark", "mode": "MODE-STANDARD", "reference_tokens": {"surface": "D035/palette/ink", "text": "D035/palette/white"}}, {"id": "forced-colours-specimen", "mode": "MODE-FORCED-COLORS", "implementation_roles": ["Canvas", "CanvasText", "ButtonFace", "ButtonText", "LinkText", "Highlight", "HighlightText"], "limit": "Editable appearance and semantic role annotations only; actual OS/browser forced-colours mapping and behavior require later runtime evidence"}], "streams": [{"id": "S-HIGH", "label": "Detailed 3D"}, {"id": "S-MEDIUM", "label": "Balanced 3D"}, {"id": "S-LOW", "label": "Simplified 3D"}, {"id": "S-SEMANTIC", "label": "Quick Access"}], "profile": {"profile_id": "SP-SYSTEM-RECOVERY", "dimension": "state", "applies_to": "Shared system status and recovery presentation", "required_values": "STATE-LOADING;STATE-DEGRADED;STATE-EMPTY;STATE-PENDING;STATE-UNAVAILABLE;STATE-OFFLINE;STATE-ERROR;STATE-PERMISSION-DENIED;STATE-SESSION-EXPIRED;STATE-STALE;STATE-CONFLICT;STATE-ASSET-FAILURE;STATE-CHECKSUM-MISMATCH;STATE-FOCUS;STATE-STREAM-CHANGED;STATE-PREFERENCE-WRITE-FAILED", "minimum_evidence": "Reusable focused frames for each class on light/dark/forced-color surfaces; route/flow host retains context", "critical_distinct_frame_values": "STATE-PENDING;STATE-UNAVAILABLE;STATE-OFFLINE;STATE-ERROR;STATE-PERMISSION-DENIED;STATE-CHECKSUM-MISMATCH;STATE-STREAM-CHANGED;STATE-PREFERENCE-WRITE-FAILED", "annotation_requirements": "What happened; what was preserved; authoritative state; smallest safe action; status semantics; no provider/secret/PII leakage", "exception_rule": "This profile supplements rather than replaces a host template state profile", "browser_profile": "BP-NFR-006", "time_limit_branch": "TL-WARN-EXTEND"}, "source_hashes": [{"path": "docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md", "sha256": "fa3322d864dc8c29d2f7853d6dc9a961126f7a8aea2b575505997d05c3297064", "matches_historical_fixture_input": true}, {"path": "docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv", "sha256": "6fa43937ae5e590b31e4fc21ea9e1209d3bfcdf145a6698d2429125213166dec", "matches_historical_fixture_input": true}, {"path": "docs/phase-1-ui-reference-design/reference-template-inventory.csv", "sha256": "62b11bf2ea7bd1f168ecaa01a0da5914107ba072670328f52c13c0fbdbb5bacb", "matches_historical_fixture_input": true}, {"path": "docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md", "sha256": "fafea73bdcedcf3057d504b98514f5796b331bf0184d30d10a165aae754e336f", "matches_historical_fixture_input": true}, {"path": "docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md", "sha256": "2b543fbf8c00e244f705d0931bacb76f8a2405d2bbb9bb4e1593a28fa86d87f8", "matches_historical_fixture_input": true}, {"path": "docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md", "sha256": "bd75698b8611bcf08d64ef561b6136acd496361a86cf0cde11f341e3ecca5c20", "matches_historical_fixture_input": false}, {"path": "output/research/b01-navigation-composition-2026-10-06/state-ledger.json", "sha256": "f078e20b6fca5deec68a8876d83922d03064036aa797fb719cd6cae6d594da2b", "matches_historical_fixture_input": true}], "external_calls": 0, "limitations": ["State language is proposed synthetic copy; no real service, record, staff availability, account existence, admission, cache, storage, retry, permission or restoration is claimed", "Unknown/pending business outcomes must reconcile the same operation, not reuse a generic fresh retry", "Anonymous recovery must not invent Microsoft/staff sign-in; accepted staff expiry remains a separate profile", "Every class needs its own light/dark/forced-colour reference under the accepted profile; deduplication must name each applicable stream/profile without losing an obligation", "Exact copy, token bindings, prototype, narrow/landscape/desktop/400% evidence, primitive states, independent review, export/restore/EXIT and founder pilot acceptance remain", "Construction script is prepared locally, unexecuted and independently unreviewed. No created Figma nodes are claimed.", "Historical fixture hashes are preserved separately. Current file identities do not establish independent re-review of all current source documents.", "48 narrow shared grammar specimens supplement host coverage. Focus rings, forced-colours execution and complete-process behavior remain separate obligations."], "historical_fixture_source_hashes": [{"path": "docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md", "sha256": "fa3322d864dc8c29d2f7853d6dc9a961126f7a8aea2b575505997d05c3297064"}, {"path": "docs/phase-1-ui-reference-design/responsive-state-mode-matrix.csv", "sha256": "6fa43937ae5e590b31e4fc21ea9e1209d3bfcdf145a6698d2429125213166dec"}, {"path": "docs/phase-1-ui-reference-design/reference-template-inventory.csv", "sha256": "62b11bf2ea7bd1f168ecaa01a0da5914107ba072670328f52c13c0fbdbb5bacb"}, {"path": "docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md", "sha256": "fafea73bdcedcf3057d504b98514f5796b331bf0184d30d10a165aae754e336f"}, {"path": "docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md", "sha256": "2b543fbf8c00e244f705d0931bacb76f8a2405d2bbb9bb4e1593a28fa86d87f8"}, {"path": "docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md", "sha256": "21833e0bf533d88243e3da34be6f7f2ca401c3401a907c719c58a4fcb2196fbf"}, {"path": "output/research/b01-navigation-composition-2026-10-06/state-ledger.json", "sha256": "f078e20b6fca5deec68a8876d83922d03064036aa797fb719cd6cae6d594da2b"}], "fileKey": "GOmLP6Cv96l768ueSrZ5Dg", "streamMasters": [{"state_id": "STATE-PREFERENCE-WRITE-FAILED", "stream_id": "S-SEMANTIC", "selected_stream_id": "S-SEMANTIC", "id": "21:204", "name": "State=PREFERENCE-WRITE-FAILED, Stream=SEMANTIC"}, {"state_id": "STATE-STREAM-CHANGED", "stream_id": "S-SEMANTIC", "selected_stream_id": "S-SEMANTIC", "id": "21:272", "name": "State=STREAM-CHANGED, Stream=SEMANTIC"}]};
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
await frames.find(f => f.state.id==='STATE-PENDING'&&f.surface.id==='light').node.screenshot();
await frames.find(f => f.state.id==='STATE-PERMISSION-DENIED'&&f.surface.id==='dark').node.screenshot();
return {createdNodeIds:[root.id,...root.findAll(()=>true).map(n=>n.id)],mutatedNodeIds:[page.id],createdComponentIds:[],createdVariableIds:[],createdStyleIds:[],rootId:root.id,
  frames:frames.map(f=>({id:f.node.id,name:f.node.name,state:f.state.id,surface:f.surface.id,width:f.node.width,height:f.node.height})),annotationIds:annotations,boundsFindings,
  B01Complete:false,coveredScope:'48 shared narrow recovery grammar specimens only',limitations:input.limitations};
