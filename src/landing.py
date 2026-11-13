"""Regional landing page: Southeast Asia map with every campus, a year slider, and links to deep dives."""
import csv, json, os

def rd(p):
    return list(csv.DictReader(open(p, encoding='utf-8'))) if os.path.exists(p) else []

TAKE = ''
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
    global TAKE
    TAKE = take
    return f"""<section id="story">
  <span class="eyebrow">2 · How it happened</span>
  <h2>Singapore filled up, Johor took the overflow, and AI demand spread it further</h2>
  <p class="read sub">Four phases, from AWS's first Asian region in 2010 to the brakes of 2025 and 2026. Numbers link to the sources at the end of this section.</p>
  <div class="phases">{body}</div>
  <details class="srclist"><summary>Sources for this story ({srcs.count('<li')})</summary><ol>{srcs}</ol></details>
</section>"""


MIXG = [('Coal', ('coal',), 'var(--coal)'), ('Gas', ('gas',), 'var(--gas)'), ('Oil', ('oil',), '#3d4855'),
        ('Hydro', ('hydro',), 'var(--hydro)'), ('Wind and solar', ('wind', 'solar'), 'var(--solar)'),
        ('Other clean (geothermal, bioenergy, nuclear)', ('bioenergy', 'other_renewables', 'nuclear'), 'var(--t1)')]


