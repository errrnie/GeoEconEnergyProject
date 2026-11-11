# Cleanup notes (11 Nov 2026)

Fixes are in `countries_fixes.csv`. `countries.csv` is unchanged.

## 1. China and US now use SemiAnalysis
- **China 24 GW operational, 20 GW pipeline.** The article says China has "a fleet of over 24GW" (a floor, end-2026). It also gives "~20GW of dated pipeline" and "~30GW of announced projects". I left out the 30 GW as speculative.
- **US 56 GW operational.** The article says "56GW of capacity as of 2026YE", which is partly a forecast. The basis is unstated, but SemiAnalysis's model tracks "critical IT power".
- **US 38 GW pipeline (low confidence).** SemiAnalysis forecasts "+38GW of Datacenter IT capacity delivered in the US in 2027" (22 GW under construction plus 16 GW planned). This covers one year only, while the China figure has no stated horizon. Broker alternatives: C&W 37.7 GW under construction (whole Americas) and JLL 66 GW under construction (North America).
- SemiAnalysis APAC ex-China is about 15 GW; our ten broker APAC rows sum to 9.0 GW.

## 2. China's standard rack
- MIIT's 数据中心能效专项监察工作手册 (Feb 2024) says: "标准机架定义依据《关于数据中心建设布局的指导意见》（工信部联通〔2013〕13 号），为换算单位，以功率 2.5 千瓦为一个标准机架。"
  - Source: https://www.gov.cn/zhengce/zhengceku/202404/P020240517496566744152.pdf
- Racks in use and implied rated power:
  - 10.85M (Jun 2025, MIIT): 27.1 GW.
  - 15.56M (Jun 2026, report 2026综合算力全景分析, issuer not named): 38.9 GW. At MIIT's 71.4% occupancy, about 27.8 GW.

## 3. Build cost (US$/W = US$m/MW)
- **UAE 9.2 and Saudi Arabia 10.8** (medium confidence): T&T 2026-27, confirmed by two outlets. These are national figures; T&T publishes no Dubai or Riyadh number.
- **Paris 10.8, Amsterdam 10.8, Dublin 10.0** (low confidence): T&T 2025-26, the same vintage as London, Frankfurt and Milan. Each has a single secondary source.
- **Canada:** the only figure is Toronto 9.1 (T&T 2024, cited secondhand). Leave it blank.
- **China:** keep 7.1 (C&W APAC, national) so it is consistent with the other APAC rows. T&T gives Shanghai 5.79.

## 4. Thailand
Keep **0.113 GW operational and 1.049 GW pipeline** (C&W, end-2025), but relabel it as C&W's national coverage. C&W H1 2026 lists Thailand under construction at 859 MW, the same as Bangkok, so its Bangkok market is effectively all of Thailand. It matches the core rows' source and vintage. Alternatives:
- BMI national: 0.216/0.944. Its sub-market pipelines add up to 1,202 MW, not 944.
- C&W H1 2026: 0.134/2.084. This is newer than the Malaysia row.

## 5. Other issues
- UK cost should be 12.95 (2026-27), not 12.02.
- The UAE capacity figure dates from Jun 2025 and is a lower bound.
- C&W H1 2026 implies about 47 GW of US operational capacity, so 31.97 is out of date even on a broker basis.

## Recommended chart footnote
"China and the United States use SemiAnalysis's bottom-up, facility-by-facility model (critical IT power, end-2026 estimate; the US pipeline is 2027 deliveries only). Other countries are sums of the city markets tracked by property brokers (mainly Cushman & Wakefield, end-2025). Broker sums miss self-built, telecom and enterprise capacity, so they run lower and are not strictly comparable."

## Summary
China and the US now come from SemiAnalysis: 24/20 GW for China and 56/38 GW for the US. The US pipeline covers 2027 deliveries only, so it is low confidence. MIIT confirms a standard rack is 2.5 kW. The 15.56M racks in use (Jun 2026) imply about 39 GW rated, or 28 GW occupied. New cost figures are UAE 9.2 and Saudi Arabia 10.8 (2026-27), plus Paris, Amsterdam and Dublin at low confidence (2025-26). Canada should stay blank. Thailand keeps C&W 0.113/1.049, relabelled as national. The UK cost goes up to 12.95.
