"""Build the site: one page per market in markets/, plus the regional landing page.

    python3 src/build.py            # builds everything into docs/
"""
import csv, json, os, re, sys, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def rd(path):
    return list(csv.DictReader(open(path, encoding='utf-8'))) if os.path.exists(path) else []


def js(rows, keep=None):
    if keep:
        rows = [{k: r.get(k, '') for k in keep} for r in rows]
    return json.dumps(rows, ensure_ascii=False).replace('</', '<\\/')


def load_texts(slug):
    spec = importlib.util.spec_from_file_location(f'texts_{slug}', f'markets/{slug}/texts.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# map research statuses onto the four the map draws
STATUS = {'Cancelled': 'Paused/Cancelled', 'Paused': 'Paused/Cancelled'}

KEEP_EV = ['date', 'date_precision', 'track', 'title', 'description', 'amount_usd_m', 'significance', 'source_url', 'source_name']
KEEP_SI = ['site_name', 'operator', 'owner_investors', 'anchor_tenant', 'stack', 'state', 'town', 'lat', 'lon',
           'latlon_precision', 'it_mw', 'mw_type', 'status', 'source_url', 'confidence']
KEEP_CO = ['country', 'operational_gw', 'pipeline_gw', 'capacity_source', 'capacity_source_url',
           'crosscheck_installed_gw', 'build_cost_usd_m_per_mw', 'confidence']

# shared data
co = rd('data/shared/countries.csv')
for f in rd('data/shared/countries_apply.csv'):
    for r in co:
        if r['country'] == f['country']:
            r[f['field']] = f['new_value']
WORLD = open('geo/world.json').read()

markets = sorted(d for d in os.listdir('markets') if os.path.exists(f'markets/{d}/config.json'))
configs = {m: json.load(open(f'markets/{m}/config.json')) for m in markets}
ORDER = ['singapore', 'malaysia', 'thailand']
markets = [m for m in ORDER if m in markets] + [m for m in markets if m not in ORDER]


def nav(current):
    links = [f'<a class="brand" href="{"../" if current else ""}index.html"{" aria-current=page" if not current else ""}>Southeast Asia Compute</a>']
    for m in markets:
        href = f'../{m}/index.html' if current else f'{m}/index.html'
        cur = ' aria-current="page"' if m == current else ''
        links.append(f'<a href="{href}"{cur}>{configs[m]["name"]}</a>')
    return '<nav class="nav" aria-label="Markets">' + ''.join(links) + '</nav>'


def build_market(slug):
    cfg = configs[slug]
    tx = load_texts(slug)
    d = f'data/{slug}'
    si = rd(f'{d}/sites.csv')
    fix = {r['site_name']: r for r in rd(f'{d}/sites_coords.csv')}
    for r in si:
        r['status'] = STATUS.get(r['status'], r['status'])
        f = fix.get(r['site_name'])
        if f and f.get('lat'):
            r['lat'], r['lon'], r['latlon_precision'] = f['lat'], f['lon'], f['latlon_precision']
    base = rd(f'{d}/events.csv')
    bd = {e['date'] for e in base} | set(getattr(tx, 'SKIP_SECURITY_DATES', []))
    ev = sorted(base + [e for e in rd(f'{d}/security_events.csv') if e['date'] not in bd], key=lambda x: x['date'])
    seen, ev2 = set(), []
    for e in ev:
        k = (e['date'], e['title'][:30])
        if k not in seen:
            seen.add(k)
            ev2.append(e)
    for e in ev2:
        if e['date'] in getattr(tx, 'EVSIG', {}):
            e['significance'] = tx.EVSIG[e['date']]
    nowlabel = getattr(tx, 'NOWLABEL', {})
    tiers = [{**r, 'current_status_2026': nowlabel.get(r['current_status_2026'], r['current_status_2026'])}
             for r in rd('data/shared/chip_tiers.csv')]
    geo = json.load(open(f'geo/{cfg["geo"]}'))
    viewbtns = ''.join(
        f'<button data-v="{v["id"]}" aria-pressed="{"true" if i == 0 else "false"}">{v["label"]}</button>'
        for i, v in enumerate(cfg['views']))
    body = open(f'markets/{slug}/body.html').read().replace('__VIEWBTNS__', viewbtns)
    nx = cfg.get('next')
    if nx:
        href = f'../{nx["slug"]}/index.html' if nx['slug'] else '../index.html'
        body = body.replace('<section id="sources">', f'<section id="next" class="nextpage"><span class="eyebrow">Where the story goes next</span><p class="read">{nx["text"]}</p><a class="more" href="{href}">{nx["label"]} →</a></section>\n\n<section id="sources">', 1)
    t = open('src/template.html').read()
    t = t.replace('__BODY__', body).replace('__NAV__', nav(slug)).replace('__TITLE__', cfg['title'])
    rep = {
        '__MARKET__': json.dumps(cfg, ensure_ascii=False).replace('</', '<\\/'),
        '__GEO__': json.dumps(geo, separators=(',', ':')),
        '__WORLD__': WORLD,
        '__COUNTRIES__': js(co, KEEP_CO),
        '__EVENTS__': js(ev2, KEEP_EV),
        '__SITES__': js(si, KEEP_SI),
        '__TIERS__': js(tiers),
        '__SPEED__': js(rd('data/shared/speed_chart.csv')),
        '__CAP__': js(rd(f'{d}/capacity_chart.csv')),
        '__MIX__': js(rd(f'{d}/mix_chart.csv') or rd(f'{d}/energy_mix.csv')),
    }
    for k, v in tx.TX.items():  # text first, data last
        t = t.replace(k, v)
    for k, v in rep.items():
        t = t.replace(k, v)
    left = sorted(set(re.findall(r'__[A-Z0-9_]{3,}__', t)))
    os.makedirs(f'docs/{slug}', exist_ok=True)
    open(f'docs/{slug}/index.html', 'w').write(t)
    print(f'{slug}: {len(t):,} bytes, {len(ev2)} events, {len(si)} sites, em dashes {t.count(chr(8212))}, unfilled {left}')
    return t


pages = {m: build_market(m) for m in markets}

# landing page (built by src/landing.py when present); until then the root shows Malaysia
if os.path.exists('src/landing.py'):
    spec = importlib.util.spec_from_file_location('landing', 'src/landing.py')
    landing = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(landing)
    landing.build(nav, configs, markets)
else:
    open('docs/index.html', 'w').write(pages['malaysia'].replace('../', ''))
    print('root: Malaysia page (no landing yet)')