def mix_panels(countries):
    """Small multiples: share of generation by fuel group, 2010 to latest year (Ember via OWID)."""
    rows = rd('data/shared/energy_mix_yearly.csv')
    out = ''
    W, H, l, b, t = 260, 150, 30, 18, 8
    for c in countries:
        rs = [r for r in rows if r['country'] == c and r['twh']]
        ys = sorted({int(r['year']) for r in rs})
        if not ys:
            continue
        tot = {y: sum(float(r['twh']) for r in rs if int(r['year']) == y and any(r['fuel'] in g[1] for g in MIXG)) for y in ys}
        sh = {y: [sum(float(r['twh']) for r in rs if int(r['year']) == y and r['fuel'] in g[1]) / tot[y] * 100 if tot[y] else 0 for g in MIXG] for y in ys}
        sx = lambda y: l + (y - ys[0]) / max(1, ys[-1] - ys[0]) * (W - l - 6)
        sy = lambda v: t + (1 - v / 100) * (H - t - b)
        svg = ''
        acc = {y: 0.0 for y in ys}
        for k, g in enumerate(MIXG):
            top = [(sx(y), sy(acc[y] + sh[y][k])) for y in ys]
            bot = [(sx(y), sy(acc[y])) for y in reversed(ys)]
            if max(sh[y][k] for y in ys) > 0.2:
                d = 'M' + ' L'.join(f'{x:.1f},{yv:.1f}' for x, yv in top + bot) + 'Z'
                svg += f'<path d="{d}" fill="{g[2]}"><title>{c}, {g[0]}: {sh[ys[0]][k]:.0f}% in {ys[0]}, {sh[ys[-1]][k]:.0f}% in {ys[-1]}</title></path>'
            for y in ys:
                acc[y] += sh[y][k]
        for v in (0, 50, 100):
            svg += f'<text x="{l - 4}" y="{sy(v) + 3:.0f}" text-anchor="end" font-size="9" fill="var(--muted)">{v}%</text>'
        svg += f'<text x="{sx(ys[0]):.0f}" y="{H - 4}" font-size="9" fill="var(--muted)">{ys[0]}</text><text x="{sx(ys[-1]):.0f}" y="{H - 4}" font-size="9" text-anchor="end" fill="var(--muted)">{ys[-1]}</text>'
        last = sh[ys[-1]]
        lead = sorted(range(len(MIXG)), key=lambda k: -last[k])[:2]
        cap = ', '.join(f'{MIXG[k][0].split(" (")[0].lower()} {last[k]:.0f}%' for k in lead)
        out += f'<figure class="mixp"><figcaption><b>{c}</b><span>{ys[-1]}: {cap}</span></figcaption><svg viewBox="0 0 {W} {H}" role="img" aria-label="{c} power generation mix, {ys[0]} to {ys[-1]}">{svg}</svg></figure>'
    leg = ''.join(f'<span><i style="background:{g[2]}"></i>{g[0]}</span>' for g in MIXG)
    return f'<div class="mixgrid">{out}</div><div class="legend">{leg}</div>'


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
    for i, m in enumerate(markets):
        c = configs[m]
        cards += f'<a class="mcard" href="{m}/index.html"><span class="eyebrow">{i + 1} of {len(markets)}{" · start here" if i == 0 else ""}</span><h3>{c["name"]}</h3><p class="sub">{c.get("tagline", "")}</p><span class="more">Open {c["name"]} →</span></a>'
    path = ' <span class="arr">→</span> '.join(f'<a href="{m}/index.html"><b>{i + 1}</b> {configs[m]["name"]}</a>' for i, m in enumerate(markets))
    gl = rd('data/region/glance.csv')
    glance = ''.join(f'<tr><th scope="row"><a href="{r["slug"]}/index.html">{r["country"]}</a></th><td>{r["operating"]}</td><td>{r["pipeline"]}</td><td class="mono">{r["build_cost"]}</td><td>{r["power"]}</td><td>{r["new_load"]}</td><td class="mono">{r["tariff"]}</td><td>{r["chips"]}</td><td>{r["bargain"]}</td></tr>' for r in gl)
    mix_svg = mix_panels([configs[m]['name'] for m in markets])
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
.path{{display:flex;flex-wrap:wrap;gap:6px 8px;align-items:center;font-family:var(--mono);font-size:.82rem}}
.path a{{color:var(--fg);text-decoration:none;border:1px solid var(--line);padding:6px 10px;border-radius:2px;background:var(--surface)}}.path a:hover{{border-color:var(--accent)}}.path a b{{color:var(--accent);margin-right:4px}}.path .arr{{color:var(--muted)}}
.take ol{{margin:.4em 0 0 1.2em}}
.glance{{overflow-x:auto}}.glance table{{border-collapse:collapse;width:100%;min-width:900px;font-size:.86rem}}
.glance th,.glance td{{text-align:left;vertical-align:top;padding:9px 10px;border-bottom:1px solid var(--line)}}
.glance thead th{{font-family:var(--mono);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:400}}
.glance tbody th a{{color:var(--accent);font-weight:600;text-decoration:none}}.glance tbody th a:hover{{text-decoration:underline}}.glance tbody tr:hover{{background:var(--surface)}}
.mixgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}}
.mixp{{margin:0;background:var(--surface);border:1px solid var(--line);padding:10px 12px}}.mixp svg{{width:100%;height:auto;display:block}}
.mixp figcaption{{display:flex;justify-content:space-between;gap:8px;align-items:baseline;margin-bottom:6px}}.mixp figcaption span{{font-family:var(--mono);font-size:.72rem;color:var(--muted)}}
.srclist{{margin-top:14px}}.srclist summary{{cursor:pointer;font-family:var(--mono);color:var(--accent)}}.srclist li{{font-size:.85rem;color:var(--muted);margin:.3em 0;word-break:break-word}}
</style>
<div class="wrap">
{nav(None)}
<header class="hero">
  <span class="banner">Updated November 2026 · regional overview · sources below and on each country page</span>
  <span class="eyebrow">Southeast Asia compute · 2010 to 2026</span>
  <h1>How compute came to Southeast Asia</h1>
  <p class="lede read">The US and China hold about 90% of the world's tracked AI computing power. Outside them, Southeast Asia has become one of the busiest places to build it, and by mid-2026 it held about half of the data centre capacity under construction in Asia Pacific. It started in Singapore, crossed the causeway to Johor, stalled in Bangkok, and is now building in Jakarta and Batam, with Vietnam and the Philippines just opening. This site follows where the campuses went, why, and what each host is trading for them.</p>
  <div class="read"><span class="eyebrow">How to read this site</span><p class="sub">Start with the map and the short history below, compare the six hosts in one table, then read the country pages in order. Each country page ends with a link to the next.</p></div>
  <nav class="path" aria-label="Country pages in reading order">{path}</nav>
