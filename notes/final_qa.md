# Final QA before submission (13 Nov 2026)

I read the landing story and all six country pages: body, texts, config, and the event rows that feed the timelines. I made wording-only edits in the source files and rebuilt. `python3 src/build.py` gives "em dashes 0, unfilled []" on all six pages and builds the landing page with no errors. The CSVs keep their column counts (13, and 14 for timeline.csv) and their original CRLF line endings. Nothing is committed.

## Changes (file: old → new)

### Landing story
- `data/region/story_v2.md`: "about 8MW live in 2025" → "about 8MW operating in 2025"
- `data/region/story_v2.md`: "Thailand froze 49 data centres under construction in September 2026, more than the 35 it had running [26], as part of a pause on 166 projects." → "In September 2026 Thailand paused 166 data centre projects, including 49 under construction, more than the 35 it had operating [26]." (now frames it as a 166-project pause, matching the Thailand page)

### All six country pages
- `markets/{singapore,malaysia,thailand,indonesia,vietnam,philippines}/body.html`: "Operational capacity runs today." → "Operational capacity is built and operating today."

### Singapore
- `markets/singapore/body.html` lede: "Singapore is still Southeast Asia's largest single data centre market on official and BMI counts, though Johor has drawn level on broker figures, and it is the region's network core." → "Singapore is still one of Southeast Asia's two largest data centre markets, about level with Johor at roughly 1.1 GW operating, and it is the region's network core." (the old lede called Singapore the largest market, but the hero KPI, the landing story and the section-1 note all say it is level with Johor at about 1.1 GW)
- `markets/singapore/texts.py` chip lede: "...alongside Malaysia and Thailand." → "...alongside Malaysia and Thailand, until the rule was rescinded in May 2025."
- `markets/singapore/texts.py`: "As elsewhere, supplying a Chinese-parented buyer requires a US licence wherever it operates." → "...has required a US licence wherever it operates since November 2023, a rule reaffirmed on 31 May 2026."
- `data/singapore/events.csv` (Equinix SG6 significance): "First pilot DC-CFA allocation to go live." → "...to start operating."

### Malaysia
- `markets/malaysia/texts.py`: fixed a comma splice, "applies to Malaysia as a country, Commerce said in May 2025" → "applies to Malaysia as a country. Commerce said in May 2025"
- `markets/malaysia/texts.py`: "Since July 2026 Malaysia pays a 10% Section 301 duty, lower than Singapore, Thailand and Vietnam at 12.5%." → "Since 24 July 2026 Malaysian goods have faced a 10% US Section 301 tariff, the same as Indonesia and lower than the 12.5% on Singapore, Thailand, Vietnam and the Philippines."
- `markets/malaysia/texts.py` (Jan 2025 tier map note, shared by all pages): "AI Diffusion Rule, published 15 Jan 2025 (90 FR 4544), dropped on 13 May 2025," → "AI Diffusion Rule, announced 13 Jan 2025 and published 15 Jan 2025 (90 FR 4544), rescinded on 13 May 2025,"
- `markets/malaysia/texts.py` ("Now" tier map note, shared by all pages): "BIS confirmed in May 2026 that this still applies." → "BIS reaffirmed on 31 May 2026 that this still applies."
- `data/malaysia/events.csv` (24 Jul 2026 row): "Malaysia's rate was 10%, below Singapore, Thailand and Vietnam at 12.5%." → "Malaysia's rate was 10%, the same as Indonesia and below the 12.5% on Singapore, Thailand, Vietnam and the Philippines."
- `data/malaysia/security_events.csv` (7 Aug 2026 row): "including Alibaba using chips in Malaysia via Megaspeed" → "including Alibaba allegedly using chips in Malaysia via Megaspeed"

