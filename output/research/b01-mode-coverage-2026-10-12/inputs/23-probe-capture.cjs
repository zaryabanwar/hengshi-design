// Exercises the actual prepared capture/cleanup section against a local fault fixture.
// No Figma connection, API qualification, layout, pixels or accessibility proof.
const fs=require('node:fs');
const assert=require('node:assert/strict');
const AsyncFunction=Object.getPrototypeOf(async function(){}).constructor;
const code=fs.readFileSync(__dirname+'/figma-template.js','utf8');
const input=JSON.parse(fs.readFileSync(__dirname+'/input.json','utf8'));
const start=code.indexOf('const sheets=[],rows=[],copies=[]');
const end=code.indexOf('report.allTemporaryNodesRemoved=',start);
assert(start>0&&end>start,'The exact capture seam must exist');
const capture=code.slice(start,end)+'\nreturn report;';

async function run(fault){
  const temps=[],attempted=[],page={children:[],appendChild(n){
    if(n.parent)n.parent.children=n.parent.children.filter(v=>v!==n);
    n.parent=this;this.children.push(n);
  }};
  let serial=0,screenshots=0,sheetsCreated=0;
  function make(isSheet){
    const n={id:'temporary:'+ ++serial,type:'FRAME',children:[],parent:null,removed:false,x:0,y:0,
      itemSpacing:24,paddingLeft:24,paddingTop:24,paddingRight:24,paddingBottom:24,
      appendChild(child){page.appendChild.call(this,child);},findAll(){return [];},
      resize(w,h){this.fixedWidth=w;this.fixedHeight=h;},
      remove(){attempted.push(this.id);
        if(fault==='remove'&&this===temps.find(v=>!v.isSheet))throw Error('Injected removal failure');
        this.removed=true;if(this.parent)this.parent.children=this.parent.children.filter(v=>v!==this);
        for(const child of this.children)child.removed=true;
      },
      async screenshot(){screenshots++;if(fault==='screenshot'&&screenshots===3)throw Error('Injected screenshot failure');}
    };
    n.isSheet=isSheet;
    if(isSheet){const ordinal=++sheetsCreated;
      Object.defineProperty(n,'name',{set(value){if(fault==='configure'&&ordinal===2)throw Error('Injected sheet configuration failure');this._name=value;},get(){return this._name;}});
    }
    Object.defineProperties(n,{
      width:{get(){return this.fixedWidth||48+this.children.reduce((sum,v)=>sum+v.width,0)+Math.max(0,this.children.length-1)*24;}},
      height:{get(){return this.fixedHeight||48+Math.max(1,...this.children.map(v=>v.height));}},
      absoluteBoundingBox:{get(){const index=this.parent.children.indexOf(this);return {x:this.parent.x+24+index*(this.width+24),y:this.parent.y+24,width:this.width,height:this.height};}}
    });
    temps.push(n);page.appendChild(n);return n;
  }
  const units=input.references.map((r,i)=>({id:'original:'+i,width:320,height:r.kind==='FRAME'?2200:1600,
    clone(){const n=make(false);n.fixedWidth=this.width;n.fixedHeight=this.height;return n;}}));
  const figma={createAutoLayout(){return make(true);}};
  const root={x:1000,y:400,width:420};
  const beforeOrder=page.children.map(n=>n.id);
  let result,error;
  try{result=await new AsyncFunction('input','figma','units','unitBefore','page','root','paint','descendants','fingerprint','createdIds','base','packIds','bytes',capture)(
    input,figma,units,units.map(n=>JSON.stringify([n.width,n.height])),page,root,()=>({type:'SOLID',color:{r:1,g:1,b:1}}),
    n=>[n],n=>JSON.stringify([n.width,n.height]),[],{},ids=>({ids:[...new Set(ids)]}),()=>0);
  }catch(e){error=e;}
  if(fault==='none'){
    assert(!error,error?.message);assert.equal(result.tiles.length,48);assert.equal(screenshots,5);
  }else assert(error,'The requested injected fault must be reached');
  assert(temps.every(n=>n.removed),'All capture-owned temporaries must be removed, including the initially created sheet');
  assert.deepEqual(page.children.map(n=>n.id),beforeOrder,'Capture must leave original page order intact');
  if(fault==='remove'){
    assert.match(error.message,/Mode cleanup failed/,'Cleanup uncertainty must prevent a successful report');
    assert(temps.filter(n=>n.isSheet).every(n=>attempted.includes(n.id)),'A failed clone removal must not skip later sheets');
  }
  if(fault==='configure')assert.match(error.message,/Injected sheet configuration failure/);
  if(fault==='screenshot')assert.match(error.message,/Injected screenshot failure/);
  return {fault,result:'PASS',temporaries_created:temps.length,screenshots_attempted:screenshots,
    successful_native_export:false,scope:'Synthetic actual-capture-section control flow only'};
}
(async()=>{
  const results=[];for(const fault of ['none','configure','screenshot','remove'])results.push(await run(fault));
  process.stdout.write(JSON.stringify({source:'figma-template.js capture section',results,
    limits:['No Figma producer execution','No native image, layout, font, bounds, protocol or accessibility qualification','Receipt codec/size guard is outside this cleanup probe']},null,2)+'\n');
})().catch(e=>{console.error(e);process.exitCode=1;});
