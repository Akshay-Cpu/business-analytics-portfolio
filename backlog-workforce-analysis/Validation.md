# Validation and limits

Independent CSV checks passed for 42 delivery rows, 126 labour rows, 42 dates and three departments; unique keys and relationship coverage; daily transfer balance; nonnegative hours; training within transferred hours; recycling cover; delivery capacity; and backlog roll-forward.

Every saved delivery/labour calculation and dimension value was compared against the supplied CSV snapshot (absolute tolerance 0.0000001 or relative 0.000000001 for numbers). All four delivered CSVs remain byte-identical to the originals. Raw delivery/labour inputs and both dimensions retain their original values. The two native charts and original table counts are preserved.

Verified figures: backlog peak 868 and final 638; peak-to-final decline 26.5%; transferred paid hours 585; training hours 18. Baseline/disruption/reassignment output per paid hour rounds to 2.45/1.88/1.95, and recycling load to 86.7%/44.4%/74.0%.

The workbook was recalculated in the authoring engine and scanned for formula errors; no errors were found. Increasing first-day incoming orders by 10 increased final backlog from 638 to 648; restoring the input restored 638. An unrecognised raw department label returned UNMAPPED; the original label was restored before export. The revised mapping is the only calculation change. Display formatting now shows worker efficiency as a percentage instead of rounding 0.45 to 0.5.

The dashboard, both native charts, all eight sheet opening views and both public PDF pages were visually reviewed. No live Microsoft Excel or Power BI execution was performed. DAX remains proposed and requires implementation checks. Run `python validate_data.py` from the repository root to check the CSVs with Python's standard library; that script does not recalculate Excel or execute DAX.

The workbook is a fixed-case simulation with positional links from Daily Flow to raw labour rows. Do not independently sort raw labour rows. Delivery required-hours inputs are a fixed original snapshot and need updating after demand/rate changes. The workbook is not a general staffing optimiser. Native productivity and demand changes prevent attributing the backlog decline to reassignment alone.
