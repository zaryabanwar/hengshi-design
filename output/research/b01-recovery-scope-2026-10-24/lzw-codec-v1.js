// LZW over UTF-8 bytes; fixed 16-bit big-endian codes, dictionary reset at 4096.
function encodeScope(text) {
  const bytes=[];
  for(const c of text){const x=c.codePointAt(0); if(x<128)bytes.push(x);else if(x<2048)bytes.push(192|(x>>6),128|(x&63));else if(x<65536)bytes.push(224|(x>>12),128|((x>>6)&63),128|(x&63));else bytes.push(240|(x>>18),128|((x>>12)&63),128|((x>>6)&63),128|(x&63));}
  let dict=new Map(Array.from({length:256},(_,i)=>[String.fromCharCode(i),i])),next=256,w='';const codes=[];
  for(const b of bytes){const c=String.fromCharCode(b),wc=w+c;if(dict.has(wc))w=wc;else{codes.push(dict.get(w));if(next<4096)dict.set(wc,next++);else{dict=new Map(Array.from({length:256},(_,i)=>[String.fromCharCode(i),i]));next=256;}w=c;}}
  if(w)codes.push(dict.get(w));
  const raw=codes.flatMap(n=>[n>>8,n&255]),alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';let result='';
  for(let i=0;i<raw.length;i+=3){const a=raw[i],b=raw[i+1],c=raw[i+2],n=(a<<16)|((b||0)<<8)|(c||0);result+=alphabet[(n>>>18)&63]+alphabet[(n>>>12)&63]+(b===undefined?'=':alphabet[(n>>>6)&63])+(c===undefined?'=':alphabet[n&63]);}
  return result;
}
function decodeScope(encoded) {
  const raw=Buffer.from(encoded,'base64'),codes=[];for(let i=0;i<raw.length;i+=2)codes.push(raw.readUInt16BE(i));
  if(!codes.length)return '';
  let dict=Array.from({length:256},(_,i)=>String.fromCharCode(i)),next=256,w=dict[codes[0]],result=w;
  for(const code of codes.slice(1)){const entry=dict[code]??(code===next?w+w[0]:null);if(entry===null)throw Error('Invalid LZW');result+=entry;if(next<4096)dict[next++]=w+entry[0];else{dict=Array.from({length:256},(_,i)=>String.fromCharCode(i));next=256;}w=entry;}
  return Buffer.from(result,'latin1').toString('utf8');
}
module.exports={encodeScope,decodeScope};
