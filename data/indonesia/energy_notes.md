# Indonesia energy notes: is the data centre bet a coal bet?

12 Nov 2026. Sources in energy.csv. "Derived" = my arithmetic.

## Short answer

On Java, yes. 99% of PLN's data centre load is on the Java-Madura-Bali grid, which runs about 60% on coal, and RUPTL adds no Java fossil capacity after 2029. Batam is a separate 844 MW gas grid.

## Key facts

- **Mix:** coal was 66.7% of national power in 2025, against a 62% target. HEESI 2025 counts 494 TWh including captive plants. Java-Madura-Bali runs on coal 60%, gas 31% and renewables 8%.
- **Captive coal:** 19.3 GW, of which 15.4 GW serves nickel. Off-grid use reached 137 TWh, 2.4x the 2021 level.
- **Overcapacity fading:** Java's reserve margin of 37.5% (2025) falls below 33% by 2027. Java had rolling blackouts in June 2026.
- **RUPTL 2025-2034:** 69.5 GW, 76% of it renewable. 16.6 GW is fossil (6.3 GW coal), and 33.5 GW goes to Java.
- **JETP:** about $3.1bn approved of $21.4bn pledged. Cirebon-1's early retirement was cancelled.
- **Price and speed:** 6.3 vs 10.6 US cents/kWh in Malaysia (broker estimate), but a 100 MW connection takes 36 months vs 12.
- **Gas:** 31% of output was exported in 2025. LNG exports fell 23% in Jan-Sep 2026. Natuna export gas now goes to Batam: 25 MMSCFD at first, and up to 111 from 2027.
- **Batam:** 844 MW capability, 755 MW peak. DayOne's 450 MW is 53% of capability (derived).
- **Water:** Duriangkang supplies 80% of Batam's 382 ML/d. Data centres could need 32 ML/d by 2032, and residents protested on 5 Oct 2026.

## Scenarios (student estimates, upper bound)

**Method.** Demand is GW x 0.85 x 8,760 h, minus today's 4.32 TWh (580 MW).

- **Coal:** Mt = TWh x 11.22 GJ/MWh / 18.84 GJ/t. The heat rate is PLN Indonesia Power's 2,680 kcal/kWh. The coal is 4,500 kcal/kg GAR, the midpoint of the 4,000-5,000 design range.
- **Gas:** 9.14 GJ/MWh (Grati). bcm = PJ / 40, and Mt LNG = bcm / 1.36.

| 2030 case | DC TWh | % 2025 gen | Extra TWh | Coal PJ / Mt (range) | Gas bcm / Mt LNG |
|---|---|---|---|---|---|
| Low: IDPRO 2.7 GW | 20.1 | 4.1% | 15.8 | 177 / 9.4 (8.5-11.0) | 3.61 / 2.65 |
| Mid: PLN 3.5 GW | 26.1 | 5.3% | 21.7 | 244 / 13.0 (11.7-15.1) | 4.97 / 3.65 |
| High: IDPRO 11 GW | 81.9 | 16.6% | 77.6 | 871 / 46.2 (41.6-53.9) | 17.73 / 13.04 |

**Worked example (High):** 11 x 0.85 x 8,760 = 81.9 TWh; minus 4.32 = 77.6; x 11.22 = 871 PJ; / 18.84 = 46.2 Mt coal. On gas: 77.6 x 9.14 = 709 PJ; / 40 = 17.7 bcm; / 1.36 = 13.0 Mt LNG.

Ember's 26 TWh matches Mid. Mid adds 9% to 2024 power-sector coal (139 Mt); High adds a third. In Batam, 450 MW on gas needs 0.77 bcm, about 74 MMSCFD, which is two thirds of the Natuna contract.

## Conflicts

- **Coal share:** 61.8% (Ember, 2023), 64% (EIA), 67% (RUPTL) and 62.5% (HEESI 2024, derived).
- **Generation:** 371.6 TWh (2024) vs 494 TWh (2025), because the 2025 figure adds captive plants.
- **LNG exports, 2024:** about 17.6 Mt (EIA) vs about 11.7 Mt (HEESI), both derived.
- **Captive coal:** 19.3 GW (CREA) vs 17.3 GW (HEESI); 134 TWh (Ember) vs 101 TWh (HEESI).
- **Reserve:** a 37.5% planning margin vs a 15.2% operating reserve at peak.
- **IDPRO forecast:** 2.7 GW in January, then 11-11.7 GW in September.
- **Not verified:** official DC tariff; year of the Java-Bali mix.

## Takeaways

1. On Java, the marginal fuel for data centres is existing coal.
2. The Mid case's 13 Mt is small next to 817 Mt of output, so connection time is the limit.
3. In Batam, one campus nearly absorbs the new Natuna gas, and water is short.
4. Renewable claims rest on RECs: 6.4 TWh, against 78 TWh in the High case.

## Indonesia vs Malaysia and Thailand

Malaysia and Thailand meet extra data centre load with imported LNG. Indonesia meets it with its own coal, and in Batam with gas held back from export. That makes Indonesia the most fuel-secure of the three but the most carbon-heavy, and its bottleneck is connecting to the grid rather than paying for fuel.
