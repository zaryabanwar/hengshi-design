// Preparation only. No provider invocation is authorized by this file.
// EXPECTED is injected from the frozen census and the reviewed D094 recipe.
const assert = (condition, message) => { if (!condition) throw Error(message); };
const clone = value => JSON.parse(JSON.stringify(value));
const walk = node => [node, ...('children' in node ? node.children.flatMap(walk) : [])];
const reactions = node => 'reactions' in node ? clone(node.reactions) : [];
const captions = {HIGH:'Detailed 3D',MEDIUM:'Balanced 3D',LOW:'Simplified 3D',SEMANTIC:'Quick Access'};
const tupleKey = tuple => tuple.join('/');
const triggerFor = edge => edge.trigger === 'KEY_ESCAPE'
  ? {type:'ON_KEY_DOWN',device:'KEYBOARD',keyCodes:[27]} : {type:'ON_CLICK'};
const desiredReaction = (edge, destinationId) => ({trigger:triggerFor(edge),actions:[{
  type:'NODE',destinationId,navigation:'CHANGE_TO',transition:null
}]});
const stable = value => Array.isArray(value) ? value.map(stable) : value && typeof value === 'object'
  ? Object.fromEntries(Object.keys(value).sort().map(key => [key,stable(value[key])])) : value;
const exact = (actual, expected) => JSON.stringify(stable(actual)) === JSON.stringify(stable(expected));
const canonicalAction = a => a.type === 'NODE' ? ({...a,
  resetVideoPosition:a.resetVideoPosition ?? false,resetScrollPosition:a.resetScrollPosition ?? false,
  resetInteractiveComponents:a.resetInteractiveComponents ?? false,preserveScrollPosition:a.preserveScrollPosition ?? false
}) : a;
const canonicalReaction = r => {
  const result = {...r,actions:(r.actions || []).map(canonicalAction)};
  // Official readback may include the deprecated single-action alias as well.
  // Remove only a fully equivalent redundant alias; retain conflicting values.
  if (result.actions.length === 1 && r.action && exact(canonicalAction(r.action),result.actions[0])) delete result.action;
  return result;
};
const equivalent = (actual, expected) => exact(actual.map(canonicalReaction),expected.map(canonicalReaction));
const asciiError = error => String(error).replace(/[^\x20-\x7e]/g,'?').slice(0,180);
const reportBytes = value => {
  const forms = [JSON.stringify(value),JSON.stringify(value,null,2),JSON.stringify(JSON.stringify(value))];
  return Math.max(...forms.map(s => [...s].reduce((n,c) => n+(c.codePointAt(0)<128?1:c.codePointAt(0)<2048?2:c.codePointAt(0)<65536?3:4),0)));
};
const failureReport = (error, plans, unresolved) => ({product:'Hengshi Design v1',status:'DOING',
  result:plans.length ? (unresolved.length?'ROLLBACK_INCOMPLETE':'ROLLED_BACK') : 'ABORTED_PREFLIGHT',
  error:asciiError(error),createdNodeIds:[],mutatedNodeIds:plans.map(p=>p.node.id),unresolved,
  limits:'No automatic retry. Inspect partial results before further action. No native behavior or B01/Phase1 verdict.'});
const visualFields = ['id','type','name','x','y','width','height','rotation','visible','opacity',
  'fills','strokes','effects','fillStyleId','strokeStyleId','effectStyleId','boundVariables',
  'componentProperties','variantProperties','characters','fontName','fontSize','textStyleId',
  'lineHeight','letterSpacing','textAutoResize','layoutMode','clipsContent','overflowDirection'];
