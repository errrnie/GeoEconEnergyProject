import csv, json, os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
sys.path.insert(0, 'src')
from texts import TX, NOWLABEL  # placeholder -> html text

rd = lambda f: list(csv.DictReader(open('data/' + f))) if os.path.exists('data/' + f) else []
j = lambda rows, k=None: json.dumps([{a: r.get(a, '') for a in k} for r in rows] if k else rows, ensure_ascii=False).replace('</', '<\\/')

co = rd('countries.csv')
for f in rd('countries_apply.csv'):  # curated fixes: country,field,new_value
    for r in co:
        if r['country'] == f['country']:
            r[f['field']] = f['new_value']
si = rd('sites.csv')
fix = {r['site_name']: r for r in rd('sites_coords.csv')}
for r in si:
    if r['site_name'] in fix and fix[r['site_name']]['lat']:
        f = fix[r['site_name']]
        r['lat'], r['lon'], r['latlon_precision'] = f['lat'], f['lon'], f['latlon_precision']
base = rd('events.csv'); bd = {e['date'] for e in base} | {'2026-06-05'}
ev = sorted(base + [e for e in rd('security_events.csv') if e['date'] not in bd], key=lambda x: x['date'])
seen = set(); ev2 = []
for e in ev:
    k = (e['date'], e['title'][:30])
    if k not in seen:
        seen.add(k); ev2.append(e)

SIG={'2024-05-02':'Kicked off a run of more than US$12 billion in new hyperscaler pledges over the next five months.','2025-12-22':'Showed the scale of Nvidia hardware flowing to one firm under US scrutiny, though Bloomberg found no clear evidence of smuggling.','2026-05-31':'Confirmed that ownership, not location, decides chip access for Chinese-parented firms in Malaysia.'}
for e in ev2:
    if e['date'] in SIG: e['significance']=SIG[e['date']]
keep_ev = ['date', 'date_precision', 'track', 'title', 'description', 'amount_usd_m', 'significance', 'source_url', 'source_name']
keep_si = ['site_name', 'operator', 'owner_investors', 'anchor_tenant', 'stack', 'state', 'town', 'lat', 'lon', 'latlon_precision', 'it_mw', 'mw_type', 'status', 'source_url', 'confidence']
keep_co = ['country', 'operational_gw', 'pipeline_gw', 'capacity_source', 'capacity_source_url', 'crosscheck_installed_gw', 'build_cost_usd_m_per_mw', 'confidence']

t = open('src/template.html').read()
rep = {
    '__GEO__': open('geo/geo.json').read(),
    '__WORLD__': open('geo/world.json').read(),
    '__COUNTRIES__': j(co, keep_co),
    '__EVENTS__': j(ev2, keep_ev),
    '__SITES__': j(si, keep_si),
    '__TIERS__': j([{**r,'current_status_2026':NOWLABEL.get(r['current_status_2026'],r['current_status_2026'])} for r in rd('chip_tiers.csv')]),
    '__SPEED__': j(rd('speed_chart.csv')),
    '__JOHOR__': j(rd('johor_chart.csv')),
    '__MIX__': j(rd('energy_mix.csv')),
}
rep.update(TX)
for k, v in rep.items():
    t = t.replace(k, v)
left = [w for w in set(__import__('re').findall(r'__[A-Z_]{3,}__', t))]
open('docs/index.html', 'w').write(t)
print('bytes', len(t), 'em dashes', t.count('—'), 'unfilled', left, 'events', len(ev2))
