import importlib.util, os
_spec = importlib.util.spec_from_file_location('_my', os.path.join(os.path.dirname(__file__), '..', 'malaysia', 'texts.py'))
_my = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_my)

NOWLABEL = _my.NOWLABEL
TX = {k: _my.TX[k] for k in ['__GNOTE__', '__NOWCOL__', '__NOWDEFAULT__', '__TNOTE_JAN__']}
TX['__TNOTE_NOW__'] = _my.TX['__TNOTE_NOW__'].replace(', including Johor', ', including in Singapore')
TX['__SG_NOTE__'] = "Mid-2026 uses Knight Frank so both markets share a source; the two are effectively level. Singapore allocated about 80 MW in 2023 and 200 MW in August 2026 (EDB)."

TX['__CHIP_H2__'] = "The trusted hub is where the chip money is booked"
TX['__CHIP_LEDE__'] = (
    '<p class="read sub">Singapore was in the middle tier of the January 2025 US chip rule, alongside Malaysia and Thailand. '
    'It needs no US country licence today, but as the place where much of the region\'s chip trade is booked, it sits at the centre of Washington\'s diversion worries.</p>')
TX['__CHIP_BODY__'] = '''
  <div class="two">
    <div class="callout"><h3>Singapore's position today</h3>
      <p class="sub">Singapore is in US Country Group A:6, so it needs no country licence for advanced chips. As elsewhere, supplying a Chinese-parented buyer requires a US licence wherever it operates. In February 2025 Singapore charged three men in a US$390 million server fraud case reportedly linked to Nvidia chips.</p></div>
    <div class="callout"><h3>Megaspeed</h3>
      <p class="sub">Megaspeed is registered in Singapore, with its largest operation in Malaysia. Since October 2025 the New York Times and Bloomberg have reported US and Singapore investigations into whether it diverted Nvidia chips to China, and in November 2026 reports alleged larger flows through Singapore and Malaysia. These are allegations. Megaspeed denies any diversion, and nobody has been charged.</p></div>
  </div>
  <div class="stat">
    <div class="box"><b class="mono">~18%</b><span>Share of Nvidia's FY2025 revenue billed to Singapore, against under 2% of shipments</span></div>
    <div class="box"><b class="mono">US$390m</b><span>Value in the February 2025 server fraud case</span></div>
    <div class="box"><b class="mono">A:6</b><span>US country group, so no country licence needed</span></div>
  </div>
'''
TX['__ENERGY__'] = '''
  <h2>An island that imports all of its power fuel</h2>
  <p class="read sub">Singapore has no oil, no gas, no rivers for hydro and little room for solar. Gas makes 93% of its electricity, about half by pipeline from Indonesia and Malaysia and half as LNG. The Indonesian pipeline contracts run out by 2028, and Qatar's cargoes stopped in April 2026 when war hit the Gulf. Rationing data centres is partly an energy security decision.</p>
  <div class="stat">
    <div class="box"><b class="mono">93%</b><span>Power from gas, 2025 (EMA)</span></div>
    <div class="box"><b class="mono">~7%</b><span>Data centres' share of national electricity use (2024, latest official figure)</span></div>
    <div class="box"><b class="mono">~3 Mt/yr</b><span>Projected gas supply gap from 2028</span></div>
    <div class="box"><b class="mono">6 GW</b><span>Low-carbon electricity import target for 2035, raised from 4 GW in 2024</span></div>
  </div>
  <div class="figure"><h3>Where Singapore's power comes from</h3><svg id="mixchart" role="img" aria-label="Singapore generation mix by fuel"></svg>
    <div class="legend"><span><i style="background:var(--gas)"></i>Natural gas (imported)</span><span><i style="background:var(--oth)"></i>Oil and other (solar, waste, imports from 2022)</span></div>
    <p class="note">Energy Market Authority, fuel mix for electricity generation, yearly.</p></div>
  <div class="two">
    <div class="callout"><h3>The import route out</h3>
      <p class="sub">Singapore plans to import up to 6 GW of low-carbon power by 2035, has conditionally approved 3.4 GW from Indonesia and 1.75 GW from the Australia-Asia PowerLink, and began buying small volumes from Laos via Thailand and Malaysia in 2022 and from Malaysia's ENEGEM exchange in 2024. Most of these projects are still conditional.</p></div>
    <div class="callout"><h3>Compared with its neighbours</h3>
      <p class="sub">Singapore's whole grid is a gas import problem, so it guards each new megawatt. Malaysia and Thailand still have some domestic fuel and much more land, which is why the region's growth went to them. Singapore exports the hardest part of the energy problem to its neighbours and keeps the network, the contracts and the headquarters.</p></div>
  </div>
'''
