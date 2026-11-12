import json
TX = {}

TX['__GNOTE__'] = (
    "‡ China and the United States come from SemiAnalysis's building-by-building model (Sep 2026; end-2026 estimate, IT power per its model page). "
    "The US pipeline covers 2027 deliveries only. China's pipeline counts projects with delivery dates and leaves out about 30 GW more that is only announced. "
    "As a rough cross-check, China counts racks at 2.5 kW each: 15.56 million racks in use (June 2026, conference report) at the industry ministry's 71.4% occupancy works out to about 28 GW. "
    "Most other countries are sums of the city markets tracked by brokers, mainly Cushman &amp; Wakefield (2025 to 2026), which miss self-built and telecom capacity, so those bars run lower and are not strictly comparable. "
    "Starred rows use partial sources. Dollars (est.): GW × each country's build cost per MW (Cushman &amp; Wakefield 2026 cost guide or Turner &amp; Townsend), building only, chips excluded; † uses a generic US$9.5m per MW where no country cost was found."
)

NOWLABEL = {
    'Licence-free (no country cap)': 'No licence needed',
    'Watch list: diversion concern': 'No licence needed, but flagged for diversion',
    'Licence required (presumption of approval)': 'Licence needed, usually approved',
    'Case-by-case licences / special deal': 'Licence or special deal',
    'Embargoed': 'Licence needed, usually denied',
}
NOWCOL = {
    'No licence needed': 'var(--t1)',
    'No licence needed, but flagged for diversion': 'var(--t2)',
    'Licence or special deal': 'var(--us)',
    'Licence needed, usually approved': 'var(--other)',
    'Licence needed, usually denied': 'var(--t3)',
    'Not checked': 'var(--t0)',
}
TX['__NOWCOL__'] = json.dumps(NOWCOL)
TX['__NOWDEFAULT__'] = 'Not checked'

TX['__CHIP_H2__'] = "Malaysia was put in the middle tier, and the US is still watching"
TX['__CHIP_LEDE__'] = (
    '<p class="read sub">In January 2025 the US sorted the world into three tiers for advanced AI chips. '
    'Close allies could buy freely, embargoed countries like China could not buy at all, and everyone in between, Malaysia included, '
    'faced a national cap. The rule was scrapped four months later, but the worry behind it, chips leaking to China through third countries, did not go away.</p>'
)
TX['__TNOTE_JAN__'] = (
    "AI Diffusion Rule, published 15 Jan 2025 (90 FR 4544), dropped on 13 May 2025, two days before companies had to comply. "
    "Tier 2 countries were capped at roughly 50,000 H100-equivalent chips for 2025 to 2027 (Council on Foreign Relations estimate), which could double with security commitments. "
    "Approved cloud firms based in Tier 1 countries could build in Tier 2 outside the cap, as long as at least 75% of their compute stayed in Tier 1 (50% in the US for US firms) and no more than 7% went to any one other country. "
    "Tier 2 is every country not named in Tier 1 or Tier 3."
)
TX['__TNOTE_NOW__'] = (
    "As of Nov 2026 nothing has replaced the tiers. The older 2023 rules still require licences for groups of countries of concern; countries in grey were not checked one by one. "
    "What matters is who the buyer is: since November 2023, supplying top chips to any company headquartered in China or Macau, or with a parent there, has required a US licence wherever it operates, including Johor. BIS confirmed in May 2026 that this still applies. "
    "A Commerce draft to require licences for Malaysia and Thailand was reported in July 2025 and reportedly shelved in August 2026. "
    "Main sources: BIS, Federal Register, Bloomberg, Baker McKenzie, Morgan Lewis."
)

