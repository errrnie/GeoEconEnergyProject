# Macro fact-check: regional story and two macro claims

Checked 12 Nov 2026 against `data/region/story.md`, `countries.csv`, `hubs.csv`, `timeline.csv` and sources re-opened online. "Re-checked" means I opened the source in this pass. "Project-verified" means the claim matches `timeline.csv` or earlier notes and I did not re-open it.

## (a) Claim table, problems first

### Phase verdict in one paragraph

The four phases are broadly right, but two need fixing. Phase 2 (2019 to 2022) is when Singapore paused and developers bought land in Johor. Johor was then almost empty: AMRO says its capacity was "almost zero" in 2020 and about 397MW in 2024, and Cushman & Wakefield (C&W) has it going from 401MW to 897MW in 2025 alone. So the spillover was decided in 2019 to 2022 but built in 2023 to 2025, when AI demand arrived. Phase 1 also misses the Chinese first wave: Alibaba Cloud chose Singapore as its overseas HQ in 2015, and Huawei, Alibaba and Tencent entered Malaysia in 2017 to 2020, before US export controls existed. The phase 3 causal link from export controls to "both camps could build" is too strong; Chinese clouds were already there, and controls mainly added a later wave of Chinese AI training demand (2025 onward).

### Problems

| # | Claim (story.md) | Verdict | What sources say | Suggested fix | URL |
|---|---|---|---|---|---|
| 1 | Phase 2: "Demand did not wait. It went across the causeway to Johor" (dated 2019 to 2022) | OVERSTATED (timing) | AMRO: Johor capacity "almost zero" in 2020; 396.9MW across 12 sites in 2024 (Table A1.1). C&W: Johor 401MW to 897MW operational during 2025. ISEAS: GDS (now DayOne) announced 54MW in Johor in Jul 2021; Bridge and ByteDance opened a facility in Oct 2022. | "Developers began buying land in Johor during the pause (GDS announced its first 54MW there in 2021), but most of Johor's capacity was built after 2023." | https://amro-asia.org/wp-content/uploads/2026/05/Malaysia-ACR-2026-SI-1-Data-Center-Boom-in-Malaysia.pdf ; https://www.cushmanwakefield.com/en/Singapore/news/2026/03/apac-data-centre-development-pipeline-hits-record-in-2025 ; https://www.iseas.edu.sg/wp-content/uploads/2026/08/TRS22_26.pdf |
| 2 | "By mid-2026 Johor had 1,110MW operating, more than Singapore's 1,068MW" | OVERSTATED (source-dependent) | C&W H1 2026 (via Katadata): Johor 1,110MW, Singapore 1,068MW. Knight Frank Data Centre Atlas 2026: Johor 1,110MW live but Singapore 1,118MW. On Knight Frank, Singapore is still slightly larger. | "about level with Singapore (1,068 to 1,118MW, depending on the source)" | https://databoks.katadata.co.id/en/technology-telecommunications/statistics/6ac764678fadc/asia-pacific-data-center-key-markets-h1-2026-jakarta-makes-the-list ; https://www.knightfrank.co.uk/site-assets/research/report-pdfs/data-centres/data-centre-atlas-2026.pdf |
| 3 | "Malaysia had 1,039MW under construction, the most in Asia Pacific" | OVERSTATED | C&W H1 2026 (re-checked): "Malaysia leads with 1,039 megawatts (MW) under construction, followed by Thailand at 859MW." The sentence sits in the Southeast Asia paragraph; the release gives no APAC-wide ranking. SEA holds "approximately 50%" of APAC under-construction capacity (4.8GW). | "the most in Southeast Asia, which holds about half of Asia Pacific's capacity under construction" | https://www.cushmanwakefield.com/en/singapore/news/2026/08/apac-dc-h1-2026 |
| 4 | Phase 3: export controls split the chip world, so "Southeast Asia became a place both camps could build. ISEAS calls Malaysia a 'dual-stack' host" | OVERSTATED (causal) | ISEAS dates a Chinese "first wave" to 2017 to 2020 (Huawei Mar 2017, Alibaba Oct 2017, Tencent Aug 2020) and treats US export controls as a risk to Malaysia, not a driver of the boom. AMRO does say "US-China tech decoupling" made Malaysia appealing. The clearest control-driven demand came later: FT (27 Nov 2025) reports Alibaba and ByteDance training models in Southeast Asian data centres, rising after the April 2025 H20 curbs; WSJ via Tom's Hardware (13 Mar 2026) reports ByteDance access to 36,000 B200s through Malaysia's Aolani Cloud, which Nvidia says is compliant. | "Chinese clouds arrived first (2015 to 2020). Export controls later added a new reason to build: Chinese firms can legally rent Nvidia capacity in Southeast Asia that they cannot import at home." | https://www.iseas.edu.sg/wp-content/uploads/2026/08/TRS22_26.pdf ; https://www.irishtimes.com/business/2025/11/27/chinas-tech-giants-take-ai-model-training-offshore-to-tap-nvidia-chips ; https://www.tomshardware.com/pc-components/gpus/chinas-bytedance-to-access-36-000-blackwell-gpu-cluster-through-malaysia-cloud-operator-nvidia-confirms-no-objections-deal-is-in-line-with-us-export-controls |
| 5 | Takeaway 2: "Speed to power, more than tax breaks, decided where AI capacity landed" | UNSOURCED | No source ranks power above incentives. ISEAS lists low land, water and power costs, DESAC incentives, Green Lane, the AI capex race and fast colocation builds. AMRO lists proximity, the lowest average tariff in ASEAN-5, and DESAC and Malaysia Digital incentives. CBRE (May 2026) gives partial support: "access to power is increasingly outweighing traditional location advantages." | "Fast power, cheap land and power, and a next-door cable hub decided where capacity landed; incentives helped." | https://www.iseas.edu.sg/wp-content/uploads/2026/08/TRS22_26.pdf ; https://amro-asia.org/wp-content/uploads/2026/05/Malaysia-ACR-2026-SI-1-Data-Center-Boom-in-Malaysia.pdf ; https://w.media/malaysia-and-india-top-growth-as-power-availability-redraws-data-center-footprint-cbre/ |
| 6 | Takeaway 3: "US-China decoupling made Southeast Asia a neutral host for both stacks" | OVERSTATED | ISEAS calls dual-stack infrastructure "geopolitically contentious." Malaysia began requiring permits for US AI chip exports in Jul 2025 (MITI). Singapore charged three men on 27 Feb 2025 in a fraud case over servers likely containing Nvidia chips. Hosts are policing US rules, which is not neutrality. | "Southeast Asia hosts both stacks, and doing so now means policing US chip rules." | https://www.iseas.edu.sg/wp-content/uploads/2026/08/TRS22_26.pdf ; https://www.thestar.com.my/aseanplus/aseanplus-news/2025/02/27/three-men-charged-with-fraud-in-singapore-case-allegedly-linked-to-nvidia-chips |
| 7 | Phase 1: "with a few Chinese clouds such as Alibaba in Kuala Lumpur from 2017" | MISSING | Alibaba Cloud press release (19 Aug 2015): Singapore data centre to open in early Sep 2015; "Singapore to become Alibaba Cloud's overseas headquarters." ISEAS: Huawei's ~US$120m Malaysia investment in Mar 2017 started a Chinese first wave. | Add Alibaba Singapore (2015) and the Chinese first wave in Malaysia (2017 to 2020). | https://www.alibabacloud.com/press-room/aliyun-to-open-singapore-cloud-data-center-to-serve-southeast |
| 8 | Phase 1: Singapore as "connectivity and business hub" (no driver given) | MISSING | AMRO cites Singapore's "dense network of undersea cables and landing sites" as the reason nearby Malaysia gets low latency. Cables explain both the hub and why overflow stayed next door. | Name subsea cables as the reason the hub, and its overflow, sit where they do. | https://amro-asia.org/wp-content/uploads/2026/05/Malaysia-ACR-2026-SI-1-Data-Center-Boom-in-Malaysia.pdf |
| 9 | "US clouds began building in-country regions where data rules and market size justified it: Jakarta" | OVERSTATED | Indonesia's GR 71/2019 (Oct 2019) relaxed localisation: private operators may host abroad; localisation stays for public bodies (and sector rules for banking). So Jakarta regions came just after the general rule was loosened; market size and public-sector and finance demand fit better. | "Indonesia's market size, plus localisation rules that still bind the public sector and banks, pulled in Google (2020) and AWS (2021)." | https://www.ahp.id/client-update-25-october-2019/ |
| 10 | Phase 4: "Hosts then started braking themselves" (Johor, Thailand, Singapore) | MISSING | Not mentioned: Malaysia's federal halt on non-AI data centre approvals (24 Feb 2026, in timeline.csv); Malaysia's July 2025 tariff revision, which AMRO says may lift data centre bills 10 to 14%; Malaysia's chip export permits (Jul 2025). Also, Singapore braked first, in 2019. | Add the tariff revision and federal halt; say the brakes are now region-wide. | https://amro-asia.org/wp-content/uploads/2026/05/Malaysia-ACR-2026-SI-1-Data-Center-Boom-in-Malaysia.pdf ; https://thesun.my/news/malaysia-news/govt-halts-non-ai-data-centre-approvals-over-energy-water-concerns-says-pm-anwar |
| 11 | Phase 3: "AI made data centres bigger and hungrier for power" (no capex driver) | MISSING | ISEAS names the "ChatGPT-driven AI capex race," with Microsoft and Google commitments encouraging AWS and Oracle to follow. Synergy (Mar 2025): capacity growth is driven by ever-larger new sites, "supercharged" by AI. | Name the hyperscaler capex race as the driver of the 2024 pledges. | https://www.iseas.edu.sg/wp-content/uploads/2026/08/TRS22_26.pdf ; https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity |
| 12 | Whole story: no ESG or emissions angle | MISSING | Ember (27 May 2025): Malaysia's data centre demand 9TWh (2024) to 68TWh (2030); related emissions 5.9 to 40 MtCO2e. Singapore's 2026 award winners each committed to source over 50% green energy (EDB, per project notes). | One sentence on emissions and green-power conditions. | https://ember-energy.org/latest-insights/from-ai-to-emissions-aligning-asean-digital-growth-with-energy-transition/ ; https://www.edb.gov.sg/en/news-and-insights/four-data-centre-proposals-selected-as-part-of-second-data-centre |
| 13 | "In 2019 Singapore stopped approving new data centres because they used too much land, water and energy" | OVERSTATED (minor) | Computer Weekly (re-checked): moratorium "amid concerns about the growing carbon footprint of datacentres," which are "intensive users of resources like land, water and energy." | "over their carbon footprint and heavy use of land, water and energy" | https://www.computerweekly.com/news/252522992/Singapore-to-restart-datacentre-builds-with-sustainability-focus |
| 14 | "No other market combined proximity, power and speed" | UNSOURCED (judgment) | Reasonable, and Batam is the obvious test (next door, but ~8MW live in 2025 and no large power deal until Apr 2026). Label it as the author's reading. | Keep, but cite DC Byte and DayOne for the Batam contrast. | https://www.dcbyte.com/wp-content/uploads/2025/07/DC-Byte-Market-Spotlight-SIJORI.pdf |
| 15 | Source [13] for Microsoft's US$2.2bn Malaysia pledge | WEAK SOURCE | A 2025 trade article is cited for a 2024 pledge. Primary: Microsoft, 2 May 2024 (already in timeline.csv). | Cite Microsoft directly. | https://news.microsoft.com/apac/2024/05/02/microsoft-announces-us2-2-billion-investment-to-fuel-malaysias-cloud-and-ai-transformation/ |
| 16 | "Batam just signed a 450MW power deal" | MINOR | DayOne PPA was 17 Apr 2026, about seven months ago. | "signed a 450MW power deal in April 2026" | https://dayonedc.com/markets/dayone-signs-indonesias-largest-511mva-450mw-ppa-to-expand-hyperscale-data-center-platform-in-batam/ |

