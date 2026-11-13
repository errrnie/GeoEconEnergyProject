# Southeast Asia Compute

An interactive story of how AI data centres came to Southeast Asia: where the campuses went, why, whose computing they serve, and what each host gives up in power, water and fuel imports. Built as a final project for *Geo-economics of Asian Energy Security* (Tsinghua University, Schwarzman College, fall 2026).

**Live site:** served by GitHub Pages from `docs/`. The landing page has a regional map that fills in by year and a short history of the region's build-out. Six country deep dives follow the story in order: Singapore, Malaysia, Thailand, Indonesia, Vietnam and the Philippines.

## What's inside

| Path | What it is |
|---|---|
| `docs/` | The built site: `index.html` (regional landing) and one folder per country |
| `markets/<country>/` | Each country's settings (`config.json`), page body (`body.html`) and prose (`texts.py`) |
| `data/<country>/` | Datasets behind each page, one row per fact, each with a source URL and confidence rating |
| `data/region/` | Regional story (`story_v2.md`), hubs, timeline and country summary |
| `data/shared/` | Global capacity and build costs, chip tiers, grid connection times, yearly energy mix |
| `notes/` | Research notes, fact-checks and the cross-site consistency audit |
| `src/template.html` | Shared page layout, styles and chart code |
| `src/build.py`, `src/landing.py` | Build every country page and the landing page into `docs/` |
| `geo/` | Map geometry (Natural Earth via world-atlas) and the view definitions |

## Rebuild

```bash
python3 src/build.py      # writes docs/index.html and docs/<country>/index.html
```

To change data, edit a CSV in `data/` and rebuild. To change wording, edit the country's `body.html` or `texts.py`, or `data/region/story_v2.md` for the landing story. To add a country, add `markets/<country>/` and `data/<country>/`.

## Method notes

- China and US capacity come from SemiAnalysis's building-level model; other countries are broker city-market sums (mainly Cushman & Wakefield, BMI for the Philippines), so they are not strictly comparable.
- Dollar figures are estimates: capacity × build cost per MW, building only, chips excluded.
- 2030 fuel scenarios are student estimates and upper bounds (new load assumed met by the marginal fuel: LNG, or coal on Java).
- Sites without a public location are placed at their town or technology park and labelled as approximate.
- Megaspeed and other chip diversion material reports allegations; no one has been charged unless stated.

All data comes from public sources, cited row by row.