TX['__CHIP_BODY__'] = '''
  <div class="two">
    <div class="callout"><h3>Malaysia's position today</h3>
      <p class="sub">As far as public records show, no US licence or cap applies to Malaysia as a country, although Commerce said in May 2025 it would add requirements for Malaysia and Thailand and has not published them. Instead Malaysia polices itself. Since 14 July 2025 anyone moving US AI chips out of or through Malaysia needs a Strategic Trade Permit, and the October 2025 US trade deal asked Malaysia to cooperate on US export controls, though that deal remains unratified and under review after the US Supreme Court struck down the tariffs behind it. The pressure now runs through ownership. Supplying top chips to a Chinese-parented tenant in Johor requires a US licence, while supplying a US hyperscaler next door does not.</p></div>
    <div class="callout"><h3>The Megaspeed case</h3>
      <p class="sub">Megaspeed, a Singapore cloud firm that began as the overseas arm of Chinese game company 7Road, ran a data centre in Sedenak, Johor, through a Malaysian unit, and its largest site was in Malaysia. Bloomberg counted at least US$4.6 billion and about 136,000 Nvidia GPUs imported by its Malaysian and Indonesian units from 2023 to November 2025, including about US$787 million of GB300s brought into Malaysia that November, after Nvidia says it stopped selling to the firm. US prosecutors are reportedly investigating. Nobody has been charged. Megaspeed denies any diversion and says on-site reviews by the US Commerce Department, Malaysia's trade ministry and Nvidia found no violations; Nvidia says it has no reason to believe its secrets were compromised. In February 2026 Bain's Bridge Data Centres, its Malaysian landlord, gave the 68.4 MW meant for Megaspeed to another tenant.</p></div>
  </div>
  <div class="stat">
    <div class="box"><b class="mono">US$4.6bn+</b><span>Nvidia hardware imported by Megaspeed's Malaysian and Indonesian units, 2023 to Nov 2025 (Bloomberg, reported)</span></div>
    <div class="box"><b class="mono">72</b><span>AI servers seized by Malaysian customs at KLIA, June 2026</span></div>
    <div class="box"><b class="mono">2</b><span>US criminal cases since Nov 2025 alleging chips or servers were routed to China via Malaysia</span></div>
  </div>
  <div class="callout"><h3>Why this is an energy security question too</h3>
    <p class="sub">Proven diversion, like the two US prosecutions involving Malaysia, invites tighter rules on the whole country, and tighter rules can leave powered buildings in Johor waiting for chips. TNB's five-year take-or-pay contracts protect the utility, but the land, water and new gas plants are committed either way. When the chips do arrive, they mostly serve foreign-owned clouds, while the electricity, water and grid risk stay in Malaysia.</p></div>
'''

