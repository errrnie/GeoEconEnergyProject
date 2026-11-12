import fs from 'fs';import * as tc from 'topojson-client';import {geoEqualEarth,geoPath} from 'd3-geo';
const w=JSON.parse(fs.readFileSync('package/countries-110m.json'));
const fc=tc.feature(w,w.objects.countries);
fc.features=fc.features.filter(f=>f.properties.name!=='Antarctica');
const W=960,H=470;const pr=geoEqualEarth().fitSize([W,H],fc);const p=geoPath(pr).digits(1);
const out=fc.features.map(f=>({id:f.id,name:f.properties.name,d:p(f)})).filter(x=>x.d);
// label point for Malaysia
const pts={Malaysia:pr([102.5,3.8]),Thailand:pr([101,15]),Singapore:pr([103.8,1.35]),Indonesia:pr([117,-2]),Vietnam:pr([106,14]),Philippines:pr([122,12])};
fs.writeFileSync('world.json',JSON.stringify({W,H,paths:out,pts}));
console.log(out.length,fs.statSync('world.json').size,out.find(x=>x.name==='Malaysia').id);
