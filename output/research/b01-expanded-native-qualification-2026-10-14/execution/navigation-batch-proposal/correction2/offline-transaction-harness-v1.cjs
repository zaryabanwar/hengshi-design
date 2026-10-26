// Synthetic Plugin API boundary harness; this is not Figma/provider or product evidence.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const base = __dirname;
const expected = JSON.parse(fs.readFileSync(path.join(base,'expected-scope-v1.json'),'utf8'));
const body = fs.readFileSync(path.join(base,'batch-body-v1.js'),'utf8');
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
const run = new AsyncFunction('figma','EXPECTED',body);
const copy = o => JSON.parse(JSON.stringify(o));
function fixture(options={}) {
  const all = new Map(); let sequence=0, writes=0, injected=false;
  const node = (type,name,id,extra={}) => {
    const n = {id:id||'900:'+ ++sequence,type,name,parent:null,children:[],x:0,y:0,width:320,height:1150,
      visible:true,opacity:1,reactions:[],...extra};
    if(options.dualReadback || options.dualAfterWrite || options.conflictingAlias) {
      let stored=[];
      Object.defineProperty(n,'reactions',{enumerable:true,get:()=>stored.map(r=>{
        if(!r.actions?.length || (options.dualAfterWrite && !writes))return copy(r);
        return {...copy(r),action:options.conflictingAlias?{type:'BACK'}:copy(r.actions[0])};
      }),set:value=>{stored=copy(value);}});
    }
    n.setReactionsAsync = async value => {
      writes++;
      if (options.rollbackFailures && injected) throw Error('恢復錯誤'.repeat(300));
      n.reactions=copy(value);
      if (options.failAfter===writes && !injected) {
        injected=true;
        if(options.concurrent) n.reactions=[{trigger:{type:'ON_CLICK'},actions:[{type:'BACK'}]}];
        if(options.concurrentFlag) n.reactions[0].actions[0].resetInteractiveComponents=true;
        throw Error('Injected setter interruption');
      }
    };
    all.set(n.id,n); return n;
  };
  const attach = (p,n) => {p.children.push(n);n.parent=p;return n;};
  const text = (p,name,characters) => attach(p,node('TEXT',name,null,{characters,fontName:{family:'Inter',style:'Regular'},fontSize:16,textStyleId:'fixture-style',children:[]}));
  const button = (p,name,label,id) => {
    const b=attach(p,node('INSTANCE',name,id,{componentProperties:{'Label#fixture':{type:'TEXT',value:label}}}));
    text(b,'Inherited base label',label);return b;
  };
  const page=node('PAGE','Page 1',expected.page);
  const section=attach(page,node('SECTION','B01 / Four-stream three-host qualification / v1',expected.section));
  const set=attach(section,node('COMPONENT_SET','B01 qualification / NAVIGATION / v1',expected.set));
  const protectedNode=attach(page,node('FRAME','Protected original','fixture-protected'));
  text(protectedNode,'Protected original label','Keep');
  const captions={HIGH:'Detailed 3D',MEDIUM:'Balanced 3D',LOW:'Simplified 3D',SEMANTIC:'Quick Access'};
  const roles=new Map();
  for(const item of expected.roots) {
    const [active,pending,disclosure]=item.tuple;
    const root=attach(set,node('COMPONENT','Active='+active+', Pending='+pending+', Disclosure='+disclosure,item.id,{variantProperties:{Active:active,Pending:pending,Disclosure:disclosure}}));
    text(root,'Trial scroll marker','Trial scroll marker');
    text(root,'Context summary / fixed Services fixture','Trial fixture · Services\nIn force '+captions[active]);
    button(root,'Underlying Services fixture (unwired while modal open)','Services (fixture)');
    const menu=button(root,'Menu action',disclosure==='OPEN'?'Close menu':'Menu',root.id==='144:3286'?'144:3280':root.id==='144:3241'?'144:3235':undefined);
    const b=attach(root,node('FRAME','PRIM-001 / Delivery stream control / B01 v1',null,{visible:disclosure==='OPEN'}));
    text(b,'Legend','Delivery stream — currently '+captions[active]);
    const rs={'owned host':root,Open:menu,Close:menu};
    for(const mode of Object.keys(captions)) {
      const c=attach(b,node('FRAME','Native-radio appearance reference / S-'+mode,root.id==='144:3241'&&mode==='MEDIUM'?'144:3225':undefined));
      text(c,'Choice',(mode===pending?'● ':'○ ')+captions[mode]);rs['choose/'+mode]=c;
    }
    for(const value of expected.bodyCopy.slice(0,2))text(b,value,value);
    rs['Apply selection']=button(b,'PRIM-015 / General action button / base','Apply selection');
    text(b,expected.bodyCopy[2],expected.bodyCopy[2]);
    roles.set('NAVIGATION/'+item.tuple.join('/'),rs);
  }
  for(const [control,target] of [['144:3280','144:3241'],['144:3235','144:3286'],['144:3225','147:3271']])all.get(control).reactions=[{trigger:{type:'ON_CLICK'},actions:[{type:'NODE',destinationId:target,navigation:'CHANGE_TO',transition:null}]}];
  if(options.captionDrift)all.get('144:3280').componentProperties['Label#fixture'].value='Different';
  if(options.unexpectedReaction)protectedNode.children[0].reactions=[]; // Outside originals are never changed by this script.
  if(options.unexpectedReaction)roles.get('NAVIGATION/HIGH/HIGH/CLOSED')['choose/LOW'].reactions=[{trigger:{type:'ON_CLICK'},actions:[{type:'BACK'}]}];
  if(options.wrongParent)all.get('144:3241').parent=protectedNode;
  if(options.copyDrift)roles.get('NAVIGATION/HIGH/HIGH/OPEN')['Apply selection'].children[0].characters='Publish';
  const before=new Map([...all.values()].map(n=>[n.id,JSON.stringify(n.reactions)]));
  const api={editorType:'figma',fileKey:expected.fileKey,currentPage:page,
    getNodeByIdAsync:async id=>all.get(id)||null,setCurrentPageAsync:async p=>{api.currentPage=p;}};
  return {api,all,roles,before,writes:()=>writes};
}
(async()=>{
  const results=[];
  for(const [name,options,wanted] of [
    ['complete scoped graph',{},'APPLIED'],
    ['effective caption drift',{captionDrift:true},'ABORTED_PREFLIGHT'],
    ['unexpected hidden reaction',{unexpectedReaction:true},'ABORTED_PREFLIGHT'],
    ['variant owner drift',{wrongParent:true},'ABORTED_PREFLIGHT'],
    ['rendered Apply caption drift',{copyDrift:true},'ABORTED_PREFLIGHT'],
    ['interrupted setter with full restoration',{failAfter:9},'ROLLED_BACK'],
    ['concurrent reaction is not overwritten',{failAfter:9,concurrent:true},'ROLLBACK_INCOMPLETE'],
    ['concurrent optional Action flag is not overwritten',{failAfter:9,concurrentFlag:true},'ROLLBACK_INCOMPLETE'],
    ['all rollback failures preserve IDs within output budget',{failAfter:105,rollbackFailures:true},'ROLLBACK_INCOMPLETE'],
    ['documented dual-field readback',{dualReadback:true},'APPLIED'],
    ['dual-field readback begins after first write',{dualAfterWrite:true},'APPLIED'],
    ['interrupted dual-field write restores safely',{dualReadback:true,failAfter:9},'ROLLED_BACK'],
    ['contradictory action alias denied',{conflictingAlias:true},'ABORTED_PREFLIGHT']
  ]) {
    const f=fixture(options), report=await run(f.api,expected);
    assert.equal(report.result,wanted,name+': '+report.error);
    if(wanted==='ABORTED_PREFLIGHT')assert.equal(f.writes(),0);
    if(wanted==='APPLIED') {
      assert.equal(f.writes(),105);assert.equal(report.totalSameSetEdges,108);
      assert.equal(report.mutatedNodeIds.length,105);assert.ok(Buffer.byteLength(JSON.stringify(report))<18000);
      for(const edge of expected.edges) {
        const c=f.roles.get(edge.source)[edge.control];assert.equal(c.reactions.length,1);
        const target=expected.roots.find(r=>'NAVIGATION/'+r.tuple.join('/')===edge.destination);
        assert.equal(c.reactions[0].actions[0].destinationId,target.id);
        assert.equal(c.reactions[0].actions[0].navigation,'CHANGE_TO');
        assert.equal(c.reactions[0].actions[0].transition,null);
        if(edge.trigger==='KEY_ESCAPE')assert.deepEqual(c.reactions[0].trigger,{type:'ON_KEY_DOWN',device:'KEYBOARD',keyCodes:[27]});
      }
    }
    if(wanted==='ROLLED_BACK')for(const n of f.all.values())assert.equal(JSON.stringify(n.reactions),f.before.get(n.id));
    if(wanted==='ROLLBACK_INCOMPLETE') {
      assert.equal(report.unresolved.length,options.rollbackFailures?105:1);
      if(options.rollbackFailures) {
        assert.equal(report.mutatedNodeIds.length,105);
        assert.deepEqual(new Set(report.unresolved.map(x=>x.id)),new Set(report.mutatedNodeIds));
        assert.ok(report.unresolved.every(x=>x.code==='CONCURRENT_OR_RESTORE_FAILURE'));
        assert.ok(!/[^\x20-\x7e]/.test(JSON.stringify(report)));
      } else {
        const conflict=f.all.get(report.unresolved[0].id);
        if(options.concurrentFlag)assert.equal(conflict.reactions[0].actions[0].resetInteractiveComponents,true);
        else assert.equal(conflict.reactions[0].actions[0].type,'BACK');
        for(const n of f.all.values())if(n!==conflict)assert.equal(JSON.stringify(n.reactions),f.before.get(n.id));
      }
    }
    const serializedBytes=[JSON.stringify(report),JSON.stringify(report,null,2),JSON.stringify(JSON.stringify(report))].map(s=>Buffer.byteLength(s));
    assert.ok(Math.max(...serializedBytes)<18000,name+': output budget');
    results.push({name,result:report.result,writes:f.writes(),newEdges:report.newEdges,reportBytes:serializedBytes,unresolved:report.unresolved?.length||0});
  }
  const out={product:'Hengshi Design v1',status:'DOING',date:'2026-10-15',cases:results,
    limits:'Synthetic Plugin API transaction harness only. No Figma/provider call, capability/auth/quota check, native behavior, application correctness, accessibility or B01/Phase1 verdict.'};
  fs.writeFileSync(path.join(base,'offline-transaction-results-v1.json'),JSON.stringify(out,null,2)+'\n');
  process.stdout.write(JSON.stringify(out,null,2)+'\n');
})().catch(e=>{process.stderr.write(e.stack+'\n');process.exitCode=1;});
