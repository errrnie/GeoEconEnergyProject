# Malaysia data center sites: method and caveats

File: `sites.csv` (62 rows). Compiled 10 Nov 2026.

## Method
1. Built a candidate list from the ISEAS paper (James Chai, "Behind Malaysia's Data Centre Boom", TRS22/26) and from aggregators (DC Market Insights, Coloprice, Baxtel, Data Center Map). Aggregators were used only to find candidates, never as the sole basis for a number, except where a row's notes say so.
2. Checked each site against a company release, a government source (MIDA, a state official) or reputable trade press (w.media, DCD, The Star, Malay Mail, EdgeProp, FMT). Every row cites one primary `source_url`. Other sources are named in `notes`.
3. Re-opened the sources for 12 randomly sampled rows (seed 7) and checked the key numbers. Two fixes came out of this (see "Verification pass").

## Field rules
- **it_mw**: copied as the source states it. `mw_type`=IT only when the source says IT load. `Facility` means grid/TNB power allocation or gross power. `Unspecified` means the source gives "MW" with no basis. Campus or ultimate capacity is used unless the notes say "phase 1". The column mixes these types, so do not sum it without filtering on mw_type.
- **capex_usd_m**: filled only when the source itself gives a USD figure. RM-only figures appear in `notes` and were not converted. For land-only rows, capex is the land price (noted). National cloud pledges (AWS 6,200; Microsoft 2,200; Oracle 6,500) are country-level figures, not site capex.
- **stack**: tenant first, then operator HQ. China = a confirmed or reported Chinese anchor tenant, or a Chinese or Chinese-origin operator. US = a US hyperscaler owner or tenant, or a US-HQ operator with no known Chinese tenant. Mixed = material ties to both (only YTL: NVIDIA AI cloud plus the GDS co-development deal). Other = non-US/China operator and no known US/China tenant. Unknown = tenant unknown and the ties are ambiguous or alleged (e.g., Megaspeed). Ownership capital goes in a separate column (`owner_capital_nationality`). For example, Bridge MY06 is Bain-owned (US) but stack=China because ByteDance is the tenant.
- **DayOne** rows are tagged China. DayOne is GDS's former international arm, GDS keeps about 24%, and ISEAS reports about 70% of GDS's SEA clients are Chinese. The operator is now Singapore-HQ, so this is a judgment call.
- **lat/lon**: town centroids only (`latlon_precision`=town). Six cloud-region or unlocated rows (Microsoft Malaysia West, AWS, Oracle, Alibaba, Tencent Cloud Johor, Huawei 2015) have blank coordinates because no town is disclosed. Sedenak Tech Park rows are plotted at one Sedenak point. Kota Tinggi rows (Digital Edge, MSFusion) are plotted at Kota Tinggi town, though the sites are probably nearer Ulu Tiram/Bandar Cemerlang.
- **status**: "Under construction" needs evidence of groundbreaking or works. A land purchase, MOU, financing or announcement alone = Announced.
- **confidence**: High = company or government source. Medium = reputable press. Low = single secondary source, or a key field resting on an aggregator.

## Sources consulted (main)
ISEAS TRS22/26 (via WebFetch; direct download was blocked by proxy policy). Company releases: AirTrunk, DayOne, STACK, Equinix, Vantage (BusinessWire), NEXTDC, NTT, EdgeConneX, Google Cloud Press Corner, Amazon, Bridge (PR Newswire, MIDA), YTL/MIDA, TM Global, STT GDC (HPCwire). Press: w.media, DatacenterDynamics, The Star, Malay Mail, EdgeProp, FMT, Techwire Asia, Digital News Asia, Technode, Mingtiandi, Investment Monitor, SolarQuarter. Chinese-language: QQ News (Reuters relay) on ByteDance's RM10bn plan. Aggregators for candidates: DC Market Insights, Coloprice, Baxtel, Data Center Map, myBina.

