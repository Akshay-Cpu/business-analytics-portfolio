"""Check the delivered synthetic snapshot. Run: python validate_data.py"""
import csv
from pathlib import Path
from decimal import Decimal as D
from collections import defaultdict

root = Path(__file__).resolve().parent
def load(name):
    with (root/name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))
rows, items, targets = load('Daily_Analysis.csv'), load('Items.csv'), load('Daily_Targets.csv')
def num(row, col): return D(row[col])
def total(data, col): return sum((num(r,col) for r in data), D(0))
assert len(rows)==366 and len({(r['Date'],r['ItemID']) for r in rows})==366
assert len(items)==6 and len({r['ItemID'] for r in items})==6
assert len(targets)==31 and len({r['Date'] for r in targets})==31
assert {r['ItemID'] for r in rows}=={r['ItemID'] for r in items}
days=defaultdict(list)
previous={}
for r in sorted(rows,key=lambda r:(r['Date'],r['ItemID'])):
    n=lambda c:num(r,c)
    key=r['ItemID']
    if key in previous: assert n('OpeningUnits')==previous[key]
    previous[key]=n('ClosingUnits')
    assert n('DirectSalesUnits')==min(n('DemandUnits'),n('OpeningUnits')+n('ReceiptUnits')-n('TransferInUnits'))
    assert n('ClosingUnits')==n('OpeningUnits')+n('ReceiptUnits')-n('SalesUnits')>=0
    assert n('ShortageUnits')==n('DemandUnits')-n('DirectSalesUnits')>=0
    assert n('UnservedUnits')==n('ShortageUnits')-n('TransferOutUnits')>=0
    assert n('SalesUnits')==n('DirectSalesUnits')+n('TransferInUnits')
    assert n('RevenueGBP')==n('SalesUnits')*n('PriceGBP')
    assert n('SubstituteRevenueGBP')==n('TransferInUnits')*n('PriceGBP')
    assert n('UnservedValueGBP')==n('UnservedUnits')*n('PriceGBP')
    assert n('StockoutItemDay')==int(n('ShortageUnits')>0)
    if r['Date']<'2025-12-01':
        assert all(r[c]=='' for c in ['BaselineForecast','AdjustedForecast','BaselineAbsError','AdjustedAbsError','BaselineError','AdjustedError'])
    else:
        for prefix in ['Baseline','Adjusted']:
            error=n(prefix+'Forecast')-n('DemandUnits')
            assert n(prefix+'Error')==error and n(prefix+'AbsError')==abs(error)
    days[r['Date']].append(r)
for day in days.values(): assert total(day,'TransferInUnits')==total(day,'TransferOutUnits')
dec=[r for r in rows if r['Date']>='2025-12-01']
assert total(dec,'RevenueGBP')==D('69293.5')
assert total(targets,'RevenueTargetGBP')==D('70000')
assert total(dec,'ShortageUnits')==244
assert total(dec,'TransferOutUnits')==137
assert total(dec,'UnservedUnits')==107
assert total(dec,'SubstituteRevenueGBP')==D('1057.5')
for label,start,end in [('Holdout','2025-12-01','2025-12-07'),('Christmas','2025-12-20','2025-12-26'),('December','2025-12-01','2025-12-31')]:
    data=[r for r in rows if start<=r['Date']<=end]
    demand=total(data,'DemandUnits')
    print(label, 'WAPE baseline/adjusted:',*[f'{100*total(data,c)/demand:.2f}%' for c in ['BaselineAbsError','AdjustedAbsError']])
print('Snapshot checks passed: keys, inventory, transfers, revenue, targets and forecast errors.')
