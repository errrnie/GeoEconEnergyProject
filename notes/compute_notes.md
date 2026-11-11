# Middle power compute: data notes

Built 10 Nov 2026. Companion to `countries.csv` (23 countries). Every number in the CSV was read from a source listed below. Nothing was estimated or interpolated, except two rows (Spain, Thailand) where I used market-level figures; those are flagged in the row notes.

## 1. Method

### Capacity (operational_gw, pipeline_gw)
- **Core 15 countries:** Cushman & Wakefield (C&W) data, analysed by Computer Weekly (Antony Adshead, "Data dive: A new American Century in the datacentre pipeline?", 15 Apr 2026), republished by OfficeChai (19 Sep 2026) and the Centre for British Progress report (18 Sep 2026).
  - The Computer Weekly article and the British Progress report were not reachable from this environment.
  - I re-opened the OfficeChai table twice; all 15 rows match the figures in the brief.
  - IT-Connect (23 Sep 2026) independently gives the US at about 32 GW operational, 70.6 GW pipeline and 102.6 GW total, Malaysia at 4.87 GW total and India at 5.1 GW, and dates the Computer Weekly piece to 15 Apr 2026.
  - "Pipeline" means under construction plus planned. Not all of it will be built.
- **The country rows look like sums of C&W's tracked metro markets, not national censuses.** Evidence: Ireland 1.27 GW equals C&W Dublin at 1,264 MW. Singapore, a single market, is 1,043 MW. Malaysia's 1.29 GW is close to Johor's 897 MW plus Greater KL.
- **The 8 added countries** come from the same C&W family where possible:
  - Singapore: C&W APAC H2 2025 market table. The market is the whole country.
  - Vietnam: C&W Vietnam, Apr 2026.
  - UAE: C&W 2025 Global Data Center Market Comparison (GDCMC).
  - Spain and Italy: C&W EMEA market tables in the 2026 France study, sourced from DC Byte and C&W.
  - Thailand: C&W Bangkok only, used as a proxy for the country.
  - Philippines (BMI) and Saudi Arabia (S&P Global) have no C&W national figure available, so they are marked non-C&W.
- **What I could not reach:** C&W GDCMC 2026 (May 2026) has market data for Bangkok, Manila, HCMC, Hanoi, Abu Dhabi, Dubai, Riyadh, Dammam, Jeddah, Madrid, Zaragoza, Barcelona and Milan. It sits in a flipbook with Infogram charts that this environment could not open. That is the best way to make the 8 added rows fully consistent.

### Cross-check (crosscheck_installed_gw)
- DC Market Insights, page updated 12 Oct 2026. Figures are installed IT load at end-2025, DCMI's own modelled estimates, rounded to 0.1 GW.
- I re-opened the page and confirmed 11 values.
- Thailand, Vietnam and the Philippines are not on DCMI's list, so those cells are blank.

### Build cost (build_cost_usd_m_per_mw)
- US$/W and US$m/MW are the same unit.
- **APAC rows** use the C&W APAC Data Centre Construction Cost Guide 2026, mid-range, mid-spec build, national level.
  - I chose it so Malaysia can be compared with its peers on one basis.
  - C&W does not say whether "per MW" means IT MW.
- **Non-APAC rows** use Turner & Townsend (T&T).
  - Basis is US$/W of IT load for a 60 MW air-cooled build-to-suit hyperscale site. It includes shell, fit-out, M&E and contractor costs. It excludes land, utility works, IT equipment and fees. FX is averaged Oct 2025 to Oct 2026.
  - The 2026-27 edition (Oct 2026, 62 markets) is used for the US national average (12.08) and Sao Paulo (11.66).
  - London, Frankfurt and Milan come from the 2025-26 edition via Il Sole 24 Ore. T&T says North America and Europe costs rose 13% in a year, so these three are probably understated against 2026-27 values.
- **Blank cells** (Canada, France, Ireland, Netherlands, Spain, UAE, Saudi Arabia): the full T&T 62-market chart and the C&W US/Canada guide could not be read. Figures for these countries appeared only as secondary citations (Dublin 10.0, Madrid 10.0, UAE 8.8, Saudi 10.8), which I left out.

### GPU share
- Epoch AI insight (published 5 Jun 2025, data as of May 2025): US about three-quarters, China 15%. Germany, Japan and France are described only as "marginal".
- The arXiv paper (Pilz et al. 2025, 2504.16026) gives the EU only in absolute terms: about 50,000 H100-equivalents, against 850,000 for the US and 110,000 for China (Mar 2025). EU is not a country row, so it is not in the CSV.
- No other country share could be verified. The Epoch GPU clusters dataset (gpu_clusters.csv) is deprecated and could not be downloaded here.

