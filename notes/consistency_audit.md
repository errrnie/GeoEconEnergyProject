# Consistency and story-flow audit (pre-publication)

Audited 12 Nov 2026. I read the source files listed below and changed nothing else. I compared every figure against the other pages, the shared and regional data, and the three fact-check reports. I did not re-open outside sources. Where two project files disagree, the proposed wording follows the fact-check reports or the better-sourced row, and says "verify" where neither settles it.

Scope: `src/landing.py`, `notes/story_v2.md` and `data/region/story_v2.md`, `data/region/*` (including the old `story.md`), `markets/{singapore,malaysia,thailand}/*`, the shared data, and the timeline CSVs that feed each page. I also checked the Indonesia and Vietnam notes.

**The files changed while I was auditing.** Between 19:01 and 19:07 these appeared or changed: draft pages `markets/indonesia/` and `markets/vietnam/`, a new `data/philippines/`, a rewritten `src/landing.py`, and `data/region/story_v2.md`. I re-checked the landing, both story copies and the main Vietnam text against the issues below. The `docs/` build still predates all of this.

---

## 0. Landing story: fixed during the audit, with leftovers

When I started, `src/landing.py` read a missing `data/region/landing_text.html`, so the built landing had **no narrative**. The updated `landing.py` now renders `data/region/story_v2.md` between the map and the cards and builds the cards heading from the page count. Both changes are good. What remains:

| # | File | Issue | Fix |
|---|---|---|---|
| 0a | `notes/story_v2.md` vs `data/region/story_v2.md` | There are now **two different copies**. The `data/region` one adds deep-dive links and a "Beyond Johor and Singapore" section; the `notes` one does not. | Keep only `data/region/story_v2.md` and delete or clearly mark the copy in `notes/`. Apply the story fixes in this audit to the `data/region` copy. |
| 0b | `data/region/story.md` | The **old, uncorrected** story is still next to v2 ("more than Singapore's 1,068MW", "the most in Asia Pacific", "neutral host for both stacks", "Speed to power, more than tax breaks", "Demand did not wait"). | Delete or archive it. |
| 0c | `data/region/story_v2.md` | It links to `indonesia/index.html` and `vietnam/index.html`. These work only if both drafts build. If either is held back, the link is a 404. | Publish both pages or remove the links. |
| 0d | `src/landing.py` banner | "Draft · regional overview · sources linked on each country page". The story now has its own source list. | "Draft · regional overview · sources below and on each country page". |

---

## 1. Number consistency (problems first)

### 1.1 Singapore operating capacity: four numbers, and the page contradicts its own chart

| Where | Current text | Figure / source |
|---|---|---|
| `markets/singapore/body.html` hero KPI | "Live data centre capacity ~1.46 GW · BMI, 2026, up from about 1 GW when the pause ended in 2022" | 1,460 MW, BMI |
| `markets/singapore/config.json` funnel | `"Singapore live capacity, 2026 (BMI)",1460` next to `"Johor live capacity, H1 2026 (Knight Frank)",1110` | BMI vs Knight Frank (mismatched sources) |
| `markets/singapore/body.html` why-card | "Johor added about 700 MW in 18 months and drew level." | implies about 1.1 GW |
| Capacity chart (`data/singapore/capacity_chart.csv`) | 2026 H1 Singapore 1,118 | Knight Frank |
| Global chart (`data/shared/countries.csv`) | Singapore 1.043 GW op | C&W H2 2025 |
| `data/region/hubs.csv`, `countries.csv` | 1,043 (note: H1 2026 1,068) | C&W |
| `notes/story_v2.md` | "about level with Singapore, which sources put at 1,068MW to 1,118MW" | C&W / KF |

**Contradictions on the Singapore page itself:**
- The global section says "Singapore has the most operating capacity in Southeast Asia". The chart right below it shows **Malaysia 1.29 GW against Singapore 1.043 GW**.
- The hero says ~1.46 GW and the driver card says Johor "drew level" at about 1.1 GW. They cannot both hold.
- The funnel shows Singapore 350 MW ahead of Johor. That only happens because the two bars use different sources.

**Proposed single wording:** use Knight Frank's mid-2026 figures for both markets everywhere and mention BMI once as a broader count.
- Hero KPI: "Operating capacity **~1.1 GW** · Knight Frank, mid-2026 (1,118 MW), level with Johor. BMI's broader count is about 1.46 GW."
- Funnel bar: `"Singapore operating capacity, mid-2026 (Knight Frank)",1118,"~1.12 GW"`
- Lede: "Singapore is still one of Southeast Asia's two largest data centre markets, level with Johor next door, and it is the region's network core."
- Global section: "Singapore has a large operating base for one city but one of the smallest pipelines on the chart, which is what rationing looks like."
- Also check `data/shared/countries.csv` (Singapore notes, "Knight Frank 2025 live: 1,110 MW"). 1,110 is Johor's mid-2026 figure, so this may be a mix-up. **Verify.**

