# Data Sources

## AIS / Ship counts
- **hormuz.data-tracking.net** — daily inbound/outbound counts, 30-day history
- **WTO/AXSMarine Trade Tracker** — datalab.wto.org/Strait-of-Hormuz-Trade-Tracker

## Validated anchor points
- Jan–Feb 2026: ~130 vessels/day total, ~65 inbound / ~65 outbound
- Feb 28, 2026: crisis begins (military escalation)
- Mar 7, 2026: ~6 vessels/day (97% drop)
- Jun 17, 2026: 13 inbound + 13 outbound
- Jun 19, 2026: peace deal signed, gradual reopening

## References
- ScienceDirect: doi:10.1016/j.rsase.2026.001141
- UNCTAD: unctad.org/news/hormuz-disruption-deepens-global-economic-strain

## Limitations

These counts are AIS-derived estimates, not a full census of traffic through the strait. AIS (Automatic Identification System) only sees a vessel if its transponder is switched on and broadcasting an undistorted position. Three known gaps apply here:

- **Dark transits.** Tankers routinely switch their transponder off for part or all of a transit ("going dark"), especially vessels tied to sanctioned trade (the Iranian and Russian "shadow fleet"). A dark vessel is invisible to every AIS-based tracker, including this dataset.
- **GPS/AIS spoofing.** Counterfeit GPS signals broadcast in the Gulf region cause navigation systems, and the AIS positions derived from them, to report false locations. Vessels have been observed appearing to circle over airports or drift inland. Spoofed positions can distort counts even when a transponder is technically active.
- **Ghost ships.** Identity duplication (reusing the AIS identity of a scrapped vessel) and identity swapping between nearby ships are documented in the strait, both of which corrupt vessel-level counts.

Field reporting specific to the Strait of Hormuz suggests AIS-based traffic figures may undercount actual transits by as much as 50% (Tradlinx). Independent peer-reviewed studies elsewhere (Scotland's Marine Protected Areas, the Salish Sea) find comparable or larger AIS underrepresentation, with the degree varying heavily by vessel size and type. Treat the numbers in this project as a directional, lower-bound estimate of traffic, not an exact count.

Multiple independent analysts document how large this gap actually got in the Strait during 2026: Vortexa (via the New York Post) estimated 37% of outbound tankers ran dark in the war's early months, rising to 65%+ by May; Bloomberg reported dark transits as the majority of Hormuz traffic by early June; Lloyd's List Intelligence tracked a further escalation to 42% (late June) → 55% → nearly 70% (week of July 13–19) as the mid-July re-closure deepened. Despite this, Vortexa estimates actual daily throughput held at roughly 7–10 vessels, a figure consistent with Kpler's count of 895 crossings between March 1 and May 19, 2026.

Based on this research, a flat addition of +5 vessels per direction, per day, has been applied across the entire dataset used for this project's visualization, to better approximate real traffic rather than the raw AIS-visible count alone. This is an evidence-informed approximation grounded in the analyst estimates above, not a precise correction, and not a graphical convenience — it reflects documented dark-fleet activity that the raw AIS data cannot see by construction.

Sources: [Tradlinx — AIS Data in the Strait of Hormuz May Be Missing Half the Picture](https://blogs.tradlinx.com/ais-data-in-the-strait-of-hormuz-may-be-missing-half-the-picture-here-is-why-that-matters-for-logistics/), [Scientific American — GPS spoofing is scrambling ships in the Strait of Hormuz](https://www.scientificamerican.com/article/gps-spoofing-is-scrambling-ships-in-the-strait-of-hormuz/), [gCaptain — Electronic Fog of War](https://gcaptain.com/electronic-fog-of-war-gps-spoofing-distorts-ship-traffic-near-hormuz/), [ScienceDirect — AIS data underrepresents vessel traffic around coastal Scotland](https://www.sciencedirect.com/science/article/pii/S0964569125004533), [New York Post — Nearly 900 outbound tankers went 'dark'](https://nypost.com/2026/06/04/world-news/two-thirds-of-tankers-going-dark-to-pass-through-strait-of-hormuz-analysts/), [Bloomberg — Hormuz tracker: dark transits mount](https://www.bloomberg.com/news/articles/2026-06-09/hormuz-tracker-dark-transits-mount-in-sign-of-bigger-flows), [Lloyd's List Intelligence — Strait of Hormuz brief, July 21, 2026](https://www.lloydslistintelligence.com/resources/blog/strait-of-hormuz-brief-21-july-2026)
