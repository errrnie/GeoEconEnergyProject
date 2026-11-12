"""Regional landing page: Southeast Asia map with every campus, a year slider, and links to deep dives."""
import csv, json, os

def rd(p):
    return list(csv.DictReader(open(p, encoding='utf-8'))) if os.path.exists(p) else []

NUM = {3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven'}
ISO = {'Singapore': '702', 'Malaysia': '458', 'Thailand': '764', 'Indonesia': '360', 'Vietnam': '704', 'Philippines': '608'}


def _inline(t):
    import html as H, re
    t = H.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\[(\d+)\]', r'<sup><a href="#s\1">\1</a></sup>', t)
    return t.replace('</a></sup><sup><a', '</a>,<a')


def render_story(path):
    """Markdown story (## sections, paragraphs, numbered lists, [n] citations) to HTML sections."""
    import re
    if not os.path.exists(path):
        return ''
    secs = re.split(r'^## ', open(path, encoding='utf-8').read(), flags=re.M)[1:]
    body, srcs, take = '', '', ''
    for sec in secs:
        head, _, rest = sec.partition('\n')
        paras = [p.strip() for p in rest.strip().split('\n\n') if p.strip()]
        if head.startswith('Sources'):
            for line in rest.strip().split('\n'):
                m = re.match(r'(\d+)\. (.*?)(https?://\S+)?$', line.strip())
                if m:
                    url = m.group(3) or ''
                    srcs += f'<li id="s{m.group(1)}">{_inline(m.group(2).strip())}' + (f' <a href="{url}" target="_blank" rel="noopener">link</a>' if url else '') + '</li>'
            continue
        if head.startswith('Five takeaways'):
            items = [re.sub(r'^\d+\. ', '', l) for l in rest.strip().split('\n') if l.strip()]
            take = '<div class="callout"><h3>Five takeaways</h3><ol class="read">' + ''.join(f'<li>{_inline(i)}</li>' for i in items) + '</ol></div>'
            continue
        body += f'<div class="phase"><h3>{_inline(head)}</h3>' + ''.join(f'<p class="read">{_inline(p)}</p>' for p in paras) + '</div>'
    return f"""<section id="story">
  <span class="eyebrow">2 · How it happened</span>
  <h2>Singapore filled up, Johor took the overflow, and AI demand spread it further</h2>
  <div class="phases">{body}</div>
  {take}
  <details class="srclist"><summary>Sources for this story ({srcs.count('<li')})</summary><ol>{srcs}</ol></details>
</section>"""


def build(nav, configs, markets):
    tpl = open('src/template.html').read()
    head = tpl[:tpl.index('<div class="wrap">')].replace('__TITLE__', 'Southeast Asia Compute')
    sites = []
    for m in markets:
        fix = {r['site_name']: r for r in rd(f'data/{m}/sites_coords.csv')}
        for r in rd(f'data/{m}/sites.csv'):
            f = fix.get(r['site_name'])
            if f and f.get('lat'):
                r['lat'], r['lon'] = f['lat'], f['lon']
            if not (r.get('lat') and r.get('lon')):
                continue
            sites.append({'n': r['site_name'], 'c': configs[m]['name'], 'm': m, 'lat': float(r['lat']), 'lon': float(r['lon']),
                          's': r['stack'], 'st': r['status'], 'mw': r['it_mw'], 'y': r['year_announced'] or r['year_live'] or '',
                          'op': r['operator']})
    hubs = rd('data/region/hubs.csv')
    rc = rd('data/region/countries.csv')
    tl = rd('data/region/timeline.csv')
    story = render_story('data/region/story_v2.md')
    geo = json.load(open('geo/sea.json'))['sea']
    cards = ''
    for m in markets:
        c = configs[m]
        cards += f'<a class="mcard" href="{m}/index.html"><span class="eyebrow">Deep dive</span><h3>{c["name"]}</h3><p class="sub">{c.get("tagline", "")}</p><span class="more">Open {c["name"]} →</span></a>'
    for r in rc:
        if r['country'].lower() in markets or r['country'] not in ('Indonesia', 'Vietnam', 'Philippines'):
            continue
        cards += (f'<div class="mcard soon"><span class="eyebrow">Coming next</span><h3>{r["country"]}</h3>'
                  f'<p class="sub">{r.get("top_hubs", "")}</p></div>')
    data = json.dumps({'sites': sites, 'hubs': hubs, 'geo': geo, 'deep': {configs[m]['name']: m for m in markets}},
                      ensure_ascii=False).replace('</', '<\\/')
    tl_js = json.dumps(tl, ensure_ascii=False).replace('</', '<\\/')
    body = f'''
<style>
.mcards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}}
.mcard{{display:grid;gap:6px;align-content:start;background:var(--surface);border:1px solid var(--line);border-top:3px solid var(--accent);padding:14px 16px;color:var(--fg);text-decoration:none;border-radius:2px}}
.mcard:hover{{border-color:var(--accent)}}.mcard.soon{{border-top-color:var(--line);opacity:.75}}
.mcard .more{{font-family:var(--mono);font-size:.78rem;color:var(--accent)}}
.seamap svg{{width:100%;height:auto;display:block}}
.seamap path{{fill:#1a2430;stroke:#3b4b5e;stroke-width:.6}}
.seamap path.deep{{fill:#2a2215;stroke:var(--accent);cursor:pointer}}.seamap path.deep:hover{{fill:#3a2d18}}
.yr{{display:flex;gap:14px;align-items:center;flex-wrap:wrap}}
.yr input{{flex:1;min-width:200px;accent-color:var(--accent)}}
.yr b{{font-family:var(--display);font-size:2rem;color:var(--accent);min-width:3ch}}
.hist svg{{width:100%;height:auto;display:block}}
.phases{{display:grid;gap:18px}}.phase{{border-left:3px solid var(--line);padding-left:16px}}.phase h3{{color:var(--accent)}}
.phase p,.callout li{{margin:.5em 0}}.phase sup a,.callout sup a{{color:var(--accent);text-decoration:none;font-family:var(--mono);font-size:.75em}}
.srclist{{margin-top:14px}}.srclist summary{{cursor:pointer;font-family:var(--mono);color:var(--accent)}}.srclist li{{font-size:.85rem;color:var(--muted);margin:.3em 0;word-break:break-word}}
</style>
<div class="wrap">
{nav(None)}
<header class="hero">
  <span class="banner">Draft · regional overview · sources linked on each country page</span>
  <span class="eyebrow">Southeast Asia compute · 2010 to 2026</span>
  <h1>How compute came to Southeast Asia</h1>
  <p class="lede read">The US and China hold about 90% of the world's tracked AI computing power. Outside them, Southeast Asia has become one of the busiest places to build it, and by mid-2026 it held about half of the data centre capacity under construction in Asia Pacific. It started in Singapore, crossed the causeway to Johor, and is now reaching Bangkok, Jakarta, Batam and Ho Chi Minh City. This site follows where the campuses went, why, and what each host is trading for them.</p>
</header>

<section id="map">
  <span class="eyebrow">1 · Where the campuses are</span>
  <h2>A map that fills in year by year</h2>
  <p class="read sub">Each dot is a data centre campus from the country deep dives, coloured by whose stack it mainly serves. Drag the slider to see campuses appear by the year they were announced. Highlighted countries open their deep dive.</p>
  <div class="yr"><b id="yrv">2026</b><input type="range" id="yr" min="2012" max="2026" value="2026" aria-label="Show campuses announced up to this year"><span class="note" id="yrn"></span></div>
  <div class="figure seamap"><svg id="sea" role="img" aria-label="Map of Southeast Asia data centre campuses"></svg></div>
  <div class="legend"><span><i style="background:var(--us)"></i>US-linked</span><span><i style="background:var(--cn)"></i>China-linked</span><span><i style="background:var(--other)"></i>Other or local</span><span><i style="background:var(--unk)"></i>Unknown</span><span><i style="border:2px solid var(--accent);background:transparent"></i>Deep dive available</span><span><i style="border:2px dashed var(--accent);background:transparent;border-radius:50%"></i>Other hubs (operating plus pipeline MW)</span></div>
  <div class="figure hist"><h3>Campuses announced per year</h3><svg id="hist" role="img" aria-label="Campuses announced per year by country"></svg></div>
</section>

{story}

<section id="countries">
  <span class="eyebrow">3 · Country deep dives</span>
  <h2>{NUM[len(markets)]} hosts, {NUM[len(markets)].lower()} bargains</h2>
  <div class="mcards">{cards}</div>
</section>

<section id="sources">
  <span class="eyebrow">Sources and method</span>
  <p class="sources">Campus locations come from each country's dataset; sites known only by town or province are placed approximately. Every row links to its source on the country pages. Built by Ernie Vita with Claude; code and data on <a href="https://github.com/errrnie/GeoEconEnergyProject">GitHub</a>.</p>
</section>
</div>
<script>
const D={data},TL={tl_js};
const NS="http://www.w3.org/2000/svg";
function el(t,a,p){{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e}}
const SC={{"US":"var(--us)","China":"var(--cn)","Other":"var(--other)","Unknown":"var(--unk)","Mixed":"var(--unk)"}};
const G=D.geo,[x0,y0,x1,y1]=G.bbox,s=Math.min(G.W/(x1-x0),G.H/(y1-y0)),P=(lo,la)=>[(lo-x0)*s,(y1-la)*s];
function draw(){{const yr=+document.getElementById("yr").value;document.getElementById("yrv").textContent=yr;
  const m=document.getElementById("sea");m.innerHTML="";m.setAttribute("viewBox",`0 0 ${{G.W}} ${{G.H}}`);
  G.paths.forEach(p=>{{const slug=D.deep[p.name];const e=el("path",{{d:p.d,class:slug?"deep":""}},m);
    if(slug){{e.setAttribute("tabindex",0);e.setAttribute("role","link");e.setAttribute("aria-label",p.name+" deep dive");
      const go=()=>location.href=slug+"/index.html";e.onclick=go;e.onkeydown=ev=>{{if(ev.key==="Enter")go()}};el("title",{{}},e).textContent=p.name+": open deep dive"}}}});
  (G.labels||[]).forEach(([lo,la,t])=>{{const [x,y]=P(lo,la);const e=el("text",{{x,y,"text-anchor":"middle","font-size":13,fill:"var(--muted)"}},m);e.textContent=t}});
  const shown=D.sites.filter(x=>!x.y||+x.y<=yr);
  shown.forEach((x,i)=>{{const [cx,cy]=P(x.lon,x.lat);const jx=((x.n.length*37)%9-4)*.8,jy=((x.n.length*53)%9-4)*.8;const r=2.2+Math.sqrt(+x.mw||30)*.18;
    const solid=x.st==="Operational";const c=el("circle",{{cx:cx+jx,cy:cy+jy,r,fill:solid?SC[x.s]||"var(--unk)":"none",stroke:SC[x.s]||"var(--unk)","stroke-width":1.2,"fill-opacity":.8}},m);
    el("title",{{}},c).textContent=`${{x.n}} (${{x.c}}) · ${{x.op}} · ${{x.st}}${{x.y?" · announced "+x.y:""}}`}});
  D.hubs.filter(h=>!D.deep[h.country]&&h.lat&&h.lon).forEach(h=>{{const [x,y]=P(+h.lon,+h.lat);const mw=(+h.operational_mw||0)+(+h.pipeline_mw||0);const r=4+Math.sqrt(mw||50)*.25;
    const c=el("circle",{{cx:x,cy:y,r,fill:"none",stroke:"var(--accent)","stroke-dasharray":"3 2","stroke-width":1.4}},m);
    el("title",{{}},c).textContent=`${{h.hub}}, ${{h.country}}: ${{h.operational_mw||"?"}} MW operating, ${{h.pipeline_mw||"?"}} MW pipeline (${{h.source_name}}). Deep dive coming.`;
    const t=el("text",{{x:x+r+3,y:y+4,"font-size":11,fill:"var(--fg)"}},m);t.textContent=h.hub.replace(/\\s*\\(.*\\)/,"")}});
  document.getElementById("yrn").textContent=`${{shown.length}} of ${{D.sites.length}} mapped campuses announced by ${{yr}} (campuses with no announcement year always show)`;}}
document.getElementById("yr").oninput=draw;draw();
(function(){{const svg=document.getElementById("hist"),ys=[];for(let y=2012;y<=2026;y++)ys.push(y);
  const cs=[...new Set(D.sites.map(x=>x.c))],col={{Singapore:"#c792ea",Malaysia:"var(--accent)",Thailand:"var(--t1)",Indonesia:"var(--cn)",Vietnam:"var(--us)"}};
  const W=760,H=220,l=30,b=24,bw=(W-l)/ys.length-6;svg.setAttribute("viewBox",`0 0 ${{W}} ${{H}}`);
  const cnt=ys.map(y=>cs.map(c=>D.sites.filter(x=>+x.y===y&&x.c===c).length));const max=Math.max(1,...cnt.map(a=>a.reduce((p,q)=>p+q,0)));
  ys.forEach((y,i)=>{{let acc=0;const x=l+i*(bw+6);cs.forEach((c,k)=>{{const v=cnt[i][k];if(!v)return;const h=v/max*(H-b-14);const r=el("rect",{{x,y:H-b-acc-h,width:bw,height:h,fill:col[c]||"var(--other)"}},svg);el("title",{{}},r).textContent=`${{c}} ${{y}}: ${{v}}`;acc+=h}});
    const t=el("text",{{x:x+bw/2,y:H-6,"text-anchor":"middle","font-size":10,fill:"var(--muted)"}},svg);t.textContent=String(y).slice(2)}});
  const lg=document.createElement("div");lg.className="legend";lg.innerHTML=cs.map(c=>`<span><i style="background:${{col[c]||"var(--other)"}}"></i>${{c}}</span>`).join("");svg.after(lg)}})();
</script>
'''
    out = head + body
    open('docs/index.html', 'w').write(out)
    print(f'landing: {len(out):,} bytes, {len(sites)} mapped sites, {len(hubs)} hubs, {len(tl)} regional events')
