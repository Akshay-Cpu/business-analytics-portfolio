# Holiday Demand Forecasting and Revenue Analysis

A guided business analytics portfolio case study using Excel and synthetic data.

The scenario is inspired by firsthand restaurant experience with demand pressure and substitute products. The analysis was prepared retrospectively through guided, AI-assisted portfolio work. It examines forecasting, revenue performance and business trade-offs using fictional observations.

**All data and results are synthetic.** Cedar Kitchen, its menu, dates, prices and target are fictional. No employer or customer records are used. This analysis was built afterwards for a portfolio and was never used during employment; it does not establish the real monthly outcome or promotion effectiveness.

## Business question

Could a simple weekday forecast highlight Christmas demand pressure, and how much demand would remain unserved after allowing for substitute sales?

The case uses 366 daily item records across six fictional products in November and December 2025. The Excel workbook compares a November weekday baseline with an assumed December adjustment, then tracks shortages, substitute sales and the revenue target.

## What the scenario shows

- December revenue: **£69,293.50** against a **£70,000** fictional target; **£706.50 short**.
- Of **244** requests facing a first-choice shortage, **137** switched to substitutes and **107** remained unserved.
- Full-December weighted forecast error (WAPE) was **9.34%** for the baseline and **4.61%** for the adjustment.

The adjustment is broadly consistent with how the synthetic demand was generated. Its lower error is a teaching example, not independent evidence that it would work in a real restaurant. Substitute revenue is already included in total revenue.

## Open the project

1. Read the [two-page case study](Christmas_Case_Study.pdf).
2. Download [the Excel workbook](Christmas_Portfolio.xlsx) and start on Dashboard. Analysis contains formulas; Daily inputs contains the fixed synthetic observations. Notes explains the editable multipliers and target.
3. For detail, see [methodology](Methodology.md), [data dictionary](Data_Dictionary.md) and [validation](Validation.md).

## Tools and status

Excel analysis and charts are complete. [Power BI build notes](PowerBI_Specification.md) and [DAX definitions](PowerBI_Measures.dax) are included as a next step. **No finished PBIX or published Power BI dashboard is supplied.**

The useful lesson is that sales alone can hide unmet demand during stockouts. A real implementation would require checking stockout records and demand estimates, then testing forecasts on more history.
