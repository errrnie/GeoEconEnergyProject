import importlib.util, os
_spec = importlib.util.spec_from_file_location('_my', os.path.join(os.path.dirname(__file__), '..', 'malaysia', 'texts.py'))
_my = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_my)

NOWLABEL = _my.NOWLABEL
TX = {k: _my.TX[k] for k in ['__GNOTE__', '__NOWCOL__', '__NOWDEFAULT__', '__TNOTE_JAN__']}
TX['__TNOTE_NOW__'] = _my.TX['__TNOTE_NOW__'].replace(', including Johor', ', including in the Philippines')
TX['__SG_NOTE__'] = ''

TX['__CHIP_H2__'] = "A treaty ally with no special chip treatment"
TX['__CHIP_LEDE__'] = (
    '<p class="read sub">The Philippines is a US treaty ally, yet the January 2025 US chip rule put it in the capped middle tier with its neighbours, not in the top tier with close allies. '
    'The rule was rescinded in May 2025 before compliance began, and today the Philippines needs no US country licence for advanced AI chips.</p>')
TX['__CHIP_BODY__'] = '''
  <div class="two">
    <div class="callout"><h3>Choosing a side in public</h3>
      <p class="sub">In April 2024 the US, Japan and the Philippines launched the Luzon Economic Corridor linking Subic, Clark, Manila and Batangas. In April 2026 the Philippines signed the US-led Pax Silica declaration on chip and AI supply chains, and a US-backed chip and AI hub has been proposed for New Clark City, on former US base land, though the state developer says it will host chip and electronics plants rather than large data centres. No other host on this site has aligned this openly.</p></div>
    <div class="callout"><h3>Alliance did not buy a better deal</h3>
      <p class="sub">Since July 2026 Philippine goods pay a 12.5% US Section 301 tariff, the same as Singapore, Thailand and Vietnam and above Malaysia and Indonesia at 10%. On chips, as everywhere, supplying a Chinese-parented buyer needs a US licence. No Philippine chip diversion case was found.</p></div>
  </div>
  <div class="stat">
    <div class="box"><b class="mono">Apr 2026</b><span>Signs the US-led Pax Silica declaration, the 13th country to do so</span></div>
    <div class="box"><b class="mono">12.5%</b><span>US Section 301 tariff since July 2026</span></div>
    <div class="box"><b class="mono">40%</b><span>Share of the national grid operator owned by State Grid Corporation of China</span></div>
  </div>
'''
TX['__ENERGY__'] = '''
  <h2>Coal carries the load, and new gas has to be imported</h2>
  <p class="read sub">The Philippines has little fuel of its own. Coal made 62.5% of power in 2024, up from 59.6% in 2022, and the Malampaya gas field that feeds the Batangas plants was expected to run dry around 2027, so the country began importing LNG in April 2023. New Malampaya wells began flowing in November 2026 and should extend output to about 2034, but LNG imports keep rising. Luzon, where almost every data centre sits, saw peak demand rise 11.7% in 2024, and in April that year forced outages at 19 plants put the grid on red alert with rotating brownouts.</p>
  <div class="stat">
    <div class="box"><b class="mono">62.5%</b><span>Power from coal in 2024 (Department of Energy)</span></div>
    <div class="box"><b class="mono">~2034</b><span>Malampaya gas field's new expected end of output, after new wells came online in Nov 2026 (Department of Energy)</span></div>
    <div class="box"><b class="mono">US$0.21</b><span>Residential power per kWh, second only to Singapore in the region (World Bank)</span></div>
    <div class="box"><b class="mono">40%</b><span>Share of the grid operator NGCP owned by State Grid of China</span></div>
  </div>
  <div class="figure"><h3>Where the Philippines' power comes from</h3><svg id="mixchart" role="img" aria-label="Philippines generation mix by fuel"></svg>
    <div class="legend"><span><i style="background:var(--coal)"></i>Coal</span><span><i style="background:var(--gas)"></i>Gas</span><span><i style="background:var(--solar)"></i>Renewables and hydro</span><span><i style="background:var(--oth)"></i>Oil</span></div>
    <p class="note">Department of Energy, 2024 Power Statistics Summary. Renewables and hydro add up geothermal, hydro, wind, solar and biomass; geothermal and hydro alone made about 17% in 2024.</p></div>
  <div class="figure"><h3>What data centres could add by 2030, in LNG</h3><svg id="scenchart" role="img" aria-label="Extra LNG needed in 2030 under three data centre scenarios"></svg>
    <div style="overflow-x:auto"><table class="sc"><thead><tr><th>Scenario (est.)</th><th>Data centre use, TWh</th><th>Share of 2024 generation</th><th>Extra gas, bcm</th><th>Extra LNG, Mt</th></tr></thead><tbody id="scenrows"></tbody></table></div>
    <p class="note">Student estimates, same method as the other country pages. Demand above today's roughly 140 MW is assumed met by imported LNG at a 7.3 GJ/MWh heat rate, since domestic gas is in decline. Coal still dominates, so the real mix may be dirtier. Low: BMI's 140 MW operating plus 43 MW under construction and 221 MW planned. Mid: the 1.2 GW of applications Meralco reported in 2024. High: the masterplan's 1.5 GW, a 2033 target pulled forward to 2030 as a stretch. The dashed line is the 1.17 Mt of LNG the country was expected to import in 2024 (GIIGNL).</p></div>
  <div class="two">
    <div class="callout"><h3>Expensive power is the brake</h3>
      <p class="sub">The World Bank puts residential power at about US$0.21 per kWh, against US$0.05 in Malaysia and US$0.09 in Indonesia. Meralco says large users can get about 11 US cents, comparable to Thailand and Malaysia, but SM Investments said in 2025 it would sell its stake in YCO Cloud, calling power very expensive. The Department of Energy said Philippine rates were the highest in ASEAN in June 2026. A 10.2 GW green energy auction, mostly solar and due online between 2026 and 2029, helps but does not give round-the-clock supply.</p></div>
    <div class="callout"><h3>Compared with its neighbours</h3>
      <p class="sub">The mid case alone would need about as much extra LNG as the Philippines was expected to import in all of 2024. Malaysia and Thailand already import far more LNG, and Indonesia burns its own coal. The Philippines is closest to Vietnam, a small market just starting on imported LNG, but with power prices near Singapore's.</p></div>
  </div>
'''
