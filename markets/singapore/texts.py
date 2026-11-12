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
      <p class="sub">Singapore is not in the US groups of countries of concern (it sits in A:6), so it needs no country licence for advanced chips. A Commerce draft on Chinese remote access to compute abroad, reported in August 2026, names Singapore as an example; nothing has been published. As elsewhere, supplying a Chinese-parented buyer requires a US licence wherever it operates. In February 2025 Singapore charged three men in a server fraud case reportedly linked to Nvidia chips; prosecutors later cited US$390 million of transactions. More people and companies were charged in 2026, and all charges are pending.</p></div>
    <div class="callout"><h3>Megaspeed</h3>
      <p class="sub">Megaspeed is registered in Singapore, and its Malaysian affiliate, Speedmatrix, made most of the reported chip purchases. Customs records analysed by Bloomberg show its Malaysian and Indonesian units imported at least US$4.6 billion of Nvidia hardware from 2023 to November 2025, and in November 2026 The Information alleged at least US$7.5 billion moved through Megaspeed and Speedmatrix, a wider measure. Singapore police are investigating suspected breaches of domestic law. These are allegations. As of 11 November 2026 nobody had been charged, and Megaspeed denies wrongdoing. The Malaysia page has the full story.</p></div>
  </div>
  <div class="stat">
    <div class="box"><b class="mono">~18%</b><span>Share of Nvidia's FY2025 revenue billed to Singapore, against under 2% from products shipped there</span></div>
    <div class="box"><b class="mono">US$390m</b><span>Transactions cited in the 2025 server fraud case (charges pending)</span></div>
    <div class="box"><b class="mono">A:6</b><span>Not in the US groups of concern, so no country licence needed</span></div>
  </div>
'''
TX['__ENERGY__'] = '''
  <h2>An island that imports almost all of its power fuel</h2>
  <p class="read sub">Singapore has no oil, no gas, no rivers for hydro and little room for solar. Gas makes 93% of its electricity, about half by pipeline from Indonesia and Malaysia and half as LNG. The Indonesian pipeline contracts run out by 2028, and Qatar's cargoes stopped in April 2026 when war hit the Gulf. Rationing data centres is partly an energy security decision.</p>
  <div class="stat">
    <div class="box"><b class="mono">93%</b><span>Power from gas, 2025 (EMA)</span></div>
    <div class="box"><b class="mono">~7%</b><span>Data centres' share of electricity use in 2020, the last official share; recent estimates for 2024 are above 10%</span></div>
    <div class="box"><b class="mono">~3 Mt/yr</b><span>Gas supply gap in 2028 to 2029, rising to about 6 Mt by 2035 (reported by The Star, Oct 2026)</span></div>
    <div class="box"><b class="mono">6 GW</b><span>Low-carbon electricity import target for 2035, raised from 4 GW in 2024</span></div>
  </div>
  <div class="figure"><h3>Where Singapore's power comes from</h3><svg id="mixchart" role="img" aria-label="Singapore generation mix by fuel"></svg>
    <div class="legend"><span><i style="background:var(--gas)"></i>Natural gas (imported)</span><span><i style="background:var(--oth)"></i>Oil and other (solar, waste, some coal, imports from 2022)</span></div>
    <p class="note">Energy Market Authority, fuel mix for electricity generation, yearly.</p></div>
  <div class="two">
    <div class="callout"><h3>The import route out</h3>
      <p class="sub">Singapore plans to import up to 6 GW of low-carbon power by 2035, has conditional licences or approvals for 3.4 GW from Indonesia and 1.75 GW from the Australia-Asia PowerLink, and began buying small volumes from Laos via Thailand and Malaysia in 2022 and from Malaysia's ENEGEM exchange in 2024. Most of these projects are still conditional.</p></div>
    <div class="callout"><h3>Compared with its neighbours</h3>
      <p class="sub">Singapore's whole grid is a gas import problem, so it guards each new megawatt. Malaysia and Thailand still have some domestic fuel and much more land, which is why the region's growth went to them. Singapore exports the hardest part of the energy problem to its neighbours and keeps the network, the contracts and the headquarters.</p></div>
  </div>
'''