### Claims that hold

| Claim | Verdict | Note |
|---|---|---|
| AWS first Asia Pacific region, Singapore, Apr 2010 | OK (project-verified) | AWS What's New, 29 Apr 2010 |
| Google's first SEA region, Singapore, 2017 | OK (project-verified) | Google Cloud blog, 15 Jun 2017 |
| Moratorium from 2019, lifted Jan 2022, rationed since | OK (re-checked) | Computer Weekly; Singapore awarded ~80MW (2023) and 200MW (Aug 2026) since |
| AMRO links Johor's rise to proximity and Singapore's ban | OK (re-checked) | AMRO: "Singapore's ban on new large-scale data center construction during 2019-2022 helped boost data center investment" in Johor |
| Nongsa Digital Park 2018; Batam ~8MW live 2025 | OK (project-verified) | MFA 2018; DC Byte 2025 |
| Google Jakarta 2020, AWS Jakarta Dec 2021 | OK (project-verified) | |
| US export controls Oct 2022 | OK (project-verified) | BIS, 7 Oct 2022 |
| ISEAS "dual-stack," hidden Chinese colocation footprint | OK (re-checked) | GDS CEO: SEA client mix "around 70 per cent from China" (Q2 2024 call) |
| Green Lane cut 36 to 48 months to about 12 | OK (re-checked via ISEAS) | TNB, 9 Aug 2023 |
| Microsoft US$1.7bn Indonesia; AWS Malaysia 2024, Thailand 2025 | OK (project-verified) | |
| AI Diffusion Rule Tier 2, Jan 2025; rescinded 13 May 2025 | OK (project-verified) | |
| Johor stopped Tier 1 and 2 approvals, Nov 2025 | OK (re-checked via ISEAS) | ISEAS adds water-cooled projects held until at least mid-2027 |
| Thailand paused 49 projects, Sep 2026; Singapore 200MW; Google US$15bn | OK (project-verified) | |
| Jakarta 356MW live, 1,699MW pipeline; pipeline ~5x base | OK (re-checked) | C&W H1 2026: Jakarta pipeline 1,699MW (+56%); 1,699/356 = 4.8x |
| Vietnam, Philippines figures | OK (project-verified) | Low-confidence rows in countries.csv; wording already cautious |

