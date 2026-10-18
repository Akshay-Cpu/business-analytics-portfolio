# Data dictionary

All values are synthetic. One Daily_Analysis row represents one item on one date.

| Fields | Meaning |
|---|---|
| Date, ItemID | Unique daily record for one fictional item |
| Weekday | Monday=1 through Sunday=7 |
| Period | Training, December normal, Christmas or Closed |
| PriceGBP | Synthetic selling price per item-equivalent unit |
| DemandUnits | Latent first-choice requests, including unmet requests |
| OpeningUnits, ReceiptUnits | Start-of-day stock and same-day replenishment |
| TransferInUnits, TransferOutUnits | Switched requests arriving at destination/leaving source item |
| StockoutHours | Illustrative daily estimate, rounded to 0.1 hour |
| DirectSalesUnits | MIN(demand, opening + receipts − transfer-in) |
| ClosingUnits | Opening + receipts − direct sales − transfer-in |
| ShortageUnits | Demand − direct sales |
| UnservedUnits | Shortage − transfer-out |
| SalesUnits | Direct sales + transfer-in |
| RevenueGBP | Sales × price |
| SubstituteRevenueGBP | Transfer-in × destination price |
| UnservedValueGBP | Unserved × original price |
| BaselineForecast, AdjustedForecast | Forecast units, blank before December |
| BaselineAbsError, AdjustedAbsError | Absolute forecast minus demand errors |
| BaselineError, AdjustedError | Signed forecast minus demand errors |
| StockoutItemDay | 1 when shortage is positive; otherwise 0 |

Items.csv contains one row per item; Category identifies Core, Substitute or Side, and BaseDailyUnits is a synthetic generation input. Daily_Targets.csv contains one December row per date, with RevenueTargetGBP split evenly across 30 open days and a rounding adjustment on the final day. The allocation is a simple fictional pacing convention, not an empirical weekday target.


Blank forecasts/errors mean November training rows. Closed-day forecasts and errors are zero. Demand is first-choice requests; transfers do not create new demand.
