// usage: node mk2.js views.json out.json [res]
const tc=require('topojson-client');const fs=require('fs');
const [,,vf,of,res='10m']=process.argv;const V=JSON.parse(fs.readFileSync(vf));
const w=JSON.parse(fs.readFileSync(`package/countries-${res}.json`));const fc=tc.feature(w,w.objects.countries);
function proj(b,W,H){const [x0,y0,x1,y1]=b;const s=Math.min(W/(x1-x0),H/(y1-y0));return ([x,y])=>[((x-x0)*s).toFixed(1),((y1-y)*s).toFixed(1)];}
function paths(b,W,H){const p=proj(b,W,H);const out=[];
 for(const f of fc.features){const polys=f.geometry?(f.geometry.type==='Polygon'?[f.geometry.coordinates]:f.geometry.coordinates):[];
  let d='';for(const poly of polys){for(const ring of poly){
    const inb=ring.some(([x,y])=>x>=b[0]-2&&x<=b[2]+2&&y>=b[1]-2&&y<=b[3]+2);if(!inb)continue;
    let prev=null;const pts=[];for(const c of ring){const q=p(c);const k=q.join(',');if(k!==prev){pts.push(k);prev=k;}}
    if(pts.length<3)continue;d+='M'+pts.join('L')+'Z';}}
  if(d)out.push({name:f.properties.name,d});}
 return out;}
const out={};for(const v of V){out[v.id]={bbox:v.bbox,W:v.W,H:v.H,wide:!!v.wide,labels:v.labels||[],paths:paths(v.bbox,v.W,v.H)};}
fs.writeFileSync(of,JSON.stringify(out));console.log(of,fs.statSync(of).size,Object.keys(out).map(k=>k+':'+out[k].paths.length));