## (b) The two macro claims tested

### Claim A: "The US and China build most of the world's AI infrastructure at home. A handful of middle powers now host the overflow."

**First sentence: SUPPORTED.**
- Epoch AI (5 Jun 2025, data as of May 2025): the US has "about three-quarters" of global GPU cluster performance, China 15%. So the two hold about 90% of tracked AI supercomputer capacity. Caveat: Epoch's China coverage is partial.
- IEA, Energy and AI (Apr 2025): of ~415TWh of data centre electricity in 2024, the US used about 45%, China 25% and Europe 15% (shares as reported by Carbon Brief). The US and China account for "nearly 80% of global growth to 2030."
- Synergy Research (19 Mar 2025): the US holds 54% of hyperscale capacity.

**Second sentence: OVERSTATED.** Two problems.
1. "Overflow" implies capacity outside the US and China mainly absorbs their excess. Most capacity outside them serves its own region (Europe holds ~15% of global data centre power use on its own). The overflow story fits Johor, which absorbed Singapore's overflow and Chinese AI training (FT, Nov 2025), better than it fits middle powers as a group.
2. "A handful" undersells how spread out the rest is, and the hosts are small next to the leaders. Malaysia's ~1.3GW operating compares with ~32GW (C&W) to ~50GW (DCMI) in the US (project `countries.csv`). The fast movers are concentrated, though: C&W says Malaysia and India took 58% of APAC's new operational IT load in 2025.

