# Thailand sites: notes

As of 12 Nov 2026. 40 rows, same schema as the Malaysia file.

## Method
- Started from the student's Pack v1 (8 Nov 2026) and re-fetched every source used. Primary sources first: BOI releases (PR14/2568, PR41/2568, PR146/2568, PR8/2569, PR67/2569) and company releases. Then The Nation, Bangkok Post, Reuters/Bloomberg via The Star, w.media, DCD, Mingtiandi, Baxtel and Datacentermap.
- Casing matches the Malaysia file (High/Medium/Low; IT/Facility/Unspecified).
- `it_mw` is the BOI "IT load" where given, else the operator's headline figure (Unspecified). DayOne's 300MW is power capacity (Facility).
- `capex_usd_m` is filled only when the source stated USD. Baht-only values are in notes.
- Stack: anchor tenant first, else operator home country. DayOne is tagged China to match the Malaysia file. UAE capital is Other.
- Many "Announced" rows are BOI approvals, which are multi-year intent, not committed capital.

## Coordinates
Lat/lon are approximate town centroids from general geographic knowledge, not from the cited sources. All are tagged `town`. The 25 rows with only a province, or several provinces, are left blank. Do not zoom past district level.

## Double-count risk
- Bridge III (80MW) and Bridge IIO (134MW) may sit on QHI01 (200MW).
- True IDC's three BOI projects (223MW) may overlap its 250MW EEC campus.
- The two TikTok rows are user-side hosting, likely inside third-party colocation, so their MW is not additive.
- Google's US$1bn sits on the Chonburi row only.

## Conflicts
- Galaxy Peak: 23.55bn baht (w.media) vs 38bn baht (BOI, Oct 2025).
- Empyrion: 12MW at BOI approval vs 20MW at groundbreaking.
- DAMAC Rama 9: 20MW (2024 release) vs "starts at 5MW" (The Nation, Sep 2026).
- TikTok 2026: US$25bn (BOI) vs US$26.3bn (Khaosod).
- Operating sites: 35 (Sep 2026) vs 63 operating and 20 under construction (The Nation, 6 Nov 2026).

## Gaps
- No province for AWS, Microsoft, Huawei, TikTok 2025, DAMAC Digital 84MW, the True IDC 250MW campus or the unnamed 200MW project.
- STT Bangkok 1's opening year and NTT BKK3's actual opening are unconfirmed.
- NEXTDC is Low confidence and CtrlS's build status is unverified.
- Owners of Vistas, Freyr and Galaxy Peak are unknown.
- One search found no Thai project for Princeton Digital, BDx or EdgeConneX.
- Baxtel slugs hint that Microsoft uses GSA sites. This is unverified, so no anchor tenant is set.
