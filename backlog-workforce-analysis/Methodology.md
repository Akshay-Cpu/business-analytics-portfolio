# Method and assumptions

## Scenario

One fictional site operates one 7.5-hour shift on each of 42 invented dates, 2 June-13 July 2025. Initial delivery backlog is 120 orders. Home staffing is 28 delivery, 12 recycling and 24 picking workers. Orders are illustrative standard handling tasks, not truck deliveries.

The phases are baseline days 1-7, disruption days 8-21 and reassignment days 22-42. Delivery rates are assumed at 2.45, 1.88 and 2.06 orders per effective hour respectively. These are inputs, not measured estimates or forecasts.

Two recycling workers move on days 22-24 and four from day 25. Training uses six hours per day in the first three transfer days (18 total). Mentor time is 0.4 hours per moved worker per day. Transferred staff operate at 45% efficiency initially and 62% afterwards. Total transferred paid hours are 585.

## Calculations

- Effective available hours = home paid hours - moved-out hours - mentor hours + (moved-in hours - training hours) × transferred-worker efficiency.
- Delivery capacity = floor(effective available hours × assumed delivery rate).
- Completed orders = minimum(opening backlog + incoming orders, capacity).
- Closing backlog = opening backlog + incoming - completed. Next day's opening equals the previous closing. There are no cancellation adjustments.
- Productivity = total completed / total native and transferred paid hours. Calculate a ratio of totals for a phase, not the average of daily ratios.
- Department load = total required effective hours / total effective available hours. This can exceed 100%. The CSV's LoadCapped field is capped at 100%, so it should not be used to diagnose overload.
- Spare effective hours = maximum(0, available - required).

Backlog is a balance at a point in time; do not add daily closing backlogs to report outstanding orders. Peak-to-final decline is (peak - final)/peak. It is not a before/after treatment effect. Queue-cleared percentage and closing backlog/455 are workload proxies, not on-time performance or actual order age. The 455 reference is fictional.

## Preparation and refresh

Raw Labour deliberately includes case/whitespace variations. Labour formulas trim/lowercase labels and explicitly map delivery/recycling/picking to DEL/REC/PCK. Unknown labels now return UNMAPPED for review instead of being silently treated as Picking.

The workbook is a fixed 42-day case. Edits to source tables recalculate existing formulas and charts, but appending dates requires extending formulas, charts and dimensions. Daily Flow links to labour rows by position: keep the original date/department order in the raw sheets. Sorting the raw labour rows independently can misalign the calculation.

CSV files are static snapshots. Re-export after workbook edits; they are not linked live. Required delivery hours in Raw Labour are an original queue/rate snapshot, so changing demand or rates requires updating that input as well for a consistent labour-load view. This package preserves that existing snapshot rather than claiming a fully flexible staffing simulator.

## Boundaries

Native productivity and demand also change, so the model cannot isolate reassignment's effect. No control group or counterfactual comparison is supplied. No financial savings, SLA, lateness or safety outcome is measured. The original generator is not supplied; the workbook inputs and CSVs are the scenario snapshot. The public story retains the personal warehouse inspiration without adding employer incident details.