### 1.2 Johor 1,110 MW

The figure is consistent everywhere: Malaysia why-card, the Malaysia and Singapore capacity charts, hubs.csv and story_v2. Only the attribution varies (capacity chart says Knight Frank, hubs and story say C&W). Both sources report 1,110 MW.
**Proposed note wording (both capacity charts):** "Johor 1,110 MW in mid-2026 (Cushman & Wakefield and Knight Frank agree)." No number change is needed.

### 1.3 Malaysia vs Thailand LNG and the "three times" ratio

| Where | Current text |
|---|---|
| `markets/malaysia/texts.py` energy stat | "2.26 Mt · LNG Malaysia imported in 2025 (about 3.2 Mt in 2024)" |
| `markets/thailand/texts.py` energy stat | "~10.6 Mt · LNG imported in 2024 (EPPO-derived; trade data suggest about 11.5), about three times Malaysia's" |
| `markets/thailand/texts.py` "Compared with Malaysia" | "Thailand already imports about three times as much LNG" (present tense) |

**Problem:** the 3x ratio only holds for 2024 (10.6 / 3.2 = 3.3). The Malaysia page leads with **2025** (2.26 Mt), so a reader coming from it works out 10.6 / 2.26 = 4.7x. Using trade data (11.5), the 2024 ratio is 3.6x.
**Proposed single wording:**
- Thailand stat: "~10.6 Mt · LNG imported in 2024 (EPPO-derived; trade data suggest about 11.5), about three times Malaysia's 3.2 Mt that year"
- Thailand callout: "Thailand imported about three times as much LNG as Malaysia in 2024, and about four and a half times as much in 2025, when Malaysia's imports fell to 2.26 Mt."

### 1.4 Build costs 14.4 / 9.6 / 8.8

These are consistent across the Malaysia, Singapore, Thailand and draft Indonesia pages and `countries.csv`. Vietnam's notes (7.2 vs Malaysia 9.6) and Indonesia (8.3) also agree. One small gap remains:
- `markets/malaysia/texts.py` `__WHY_COST__`: "Thailand, Indonesia, India and Vietnam all build for less." The cost chart that opens from the same card also shows China (7.1) and the Philippines (8.2) below Malaysia.
  **Proposed:** "...Thailand, Indonesia, the Philippines, India, Vietnam and China all build for less."
- `markets/indonesia/body.html` says build costs are "among the lowest in the region". That is fine (8.3, behind Vietnam 7.2 and the Philippines 8.2).

### 1.5 Megaspeed totals: US$4.6bn vs US$4.8bn vs US$7.5bn (and "bought" vs "set to buy" US$2bn)

| Where | Current text |
|---|---|
| `markets/malaysia/texts.py` callout and stat | "at least US$4.6 billion and about 136,000 Nvidia GPUs imported by its Malaysian and Indonesian units from 2023 to November 2025"; stat "US$4.6bn+" |
| `markets/indonesia/texts.py` (draft) | "at least US$4.6 billion ... in 2023 to 2025" |
| `markets/singapore/texts.py` | "in November 2026 reports alleged larger flows through Singapore and Malaysia" (no figure) |
| `data/singapore/events.csv` 2026-11-11 | "Reports allege Megaspeed moved US$7.5bn of Nvidia chips via Singapore and Malaysia" (The Information) |
| `notes/megaspeed_notes.md` | Fortune citing NYT, "more than US$4.8B" over two years |
| `data/malaysia/security_events.csv` 2025-10-10 | title "NYT: Megaspeed's Malaysian unit **bought** nearly US$2B of Nvidia chips" |
| `data/singapore/events.csv` 2025-10-09 | "it was **set to buy** about US$2bn of Nvidia technology" (same NYT story, dated a day earlier) |

**Problems:**
- The three totals measure different things: customs imports by two units, chips "moved through", and a two-year NYT count. No page explains this.
- The Malaysia box is stale. It does not mention Singapore's investigation (confirmed 11 Nov) or Nvidia's board review (8 Nov), which the Singapore timeline does mention.
- The same NYT report appears as "bought" on one timeline and "set to buy" on another, with different dates.

**Proposed single wording** (Malaysia keeps the full box; Singapore and Indonesia reuse the first two sentences and link to Malaysia):
> "Bloomberg's analysis of customs records found that Megaspeed's Malaysian and Indonesian units imported at least US$4.6 billion of Nvidia hardware (about 136,000 GPUs) from 2023 to November 2025. On 11 November 2026 The Information reported that at least US$7.5 billion of Nvidia chips moved through Megaspeed and its Malaysian unit, a wider measure that is not directly comparable. US and Singapore authorities are reported to be investigating, and Nvidia's board opened an independent review on 8 November. These are allegations. Nobody has been charged, and Megaspeed denies wrongdoing."
- Keep the stat box at "US$4.6bn+ (customs records, 2023 to Nov 2025)". Drop the US$4.8bn or footnote it.
- Make the two Oct 2025 timeline rows match. Use one date, and write "was set to buy about US$2bn" on both, unless the NYT text says purchases were completed.

