# energy_mix_yearly.csv notes

**Source.** Ember, Yearly Electricity Data (2026 release, published with the Global Electricity Review, April 2026). Retrieved 2026-11-12 through OWID's energy dataset (https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv; changelog 2026-04-27). Ember's own site was blocked from this environment. For country data from 2000 onward, OWID's processing code uses only Ember, so every row (2010+) is Ember data.

**Licence.** CC BY 4.0. Credit as: "Source: Ember, Yearly Electricity Data (2026); processed by Our World in Data."

**Fields.** `share_pct` is the % of generation. For `net_imports` it is the % of demand instead (negative means net exporter), and it is blank for `total_generation` and `demand`. `other_renewables` excludes bioenergy.

**Gaps.**
- 2025 is missing for Indonesia, Laos, Myanmar and Brunei, so their latest year is 2024.
- Blank source values are left out. In many 2025 rows `other_renewables` is missing, but the totals still reconcile.
- 2025 figures are preliminary.

**Caveats.**
- Malaysia: the figures are national, including Sarawak hydro. The Peninsular grid serving Johor is more fossil-heavy, and this dataset doesn't split it out.
- Indonesia: captive coal for smelters may be under-counted (not verified), so treat coal as a possible lower bound.
- Singapore: net imports are 0.29 TWh (2025). Planned imports don't show yet.
- Laos is a major net exporter.

**Latest-year ASEAN shares (%)**

| Country | Year | Coal | Gas | Renewables | Net imports, % of demand |
|---|---|---|---|---|---|
| Singapore | 2025 | 0.9 | 91.1 | 5.5 | 0.5 |
| Malaysia | 2025 | 44.6 | 33.8 | 20.7 | -0.6 |
| Thailand | 2025 | 17.8 | 65.5 | 16.6 | 16.4 |
| Indonesia | 2024 | 61.5 | 18.5 | 18.1 | 0.3 |
| Vietnam | 2025 | 48.1 | 6.2 | 45.4 | 1.1 |
| Philippines | 2025 | 58.7 | 17.3 | 23.3 | 0.0 |
| Cambodia | 2025 | 56.6 | n/r | 40.9 | 20.7 |
| Laos | 2024 | 23.3 | 0.0 | 76.7 | -235.1 |
| Myanmar | 2024 | 5.5 | 46.1 | 47.9 | 1.0 |
| Brunei | 2024 | 19.8 | 79.1 | 0.2 | 0.0 |

Renewables = OWID `renewables_share_elec`. n/r = not reported.