# filled after remaining agents report
TX['__WHY_SG__'] = "Singapore paused new data centres from 2019 to 2022 and has since released only about 280 MW through two tenders. Johor, just across the strait, added about 700 MW in 18 months and drew level at about 1.1 GW in mid-2026."
TX['__WHY_SPEED__'] = "TNB's Green Lane, launched in August 2023, promised to cut the wait for a large high-voltage connection from 36 to 48 months to about 12. In Northern Virginia, Tokyo or Amsterdam the wait now runs 4 to 10 years."
TX['__WHY_COST__'] = "At about US$9.6 million per MW, Malaysia sits mid-table. It is far cheaper than Singapore (14.4) or Japan (16.0), but Thailand, Indonesia, India and Vietnam all build for less."
TX['__SG_NOTE__'] = "Mid-2026 uses Knight Frank so both markets share a source; the two are effectively level. Singapore allocated about 80 MW in 2023 and 200 MW in August 2026 (EDB)."
TX['__ENERGY__'] = '''
  <h2>The data centre bet is turning into a fuel import bet</h2>
  <p class="read sub">Peninsular Malaysia, where almost all the data centres sit, already makes most of its power from imported coal. It plans to retire that coal and build gas instead, just as its own gas fields decline. So more and more of each new megawatt of data centre load will run on imported LNG.</p>
  <div class="stat">
    <div class="box"><b class="mono">58.6%</b><span>Peninsular power from coal in 2025. Malaysia imported a record 36.3 Mt of coal, three quarters from Indonesia</span></div>
    <div class="box"><b class="mono">9 GW</b><span>New gas power the government now targets by 2030, mainly for demand growth</span></div>
    <div class="box"><b class="mono">2.26 Mt</b><span>LNG Malaysia imported in 2025 (about 3.2 Mt in 2024)</span></div>
    <div class="box"><b class="mono">~13%</b><span>Peninsular reserve margin once unavailable plant is excluded (The Edge). Official figure 25%</span></div>
  </div>
  <div class="figure"><h3>Where Peninsular power comes from</h3><svg id="mixchart" role="img" aria-label="Peninsular Malaysia generation mix by fuel"></svg>
    <div class="legend"><span><i style="background:var(--coal)"></i>Coal (imported)</span><span><i style="background:var(--gas)"></i>Gas</span><span><i style="background:var(--solar)"></i>Solar</span><span><i style="background:var(--hydro)"></i>Hydro and other</span></div>
    <p class="note">Grid System Operator data via The Star (8 Jan 2026) and Baird Maritime. In April 2026 a heatwave and data centre load pushed gas to 42.6%, its highest share since 2019, with record gas output.</p></div>
  <div class="figure"><h3>What data centres could add by 2030, in LNG</h3><svg id="scenchart" role="img" aria-label="Extra LNG needed in 2030 under three data centre scenarios"></svg>
    <div style="overflow-x:auto"><table class="sc"><thead><tr><th>Scenario (est.)</th><th>Data centre use, TWh</th><th>Share of 2030 Peninsular demand</th><th>Extra gas, bcm</th><th>Extra LNG, Mt</th></tr></thead><tbody id="scenrows"></tbody></table></div>
    <p class="note">Student estimates. Extra demand above 2026 (10.5 TWh) is assumed to be met by gas at the Peninsular fleet's 2024 heat rate (about 7.8 GJ per MWh, derived from Energy Commission and grid operator data, ±10%); 1 Mt LNG = 1.36 bcm. This is an upper bound: some demand will be met by coal until 2029 to 2031, by solar, and by domestic or Thai pipeline gas. Low: about 3 GW average load, extending the current draw trend. Mid: the government's own 2030 projection. High: all 8.3 GW with supply deals running at 85%. Share uses 2030 Peninsular demand of about 187 TWh, implied by the government's Mid projection being 21% of demand.</p></div>
  <div class="two">
    <div class="callout"><h3>Who carries the price risk</h3>
      <p class="sub">Malaysia's biggest new LNG contract, 2 million tonnes a year from Qatar from 2028, sits behind the Strait of Hormuz. When the strait was disrupted in March 2026, Asian LNG prices rose by about half. Fuel costs pass through a monthly surcharge, but about 85% of households are exempt, so heavier users, industry and data centres absorb most of the swing unless the government caps it. The government says data centres must pay for the grid they cause, but no published figures yet show they do.</p></div>
    <div class="callout"><h3>Energy in, compute out</h3>
      <p class="sub">The fuel is imported and burned in Malaysia, the emissions and water use stay in Malaysia, and the computing largely goes to foreign-owned clouds, American and Chinese. Malaysia is in effect exporting its electricity as compute. Whether that is a good deal depends on what it keeps: tariffs that cover the gas, local jobs, and a say over who uses the chips.</p></div>
  </div>
'''

SKIP_SECURITY_DATES = ['2026-06-05']
EVSIG = {'2024-05-02': 'Kicked off a run of more than US$12 billion in new hyperscaler pledges over the next five months.',
         '2025-12-22': 'Showed the scale of Nvidia hardware flowing to one firm under US scrutiny, though Bloomberg found no clear evidence of smuggling.',
         '2026-05-31': 'Confirmed that ownership, not location, decides chip access for Chinese-parented firms in Malaysia.'}
