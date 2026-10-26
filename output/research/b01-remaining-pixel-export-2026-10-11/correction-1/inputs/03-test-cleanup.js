// Synthetic local tooling fault test; no Figma connection or browser evidence.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
const folder = path.resolve(__dirname, '..');
const input = JSON.parse(fs.readFileSync(path.join(folder,'input.json'),'utf8'));

async function run(code, failRemoval=false) {
  const nodes = new Map(), temps = [], removals = [];
  const page = {id:'0:1',type:'PAGE',children:[],appendChild(child){
    if(child.parent)child.parent.children=child.parent.children.filter(n=>n!==child);
    child.parent=this;this.children.push(child);
  }};
  for (const spec of input.parentSpecs) {
    const parent={...spec,type:'FRAME',parent:page,children:[],x:0,y:0,width:440,height:100};
    page.children.push(parent); nodes.set(parent.id,parent);
  }
  for (const spec of input.expected) {
    const node={...spec,type:'FRAME',visible:true,opacity:1,x:0,y:0,rotation:0,
      findAll:()=>[],findAllWithCriteria:()=>[]};
    node.parent=nodes.get(spec.parentId); node.parent.children.push(node); nodes.set(node.id,node);
  }
  nodes.set(page.id,page);
  const originalOrder=page.children.map(n=>n.id);
  let creates=0;
  const figma={editorType:'figma',fileKey:input.fileKey,currentPage:page,
    getNodeByIdAsync:async id=>nodes.get(id),setCurrentPageAsync:async()=>{},
    loadFontAsync:async()=>{},createAutoLayout:()=>{
      const order=++creates;
      const node={id:'temporary:'+order,type:'FRAME',parent:page,children:[],removed:false,
        appendChild(child){if(child.parent)child.parent.children=child.parent.children.filter(n=>n!==child);child.parent=this;this.children.push(child);},
        remove(){removals.push(order);if(failRemoval&&order===2)throw Error('Injected removal failure');
          this.removed=true;if(this.parent)this.parent.children=this.parent.children.filter(n=>n!==this);}};
      Object.defineProperty(node,'name',{get:()=>node._name||'',set:value=>{
        if(order===2&&value==='Temporary full-resolution comparison row')throw Error('Injected row configuration failure');
        node._name=value;}});
      temps.push(node);page.children.push(node);return node;
    }};
  let error;
  try {await new AsyncFunction('figma',code)(figma);}
  catch(e){error=e;}
  assert(error,'The intended early failure must be injected before export');
  return {temps,removals,error,page,originalOrder};
}

(async()=>{
  const original=fs.readFileSync(path.join(folder,'figma-call.js'),'utf8');
  const corrected=fs.readFileSync(path.join(__dirname,'figma-call.js'),'utf8');
  const before=await run(original);
  assert.equal(before.temps.length,2,'Expected fault point was not reached: '+before.error.message);
  assert.equal(before.temps[1].removed,false,'Initial source reproduces orphaned standalone row');
  const after=await run(corrected);
  assert.deepEqual(after.removals,[2,1],'Attempt row removal and sheet removal after early row failure');
  assert(after.temps.every(n=>n.removed),'Every tracked temporary node must be removed on this success path');
  assert.deepEqual(after.page.children.map(n=>n.id),after.originalOrder,'Original page order must survive cleanup');
  const removalFailure=await run(corrected,true);
  assert.deepEqual(removalFailure.removals,[2,1],'One removal failure must not skip later cleanup');
  assert.equal(removalFailure.temps[0].removed,true,'Sheet removal must still be attempted');
  assert.match(removalFailure.error.message,/Temporary cleanup had 1 failures/,'Cleanup failure must require inspection');
  console.log(JSON.stringify({baseline_orphan_reproduced:true,corrected_early_failure_cleanup:'PASS',later_removal_after_failure:'PASS',scope:'Synthetic local tooling lifecycle only; no actual Figma execution/pixel/API certification'}));
})().catch(e=>{console.error(e);process.exitCode=1;});