### 1.6 Chip-rule dates (Nov 2023 China-parent rule, May 2026 guidance, Diffusion Rule)

The country page prose is right. `__TNOTE_NOW__` says "since November 2023 ... BIS confirmed in May 2026". The fact-check's **wrong** framing ("since 31 May 2026" / "closed the gap") survives in the data that feeds the pages:

| File | Current text | Visible where |
|---|---|---|
| `data/singapore/events.csv` 2026-05-31 | title "US BIS guidance requires licences for chips to China-parented firms anywhere"; "a step reported to close the route Chinese firms used to build compute in Singapore and Malaysia" | Singapore timeline (All events) |
| `data/indonesia/events.csv` 2026-05-31 | "closing the gap opened in May 2025" | Indonesia timeline |
| `data/shared/chip_tiers.csv` (about 40 rows, incl. Indonesia, Philippines) | "buyers whose ultimate parent is in China/D:5 or Macau need a licence, BIS guidance 31 May 2026" / "Parent-company rule (31 May 2026 guidance)" | hover text on the "Now" map, **every page** |
| `notes/chip_notes.md` l.16; `data/thailand/chips_geo_notes.md` l.8 | "Since 31 May 2026, China- or Macau-parented buyers need a licence anywhere" | notes (source of future copy) |

**Proposed single wording** (all of the above):
> "Since 17 November 2023, anyone supplying advanced US AI chips to a company headquartered in China or Macau, or with its ultimate parent there, has needed a US licence wherever that company operates. BIS guidance of 31 May 2026 confirmed this still applies and let existing operators keep chips already installed."
- Timeline title for every 2026-05-31 row: "BIS reaffirms licences for China-parented buyers anywhere" (Malaysia's EVSIG already says this well).
- chip_tiers short form: "Parent-company rule (since Nov 2023, reaffirmed 31 May 2026)".

**AI Diffusion Rule dates:**
- `data/singapore/events.csv` dates it **2025-01-15**. Every other timeline (Malaysia, Thailand, Indonesia, Vietnam, region) uses 2025-01-13. **Proposed:** 2025-01-13 everywhere, with "announced 13 Jan, published 15 Jan" in the note (`__TNOTE_JAN__` already says "published 15 Jan").
- `data/vietnam/events.csv` 2025-01-13: "framework took effect". The other pages say compliance never began. **Proposed:** "was announced; Vietnam fell into Tier 2. It was rescinded before compliance began."
- `data/region/timeline.csv` 2025-01-13: "(issued 15 January per BIS)". **Proposed:** "(announced 13 January, published 15 January)".

**Malaysia/Thailand draft rule**, worded three ways:
- Malaysia callout: "Commerce said in May 2025 it would add requirements for Malaysia and Thailand and has not published them" (implies the rule is still pending).
- Thailand lede: "a US draft aimed specifically at Malaysia and Thailand followed in July 2025".
- Thailand callout and shared note: "reportedly shelved in August 2026".
**Proposed (both pages):** "Commerce said in May 2025 it would add licence requirements for Malaysia and Thailand. Bloomberg reported a draft in July 2025, which was reportedly shelved in August 2026. No rule was published."

### 1.7 US tariffs on each country (no page gives them on a common basis)

| Country | Where | Current text |
|---|---|---|
| Thailand | `markets/thailand/texts.py` stat | "12.5% · US tariff on most Thai goods since July 2026, against Malaysia's 10%" |
| Malaysia | `data/malaysia/events.csv` 2025-10-26 (Malaysia timeline) | "Trump and Anwar signed a trade deal holding the US tariff at 19%." No later update. |
| Malaysia | `markets/malaysia/texts.py` chip callout | deal "unratified and under review after the US Supreme Court struck down the tariffs behind it" (no current rate) |
| Indonesia | `markets/indonesia/texts.py` (draft) | "10% US duty on most Indonesian goods since July 2026" |
| Vietnam | `data/vietnam/events.csv`, notes | 12.5% Section 301 from 24 Jul 2026 (covers about 37% of exports) |
| Singapore | none | no rate anywhere |

**Problem:** a reader of the Malaysia page sees 19%, and the Thailand page says Malaysia pays 10%. The legal basis of Malaysia's 10% comes only from Tilleke's line on Thailand. **Verify** whether it is Section 301, as it is for Indonesia.
**Proposed single wording** (one shared footnote, plus a Malaysia timeline row dated 2026-07-24):
> "After the Supreme Court struck down the IEEPA tariffs on 20 Feb 2026, a temporary 10% Section 122 tariff applied until 24 Jul 2026. Since then Section 301 duties apply: 12.5% on most Thai goods and on Vietnamese goods covered by the case, and 10% for Malaysia and Indonesia. The 2025 to 2026 reciprocal deals (19 to 20%) are signed but not in force."
Add Singapore's rate or say "not covered".

### 1.8 Singapore tenders: 80 MW (2023) and 200 MW (2026)

Dates and sizes match across `markets/malaysia/texts.py` (`__WHY_SG__`, `__SG_NOTE__`), the Singapore page, `data/malaysia/events.csv`, `data/singapore/events.csv` and the regional timeline (pilot 14 Jul 2023, about 80 MW provisional; DC-CFA2 launched 1 Dec 2025, 200 MW awarded 21 Aug 2026). Two wording issues:
- "tender" (Malaysia, Singapore pages) vs "call" (story_v2, timeline) vs "DC-CFA" (Singapore timeline). **Proposed:** "call for application" on first mention on each page, then "call".
- `__WHY_SG__`: "has since released only about 280 MW through two tenders". This leaves out the 2024 Green Data Centre Roadmap (at least 300 MW from efficiency, on the Singapore timeline), and Singapore's own base grew more than 280 MW on BMI's count. **Proposed:** "...has since awarded only about 280 MW of new capacity through two calls for application, plus efficiency gains under a 2024 roadmap."

### 1.9 Thailand pause: 49 vs 166

- `notes/story_v2.md`: "Thailand paused 49 projects under construction in September 2026, more than the 35 it had running."
- Thailand hero, tagline and callout: "paused 166 projects".
**Proposed (landing):** "Thailand paused 166 projects in September 2026, 49 of them under construction, more than the 35 it had running." This links the two headline numbers.

### 1.10 Malaysia "31%": national vs Peninsular

- Hero KPI (fixed): "Data centres' share of **Peninsular** power demand 31% by 2035".
- `data/malaysia/events.csv` 2026-06-30 (a key date, so it shows by default): title "Data centres forecast to use 31% of power by 2035", significance "nearly a third of **national** demand", description "about 7% of electricity".
**Proposed:** title "Data centres forecast to use 31% of Peninsular power by 2035"; significance "Puts the stakes in one number: nearly a third of Peninsular demand."

### 1.11 Indonesia and Vietnam capacity (conflicts the next pages will bring)

| Figure | Values in the project |
|---|---|
| Indonesia operating | Global chart 0.39 GW (C&W via Computer Weekly); story_v2 Greater Jakarta 356 MW (C&W H1 2026); draft page KPI ~0.58 GW (PLN, national IT); Batam 8 MW (DC Byte 2025) |
| Indonesia page note | `markets/indonesia/body.html`: "Indonesia's bar is the Jakarta broker market." The bar (0.39) matches neither 356 nor 322 MW |
| Indonesia fuel | story_v2 "About 82% of Indonesia's power comes from fossil fuels" (Knight Frank) vs draft page "~67% coal" (ESDM 2025) |
| Vietnam operating | story_v2 "about 73MW operating" vs `data/vietnam/notes.md` "roughly 60 to 150MW depending on the source" (Viettel about 104 MW; Savills 524.7 MW) |
| Vietnam US presence | region `countries.csv` "AWS Local Zone in Hanoi (reported, date not verified)" vs Vietnam notes "2026-06-19: AWS Local Zone Hanoi goes live" |

**Proposed:**
- Indonesia global-chart note: "Indonesia's bar (0.39 GW operating) is Cushman & Wakefield's tracked market, which is mostly Greater Jakarta (356 MW in H1 2026). PLN counts about 580 MW of data centre IT capacity nationally."
- story_v2 Indonesia: replace the 82% fossil line with "Coal made about two thirds of Indonesia's power in 2025, and about 60% on the Java grid where almost all data centres sit." This matches the Indonesia page.
- Vietnam: the new draft page uses "~73 MW (C&W, Apr 2026); other estimates run from 60 to 148 MW", which matches the landing's 73 MW. Keep that and update the AWS Hanoi line in `data/region/countries.csv` (it went live on 19 Jun 2026, per the Vietnam page).

### 1.11b New Vietnam draft (`markets/vietnam/`, 19:06) checked against the issues above
- Its chip lede says Vietnam needed a licence "from October 2023". Malaysia's note says "since November 2023". Both mean the October 2023 rules, which took effect on 17 Nov 2023. Use "rules issued in October 2023 (in force 17 Nov 2023)" on every page.
- Chip lede "the rule's repeal in May 2025" should read "rescission", to match the other pages. `data/vietnam/events.csv` still says the Diffusion framework "took effect" (1.6).
- The tariff stat (12.5% Section 301 since July 2026, after the earlier 20%) matches 1.7.
- The C4ADS allegation (GPUs routed "through Vietnam, India and Malaysia") does not appear on the Malaysia page. Add one clause to Malaysia's enforcement list, or drop "Malaysia" from Vietnam's sentence.
- The energy callout's LNG comparisons (Malaysia high case about 7 Mt, Thailand about 9 Mt) match the configs (7.35, 9.04).
- It uses the "Middle power compute" eyebrow and the "Proposed" and "Approved" site statuses (2.3).

### 1.12 Smaller number and status mismatches

| File | Current | Proposed |
|---|---|---|
| `data/thailand/events.csv` 2026-08-14 | "Grid-access bond of 4.5m baht per MW **proposed** ... status not final" | Delete the row, or retitle it "Grid bond details reported" and note that the NEPC approved it on 15 Jul. The Thailand body and the 15 Jul row already say "approved", so the page contradicts itself. |
| `data/malaysia/events.csv` 2023-08-09 (key date) | "TNB launched a fast-track that **cut** grid connection ... to about 12" | "...that **aimed to cut** ...". Same in `markets/indonesia/body.html`: "against about 12 under Malaysia's Green Lane" becomes "against the roughly 12 months Malaysia's Green Lane targets". |
| `markets/thailand/body.html` KPI and `config.json` funnel | "Data centre **load** today ~0.1 to 0.2 GW" / "Running today" | "Operating capacity today ~0.1 to 0.2 GW". BMI's 216 MW is capacity, not load. |
| Singapore hero | "up from about 1 GW when the pause ended in 2022" | Keep this with the ~1.1 GW headline ("up from about 1 GW in 2022"). Next to 1.46 GW it mixes two series. |
| Hormuz / Qatar | Malaysia "When the strait was disrupted in March 2026"; Thailand "The March 2026 Hormuz disruption"; Singapore "Qatar's cargoes stopped in April 2026 when war hit the Gulf" | Shared phrase: "the March 2026 Hormuz disruption, which halted Qatari LNG cargoes to Singapore from April". |

---

## 2. Wording consistency

### 2.1 Macro claims corrected in `macro_factcheck.md` that are still live

| # | File | Current text (old version) | Proposed |
|---|---|---|---|
| A | `src/landing.py` hero lede | **Mostly fixed during the audit.** The old "The overflow is landing in Southeast Asia" is gone. The new line still says capacity "is now reaching Bangkok, Jakarta, Batam and Ho Chi Minh City", but Bangkok is paused and Ho Chi Minh City has about 33 MW. | "...It started in Singapore, crossed the causeway to Johor, stalled in Bangkok, and is now building in Jakarta and Batam, with Vietnam just opening." |
| B | `markets/singapore/body.html` why-card | "Everyone's neutral ground ... That neutrality is now under strain from chip diversion cases." | "**Both stacks, under US rules.** American, Chinese and local operators all run sites here, and many firms book Asian revenue through Singapore. Hosting both now means policing US chip rules, as the 2025 server fraud case showed." |
| B | `markets/singapore/body.html` weak points | "Its neutral-hub reputation is being tested..." | "Its reputation as a trusted hub is being tested..." |
| C | `markets/malaysia/body.html` why-card | "US chip controls from October 2022 pushed Chinese firms to compute offshore, while the AI boom sent US hyperscalers looking for capacity they could get quickly." | "Chinese clouds arrived first (Alibaba in 2017). US chip controls later added a new reason, since Chinese firms can legally rent Nvidia capacity here that they cannot import at home. Meanwhile the AI boom sent US hyperscalers looking for fast capacity." |
| C | `data/malaysia/events.csv` 2022-10-07 (key date) | significance "Created the incentive for Chinese firms to seek compute in third countries such as Malaysia." | "Began the controls that, from 2025, made offshore Nvidia capacity in Malaysia valuable to Chinese firms." |
| C | `data/region/timeline.csv` 2022-10-07 | "Started the decoupling that made neutral Southeast Asian hosts valuable to both sides." | Same as above, with "Southeast Asia" in place of "Malaysia". |
| D | `notes/story_v2.md` §4 | does not mention Malaysia's federal halt on non-AI approvals (macro #10) | add: "Malaysia halted approvals for non-AI data centres in February 2026." |
| E | `notes/story_v2.md` | emissions covered only through Singapore's green-power condition (macro #12, partly fixed) | add one Ember line (Malaysia data centre demand 9 to 68 TWh, 2024 to 2030). |
| F | `data/region/countries.csv` and `data/shared/countries.csv` Malaysia notes | "1,039MW under construction, the most in APAC" | "the most in Southeast Asia" (not shown on any page, but these rows feed later copy). |

Claim B is correct everywhere ("Outside the Americas, Asia Pacific has the largest pipeline"). Old `story.md` holds every other uncorrected claim. See section 0.

### 2.2 Allegations framing

| File | Current | Proposed |
|---|---|---|
| `markets/malaysia/texts.py`, callout "Why this is an energy security question too" | "**Proven diversion, like the two US prosecutions** involving Malaysia, invites tighter rules on the whole country" | "Diversion cases, proven or not, such as the two US prosecutions involving Malaysia, invite tighter rules on the whole country". Charges are not proof, and the fact-check (#11) asked for this change. |
| `markets/malaysia/texts.py` Megaspeed box | "Nvidia says it has no reason to believe its secrets were compromised" (this answers the October 2026 spying story, not diversion) | Replace with the shared box in 1.5. |
| `data/thailand/events.csv` 2026-03-01 (key date) | significance "Put Thailand at the centre of a US AI chip smuggling case." The indictment named only "a company based in Southeast Asia" | "Two months later Bloomberg's sources tied the case's 'Company-1' to a Bangkok firm." |
| Thailand page | omits the Nov 2025 DOJ case (A100s via Malaysia **and Thailand**), which Malaysia counts as one of its "2 US criminal cases" | Add one clause to the Thailand chip callout. Otherwise the two pages tell different enforcement stories. |

The Singapore, Thailand and Indonesia pages already use "These are allegations ... nobody has been charged". Use that exact closing sentence on Malaysia too.

### 2.3 Terms to standardise

| Concept | Current variants | Use |
|---|---|---|
| Built and running capacity | "operational" (chart), "operating" (map, hubs), "live" (Singapore KPI and funnel, story_v2), "running today" (Thailand funnel), "load" (Thailand KPI) | **operating** in prose; keep "Operational" only as the chart legend. Use "drawn" or "load" only for grid draw (Malaysia's 1.37 GW). |
| Not yet built | "pipeline", "planned pipeline" (Thailand funnel and scenario), "pipeline with dates" (old), "announced", "promised" | **pipeline = under construction + planned**. Define it once on the landing. Thailand: "Pipeline (The Nation, Aug 2026)", not "Planned pipeline". |
| Stack tags | Landing legend "Other or local" / "Unknown"; country pages "Other or Malaysian" / "Unknown or mixed" | "Unknown or mixed" on the landing too. |
| Chinese ownership | "Chinese-parented" (Malaysia, Singapore, Thailand prose), "China-parented" (timelines, chip notes) | **China-parented** (closest to BIS wording). |
| DayOne tag | China-linked in `data/malaysia/sites.csv` and `data/thailand/sites.csv`; **Mixed** in `data/singapore/sites.csv` and `data/indonesia/sites.csv` | Pick one rule and state it once on the landing ("DayOne is tagged China-linked as GDS's former arm; a judgment call"). |
| Site status | `Paused/Cancelled` (Malaysia), `Cancelled` (Indonesia), `Proposed`, `Approved` (Vietnam) | The template styles only Operational, Announced and Paused/Cancelled. Indonesia's "Cancelled" and Vietnam's "Proposed" and "Approved" will draw like **under construction**. Map them to the four statuses before Indonesia and Vietnam go live. |
| "Middle powers" | Eyebrow "Middle power compute · ..." on all four country pages; README "middle-power AI infrastructure"; the landing never uses it, and the macro check replaced "middle powers" with "fast-growing hosts" | Make the eyebrow match the landing and nav: "Southeast Asia compute · Malaysia · 2017 to 2026". Or define "middle powers" once on the landing. Singapore does not fit the term well. |
| Singapore's capacity calls | "tender", "call", "DC-CFA" | see 1.8 |
| Diffusion Rule end | "scrapped" (Malaysia and Thailand ledes), "dropped" (note), "rescinded" (timelines) | "rescinded" in prose; the note keeps the precise "BIS announced its rescission ... stopped enforcing it". |
| Landing histogram colours | `col={...Indonesia:"var(--cn)",Vietnam:"var(--us)"}` in `src/landing.py` | These are the China-linked and US-linked colours from the map legend on the same page, so Indonesia bars read as "China". Use neutral country colours. |

---

## 3. Story flow

### 3.1 How it reads now
- **Landing** (as of 19:07) runs lede → map → story → cards, with deep-dive links in the story. That is the right order. Leftovers are in section 0 and 2.1-A.
- **Country pages** all open with a self-contained hero, and **none ends with a link onward**. Every page ends on a risk list and then sources. Malaysia's lede opens with the global US/China framing, not Singapore. Thailand never mentions Singapore or Johor spillover. Only Singapore's lede points to Johor and Batam.
- **Contradictions between pages:** Thailand's callout says "Malaysia promised 8.3 GW and kept building". The landing (story_v2) says hosts braked region-wide, and Malaysia's own timeline shows Johor's water rule (Nov 2025) and the non-AI halt (Feb 2026). Indonesia's draft says Batam "became" Singapore's other overflow, while the landing says the deal "could make Batam a second Johor" and Batam had 8 MW operating in 2025.
- **Eyebrow date spans** do not line up with the story. Singapore's is "2014 to 2026" while the landing story starts with AWS Singapore in April 2010, and the Singapore page itself says AWS has been there "for over a decade". **Proposed:** Singapore "2010 to 2026", and add the AWS 2010 row to `data/singapore/events.csv` (it is already in the regional timeline).

### 3.2 Proposed "how the pages connect" outline

1. **Landing: the regional arc.** US/China hold about 90% → Singapore decade (2010 to 2018) → pause and land grab (2019 to 2022) → AI build-out (2022 to 2024) → brakes and chip rules (2025 to 2026) → beyond Johor and Singapore. The narrative now sits before the cards. End it with a "read in this order" line. The global capacity chart, January 2025 tier map and US/China compute shares live **here only**.
2. **Singapore: the hub that chose scarcity.** Cables, trust and booking centre; pause and rationing; gas imports. It **hands off** to Johor (Malaysia) and Batam (Indonesia).
3. **Malaysia: the main winner.** Johor took Singapore's overflow, then AI demand from both stacks. 8.3 GW promised, 1.37 GW drawn, LNG bet, Megaspeed. It **hands off** to Thailand as the contrast.
4. **Thailand: the pause.** Cheaper builds and cloud regions, then 166 projects paused and a data centre tariff. It **hands off** to the next big pipeline.
5. **Indonesia: the next front, on two fronts.** A Jakarta home market on coal, and Batam as Singapore's second overflow (this loops back to page 2). It **hands off** to Vietnam.
6. **Vietnam: the open door, still small.** Full foreign ownership, data localisation, the only host here already needing a US licence for top chips (D:1). It **returns** to the landing for the comparison.

### 3.3 Bridge lines (drop-in, 1 to 2 sentences)

**Landing, end of narrative (before the cards):**
> "The country pages follow that path in order. Start with Singapore, where the story begins, then follow the overflow to Johor, the pause in Thailand and the next fronts in Indonesia and Vietnam."

**Landing cards h2:** this is now built from the page count ("Five hosts, five bargains"), so no change is needed.

**Singapore**
- Lede, final sentence (replaces "This page follows how the hub chose scarcity and what that did to the region."): "This page follows how the hub chose scarcity. The capacity it turned away crossed the causeway to Johor, which the Malaysia page picks up, and more slowly the strait to Batam."
- Ending (after Leverage): "Next: Malaysia, where Singapore's overflow became the region's largest build-out."

**Malaysia**
- Lede, new first sentences: "When Singapore paused new data centres in 2019, developers looked across the causeway to Johor. AI demand from both US and Chinese firms then filled it, making Malaysia the region's clearest winner so far." Keep the 90% sentence after this, or drop it once the global framing lives on the landing.
- Ending: "Malaysia's brakes since late 2025 are selective. Thailand, the next page, went further and stopped the clock on 166 projects."

**Thailand**
- Lede, opening (replaces "Thailand drew some of the region's largest cloud pledges, then hit the brakes."): "In 2025 Thailand looked like the next Johor, with cheaper builds and new AWS and Google regions. In September 2026 it chose to pause instead."
- Ending: "With Thailand paused and Johor short of water, the region's next large pipeline is Indonesia's, in Jakarta and on Batam across the strait from Singapore."
- Fix the "Compared with Malaysia" callout: "Malaysia braked selectively, with water rules in Johor and a halt on non-AI projects, while honouring 8.3 GW of supply deals. Thailand stopped the clock on 166 projects and moved to charge data centres more for power."

**Indonesia (draft)**
- Lede: change "became Singapore's other overflow after Johor" to "**is becoming** Singapore's second overflow after Johor". Optional opener: "Indonesia holds the region's next large pipeline, and Batam brings the story back to Singapore."
- Ending: "Vietnam, the last page, has opened its doors in law, but its capacity is still small, and it is the only host here that already needs a US licence for top chips."
- Bridge to Malaysia in the energy section (both pages benefit): "Malaysia's coal comes mostly from Indonesia (three quarters of its 2025 imports), so the two grids are already linked by fuel."

**Vietnam (to write)**
- Lede: "Vietnam is the newest contender. It allowed full foreign ownership of data centres from 2025 and keeps important data onshore, but its operating base is roughly 70 to 150 MW."
- Ending: "Back to the regional map to compare all five hosts."

### 3.4 Repeated on every page; move to the landing

| Module | Where now | Recommendation |
|---|---|---|
| Section 1 global chart (same h2, controls, legend and `__GNOTE__` on all four pages) | `body.html` §1 on each page; `__GNOTE__` copied from Malaysia | Move it to the landing. On country pages, swap in a Southeast Asia-only bar (5 to 6 rows, current country highlighted) or a single line ("Malaysia: 1.29 GW operating, 3.59 GW pipeline; see the regional chart"). |
| January 2025 tier world map and `__TNOTE_JAN__` (identical), `__TNOTE_NOW__` (only the place name changes) | §6 on each page | Move the world map and both notes to a landing section, "The chip rules". Each country page keeps only its own position callout and one status line. |
| "Two stacks" why-panel (Epoch 75% / 15%, SemiAnalysis ~4 GW) | `src/template.html` `PANELS.stacks`, shown on every page | Landing only. On country pages, show that country's stack counts instead. |
| Chip ledes ("In January 2025 the US sorted the world into three tiers...") | Malaysia and Thailand nearly word for word; Singapore and Indonesia paraphrase it | Explain the tiers once on the landing. Each country lede starts from its own position. |
| Megaspeed box | Malaysia, Singapore, Indonesia | Full story on Malaysia (largest site). Two sentences plus a link elsewhere (see 1.5). |
| Johor vs Singapore capacity chart | Malaysia and Singapore (same data) | Keep it on both, since it is the hinge of the story, but use the same source note (1.2). |

---

## 4. Top 10 fixes, in priority order

1. **Clean up the story sources.** The landing now renders `data/region/story_v2.md`. Delete the old `story.md` and the out-of-sync `notes/story_v2.md`. Confirm the Indonesia and Vietnam links resolve, then rebuild `docs/` (section 0).
2. **Landing lede and story text.** Drop "reaching Bangkok" (2.1-A). In the story, use 166 paused with 49 under construction (1.9), Indonesia's coal share (1.11), and add the federal halt (2.1-D).
3. **Singapore capacity.** Use one series (Knight Frank about 1.1 GW, level with Johor) in the hero, funnel and lede. Remove "most operating capacity in Southeast Asia", which the page's own chart contradicts (1.1).
4. **Chip-rule dating.** Change "31 May 2026 / closed the gap" to "since Nov 2023, reaffirmed 31 May 2026" in the Singapore and Indonesia timelines and in `chip_tiers.csv` hover text on every page. Use 13 Jan 2025 for the Diffusion Rule everywhere. Fix Vietnam's "took effect". Align the Malaysia/Thailand draft-rule sentence (1.6).
5. **Malaysia "Proven diversion, like the two US prosecutions"**: reword to allegations framing (2.2). This is a legal-risk sentence.
6. **Megaspeed.** Use one shared box that separates US$4.6bn (customs, 2023 to Nov 2025) from US$7.5bn (The Information, 11 Nov 2026), drop or footnote US$4.8bn, add the Singapore probe and Nvidia board review, and fix the "bought" vs "set to buy" US$2bn rows (1.5).
7. **US tariffs.** Add one shared, dated line per country. The Malaysia timeline still says 19% while the Thailand page says Malaysia pays 10%. Verify Malaysia's legal basis and Singapore's rate (1.7).
8. **Cross-page contradictions in the Thailand material.** Fix the LNG "three times" year basis (1.3), "Malaysia ... kept building" (3.3), 49 vs 166 on the landing (1.9), and the "proposed" grid bond row against the approved bond (1.12).
9. **Bridges.** Add the lede and ending bridge lines (3.3). Change Indonesia's "became" to "is becoming". Fix the Singapore eyebrow to 2010.
10. **De-duplicate and standardise.** Move the global chart, tier map and US/China panel to the landing (3.4). Replace the "Middle power compute" eyebrows. Standardise operating/pipeline/China-parented and DayOne tagging. Map the Indonesia and Vietnam site statuses before those pages build (2.3). Also fix Malaysia's "31% national" timeline row (1.10) and the "cut" vs "aimed to cut" Green Lane wording (1.12).

---

## Summary

The site is close, but it is not ready to publish. The landing story now renders (fixed mid-audit), but an old uncorrected story file and a second, out-of-sync v2 copy remain. Singapore's page gives four capacity figures (1.46, 1.12, 1.07, 1.04 GW) and claims a lead its own chart contradicts. The 2023 China-parent rule is still dated to May 2026 in timeline and map data on several pages. Malaysia calls two prosecutions "proven diversion". Megaspeed totals (4.6, 4.8, 7.5bn), tariffs (19% vs 10%) and the LNG "three times" ratio need one dated wording each. For flow, each page needs a lede that picks up the previous page and an ending that hands off: Singapore, Johor, Thailand's pause, then Indonesia and Vietnam. Shared global modules belong on the landing only.
