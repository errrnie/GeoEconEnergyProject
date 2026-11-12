import importlib.util, os
_spec = importlib.util.spec_from_file_location('_my', os.path.join(os.path.dirname(__file__), '..', 'malaysia', 'texts.py'))
_my = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_my)

NOWLABEL = _my.NOWLABEL
TX = {k: _my.TX[k] for k in ['__GNOTE__', '__NOWCOL__', '__NOWDEFAULT__', '__TNOTE_JAN__']}
TX['__TNOTE_NOW__'] = _my.TX['__TNOTE_NOW__'].replace(', including Johor', ', including in Vietnam')
TX['__SG_NOTE__'] = ''

TX['__CHIP_H2__'] = "Already licensed before the AI rules, and named in a diversion report"
TX['__CHIP_LEDE__'] = (
    '<p class="read sub">Vietnam sat in the middle tier of the January 2025 US chip rule, like its neighbours. '
    'Unlike them, it already needed a US licence for advanced AI chips under rules issued in October 2023 (in force 17 November 2023), because the US lists it in a group of countries with arms-related controls. '
    'Those licences are usually approved, and the rule\'s rescission in May 2025 did not change that.</p>')
TX['__CHIP_BODY__'] = '''
  <div class="two">
    <div class="callout"><h3>US chips through local champions</h3>
      <p class="sub">Nvidia signed an agreement with the government in December 2024 to set up an AI research centre and an AI data centre, and FPT readied an AI factory with thousands of H100s the same month. Viettel put Vietnam's first Nvidia DGX B200 into service in February 2026. In the October 2025 trade framework, Vietnam asked to be taken off the US control lists that make these licences necessary.</p></div>
    <div class="callout"><h3>The diversion allegation</h3>
      <p class="sub">A September 2026 C4ADS report alleged that 50 shipments of restricted Nvidia GPUs, worth about US$13.4 million, were routed through Vietnam, India and Malaysia to Hong Kong and China in 2023 to 2025. These are allegations, and no Vietnamese firm was named. In August 2026, Chinese speakers at a forum in Hanoi offered to build AI factories with Chinese GPUs and capital; no government commitment was reported.</p></div>
  </div>
  <div class="stat">
    <div class="box"><b class="mono">Oct 2023</b><span>US licence needed for advanced AI chips, usually approved</span></div>
    <div class="box"><b class="mono">12.5%</b><span>US Section 301 tariff since July 2026, after the Supreme Court struck the earlier 20% rate</span></div>
    <div class="box"><b class="mono">40%</b><span>US tariff announced in July 2025 on goods transshipped through Vietnam</span></div>
  </div>
'''
TX['__ENERGY__'] = '''
  <h2>Vietnam's limit is the wire to the north, more than the fuel</h2>
  <p class="read sub">Vietnam runs on coal and water. In 2024 coal made about half its electricity and hydro more than a quarter, so a dry year hits hard. In May and June 2023 drought cut hydro, coal deliveries fell short and the north could not draw on surplus power in the south, leaving 900 GWh unmet. The government answered with a 591 km, 500 kV line built in six months. Data centres sit at both ends of that line, in Hanoi and Ho Chi Minh City.</p>
  <div class="stat">
    <div class="box"><b class="mono">49.5%</b><span>Power from coal in 2024, up from 46.2% in 2023 (EVN)</span></div>
    <div class="box"><b class="mono">28.7%</b><span>Power from hydro in 2024, the share a drought can take away</span></div>
    <div class="box"><b class="mono">US$1.4bn</b><span>Cost of the 2023 northern power shortages, about 0.3% of GDP (World Bank)</span></div>
    <div class="box"><b class="mono">5,000 MW</b><span>Central-to-north transfer after the 2024 line, double the earlier limit</span></div>
  </div>
  <div class="figure"><h3>Where Vietnam's power comes from</h3><svg id="mixchart" role="img" aria-label="Vietnam generation mix by fuel"></svg>
    <div class="legend"><span><i style="background:var(--coal)"></i>Coal</span><span><i style="background:var(--gas)"></i>Gas</span><span><i style="background:var(--solar)"></i>Renewables and hydro</span><span><i style="background:var(--oth)"></i>Oil</span><span><i style="background:var(--us)"></i>Imported power</span></div>
    <p class="note">EVN annual reports, power produced and bought by source. Hydro was 28.7% in both years; solar, wind and biomass were about 13%. No full-year fuel split for 2022 was found.</p></div>
  <div class="figure"><h3>What data centres could add by 2030, in LNG</h3><svg id="scenchart" role="img" aria-label="Extra LNG needed in 2030 under three data centre scenarios"></svg>
    <div style="overflow-x:auto"><table class="sc"><thead><tr><th>Scenario (est.)</th><th>Data centre use, TWh</th><th>Share of 2024 generation</th><th>Extra gas, bcm</th><th>Extra LNG, Mt</th></tr></thead><tbody id="scenrows"></tbody></table></div>
    <p class="note">Student estimates, same method as the other country pages. Demand above today's roughly 73 MW is assumed met by imported LNG, the fuel the revised power plan grows fastest (22.5 GW of LNG plants by 2030, with coal held at about 31 GW), at a 7.3 GJ/MWh heat rate. In 2024 coal met most new demand, so the real mix may be dirtier. Low: Cushman &amp; Wakefield's 73 MW operating plus 137 MW pipeline to 2030. Mid: the government's 870 MW aim. High: Savills' 950 MW forecast. Even the high case is about 2% of 2024 generation.</p></div>
  <div class="two">
    <div class="callout"><h3>Small load, weak links</h3>
      <p class="sub">Electricity sales grew 9% in 2024, about 23 TWh in one year. Every scenario above adds less than a third of that by 2030. The risk is where the load lands and when: a dry season, a coal shortfall or a congested line, plus a reported two to three years to connect 100 MW in the main clusters. A 2024 decree lets large users buy renewable power directly, and the first LNG plants, 1,624 MW at Nhon Trach, came online in 2025.</p></div>
    <div class="callout"><h3>Compared with its neighbours</h3>
      <p class="sub">Malaysia's high case needs about 7 Mt of extra LNG a year, Thailand's about 9 Mt. Vietnam's needs under 1 Mt because its data centre market is still small. Indonesia burns its own coal. If Vietnam's pipeline grows the way Johor's did, it will add LNG import exposure just as the country starts importing LNG for the first time.</p></div>
  </div>
'''