**Corrected wording:** "The US and China hold about 90% of the world's tracked AI computing power. Outside them, a few fast-growing hosts such as Malaysia and India are adding capacity that serves their regions and, increasingly, US and Chinese firms."

### Claim B: "Outside the US, the pipeline is moving to Asia."

**Verdict: PARTLY SUPPORTED. Asia Pacific has the largest and fastest-growing pipeline outside the Americas, but "moving" overstates a shift, and most of it is still only planned.**

| Source | Asia Pacific | Europe, Middle East and Africa | Americas / US |
|---|---|---|---|
| C&W APAC updates (30 APAC markets, incl. mainland China) | Pipeline ~14.3GW end-2024, 16.6GW H1 2025, 19.4GW end-2025, 26.5GW H1 2026 (4.8GW under construction, 21.7GW planned) | n/a | n/a |
| C&W Global Data Center Market Comparison (29 May 2026) | Not given in release | 11.4GW operating, 2.7GW under construction, 12.1GW planned (14.8GW pipeline) | Americas: 43.4GW operating, 25.3GW UC, 191.3GW planned |
| JLL 2026 Global Outlook (6 Jan 2026) | 32GW now to 57GW by 2030 (+25GW) | +13GW of new supply to 2030 | Americas about half of global capacity; global 103 to 200GW |
| Knight Frank Global Forecast (Jan 2026) | EMEA and APAC together add 11.5GW in 2026 to 2027 | (combined) | US adds ~21 of ~33GW, about two-thirds |
| SemiAnalysis (per project cleanup notes) | APAC ex-China ~15GW | n/a | n/a |

