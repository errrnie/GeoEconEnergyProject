const tc=require('topojson-client');const fs=require('fs');
const w=JSON.parse(fs.readFileSync('package/countries-10m.json'));
const fc=tc.feature(w,w.objects.countries);
const want={'Malaysia':1,'Singapore':1,'Indonesia':1,'Thailand':1,'Brunei':1};
// bbox for Johor focus and full Malaysia
function proj(b,W,H){const [x0,y0,x1,y1]=b;const s=Math.min(W/(x1-x0),H/(y1-y0));return ([x,y])=>[((x-x0)*s).toFixed(1),((y1-y)*s).toFixed(1)];}
function paths(b,W,H){const p=proj(b,W,H);const out=[];
 for(const f of fc.features){if(!want[f.properties.name])continue;
  const polys=f.geometry.type==='Polygon'?[f.geometry.coordinates]:f.geometry.coordinates;
  let d='';for(const poly of polys){for(const ring of poly){
    const inb=ring.some(([x,y])=>x>=b[0]-1&&x<=b[2]+1&&y>=b[1]-1&&y<=b[3]+1);if(!inb)continue;
    let prev=null;const pts=[];for(const c of ring){const q=p(c);const k=q.join(',');if(k!==prev){pts.push(k);prev=k;}}
    if(pts.length<3)continue;d+='M'+pts.join('L')+'Z';}}
  if(d)out.push({name:f.properties.name,d});}
 return out;}
const johor=[102.9,1.15,104.45,2.2];
const pen=[99.6,1.15,104.7,6.75];const swk=[109.6,0.9,111.6,2.3];const res={swk:{bbox:swk,W:600,H:420,paths:paths(swk,600,420)},johor:{bbox:johor,W:800,H:540,paths:paths(johor,800,540)},pen:{bbox:pen,W:600,H:660,paths:paths(pen,600,660)}};
fs.writeFileSync('geo.json',JSON.stringify(res));
console.log(fs.statSync('geo.json').size, res.johor.paths.map(x=>x.name+':'+x.d.length));