## 2. Conflicts between sources

| Country | Broker op GW (C&W) | DCMI installed GW | Ratio | Comment |
|---|---|---|---|---|
| China | 5.49 | 30.9 | 5.6x | Biggest conflict. C&W tracks a few colo metros (Beijing, Shanghai, etc.). DCMI counts all IT load, including the state, telco and hyperscaler self-build capacity that brokers do not see. Epoch says its dataset covers only 10-20% of Chinese AI supercomputer performance. |
| United States | 31.97 | 50.4 | 1.6x | Brokers miss enterprise, legacy and some self-build capacity. Knight Frank's global live total of 60.0 GW in 2025 suggests broker universes are much smaller than DCMI's 126.6 GW year-to-date total. |
| Germany | 1.40 | 3.0 | 2.1x | C&W covers Frankfurt and Berlin. DCMI includes enterprise and edge capacity spread across the country. |
| Italy | 0.207 (Milan) | 0.8 | 3.9x | The C&W figure covers Milan only. |
| Indonesia | 0.39 | 0.7 | 1.8x | |
| Malaysia, India, Australia | about equal | about equal | 1.0x | The two sources agree closely in the newest hyperscale-led markets. |

Other conflicts:
- **UAE:** C&W (Jun 2025) puts the whole country at "more than 250 MW" live. Knight Frank puts Abu Dhabi alone at 434 MW in 2025, and DCMI has 0.5 GW. The C&W number is stale and a lower bound.
- **Thailand:** C&W Bangkok was 113 MW operational at end-2025 and 134 MW in H1 2026. BMI's national figure is 216 MW in Q2 2026 (Bangkok 145.8 MW plus Chonburi 70 MW). For pipeline, C&W H1 2026 gives 2,084 MW and BMI gives 944 MW. BMI's own sub-figures add up to 1,202 MW, more than its 944 MW national total. Thailand's pipeline is very sensitive to the source.
- **Philippines:** BMI gives 140 MW (Sep 2026). Knight Frank Manila was 65 MW and C&W Manila 68 MW (H1 2025).
- **Saudi Arabia:** S&P gives 222 MW (Q1 2025), DCMI 0.4 GW and Knight Frank Riyadh 79 MW.
- **France:** C&W's own France study (Q3 2025) gives 943 MW operational and 1,275 MW pipeline. The Computer Weekly figures are 0.92 and 1.50 GW. The gap is small and comes from different vintages.
- **Build cost:** C&W and T&T differ for the same country by about 10-20%. Japan is 16.0 (C&W) against Tokyo 18.28 (T&T). Singapore 14.4 vs 15.39. India 7.4 vs Mumbai 6.83. China 7.1 vs Shanghai 5.79. Vietnam 7.2 vs HCMC 8.32. Australia 10.0 vs Sydney 10.74. Rankings are stable across the two sources; levels are not.

## 3. What the data says about Malaysia
- **Biggest pipeline outside the US:** 3.59 GW, ahead of India (3.53), Australia (3.33) and China (2.66). Its pipeline is 2.8 times its operational base.
- **Most capacity under construction in APAC:** 1,039 MW in H1 2026 (C&W). Johor alone went from 401 MW to 897 MW operational in 2025, and reached 1,110 MW in H1 2026.
- **Operational base is about the size of Ireland or Australia** (1.29 GW). Broker and DCMI figures agree (1.3 GW), so it is a well-measured market.
- **Mid-priced to build:** US$9.6m/MW (C&W mid). That is 40% below Singapore (14.4) and Japan (16.0), but above Thailand (8.8), Indonesia (8.3), India (7.4) and Vietnam (7.2). Its edge is power, land and speed next to Singapore, not the cheapest build.
- **Singapore is the counterpoint:** 1.04 GW operational but only 0.26 GW pipeline, held back by the moratorium. The overflow goes to Johor.

## 4. Gaps
1. C&W GDCMC 2026 market tables (the flipbook could not be read). These would make Thailand, Vietnam, the Philippines, UAE, Saudi Arabia, Spain and Italy consistent with the core 15.
2. Original Computer Weekly article (blocked). The core 15 are verified through two secondary outlets only.
3. Full T&T 2026-27 table of 62 markets. Missing: London, Frankfurt, Paris, Amsterdam, Dublin, Madrid, Toronto, Johor, Bangkok, Manila, Jakarta, Seoul, Dubai, Riyadh.
4. Greater Kuala Lumpur C&W figure. This would confirm Malaysia's 1.29 GW as Johor plus KL.
5. GPU performance share for any country besides the US and China.
6. Capacity dates differ across rows: Jun 2025 (UAE), Q1 2025 (Saudi Arabia), end-2025 (most rows) and Sep 2026 (Philippines). Treat cross-country comparisons as approximate.

