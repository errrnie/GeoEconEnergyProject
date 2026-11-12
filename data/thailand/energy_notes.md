# Thailand energy notes: is the data centre bet an LNG bet?

Researched 12 Nov 2026. Every number has a sourced row in this folder's CSVs. "Derived" = my arithmetic.

## Short answer

Partly. Gas made 54% of Thai power in 2025, and extra gas means LNG because domestic and Myanmar supply are flat or falling. Generation is not the constraint (55,707 MW contracted vs a 36,792 MW record peak).

## Key facts

- **Mix 2024 (EPPO):** 235.5 TWh in total. Gas 58%, imports (mostly Laos hydro) 15%, coal and lignite 14%, renewables 10%.
- **Overcapacity:** the reserve margin is about 55% (26% after adjusting for availability) against a 15% standard. Idle IPP gas plants collect capacity payments worth 0.63 THB/kWh.
- **Gas supply:**
  - Domestic output fell from 3,261 mmscfd (2020) to 2,620 (2022) around the Erawan handover, then recovered to 2,852 (2024).
  - Myanmar pipeline gas fell from about 694 to 529 mmscfd (derived), and the Yadana contract ends in 2028.
  - LNG imports reached about 10.6 Mt in 2024 (derived).
  - Regas capacity is 19 Mtpa.
- **Price:** tariff 3.95 THB/kWh; EGAT carries 31.3bn THB of unrecovered fuel costs (150bn in 2022).
- **Data centres:** 120-200 MW today, 2.87 GW pipeline, 8-8.8 GW in the PDP; 166 projects paused on 4 Sep 2026.

## Scenarios (student estimates, upper bound)

**Method.** Same as Malaysia. All data centre electricity above today's 0.89 TWh is met by gas. That baseline is 120 MW x 0.85 x 8,760 h.

- PJ = extra TWh x heat rate (GJ/MWh).
- bcm = PJ / 40.
- Mt LNG = bcm / 1.36.

**Heat rates:**

- Central: 7.61 GJ/MWh, the mean of three RATCH CCGTs in 2024.
- Efficient: 6.47 GJ/MWh, Hin Kong Unit 1.
- Fleet: 8.77 GJ/MWh, derived from EPPO and inflated by cogeneration.

| 2030 case | DC TWh | % of 2024 gen | Extra TWh | Central PJ / bcm / Mt | Efficient Mt | Fleet Mt |
|---|---|---|---|---|---|---|
| Low: Ember 6 TWh | 6.0 | 2.5% | 5.1 | 39 / 0.97 / 0.71 | 0.61 | 0.82 |
| Mid: 2.87 GW x 0.85 x 8,760 | 21.4 | 9.1% | 20.5 | 156 / 3.90 / 2.86 | 2.44 | 3.30 |
| High: 8.8 GW x 0.85 x 8,760 | 65.5 | 27.8% | 64.6 | 492 / 12.30 / 9.04 | 7.69 | 10.42 |

**Worked example (High):** 8.8 x 0.85 x 8,760 = 65.5 TWh; minus 0.89 = 64.6 TWh; x 7.61 = 492 PJ; / 40 = 12.3 bcm; / 1.36 = 9.04 Mt.

If EGAT's 3.5 GW of requests replaces the 2.87 GW pipeline, the Mid case becomes 3.52 Mt.

**Comparison with imports.** Mid adds about 27% to 2024 LNG imports, and High nearly doubles them. Agora already projects close to 19 Mt of imports by 2030 before any of this extra demand, which would fill all of today's 19 Mtpa regas capacity.

## Conflicts

- **Gas share of generation:** 54% (EPPO, 2025) vs 65% (IEEFA).
- **LNG share of gas supply:** 27% (IEEFA), 29% (EPPO, derived) and about 40% (Ember).
- **Peak demand:** an official cited "about 40 GW", but the metered record is 36.8 GW.
- **DC requests:** 35, 3.5 and 30 GW in reports weeks apart.
- **Pause:** 49, or 166 including 117 awaiting permits.
- **EEC water demand in 2027:** 800 vs 2,890 million m3. The two sources use different scopes.
- **2,000 MW pilot:** Krungsri says UGT; legal sources say Direct PPA.
- **Not verified:** Erawan's output under Chevron and JDA volumes.

## Takeaways

1. Thailand runs on gas, and new demand at the margin is met mostly with imported LNG as Myanmar supply fades.
2. Thailand has spare generating capacity, so the limits on data centres are transmission, water and the cost of LNG.
3. The planned 2.87 GW pipeline would add about 3 Mt of LNG a year by 2030, and the full PDP figure would add about 9 Mt.
4. Thailand bills data centres directly, through a proposed 5-6 THB/kWh tariff and a 4.5m THB per MW grid guarantee.
5. Water is the local flashpoint: EEC reservoirs stood at 39-52% in June 2026, and operators do not disclose their water use.

## Thailand vs Malaysia

Malaysia's import exposure is mainly coal (59% of Peninsular power), and it is shifting to LNG from imports of only about 2.3 Mt. Thailand already imports about 10 Mt, so data centres add to an import bill that is large and exposed to price swings. Malaysia promised 8.3 GW to data centres; Thailand paused 166 projects and raised their power price. Thailand is trading speed for household protection.