## Conflicts found
1. **STT GDC Johor**: campus 120MW IT (Feb 2025 groundbreaking) vs 166MW IT (Aug 2026 financing). Used 166.
2. **YTL park**: 500MW (MIDA, ISEAS) vs "600MW park" (EdgeProp Nov 2025). FMT says 300MW is being built and commissioned. Used 500.
3. **Racks Central Pasir Gudang**: phase 1 is 70MW (w.media 30 Jun 2026) vs 90MW "RCJM1" (w.media 15 Jun 2026).
4. **DayOne Johor**: its market page says 390MW in service, while its body text says over 478MW operational across two campuses. Press says about 500MW combined for NTP+KTP. No per-campus split.
5. **PDG**: JH1 grew from 150MW (2023) to a "200MW campus" (Dec 2025). Aggregators list JH1 at 150 or 200MW and JH2 at 200 or 300MW.
6. **Vantage KUL2**: 256MW IT (Vantage) vs 436MW (DC Market Insights). KUL1 at 31MW is derived arithmetically (287 minus 256).
7. **Melaka Victoria DC**: "about 100MW" and "up to 96MW" appear in the same Malay Mail article.
8. **Google-Gamuda Port Dickson**: w.media's headline says US$345m and 400 acres; its body says RM455.23m and 389 acres.
9. **EdgeConneX KL CBD / Bukit Jalil**: 19MW / about 70MW (company) vs 17MW / 67MW (aggregator).
10. **AirTrunk JHB1/JHB2 location**: AirTrunk labels JHB1 "Johor Bahru" and JHB2 "Iskandar Puteri". Later press puts all four campuses adjacent in Iskandar Puteri.

## Gaps
- **ByteDance's own RM10bn (about US$2.1bn) AI hub (2024)** plus RM1.5bn to expand its Johor facility (Reuters via QQ News). No site found, so there is no row. Its known Johor footprint is via Bridge MY06 (confirmed) and reportedly AirTrunk and DayOne (ISEAS only).
- **Hyperscaler sites are undisclosed**: AWS, Microsoft Malaysia West, Oracle, Alibaba, Tencent Johor. Google's Nov 2026 US$15bn plan names new Selangor and Negeri Sembilan campuses without towns.
- **MW is often missing**: hyperscaler self-builds, Equinix, ZData, DayOne KTP/Tanjung Kupang/Kapar, Microsoft land sites and Area Group publish none.
- **Tenants are rarely disclosed**: most colo rows have a blank anchor_tenant. Megaspeed's 68.4MW at an unnamed Bridge Malaysia facility was replaced by Zenlayer (FMT Apr 2026), and the facility is not identified.
- **Operational dates** for Yondr/Vantage JHB1, K2 JHR1 and PDG JH1 phase 1 are not confirmed by primary sources.
- **Not included (insufficient sourcing or below threshold)**: Keppel DC Johor (Baxtel only; Microsoft tenancy is a rumour), Basis Bay, Infinaxis, Maxis, AIMS legacy KL sites, Sarawak Kota Petra Green Technology Park (Zecon; no town or IT MW), IRIX Kuching, DayOne Klang Valley/Banting (aggregator only), and the Bridge Plentong 20-acre land (RM99m, Aug 2024; purpose not stated).
- **Policy context to note on the map**: in Nov 2025, Johor asked water-cooled DC expansions to pause until about mid-2027 (Lowyat citing SCMP). This is not tied to named projects.

## Verification pass
Re-opened sources for STT Johor, Area Group, PDG JH1/JH2, BrightRay, NTT Cyberjaya, DayOne NTP, DayOne Kapar, DayOne Tanjung Kupang, Microsoft Nusa Cemerlang, NEXTDC KL1 and AirTrunk JHB3/4. All numbers matched. Fixes: STT year_announced changed to 2025, with the 120 vs 166MW conflict and the 16MW first-building detail added to notes. PDG JH1 notes now say its operational status rests on a secondary source.
