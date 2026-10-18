# Power BI: one-page build notes

This is a proposed report. DAX has not been executed in Power BI and no PBIX is included. Build one useful page before considering more.

## Import and model

Import Daily_Analysis.csv as FactDaily, Items.csv as Items, and Daily_Targets.csv as Targets. Use Date type for dates, text for item IDs/Period, whole numbers for units and errors, and decimal/fixed decimal for prices, hours and revenue. Keep empty November forecast/error cells null, not zero.

Create the Date calculated table in PowerBI_Measures.dax and mark Date[Date] as the date column. Add the other definitions individually as measures. Use active single-direction one-to-many relationships:

- Date[Date] -> FactDaily[Date]
- Items[ItemID] -> FactDaily[ItemID]
- Date[Date] -> Targets[Date]

Targets apply to the full menu. Do not join targets directly to item-day facts. Target measures return blank under item/category filters because no item targets exist.

## One report page

Title: Christmas demand and stockouts. Subtitle: Fictional restaurant; all results synthetic; retrospective portfolio.

Default to 1-31 December 2025. Add a date filter and item filter. Show revenue, whole-menu target attainment, unserved requests and modelled substitute revenue. Use GBP and one decimal place for percentages.

Add a daily line for demand, baseline and adjusted forecasts; retain 25 December as a closed day. Add an item bar chart of shortage and transferred requests. A small table shows baseline/adjusted WAPE and bias for the selected period. Users can select 1-7 December or 20-26 December to review those periods separately.

Explain below the page: substitute revenue is included in total sales; switching and demand uplifts are assumptions. Demand is synthetic first-choice demand, not observed sales. Item-filtered transfers out belong to original items; substitute sales belong to destination items.

## Check before calling the report complete

Confirm 366 unique item-day rows, six items and 31 unique target dates. At full-menu December scope, revenue should be £69,293.50, target £70,000, unserved requests 107 and baseline/adjusted WAPE approximately 9.34%/4.61%. Compare individual items and dates with Excel, check November forecast blanks, and confirm item/category selections blank whole-menu targets. Do not average row percentages. Check transfers balance only at whole-menu scope.

Hide unused detail fields from the report pane if helpful. There is no need for bookmarks, multiple report pages or fixed canvas/colour rules for this case.