### Thailand
- `markets/thailand/body.html` lede, which said "pause" twice: "In 2026 it chose to pause instead. In September 2026 it paused 166 data centre projects while it wrote new rules," → "In September 2026 it paused 166 data centre projects, 49 of them under construction, while it wrote new rules,"
- `markets/thailand/body.html` KPI, which said "operating today" twice: "operating today (The Nation; BMI 216 MW), against 8.8 GW..." → "The Nation; BMI counts 216 MW, against 8.8 GW..."
- `markets/thailand/texts.py` chip lede, which was one run-on sentence: "...reportedly shelved in August 2026, and the worry behind it, chips leaking to China, now runs through Bangkok too." → "...reportedly shelved in August 2026. The worry behind it, chips leaking to China, now runs through Bangkok too."
- `markets/thailand/texts.py`: "People familiar told Bloomberg" → "People familiar with the matter told Bloomberg"
- `markets/thailand/texts.py` stat: "US tariff on most Thai goods since July 2026, against Malaysia's 10%" → "US Section 301 tariff on most Thai goods since 24 July 2026, against 10% for Malaysia and Indonesia"
- `data/thailand/events.csv` (4 Sep 2026): title "Government pauses 49 data centres under construction" → "Government pauses 166 data centre projects, 49 under construction"; significance "more data centres than it had running" → "more data centres than it had operating"
- `data/region/timeline.csv` (4 Sep 2026): title "Thailand pauses 49 data centres under construction" → "Thailand pauses 166 data centre projects, 49 under construction"; significance "more projects than it had running" → "more data centres than it had operating"

### Vietnam
- `markets/vietnam/body.html` (two places): "AWS's Hanoi Local Zone, live since June 2026" → "AWS's Hanoi Local Zone, open since June 2026"

### Philippines
- `markets/philippines/body.html` KPI: "about ten times BMI's live count" → "about ten times BMI's operating count"
- `markets/philippines/texts.py` scenario note: "BMI's 140 MW live plus" → "BMI's 140 MW operating plus"
- `markets/philippines/texts.py`: "supplying a China-parented buyer" → "supplying a Chinese-parented buyer" (now matches the other pages)

## Checked and consistent (no change needed)
- Reading order: the landing lede and the "country pages follow that path" paragraph, plus the bridges in each config.json "next", all run Singapore → Malaysia → Thailand → Indonesia → Vietnam → Philippines → back to the overview. The landing cards follow the same order.
- Johor 1,110 MW and Singapore about 1.1 GW (Knight Frank 1,118 MW, BMI 1.46 GW broader) agree across the hero, funnel, driver cards and story.
- Megaspeed: US$4.6bn (Bloomberg customs data) and US$7.5bn (The Information, wider measure) are framed as allegations on the Singapore, Malaysia and Indonesia pages, each saying nobody has been charged and Megaspeed denies wrongdoing. The OBON/Siam AI case and the C4ADS Vietnam report are also framed as allegations.
- Malampaya is extended to about 2034 in both the Philippines text and its stat box.
- The Indonesia, Vietnam and Philippines pages and the Vietnam and Philippines event rows already give the Section 301 rates correctly.

## Flagged, not changed
1. **Hormuz timing.** The Malaysia and Thailand pages say the strait was disrupted in **March 2026**. The Singapore page says "Qatar's cargoes stopped in **April 2026** when war hit the Gulf". The Thailand event row is dated 1 Apr 2026 ("Hormuz closure"). These may both be true (disruption in March, cargoes stopping in April), but a reader may see a conflict. Please check against the sources.
2. **Landing story source [34]** (King & Wood Mallesons, Vietnam) is listed but never cited in the text.
3. **Malaysia risk note** cites "RHB Research ... 11 Jul 2026" while the funnel bars are labelled Aug 2026. The Aug figures come from the 4 Nov energy ministry release, which the note also cites, so this is probably fine.
4. **Malaysia "Why" heading** "Speed to power, not the cheapest build" is a mild "X, not Y" construction. I left it because it is a heading and reads clearly.
5. **`src/landing.py` map note** defines "Operating" as "built and running". This is a definition, not capacity prose, so I left it.
6. **Event descriptions** still use "goes live" for cloud regions (AWS, Google, Microsoft). These are service launches, not capacity figures, so I left them.
7. **Vietnam**: Starmason (60 MW, Sembcorp JV) and "STT GDC sold out of a 60 MW Ho Chi Minh City project" may or may not be the same project. Not verified.
