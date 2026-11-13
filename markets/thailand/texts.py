import importlib.util, os
_spec = importlib.util.spec_from_file_location('_my', os.path.join(os.path.dirname(__file__), '..', 'malaysia', 'texts.py'))
_my = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_my)

NOWLABEL = _my.NOWLABEL
TX = {k: _my.TX[k] for k in ['__GNOTE__', '__NOWCOL__', '__NOWDEFAULT__', '__TNOTE_JAN__']}
TX['__TNOTE_NOW__'] = _my.TX['__TNOTE_NOW__'].replace(', including Johor', ', including in Thailand')

TX['__CHIP_H2__'] = "Thailand sits in the same middle tier, under the same suspicion"
TX['__CHIP_LEDE__'] = (
    '<p class="read sub">In January 2025 the US sorted the world into three tiers for advanced AI chips, and Thailand landed in the middle tier with Malaysia. '
    'The rule was rescinded four months later. Commerce then said it would add licence requirements for Malaysia and Thailand, and Bloomberg reported a draft in July 2025 that was reportedly shelved in August 2026. The worry behind it, chips leaking to China, now runs through Bangkok too.</p>')
TX['__CHIP_BODY__'] = '''
  <div class="two">
    <div class="callout"><h3>Thailand's position today</h3>
      <p class="sub">No US licence or cap applies to Thailand as a country. The July 2025 draft for Malaysia and Thailand was reportedly shelved in August 2026, and no rule was published. A November 2025 US case also charged four men with routing Nvidia A100s to China via Malaysia and Thailand. Thailand has tightened its own checks instead: from May 2026 the Board of Investment and Customs cut incentives for "pass-through" assembly and aimed to check all electronics trade, and a joint watch list with US customs grew to 67 items in June. As in Malaysia, a Chinese-parented buyer needs a US licence for top chips wherever it operates.</p></div>
    <div class="callout"><h3>The OBON and Siam AI case</h3>
      <p class="sub">In March 2026 US prosecutors charged a Supermicro co-founder and two others, alleging about US$2.5 billion of servers moved through a Southeast Asian "Company-1" in 2024 and 2025. Bloomberg's sources say Company-1 is OBON, a Bangkok firm that said in 2024 it created Siam AI, Thailand's first Nvidia cloud partner. People familiar with the matter told Bloomberg some servers allegedly went to Alibaba, which denies involvement. OBON has not been charged, and Siam AI says it imports GPUs for its own use and has separate headquarters from OBON.</p></div>
  </div>
  <div class="stat">
    <div class="box"><b class="mono">~US$2.5bn</b><span>Servers allegedly routed via a Southeast Asian intermediary, 2024 to 2025 (US indictment); Bloomberg's sources name a Bangkok firm</span></div>
    <div class="box"><b class="mono">67</b><span>Items on the joint Thai-US customs watch list from June 2026</span></div>
    <div class="box"><b class="mono">12.5%</b><span>US Section 301 tariff on most Thai goods since 24 July 2026, against 10% for Malaysia and Indonesia</span></div>
  </div>
'''
TX['__ENERGY__'] = '''
  <h2>Thailand already leans on imported LNG</h2>
  <p class="read sub">Gas makes most of Thailand's power, and the gas is running short at home. Gulf of Thailand output dipped around the 2022 Erawan handover and has partly recovered, Myanmar's pipeline supply is fading, and proved reserves would last under five years at current output. New data centre load therefore lands on an LNG import bill that is already large.</p>
  <div class="stat">
    <div class="box"><b class="mono">54 to 60%</b><span>Power from gas, 2024 to 2026 (EPPO); IEEFA's 65% counts gas in fuel terms</span></div>
    <div class="box"><b class="mono">~10.6 Mt</b><span>LNG imported in 2024 (EPPO-derived; trade data suggest about 11.5), about three times Malaysia's 3.2 Mt that year</span></div>
    <div class="box"><b class="mono">4.6 yrs</b><span>Life of proved gas reserves at end-2025 output</span></div>
    <div class="box"><b class="mono">~51 to 55%</b><span>Reserve margin (EPPO-derived and IEEFA), against a 15% standard</span></div>
  </div>
  <div class="figure"><h3>Where Thailand's power comes from</h3><svg id="mixchart" role="img" aria-label="Thailand generation mix by fuel"></svg>
    <div class="legend"><span><i style="background:var(--gas)"></i>Gas</span><span><i style="background:var(--coal)"></i>Coal and lignite</span><span><i style="background:var(--us)"></i>Imported power (mostly Laos hydro)</span><span><i style="background:var(--solar)"></i>Renewables and hydro</span><span><i style="background:var(--oth)"></i>Oil</span></div>
    <p class="note">Energy Policy and Planning Office (EPPO), Energy Statistics 2025.</p></div>
  <div class="figure"><h3>What data centres could add by 2030, in LNG</h3><svg id="scenchart" role="img" aria-label="Extra LNG needed in 2030 under three data centre scenarios"></svg>
    <div style="overflow-x:auto"><table class="sc"><thead><tr><th>Scenario (est.)</th><th>Data centre use, TWh</th><th>Share of 2024 generation</th><th>Extra gas, bcm</th><th>Extra LNG, Mt</th></tr></thead><tbody id="scenrows"></tbody></table></div>
    <p class="note">Student estimates, same method as the Malaysia page. Demand above today's roughly 0.9 TWh is assumed met by gas at 7.61 GJ per MWh (average of three RATCH combined-cycle plants, 2024); 1 Mt LNG = 1.36 bcm. Low: Ember's 6 TWh projection. Mid: the 2.87 GW planned pipeline fully online at 85% load. High: the 8.8 GW in the draft power plan's high-growth case fully online at 85% load, a stretch by 2030. An upper bound, since some load will be met by Laos hydro, solar and spare plant.</p></div>
  <div class="two">
    <div class="callout"><h3>Who pays</h3>
      <p class="sub">Thailand has chosen to bill data centres directly. In July 2026 the national energy policy council approved a separate tariff category for data centres, with a rate of about 5 to 6 baht per kWh expected against an average tariff of about 3.95, and the same day approved a grid-access bond of 4.5 million baht per MW. EGAT still carries about 31 billion baht of fuel costs it was not allowed to pass on to consumers.</p></div>
    <div class="callout"><h3>Compared with Malaysia</h3>
      <p class="sub">Malaysia's exposure today is mostly imported coal, and its data centre boom is pushing it toward LNG from a small base. Thailand imported about three times as much LNG as Malaysia in 2024, and about four and a half times as much in 2025, when Malaysia's imports fell to 2.26 Mt, so data centres add to a bill that is large and swings with world prices. Malaysia braked selectively, with water rules in Johor and a halt on non-AI projects, while honouring 8.3 GW of supply deals. Thailand stopped the clock on 166 projects and moved to charge data centres more for power. Thailand is trading speed for protection of households.</p></div>
  </div>
'''
TX['__SG_NOTE__'] = ''
