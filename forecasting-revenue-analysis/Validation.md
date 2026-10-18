# Checks and limits

The delivered CSVs contain 366 unique item-day records, six item records and 31 target dates. The independent Python snapshot checks passed for inventory continuity, nonnegative closing stock, shortage/transfer/unserved reconciliation, daily transfer balance, revenues, target totals and forecast error arithmetic.

Every saved Analysis value was compared with the delivered CSV (numeric tolerance 0.000001 or relative 0.00000001). Raw Daily inputs and Items values are unchanged from the supplied workbook. December revenue is £69,293.50; the £70,000 target leaves a £706.50 shortfall. Of 244 requests facing shortages, 137 transfer and 107 remain unserved.

The original CSV had 30 blank cells across the adjusted forecast and four error fields on the six closed-day rows. These are now explicit zeros. The workbook's U:Y formulas now test the training date explicitly, avoiding ambiguous zero-versus-empty comparisons. November remains blank. This does not change totals or WAPE. Items, targets and the numerical observations are preserved; CSV quoting was standardised when saving the correction.

The authoring engine recalculated the workbook and found no scanned formula errors. An independent saved-file scan found no error-valued cells. Changing the Christmas multiplier from 1.20 to 1.30 changed full-December adjusted WAPE from 4.6061% to 3.8974%; restoring 1.20 restored the original result. This checks input flow, not predictive validity. Both native charts and the table structure were retained. The five sheet opening views and both chart areas were visually reviewed, along with both PDF pages.

Run `python validate_data.py` from the repository root to check the delivered snapshot using Python's standard library. It validates the CSVs; it does not recalculate Excel or execute DAX. The original generator is unavailable, so it does not recreate raw demand from the seed.

No live Microsoft Excel or Power BI execution was performed. DAX is proposed and requires the checks in PowerBI_Specification.md after implementation. Results are synthetic, and forecast adjustments and switching assumptions are not independently validated business improvements.