function visualSnapshot(root, includeReactions) {
  return JSON.stringify(walk(root).map(n => {
    const row = {parent:n.parent?.id,children:'children' in n ? n.children.map(c => c.id) : []};
    for (const key of visualFields) if (key in n) row[key] = typeof n[key] === 'symbol' ? 'MIXED' : n[key];
    if (includeReactions && 'reactions' in n) row.reactions = n.reactions;
    return row;
  }));
}
function ownChild(parent, name, type) {
  const matches = parent.children.filter(n => n.name === name && n.type === type);
  assert(matches.length === 1, 'Missing or ambiguous owned child: '+parent.id+' '+name);
  return matches[0];
}
function buttonCaption(node, expected) {
  assert(node.type === 'INSTANCE', 'Action is not an instance: '+node.id);
  const props = Object.entries(node.componentProperties).filter(([key,p]) => key.split('#')[0] === 'Label' && p.type === 'TEXT');
  assert(props.length === 1 && props[0][1].value === expected, 'Effective Label drift: '+node.id);
  const texts = walk(node).filter(n => n.type === 'TEXT');
  assert(texts.length === 1 && texts[0].characters === expected, 'Rendered Label drift: '+node.id);
}
let page, section, set, protectedBefore, ownedVisualBefore;
const rows = [], controls = new Map(), nodePlans = new Map(), attempted = [];
let report;
try {
  assert(figma.editorType === 'figma' && figma.fileKey === EXPECTED.fileKey, 'Wrong editor/file');
  page = await figma.getNodeByIdAsync(EXPECTED.page);
  assert(page?.type === 'PAGE' && page.name === 'Page 1', 'Wrong page');
  await figma.setCurrentPageAsync(page);
  figma.skipInvisibleInstanceChildren = false;
  section = await figma.getNodeByIdAsync(EXPECTED.section);
  set = await figma.getNodeByIdAsync(EXPECTED.set);
  assert(section?.type === 'SECTION' && section.parent?.id === page.id, 'Wrong owned section');
  assert(section.name === 'B01 / Four-stream three-host qualification / v1', 'Section name drift');
  assert(set?.type === 'COMPONENT_SET' && set.parent?.id === section.id && set.name === 'B01 qualification / DIRECTORY / v1', 'Wrong family set');
  assert(set.children.length === 32 && set.children.every(n => EXPECTED.roots.some(r => r.id === n.id)), 'Member census drift');
  protectedBefore = JSON.stringify(page.children.filter(n => n.id !== section.id).map(n => visualSnapshot(n,true)));
  ownedVisualBefore = visualSnapshot(section,false);
  const rootMap = new Map();
  for (const expected of EXPECTED.roots) {
    const root = await figma.getNodeByIdAsync(expected.id);
    assert(root?.type === 'COMPONENT' && root.parent?.id === set.id, 'Wrong variant owner');
    const v = root.variantProperties;
    assert(tupleKey([v.Active,v.Pending,v.Disclosure]) === tupleKey(expected.tuple), 'Tuple drift: '+root.id);
    assert(root.width === 320 && root.height === 1150 && root.children.length === 5 && walk(root).length === 22, 'Anatomy/geometry drift: '+root.id);
    const [active,pending,disclosure] = expected.tuple;
    const context = ownChild(root,'Context summary / fixed Services fixture','TEXT');
    assert(context.characters === expected.context, 'Context drift');
    const marker = ownChild(root,'Trial scroll marker','TEXT');
    assert(marker.characters === 'Trial scroll marker', 'Scroll marker drift');
    const under = ownChild(root,'Underlying Services fixture (unwired while modal open)','INSTANCE');
    buttonCaption(under,'Services (fixture)');
    const menu = ownChild(root,'Menu action','INSTANCE');
    buttonCaption(menu,disclosure === 'OPEN' ? 'Close directory' : 'Open directory');
    const body = ownChild(root,'PRIM-001 / Delivery stream control / B01 v1','FRAME');
    assert(body.visible === (disclosure === 'OPEN') && body.children.length === 9, 'Disclosure/body drift');
    const legend = body.children.filter(n => n.type === 'TEXT' && n.characters === 'Delivery stream — currently '+captions[active]);
    assert(legend.length === 1, 'In-force legend drift');
    for (const text of EXPECTED.bodyCopy) assert(body.children.filter(n => n.type === 'TEXT' && n.characters === text).length === 1, 'D057 body copy drift');
    const roleMap = new Map([['owned host',root],['Open',menu],['Close',menu]]);
    for (const mode of Object.keys(captions)) {
      const choice = ownChild(body,'Native-radio appearance reference / S-'+mode,'FRAME');
      assert(choice.children.length === 1 && choice.children[0].type === 'TEXT', 'Choice anatomy drift');
      assert(choice.children[0].characters === (pending === mode ? '● ' : '○ ')+captions[mode], 'Pending glyph drift');
      roleMap.set('choose/'+mode,choice);
    }
    const apply = ownChild(body,'PRIM-015 / General action button / base','INSTANCE');
    buttonCaption(apply,'Apply selection');
    roleMap.set('Apply selection',apply);
    const symbol = 'DIRECTORY/'+tupleKey(expected.tuple);
    rootMap.set(symbol,root);
    controls.set(symbol,roleMap);
    rows.push({root:root.id,symbol,descendants:walk(root).length-1});
  }
  for (const edge of EXPECTED.edges) {
    assert(edge.action === 'CHANGE_TO' && ['ON_CLICK','KEY_ESCAPE'].includes(edge.trigger), 'Unapproved action');
    const owner = rootMap.get(edge.source), target = rootMap.get(edge.destination);
    const control = controls.get(edge.source)?.get(edge.control);
    assert(owner && target && control && target.parent?.id === set.id && walk(owner).some(n => n.id === control.id), 'Cross-owner edge');
    assert(typeof control.setReactionsAsync === 'function' && !nodePlans.has(control.id), 'Unsupported/shared control');
    assert(/^[0-9]{1,12}:[0-9]{1,12}$/.test(control.id), 'Unexpected control ID format/size');
    nodePlans.set(control.id,{node:control,owner:owner.id,before:reactions(control),after:[desiredReaction(edge,target.id)],edge,target:target.id});
  }
  assert(nodePlans.size === 108, 'Expected 108 distinct single-action controls');
  assert(EXPECTED.preExisting.length === 0, 'Expected empty Directory reaction baseline');
  const previouslyWired = new Map(EXPECTED.preExisting.map(e=>[e.id,e.target]));
  for (const existing of EXPECTED.preExisting) {
    const p = nodePlans.get(existing.id);
    assert(p && p.owner === existing.sourceRoot && p.edge.source === existing.source && p.edge.control === existing.control && p.edge.trigger === existing.trigger, 'Unexpected pre-existing binding');
  }
  for (const n of walk(set)) {
    const current = reactions(n), planned = nodePlans.get(n.id);
    if (previouslyWired.has(n.id)) {
      assert(planned && planned.target === previouslyWired.get(n.id) && equivalent(current,planned.after), 'Unexpected Directory baseline reaction');
    } else assert(current.length === 0, 'Unexpected inherited/current reaction: '+n.id);
  }
  const mutations = [...nodePlans.values()].filter(p => !previouslyWired.has(p.node.id));
  assert(mutations.length === 108, 'Expected 108 new control reactions');
  report = {product:'Hengshi Design v1',status:'DOING',result:'APPLIED',createdNodeIds:[],mutatedNodeIds:mutations.map(p => p.node.id),
    page:page.id,section:section.id,set:set.id,variants:rows.map(r=>[r.root,...r.symbol.split('/').slice(1)]),
    roleLegend:[...new Set(EXPECTED.edges.map(e=>e.control))],
    edges:[...nodePlans.values()].map(p => [p.owner,[...new Set(EXPECTED.edges.map(e=>e.control))].indexOf(p.edge.control),p.node.id,p.target]),
    preExistingEdgesUnchanged:0,newEdges:108,totalSameSetEdges:108,
    visualStructureUnchanged:true,protectedOutsideSectionUnchanged:true,
    limits:'Directory same-set reactions only. No boundary frames/probes or reset behavior, Navigation/Recovery, native behavior verdict, source restore or B01/Phase1 acceptance.'};
  assert(reportBytes(report) < 18000, 'Success report exceeds safe limit');
  const worstFailure = failureReport('x'.repeat(180),mutations,mutations.map(p=>({id:p.node.id,code:'CONCURRENT_OR_RESTORE_FAILURE'})));
  assert(reportBytes(worstFailure) < 18000, 'Failure report exceeds safe limit');
  for (const p of mutations) {
    assert(p.node.parent && walk(await figma.getNodeByIdAsync(p.owner)).some(n => n.id === p.node.id), 'Concurrent ownership drift');
    assert(JSON.stringify(reactions(p.node)) === JSON.stringify(p.before), 'Concurrent reaction drift');
    attempted.push(p);
    await p.node.setReactionsAsync(clone(p.after));
    const observed = reactions(p.node);
    assert(equivalent(observed,p.after), 'Reaction write mismatch');
    p.afterActual = clone(observed);
  }
  for (const n of walk(set)) {
    const expected = nodePlans.get(n.id)?.after || [];
    assert(equivalent(reactions(n),expected), 'Unexpected post-write reaction: '+n.id);
  }
  assert(visualSnapshot(section,false) === ownedVisualBefore, 'Owned visual/content structure changed');
  assert(JSON.stringify(page.children.filter(n => n.id !== section.id).map(n => visualSnapshot(n,true))) === protectedBefore, 'Protected content changed');
  return report;
} catch (error) {
  const unresolved = [];
  for (const p of [...attempted].reverse()) {
    try {
      const now = reactions(p.node);
      if (p.afterActual ? exact(now,p.afterActual) : equivalent(now,p.after)) await p.node.setReactionsAsync(clone(p.before));
      else assert(exact(now,p.before), 'Concurrent reaction cannot be overwritten');
      assert(exact(reactions(p.node),p.before), 'Rollback mismatch');
    } catch (rollbackError) { unresolved.push({id:p.node.id,code:'CONCURRENT_OR_RESTORE_FAILURE'}); }
  }
  return failureReport(error,attempted,unresolved);
}
