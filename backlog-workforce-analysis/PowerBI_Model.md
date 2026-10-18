# Power BI: proposed one-page report

The Excel project is complete; this report is a next step. No PBIX or runtime-tested DAX is supplied.

## Import

Load the four  CSVs. DateKey, DayIndex, WeekIndex and order counts are whole numbers; Date is a date; hours, efficiency and rates are decimal; department keys and Phase are text. Keep the supplied grains: FactDelivery one date, FactLabour one date/department, DimDate one date, DimDepartment one department.

Create active one-to-many, single-direction relationships:

- DimDate[DateKey] -> FactDelivery[DateKey]
- DimDate[DateKey] -> FactLabour[DateKey]
- DimDepartment[DepartmentKey] -> FactLabour[DepartmentKey]

Mark DimDate using its Date column. Do not join the facts directly: that can multiply daily orders across three departments. Department selections filter labour, not delivery totals. Label the two visual sections accordingly.

## One page

Title: Warehouse backlog and staff reassignment. Subtitle: Synthetic portfolio simulation; no company records used.

Add Date and Phase filters. Show closing backlog, peak backlog and peak-to-closing decline. Use a daily backlog line, a daily incoming/completed comparison, and a department load table. Show training hours and recycling load beside the transfer discussion. Use the measures in Measures.dax, entered separately.

Closing backlog is the final selected date's balance; never sum it across dates. Peak-to-closing decline refers to the selected window. Department Load must use sum(required)/sum(available), uncapped. Neither phase comparisons nor the decline establish causal impact.

## Check before calling it complete

Verify 42 delivery rows, 126 labour rows, 42 dates and three departments, with unique keys and no unmatched relationships. Full-period peak/final backlog should be 868/638, transferred paid hours 585 and training hours 18. Baseline/disruption/reassignment productivity should round to 2.45/1.88/1.95; recycling load to 86.7%/44.4%/74.0%. Test date and phase selections against Excel. Confirm department filters are not presented as filtering delivery totals.

For Power Query cleaning practice, optionally stage RawLabourTable from Excel instead of the prepared labour CSV. Trim/lowercase labels, join to an explicit mapping table and flag unmatched labels. Inspect duplicate keys before deciding how to resolve them; do not discard them silently.
