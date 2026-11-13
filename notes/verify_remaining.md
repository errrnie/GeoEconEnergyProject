# Verification of four remaining figures (13 Nov 2026)

## 1. Indonesia power cost 6.3 vs 10.6 US cents/kWh

Verdict: CONFIRMED. Attribution can be made more precise.

- Original source: Mirae Asset Sekuritas Indonesia research note "Indonesia's Data Center Cost Edge Meets a Power Bottleneck", analyst Daniel Widjaja, published 17 Sep 2026. The note itself is not public, so the press coverage below is the best available source.
- IDX Channel, 17 Sep 2026 (https://www.idxchannel.com/market-news/data-center-indonesia-unggul-di-biaya-listrik-jadi-batu-sandungan/all): "Biaya listrik Indonesia juga berada di sekitar USDc6,3 per kilowatt-hour, dibandingkan USDc10,6 per kilowatt-hour di Malaysia." Attributed to "Analis Mirae Asset Sekuritas Daniel Widjaja dalam riset yang terbit 17 September 2026".
- Investortrust, 17 Sep 2026 (https://investortrust.id/market/116655/mirae-asset-10-emiten-ini-berpotensi-garap-infrastruktur-data-center-us-13-miliar): "sekitar US$ cent 6,3 per kWh" vs Malaysia "sebesar US$ cent 10,6 per kWh"; names the report title above and describes the figures as estimates ("diperkirakan").
- Neither article names an underlying data source for the numbers (no PLN or TNB tariff cited). Calling it a "broker estimate" is accurate.

Suggested wording (optional): "A Mirae Asset Sekuritas estimate (Sep 2026) puts data centre power at about 6.3 US cents per kWh in Indonesia against 10.6 in Malaysia."

## 2. 100 MW grid connection about 36 months in Indonesia vs about 12 in Malaysia

Verdict: CONFIRMED for the Indonesian figure, but the source is the same Mirae note, not an official PLN figure. The page framing "the roughly 12 months Malaysia's Green Lane targets" is supported separately by the TNB press release of 9 Aug 2023 (already in data/shared/speed_to_power.csv).

- IDX Channel, 17 Sep 2026 (same URL as above): "Indonesia membutuhkan sekitar 36 bulan untuk mengalirkan listrik bagi proyek data center berkapasitas 100 megawatt (MW), jauh lebih lama dibandingkan Malaysia yang hanya membutuhkan sekitar 12 bulan."
- Investortrust, 17 Sep 2026 (same URL as above): Indonesia "sekitar 36 bulan", Malaysia "sekitar 12 bulan", for a 100 MW data centre.
- No independent source with a 36-month Indonesia figure was found. Petromindo, 5 Aug 2026 (https://www.petromindo.com/news/article/data-center-industry-seeks-firm-power-connection-timelines-over-lower-tariffs) gives qualitative support only: permitting of "six to nine months across multiple ministries" under PJBTL, and IDPRO chairman Hendra Suryakusuma: "Sometimes we obtain the permit to build, but the transmission never gets finished."

Suggested replacement (driver card): "The same broker note estimates a 100 MW grid connection takes about 36 months in Indonesia, against the roughly 12 months Malaysia's Green Lane targets."
Suggested replacement (section text): "The constraint is time: about 36 months for a large connection by the same broker estimate, and a planning reserve on Java that falls toward 33% by 2027."

## 3. Vietnam 148 MW operating capacity and 870 MW 2030 target

Verdict: 148 MW CONFIRMED as reported. 870 MW CONFIRMED as a reported government target, but with a definitional caveat.

- VnExpress International, 29 Aug 2026 (https://e.vnexpress.net/news/tech/tech-news/china-offers-to-build-ai-factories-in-vietnam-5115090.html). Speaker Yang Xin (Hong Kong Chamber of Commerce in Shenzhen) at the Vietnam-China Dialogue Forum on AI and the Digital Economy, Hanoi, 27 Aug 2026: "He put Vietnam's operating data center capacity at around 148 MW." and "The government's target under its information and communications infrastructure plan is 870 MW by 2030."
- Likely origin of 148 MW: BMI (Fitch Solutions) via TechNode Global, 20 Jul 2026 (https://technode.global/2026/07/20/vietnam-emerges-as-seas-next-data-center-contender-amid-regional-capacity-shift-bmi/): "Vietnam currently has about 148 megawatts (MW) of operational data center capacity", "A further 79 MW is under construction, while more than 870 MW has been announced or planned." Note: in BMI the 870 MW is a pipeline (announced or planned), not a government target.
- Government target support: The Investor, 30 Apr 2025 (https://theinvestor.vn/vietnams-military-run-telco-giant-viettel-builds-one-of-southeast-asias-largest-data-centers-d15492.html): "Vietnam's total data center capacity stands at 182 MW, far below the 870 MW target set for 2030", citing a Ministry of Science and Technology report. So two independent sources tie 870 MW to a 2030 target. Decision 36/QD-TTg (Jan 2024) coverage checked (Vietnam Briefing, Viet Nam News) did not state an MW figure, so the plan text itself is unconfirmed.

Suggested wording: "Vietnam has about 148 MW of operating data centre capacity (BMI, Jul 2026), against a 2030 target of 870 MW cited by the Ministry of Science and Technology." Consider citing BMI/TechNode for 148 MW and The Investor for 870 MW, with VnExpress as secondary.

Side note: VnExpress says the C&W cost guide "puts the wait for a new 100 MW grid connection in Vietnam's main data center clusters at two to three years." C&W's own press release does not mention Vietnam grid timing (it lists Tokyo, Singapore, Sydney, Taipei, Johor), so keep that claim attributed to the speaker, not to C&W directly.

## 4. Cushman & Wakefield APAC Data Centre Construction Cost Guide 2026, mid-range US$m per MW

Verdict: CONFIRMED for all six markets, from C&W's own press release (primary, better than IT Brief).

- Cushman & Wakefield Singapore news release, "Asia Pacific's Data Centre Market Faces Structural Cost Shift Amid Rising AI Requirements", Amanda Phua, 1 Apr 2026 (https://www.cushmanwakefield.com/en/singapore/news/apac-dc-market-faces-structural-cost-shift-amid-rising-ai-requirements). Regional Construction Cost Index table, ranked by mid-range cost for a mid-specification build (US$ per MW): Philippines 8,200,000; Vietnam 7,200,000; Malaysia 9,600,000; Thailand 8,800,000; Singapore 14,400,000; Indonesia 8,300,000.
- Supporting: VnExpress (above) quotes Vietnam 7.2, Singapore 14.4, Malaysia 9.6, Thailand 8.8 "mid-range". Ready Media, 1 May 2026 (https://content.readymedia.com.au/article/power-play-data-centre-costs-rise-as-ai-raises-the-bar) gives Philippines construction cost growth of 17.7% year on year but no per-MW numbers.
- IT Brief URL used in data/thailand/cost_speed.csv is not fetchable from here; suggest switching the citation to the C&W release above.

Suggested citation: "Cushman & Wakefield, Asia Pacific Data Centre Construction Cost Guide 2026 (press release, 1 Apr 2026): mid-range cost for a mid-spec build."
