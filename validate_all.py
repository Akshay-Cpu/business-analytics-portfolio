"""Run the delivered CSV snapshot checks using the Python standard library."""
from pathlib import Path
import runpy

root = Path(__file__).resolve().parent
for project in ["forecasting-revenue-analysis", "backlog-workforce-analysis"]:
    print(f"\nChecking {project}")
    runpy.run_path(str(root / project / "validate_data.py"), run_name="__main__")
print("\nBoth portfolio snapshot checks passed.")