</header>
<nav class="jump" aria-label="Sections on this page"><a href="#short">Short version</a><a href="#map">Map</a><a href="#story">History</a><a href="#glance">Six hosts compared</a><a href="#power">Power mix</a><a href="#countries">Country pages</a><a href="#sources">Sources</a></nav>

<section id="short">
  <span class="eyebrow">The short version</span>
  <div class="callout take">{TAKE.replace('<div class="callout"><h3>Five takeaways</h3>', '<h3>Five takeaways</h3>').removesuffix('</div>')}</div>
</section>

<section id="map">
  <span class="eyebrow">1 · Where the campuses are</span>
  <h2>A map that fills in year by year</h2>
  <p class="read sub">Each dot is a data centre campus from the country deep dives, coloured by whose stack it mainly serves. Drag the slider to see campuses appear by the year they were announced. Highlighted countries open their deep dive. "Operating" means built and running; "pipeline" means under construction or planned. DayOne, the former international arm of China's GDS, is tagged China-linked or mixed depending on its tenants, a judgment call.</p>
  <div class="yr"><b id="yrv">2026</b><input type="range" id="yr" min="2012" max="2026" value="2026" aria-label="Show campuses announced up to this year"><span class="note" id="yrn"></span></div>
  <div class="figure seamap"><svg id="sea" role="img" aria-label="Map of Southeast Asia data centre campuses"></svg></div>
  <div class="legend"><span><i style="background:var(--us)"></i>US-linked</span><span><i style="background:var(--cn)"></i>China-linked</span><span><i style="background:var(--other)"></i>Other or local</span><span><i style="background:var(--unk)"></i>Unknown or mixed</span><span><i style="border:2px solid var(--accent);background:transparent"></i>Deep dive available</span><span><i style="border:2px dashed var(--accent);background:transparent;border-radius:50%"></i>Other hubs (operating plus pipeline MW)</span></div>
  <div class="figure hist"><h3>Campuses announced per year</h3><svg id="hist" role="img" aria-label="Campuses announced per year by country"></svg></div>
</section>

{story}

<section id="glance">
  <span class="eyebrow">3 · Six hosts compared</span>
  <h2>Same boom, different bargains</h2>
  <p class="read sub">One row per host, using the headline figure from each country page. Capacity figures come from different brokers and definitions, so treat them as orders of magnitude. Select a country to open its page.</p>
  <div class="glance"><table><thead><tr><th>Host</th><th>Operating</th><th>Pipeline</th><th>Build cost, US$m/MW</th><th>Main power source</th><th>New load met by</th><th>US tariff since Jul 2026</th><th>US AI chips</th><th>The bargain</th></tr></thead><tbody>{glance}</tbody></table></div>
  <p class="note">Build cost: Cushman &amp; Wakefield APAC Data Centre Construction Cost Guide 2026, mid-range. Tariffs: US Section 301 duties from 24 July 2026. Chips: every host needs a US licence to supply a China-parented buyer; Vietnam alone also needs one at country level.</p>
</section>

<section id="power">
  <span class="eyebrow">4 · How each host makes its power</span>
  <h2>Six grids, three fuel stories</h2>
  <p class="read sub">Singapore and Thailand run on gas, and both rely more and more on imported LNG. Indonesia, the Philippines and Malaysia lean on coal, and Vietnam on coal plus hydro, which a dry year can take away. Whatever fuel sits at the margin is what new data centre load really burns, which is why each country page ends with a 2030 fuel scenario.</p>
  {mix_svg}
  <p class="note">Share of electricity generation by fuel, Ember Yearly Electricity Data (2026 release) via Our World in Data. Imports are excluded, which matters for Thailand (Laos hydro) and Singapore. Country pages use national statistics, so their shares can differ by a few points.</p>
</section>

<section id="countries">
  <span class="eyebrow">5 · Country deep dives</span>
  <h2>{NUM[len(markets)]} hosts, read in order</h2>
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
  const cs=[...new Set(D.sites.map(x=>x.c))],col={{Singapore:"#c792ea",Malaysia:"var(--accent)",Thailand:"#4ecdc4",Indonesia:"#e8e3d3",Vietnam:"#8fa8c8",Philippines:"#d98e73"}};
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
