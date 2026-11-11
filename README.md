# Malaysia's Compute Bet

An interactive story of Malaysia's AI data centre boom: who is building, whose computing it serves, and what it asks of Malaysia's power, water and fuel imports. Built as a final project for *Geo-economics of Asian Energy Security* (Tsinghua University, Schwarzman College, fall 2026), and the start of a tracker of middle-power AI infrastructure.

**Live site:** served by GitHub Pages from `docs/`.

## What's inside

| Path | What it is |
|---|---|
| `docs/index.html` | The built page (self-contained; open it in any browser) |
| `data/` | Datasets behind the page, one row per fact, each with a source URL and confidence rating |
| `notes/` | Research notes per dataset, plus the independent fact-check |
| `src/template.html` | Page layout, styles and chart code |
| `src/texts.py` | Page prose and footnotes |
| `src/build.py` | Merges data and text into `docs/index.html` |
| `geo/` | Map geometry (Natural Earth via world-atlas) and the scripts that built it |

Key datasets: `sites.csv` (Malaysian data centre campuses), `events.csv` and `security_events.csv` (timeline), `countries.csv` plus `countries_apply.csv` (global capacity and build costs, with curated fixes), `chip_tiers.csv`, `energy.csv` and `energy_mix.csv`, `speed_chart.csv`, `johor_chart.csv`.

## Rebuild

```bash
python3 src/build.py      # writes docs/index.html
```

To change data, edit a CSV in `data/` and rebuild. To change wording, edit `src/texts.py` or `src/template.html`.

## Method notes

- China and US capacity come from SemiAnalysis's building-level model; other countries are broker city-market sums (mainly Cushman & Wakefield), so they are not strictly comparable.
- Dollar figures are estimates: capacity × build cost per MW, building only, chips excluded.
- 2030 LNG scenarios are student estimates and an upper bound (all new load assumed met by gas).
- Megaspeed material reports allegations under investigation; no one has been charged.

All data comes from public sources, cited row by row.
