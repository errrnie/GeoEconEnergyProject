import fs from 'fs';import * as tc from 'topojson-client';import {geoEqualEarth,geoPath} from 'd3-geo';
const w=JSON.parse(fs.readFileSync('package/countries-110m.json'));
const fc=tc.feature(w,w.objects.countries);
fc.features=fc.features.filter(f=>f.properties.name!=='Antarctica');
const W=960,H=470;const pr=geoEqualEarth().fitSize([W,H],fc);const p=geoPath(pr).digits(1);
const out=fc.features.map(f=>({id:f.id,name:f.properties.name,d:p(f)})).filter(x=>x.d);
// label point for Malaysia
const my=pr([102.5,3.8]);
fs.writeFileSync('world.json',JSON.stringify({W,H,paths:out,my}));
console.log(out.length,fs.statSync('world.json').size,out.find(x=>x.name==='Malaysia').id);
