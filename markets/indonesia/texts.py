import importlib.util, os
_spec = importlib.util.spec_from_file_location('_my', os.path.join(os.path.dirname(__file__), '..', 'malaysia', 'texts.py'))
_my = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_my)

NOWLABEL = _my.NOWLABEL
TX = {k: _my.TX[k] for k in ['__GNOTE__', '__NOWCOL__', '__NOWDEFAULT__', '__TNOTE_JAN__']}
TX['__TNOTE_NOW__'] = _my.TX['__TNOTE_NOW__'].replace(', including Johor', ', including in Indonesia')
TX['__SG_NOTE__'] = ''

TX['__CHIP_H2__'] = "Never singled out on chips, but not out of the picture"
TX['__CHIP_LEDE__'] = (
    '<p class="read sub">Indonesia sat in the middle tier of the January 2025 US chip rule with its neighbours. '
    'Unlike Malaysia and Thailand, it was never the target of a country-specific US draft, and it needs no US country licence for AI chips today.</p>')
TX['__CHIP_BODY__'] = '''
  <div class="two">
    <div class="callout"><h3>Indonesia's position today</h3>
      <p class="sub">Indonesia is outside the US country groups that need licences for advanced chips, and no Indonesian enforcement case on AI chips was found. As everywhere, supplying a Chinese-parented buyer requires a US licence. Indonesia joined BRICS as a full member in January 2025, and its February 2026 trade deal with Washington is signed but not in force; Indonesian goods now pay a 10% US duty.</p></div>
    <div class="callout"><h3>Megaspeed's Indonesian unit</h3>
      <p class="sub">Bloomberg's analysis of customs records says Singapore-based Megaspeed's affiliates in Malaysia and Indonesia imported at least US$4.6 billion of Nvidia hardware in 2023 to 2025, without splitting the figure between the two. US and Singapore investigations are reported as ongoing. These are allegations. Megaspeed denies any diversion, and no Indonesian case has been reported.</p></div>
  </div>
  <div class="stat">
    <div class="box"><b class="mono">Jan 2025</b><span>Indonesia joins BRICS as a full member</span></div>
    <div class="box"><b class="mono">10%</b><span>US duty on most Indonesian goods since July 2026; the 2026 trade deal is not yet in force</span></div>
    <div class="box"><b class="mono">~75%</b><span>Share of Indonesia's nickel refining controlled by Chinese firms</span></div>
  </div>
'''
TX['__ENERGY__'] = '''
  <h2>On Java, the data centre bet is a coal bet</h2>
  <p class="read sub">Indonesia is rich in coal and gas, and its data centres get the coal. Coal made about two thirds of national power in 2025, above the government's own target, and PLN buys it at a capped price. Almost all data centre load sits on the Java-Bali grid, which runs about 60% on coal. Batam is the exception, a separate gas-fired island grid now being fed with Natuna gas that once went to Singapore.</p>
  <div class="stat">
    <div class="box"><b class="mono">~67%</b><span>National power from coal, 2025 (including captive plants)</span></div>
    <div class="box"><b class="mono">~60%</b><span>Coal share on the Java-Madura-Bali grid, 2025</span></div>
    <div class="box"><b class="mono">844 MW</b><span>Batam's grid capability; DayOne's 450 MW deal is 53% of it</span></div>
    <div class="box"><b class="mono">80%</b><span>Batam's water from one reservoir, Duriangkang; residents blockaded Nongsa Digital Park in October 2026</span></div>
  </div>
  <div class="figure"><h3>Where Indonesia's power comes from</h3><svg id="mixchart" role="img" aria-label="Indonesia generation mix by fuel"></svg>
    <div class="legend"><span><i style="background:var(--coal)"></i>Coal</span><span><i style="background:var(--gas)"></i>Gas</span><span><i style="background:var(--solar)"></i>Renewables and hydro</span><span><i style="background:var(--oth)"></i>Oil</span><span><i style="background:var(--us)"></i>Imported power</span></div>
    <p class="note">PLN RUPTL 2025-2034 shares applied to energy ministry (HEESI) totals, PLN grid only. Captive coal plants at nickel smelters add another 100 to 137 TWh a year on top.</p></div>
  <div class="figure"><h3>What data centres could add by 2030, in coal</h3><svg id="scenchart" role="img" aria-label="Extra coal needed in 2030 under three data centre scenarios"></svg>
    <div style="overflow-x:auto"><table class="sc"><thead><tr><th>Scenario (est.)</th><th>Data centre use, TWh</th><th>Share of 2025 generation</th><th>Extra coal, PJ</th><th>Extra coal, Mt</th></tr></thead><tbody id="scenrows"></tbody></table></div>
    <p class="note">Student estimates, same method as the other country pages but with coal as the marginal fuel on Java. Demand above today's roughly 4.3 TWh (580 MW) is assumed met by coal at PLN's 2,680 kcal/kWh heat rate and 4,500 kcal/kg coal. Low: the industry's January 2026 forecast of 2.7 GW. Mid: PLN's 3.5 GW. High: the industry's September 2026 forecast of 11 GW, a stretch by 2030. If met by gas instead, the cases need 2.7, 3.7 and 13.0 Mt of LNG. Power plants burned about 139 Mt of coal in 2024.</p></div>
  <div class="two">
    <div class="callout"><h3>Cheap power, slow connections</h3>
      <p class="sub">Capped coal keeps power cheap, about 6.3 US cents per kWh by one broker estimate. The constraint is time: about 36 months for a large connection, and a planning reserve on Java that falls toward 33% by 2027. The national power plan adds no fossil capacity on Java after 2029, and of US$21.4 billion pledged under the clean-energy transition partnership, only about US$3.1 billion has been approved.</p></div>
    <div class="callout"><h3>Compared with its neighbours</h3>
      <p class="sub">Malaysia and Thailand will meet extra data centre load mostly with imported LNG. Indonesia meets it with its own coal, and in Batam with gas held back from export. That makes Indonesia the most fuel-secure of the region's hosts and the most carbon-heavy, and its bottleneck is connecting to the grid rather than paying for fuel.</p></div>
  </div>
'''
