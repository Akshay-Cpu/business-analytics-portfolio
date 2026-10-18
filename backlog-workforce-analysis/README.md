# Backlog Recovery and Workforce Scenario Analysis

A guided Excel portfolio case study exploring performance reporting, resource allocation and business continuity.

The scenario is inspired by firsthand warehouse experience during 2025. It was prepared retrospectively through guided, AI-assisted portfolio work to explore whether staff could move between departments while maintaining adequate cover.

**All figures, dates, staffing levels and outcomes are synthetic.** No company data, internal records or documents were used. The simulation does not reconstruct an employer’s operations and is not affiliated with or endorsed by an employer.

## Available model

A formula-based Excel workbook covering 42 operating days and three departments. It tracks incoming and completed orders, closing backlog, paid hours and department capacity. Staff transfers include training time, mentor time and lower efficiency in an unfamiliar role.

## What the scenario shows

- Backlog peaks at **868 orders** and ends at **638**, a **26.5% peak-to-final decline**. It is not fully cleared.
- Delivery output per paid hour is **2.45** at baseline, **1.88** during disruption and **1.95** during reassignment.
- Recycling load rises from **44.4%** during disruption to **74.0%** during reassignment.

Demand and native delivery productivity also change by assumption. These comparisons do not isolate the effect of moving staff or demonstrate a real company improvement.

## Explore the work

1. Read the [two-page case study](Warehouse_Case_Study.pdf).
2. Download [the workbook](Warehouse_Recovery.xlsx) and start on Dashboard. Daily Flow and Labour show the calculations; Raw Delivery and Raw Labour hold the synthetic inputs.
3. See the [method](Methodology.md), [data dictionary](Data_Dictionary.md) and [validation notes](Validation.md).

## Tools and status

Completed: Excel formulas, label cleaning, two native charts and capacity/backlog analysis. Proposed: a [Power BI model](PowerBI_Model.md) with [DAX definitions](Measures.dax). **No completed or tested PBIX is supplied.** This project does not demonstrate SQL or cybersecurity analysis.

The main lesson is to review backlog and the remaining department cover together. Moving paid hours does not create the same number of productive hours when training and mentoring are needed.