## 5. Re-verification log (sources re-opened in a second pass)
1. OfficeChai: Malaysia 1.29/3.59, China 5.49/2.66, Indonesia 0.39/1.75, Ireland 1.27/0.82 and 6 more rows. All match.
2. DCMI: US 50.4, China 30.9, Malaysia 1.3, Singapore 1.5, Italy 0.8, Spain 0.5, UAE 0.5, Saudi Arabia 0.4, Indonesia 0.7, Germany 3.0, Japan 2.6. All match. Measure is IT load at end-2025.
3. C&W EMEA page 17: Madrid 228/100/316, Zaragoza 111/blank/498, Milan 207/148/651, Dublin 1,264. Match.
4. C&W Vietnam (second URL, Vietnamese version): 73 MW, 137 MW, cost 5.7/7.2/8.7. Match.
5. Il Sole 24 Ore (second URL): London 12.02, Frankfurt 11.60, Milan 9.79. Match.
6. C&W APAC H1 2026 (second URL): Malaysia 1,039 MW UC, Johor 1,110 MW op, Bangkok 134/859/2,084. Match.
7. Two sources each: Singapore 1,043/20/237 (C&W press release and DataCenterNews Asia); C&W cost table (C&W press release, DataCenterNews Asia, NextMSC); T&T Tokyo 18.28 and Singapore 15.39 (T&T and The Standard HK); HCMC 8.32, Mumbai 6.83, Shanghai 5.79 (T&T and The Standard HK).

## Sources
- OfficeChai: https://officechai.com/ai/us-has-more-datacenter-capacity-than-the-next-14-countries-combined-china-and-india-to-trail-in-2nd-3rd-place/
- IT-Connect: https://www.it-connect.tech/u-s-data-center-capacity-dwarfs-14-countries-combined/
- C&W APAC H2 2025: https://www.cushmanwakefield.com/en/singapore/news/2026/03/apac-data-centre-development-pipeline-hits-record-in-2025
- C&W APAC H1 2026: https://www.cushmanwakefield.com/en/singapore/news/2026/08/apac-dc-h1-2026
- C&W Vietnam: https://www.cushmanwakefield.com/en/vietnam/news/2026/03/vietnam-emerges-as-a-data-centre-growth-market
- C&W APAC cost guide 2026: https://www.cushmanwakefield.com/en/singapore/news/apac-dc-market-faces-structural-cost-shift-amid-rising-ai-requirements
- C&W EMEA market table (FR study 2026): https://digital.cushmanwakefield.com/etudedatacenter-05-2026-emea-fra-fr-content-trep-datacentres---/17/
- C&W UAE 2025: https://www.cushwake.ae/en/thoughtleadership/abu-dhabi-and-dubai-take-top-global-rankings-in-data-center-growth
- C&W GDCMC 2026 (Germany release, EMEA 11.4 GW): https://www.cushmanwakefield.com/en/germany/news/2026/05/global-data-center-market-comparison
- DCMI: https://www.dcmarketinsights.com/data/global-data-center-capacity
- Knight Frank Global Forecast 2026: https://content.knightfrank.com/research/2960/documents/en/data-centres-global-forecast-report-2026-12620.pdf
- BMI Thailand: https://technode.global/2026/06/23/thailand-data-center-capacity-set-to-quadruple-as-hyperscalers-drive-growth-bmi/
- BMI Philippines: https://technode.global/2026/09/28/philippines-data-center-pipeline-expands-as-ai-demand-drives-larger-campuses-bmi/
- S&P Saudi Arabia: https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-center-frontiers/saudi-arabia-data-center-market
- T&T 2026-27: https://www.turnerandtownsend.com/insights/data-centre-construction-cost-index-2026-27/ and https://www.turnerandtownsend.com/insights/asia-pacific-home-to-worlds-costliest-and-cost-effective-data-centre-markets/
- T&T methodology: https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2026-us/methodology
- The Standard HK (T&T): https://www.thestandard.com.hk/finance/article/346763/Asia-emerges-as-data-center-hotspot-Japan-ranks-priciest-for-construction
- Forbes Brasil (T&T): https://forbes.com.br/forbes-money/forbes-real-estate/2026/10/custo-construcao-data-centers-brasil/
- Il Sole 24 Ore (T&T 2025-26): https://en.ilsole24ore.com/art/building-milan-data-centre-costs-11-per-cent-less-than-european-average-AIHra7uB
- Epoch AI: https://epoch.ai/data-insights/ai-supercomputers-performance-share-by-country ; Trends in AI Supercomputers: https://arxiv.org/html/2504.16026v2
