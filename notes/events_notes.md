# Malaysia data centre timeline: notes

Companion to `events.csv` (45 events, 2017 to Nov 2026). Built 2026-11-10.

Count by track: Investment 14, Geopolitics 13, Malaysia policy 12, Energy and water 6.

## How this was sourced

- **ISEAS Trends 22/2026 (James Chai), Appendix B.** I could not download the PDF directly because the proxy blocked it. I read it only through a fetch tool that summarises pages, so I used Appendix B to pick events and cross-check them, never as the only source for a date. Every row cites an outside source: a primary release (company, MIDA, MITI, TNB, BIS, EDB) where one was reachable, otherwise a reputable outlet (The Star, Malay Mail, FMT, The Edge, DCD, w.media, Reuters or Bloomberg syndications).
- `amount_usd_m` is filled only where a source gives a USD figure for Malaysia specifically. Funding at group level (DayOne) and purchase pledges (the US trade deal's US$150b) are left blank on purpose so that summing the column does not overstate investment.
- `mw` is filled only where a source states MW for that event. The Bridge, AirTrunk and YTL figures are planned campus capacity, not operating load.

## Date conflicts and judgment calls

| Event | Conflict | Choice |
|---|---|---|
| Non-AI data centre halt | ISEAS Appendix B lists **Mar 2026**. The Sun reports Anwar confirming it in Parliament on **24 Feb 2026**. TechWire Asia says an informal halt had been in place since about mid-2024. | 2026-02-24 (first public confirmation) |
| DESAC incentive | ISEAS: "announced Jan 2022". MIDA: tabled in Budget 2022, applications accepted from **30 Oct 2021** (MIDA's Jan 2022 newsletter publicised it). | 2021-10-30 |
| Johor Tier 1/2 halt | Bloomberg and The Star: **26 Nov 2025**. ISEAS: reported 27 Nov. w.media: 28 Nov. | 2025-11-26 (earliest report) |
| Google Malaysia cloud region | Global blog and TechCrunch: **9 Aug 2022**. Google's Malaysia press release: 12 Aug 2022. | 2022-08-09 |
| Google US$2b | Press-corner page shows both 29 May and a **30 May 2024** Kuala Lumpur dateline. | 2024-05-30 |
| Oracle US$6.5b | Oracle dateline **2 Oct 2024** (Austin and KL). AAP/Cision wire dated 1 Oct (US time). | 2024-10-02 |
| TNB Green Lane | Unveiled 8 Aug 2023 (MITI speech file is dated 230808). TNB press release issued **9 Aug 2023**. | 2023-08-09, as the brief asked |
| AI Diffusion Rule | Released **13 Jan 2025**. Federal Register publication was 15 Jan 2025. | 2025-01-13 |
| KLIA server seizure | The Star says the seizure happened on 5 Jun 2026 and was announced on **26 Jun 2026**. The Star itself treats the 5 June date as possibly a typo. | 2026-06-26 (announcement) |
| DayOne rebrand | Effective **1 Jan 2025**. Reported around 6 Jan 2025. | 2025-01-01 (Medium) |
| Bridge 400 MW deal | The w.media timestamp is 30 Nov 2024 and the dateline says 29 Nov with no year. CRESS opened in Sep 2024, which fits late 2024. A separate Bridge-TNB supply agreement was signed **7 Mar 2024** (MIDA) with no MW stated. | 2024-11-29 (Medium) |
| Gelang Patah protest | Bloomberg URL dated 7 Feb 2026 and says "Saturday". w.media (9 Feb) says "last Saturday". | 2026-02-07 |
| Microsoft 2021 "US$1b" | Microsoft's own release gives **no** dollar figure. The US$1b comes from Malaysian government statements about the Bersama Malaysia initiative as a whole. | Kept 1000, Medium |
| Jan 2026 "85% rule" | w.media (15 Jan 2026, citing The Edge) describes the 85% utilisation rule and the RM8.50/kW shortfall penalty but gives **no effective date**. The "five-year take-or-pay" wording comes from a separate TNB/RHB note (Jul 2026). | Dated to the 15 Jan 2026 report, Medium |
| Data centre tariff | ISEAS says the ultra-high-voltage class applies to loads **above 100 MW**. None of the sources I fetched (Malay Mail/Reuters, w.media) states that threshold. They give only the 10% to 14% cost rise. | Threshold left out of the CSV |
| CRESS charges | The Edge (Jun 2026): firm SAC cut from 25 to 20 sen in **Aug 2025** (no day given). The Star (17 Oct 2026) reports a combined SAC of 18 sen after an Oct 2026 revision and is internally inconsistent about the baseline. w.media says the revision *raised* the all-in CRESS cost to 48 to 50 sen. | Only the Aug 2025 cut is included (month precision). The Oct 2026 revision should be checked against the Energy Commission notice before use. |
| Johor capacity | ISEAS: about 0.4 GW operating in Jan 2025, nearly 1 GW by Dec 2025, and "2.1 GW today". Knight Frank (via The Star, Sep 2025): 5.8 GW "total capacity" including pipeline. MITI (Nov 2025): 603 MW drawn **nationally**. These measure different things (built IT capacity, pipeline, metered draw). | No Johor GW milestone included. I used the government's national draw figures (603 MW, then 1,374 MW). |
| Singapore moratorium | Start is given only as "2019". The lifting is described as Jan 2022, with the pilot call for applications opening in Q2 2022. | Year and month precision |

## Considered but left out

- **"MD2030":** I could not find a policy by that name in any reputable source. The closest matches are the National Cloud Computing Policy (Oct 2024) and the Sustainable Data Centre framework (promised for Oct 2025). Please confirm what the term refers to before adding it.
- **MITI-Digital task force to track Nvidia shipments (Mar 2025):** sourced only to a Financial Times interview relayed by Fortune. Its substance is covered by the 18 Jun 2025 and 14 Jul 2025 rows.
- **US plan to curb AI chip exports to Malaysia and Thailand (Bloomberg, 4 Jul 2025):** a reported draft rule that I could not confirm was ever issued.
- **Microsoft Malaysia West region going live (28 May 2025)** and **second region in Johor (about 4 Nov 2025):** verified. Easy to add back if more operating milestones are wanted.
- **Kota Damansara data centre application withdrawn after about 500 households objected (w.media, 3 Aug 2026):** verified. A good second community-opposition data point.
- **Megaspeed chip-diversion allegations (Oct 2025):** these concern a Singapore company. The Malaysia angle comes from secondary reporting, so it is not included.
- A news summary said a "Finnish authority" halted two Google Malaysian sites. That was a misreading. The halt was Google's sites in **Finland** (Al Jazeera, 7 Oct 2026). Excluded.

## Dates re-checked against their sources

All of these were confirmed on the source page itself, not from the URL or the search snippet:

1. Alibaba Cloud KL, 2017-10-30 (Alibaba Group)
2. Microsoft region, 2021-04-19 (Microsoft release)
3. AWS US$6b, 2023-03-02 (MIDA release and The Star)
4. Green Lane, 2023-08-09 (TNB press release PDF)
5. Singapore DC-CFA pilot, 2023-07-14 (EDB)
6. BIS controls, 2022-10-07 and 2023-10-17 (BIS press releases)
7. Google US$2b, 2024-05-30 (Google release)
8. AirTrunk JHB1, 2024-07-30 (FMT)
9. AWS region launch, 2024-08-22 (The Star)
10. Oracle, 2024-10-02 (Oracle release)
11. JS-SEZ, 2025-01-07 (Jakarta Post)
12. AI Diffusion Rule 2025-01-13 and its rescission 2025-05-13 (Kirkland)
13. Singapore fraud charges, 2025-02-27 (The Star/ANN)
14. MITI probe, 2025-06-18 (Malay Mail)
15. Strategic Trade Permit, 2025-07-14 (MITI statement)
16. MIDA as lead agency, 2025-07-21 (FMT)
17. US-Malaysia trade agreement, 2025-10-26 (The Star)
18. Johor halt, 2025-11-26 (The Star/Bloomberg)
19. Non-AI halt, 2026-02-24 (The Sun)
20. 31%-by-2035 reply, 2026-06-30 (Malay Mail)
21. KLIA seizure, 2026-06-26 (The Star)
22. DC-CFA2, 2026-08-21 (w.media)
23. Google US$15b, 2026-11-04 (Jakarta Post and Baxtel)
24. Phantom-demand figures, 2026-11-04 (Malay Mail)

Dated from the URL or byline only, without the day appearing in the body: MITI energy and water test (2026-07-16) and TNB 8.3 GW (2026-07-11).

## The 8 events that matter most

1. **2019: Singapore's data centre moratorium.** The origin story. Singapore's land and power limits pushed hyperscale demand across the causeway, and Johor became Singapore's overflow before it became a market in its own right.
2. **2022-10-07: US chip export controls on China.** This started the China-related driver. Chinese firms (ByteDance, and later the operators named in diversion cases) needed compute outside China, and Malaysia was close, cheap and not covered by the controls.
3. **2023-08-09: TNB Green Lane Pathway.** The single most important domestic policy. Cutting grid connection time from 36-48 months to about 12 turned speed to power into Malaysia's competitive edge, and it is why demand became signed load.
4. **2023-12-08: YTL-Nvidia US$4.3b.** The pivot from cloud storage to AI compute, and the moment Malaysia's boom became tied to access to Nvidia GPUs and therefore to US export policy.
5. **2024-05-02: Microsoft US$2.2b (opening the 2024 hyperscaler wave).** Microsoft, Google, AWS and Oracle together pledged roughly US$17b in about five months (2.2 + 2.0 + 6.2 + 6.5, matching ISEAS's "US$17b in 22 weeks"), and ByteDance added RM10b in the middle of that run. This is the boom in its purest form.
6. **2025-07-14: Malaysia's Strategic Trade Permit for US AI chips.** Malaysia chose to police US export rules itself to keep its GPU supply. Read it together with the Singapore fraud case (Feb 2025) and the KLIA seizure (Jun 2026) as the geopolitical price of the boom.
7. **2025-11-26: Johor halts Tier 1/2 approvals over water.** The first binding brake, and it came from a state government over water, not from the federal government over power. It foreshadowed the national non-AI halt (Feb 2026) and the federal power and water test (Jul 2026).
8. **2026-06-30: Data centres forecast to take 31% of electricity by 2035.** The energy security headline for this class. Data centres go from about 7% of national demand in 2026 to nearly a third by 2035, which turns a growth story into a grid-planning and fuel-security problem. The 4 Nov 2026 figures (1,374 MW drawn of 2,346 MW contracted) show how hard the forecasting is.