What this shows:
- APAC's pipeline is larger than EMEA's (19.4 vs 14.8GW on C&W's end-2025 basis) and grew about 85% in 18 months. JLL expects APAC to add about twice as much as EMEA by 2030.
- APAC's share of the world is not rising. JLL's figures imply APAC falls from about 31% to about 28% of global capacity by 2030, because the US grows faster still. Knight Frank expects the US to take about two-thirds of additions in 2026 to 2027.
- C&W's APAC totals include mainland China, India, Japan and Australia. Southeast Asia is about half of APAC's under-construction capacity.
- 82% of C&W's H1 2026 APAC pipeline (21.7 of 26.5GW) is planned, not under construction. Thailand's September 2026 pause shows how fast planned capacity can stall.
- The Americas figure includes Canada and Latin America, so "outside the US" cannot be isolated cleanly from C&W's regional release.

**Corrected wording:** "Outside the Americas, Asia Pacific now has the largest data centre pipeline, about 26.5GW in mid-2026 against about 15GW in Europe, the Middle East and Africa, and Southeast Asia holds half of what Asia Pacific is building."

Sources for (b): https://epoch.ai/data-insights/ai-supercomputers-performance-share-by-country ; https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai ; https://carbonbrief.org/ai-five-charts-that-put-data-centre-energy-use-and-emissions-into-context ; https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of-total-capacity ; https://www.cushmanwakefield.com/en/singapore/news/2026/08/apac-dc-h1-2026 ; https://www.cushmanwakefield.com/en/Singapore/news/2026/03/apac-data-centre-development-pipeline-hits-record-in-2025 ; https://w.media/thailand-surged-200-malaysia-70-in-planned-capacity-in-h1-2025-cw-report/ ; https://www.cushmanwakefield.com/en/germany/news/2026/05/global-data-center-market-comparison ; https://www.jll.com/en-uk/newsroom/global-data-center-sector-to-nearly-double-to-200gw-amid-ai-infrastructure-boom ; https://www.knightfrank.co.uk/newsroom/article/2026/1/us-to-capture-two-thirds-of-global-data-centre-expansion-as-power-and-policy-bottlenecks-throttle-growth-in-europe-and-asia

Caveat: I could not open the IEA executive summary directly (site error), so the 45/25/15 shares come from Carbon Brief's report of the IEA figures ("nearly half" for the US).

## (c) Reading list

Ordered from the regional story outward. "Free" means no paywall seen; some broker reports need a contact form.

| # | Title | Publisher | Date | URL | Free? | What it adds |
|---|---|---|---|---|---|---|
| 1 | Behind Malaysia's Data Centre Boom (Trends in SEA 22/2026), James Chai | ISEAS | Sep 2026 | https://www.iseas.edu.sg/wp-content/uploads/2026/08/TRS22_26.pdf | Yes | Best single account of why Malaysia won, with the Chinese first wave, "dual-stack" framing and colocation's hidden Chinese footprint. |
| 2 | Southeast Asia in the AI Race: Access, Affordability and Resilience (TRS 24/2026), Zenobia Chan | ISEAS | 2026 | https://www.iseas.edu.sg/wp-content/uploads/2026/09/TRS24_26.pdf | Yes | The host-country policy view: dependency risks of foreign-owned data centres and the case for "mixed AI stacks." |
| 3 | Data Center Boom in Malaysia (Malaysia ACR 2026, Selected Issue 1) | AMRO | May 2026 | https://amro-asia.org/wp-content/uploads/2026/05/Malaysia-ACR-2026-SI-1-Data-Center-Boom-in-Malaysia.pdf | Yes | Macro view with Johor's near-zero 2020 base, tariffs, incentives and the July 2025 tariff hit. |
| 4 | Asia Pacific Data Centre Update H1 2026 | Cushman & Wakefield | 5 Aug 2026 | https://www.cushmanwakefield.com/en/singapore/news/2026/08/apac-dc-h1-2026 | Release free; full report via form | The half-yearly pipeline series (26.5GW) behind the site's numbers, by market. |
| 5 | Global Data Center Market Comparison 2026 | Cushman & Wakefield | 29 May 2026 | https://www.cushmanwakefield.com/en/germany/news/2026/05/global-data-center-market-comparison | Yes (flipbook) | Same methodology across regions; the EMEA and Americas numbers needed to test Claim B. |
| 6 | 2026 Asia Pacific Data Centre Trends and Outlook | CBRE | May 2026 | https://www.cbre.com/insights/reports/2026-asia-pacific-data-centre-trends-and-outlook | Yes (form may apply) | Live-capacity growth by city (Johor +53% in 2025) and the "power-advantaged markets" argument. |
| 7 | 2026 Global Data Center Outlook | JLL | 6 Jan 2026 | https://www.jll.com/en-uk/insights/market-outlook/global-data-centers | Yes | Regional forecasts to 2030 (APAC 32 to 57GW; global 103 to 200GW). |
| 8 | Data Centres Global Forecast Report 2026 | Knight Frank | Jan 2026 | https://content.knightfrank.com/research/2960/documents/en/data-centres-global-forecast-report-2026-12620.pdf | Yes | Shows the US taking about two-thirds of 2026 to 2027 additions; the counterweight to "moving to Asia." |
| 9 | Data Centre Atlas 2026 | Knight Frank | Aug 2026 | https://www.knightfrank.co.uk/site-assets/research/report-pdfs/data-centres/data-centre-atlas-2026.pdf | Yes | City-level live and pipeline MW worldwide; second source for Singapore vs Johor. |
| 10 | 2026 Global Data Centre Index Report | DC Byte | 27 Jul 2026 | https://www.dcbyte.com/?p=18753 | Download offered; gating unclear | Ranks Johor first in APAC; regional top-10 and future-growth markets. |
| 11 | Energy and AI | IEA | Apr 2025 | https://www.iea.org/reports/energy-and-ai | Yes | The global baseline: 415TWh in 2024, regional shares, growth to 2030. |
| 12 | From AI to emissions: Aligning ASEAN's digital growth with energy transition goals | Ember | 27 May 2025 | https://ember-energy.org/latest-insights/from-ai-to-emissions-aligning-asean-digital-growth-with-energy-transition/ | Yes | Country power and emissions projections for ASEAN data centres (Malaysia 9 to 68TWh). |

Also useful:
- e-Conomy SEA 2025 (Google, Temasek, Bain; 11 Nov 2025), https://www.temasek.com.sg/en/news-and-resources/news-room/news/2025/e-conomy-sea-2025-report-aseans-digital-economy-poised-to-surpass-300-billion . Over 4,600MW planned in the region; capacity growth of 180% vs 120% for the rest of APAC. Free.
- Anticipating Uncertainty in Data Centres Electricity Demand (ASEAN Centre for Energy, 21 Aug 2026), https://aseanenergy.org/publications/anticipating-uncertainty-in-data-centres-electricity-demand . Why ASEAN demand forecasts vary so widely. Free.
- Epoch AI, AI supercomputer share by country (5 Jun 2025), https://epoch.ai/data-insights/ai-supercomputers-performance-share-by-country . Source for the US and China compute shares. Free.

Not found or not verified in this pass: a Structure Research public report (subscription only), an ERIA report focused on data centres, a McKinsey or EDB "AI in Southeast Asia" report, and a Brookings or CSIS report on SEA data centres. I did not list them rather than guess titles or dates.
