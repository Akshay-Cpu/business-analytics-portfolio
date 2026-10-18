# Method and assumptions

## Forecast

The forecast origin is 30 November 2025. For each item and weekday, the baseline is the rounded November mean. The adjusted forecast multiplies it by 1.04 on ordinary December days and 1.20 on 20-26 December. Forecasts are rounded to whole units and are zero on the closed day, 25 December. November forecasts are blank. No December observations train either forecast.

Keep the short 1-7 December holdout separate from the retrospective 20-26 December review and full-month summary. One month of history cannot establish annual seasonality.

WAPE = sum of absolute item-day errors / sum of demand on forecast-covered rows. Bias = sum(forecast - demand) / sum(demand). Negative bias means under-forecasting. Do not average percentages or calculate absolute errors only after aggregating items.

## Fixed synthetic scenario

The original numerical scenario is preserved. These settings explain the data; they are not estimates from a real business.

- Six items; base daily units 31-82; prices £3-£9; weekday factors 0.85-1.30; bounded noise ±6%; original generator seed 4217.
- December demand uses 1.04 times the November baseline. On 20-26 December, core demand has an additional 1.38 multiplier; other items 1.18. The closed day has zero demand.
- Normal receipts replenish towards 115% of known synthetic daily demand. This uses information a real ordering process would not know.
- Receipts for I01/I02 are constrained on 21-24 December. Each substitute gets 25 additional units per day in that interval; normal receipts resume on 26 December.
- Intended switching is 35% on 21 December and 65% on 22-24 December, rounded and capped by spare stock. Allocation goes to the veggie wrap first, then the rice bowl. Transfer-out and transfer-in balance for the full menu each day.

The original generator is not supplied. The delivered CSVs and Daily inputs sheet are the authoritative scenario snapshot; seed alone is insufficient to regenerate it. The validation script reproduces the metrics from this snapshot.

## Interpretation

Demand is first-choice requested units, known here only because it is synthetic. Sales can understate demand for stockout items and exceed original demand for substitutes. A switched request counts once as a destination sale. Substitute revenue is part of total revenue. Unserved value uses original prices and is gross sales exposure, not lost profit.

Inventory uses finished-item equivalents. Costs, waste, tax, labour, profit and customer-level behaviour are outside scope. No causal claim about employee promotion follows from assumed switching. The fictional dates and GBP do not identify the real incident or location. This independent portfolio is not employer-affiliated or endorsed.

## Editing

Notes B8/B9 are forecast multipliers; B10 is the whole-menu monthly target. The five workbook tabs retain the fixed-case formulas and two native charts. Editing multipliers does not change historical synthetic demand or inventory. New dates require extending formulas and summaries. Independent raw demand/receipt edits require rebuilding transfers, balances and hours.

CSVs are fixed exports, not live workbook links. After forecast edits, recalculate and export Analysis with the same column names and ISO dates; retain blank November forecasts. If the target changes, redistribute Daily_Targets.csv so it sums to Notes B10. Its original £70,000 is spread across 30 open days, with a final-day rounding adjustment. Never duplicate it across items.
