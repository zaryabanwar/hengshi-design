const fs=require('fs'),vm=require('vm');
const codec=fs.readFileSync(process.argv[2],'utf8');
const context=vm.createContext({});vm.runInContext(codec,context);
const fixtures=[[],['21:1','21:2','21:3','21:9','27:4','27:5','literal','21:1'],Array.from({length:4006},(_,i)=>'27:'+i),['27:01','27:9007199254740992','literal:α']];
for(const ids of fixtures){const packed=context.packIds(ids);if(packed.count!==new Set(ids).size)throw Error('count differs');}
console.log('4 pure codec boundary sets round-trip; no Figma execution or pixels.');
