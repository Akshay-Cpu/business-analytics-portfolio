"""Validate the synthetic snapshot: python validate_data.py"""
from pathlib import Path
import csv,math
from collections import defaultdict
root=Path(__file__).resolve().parent
def load(name):
 with (root/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
delivery,labour,dates,depts=[load(n+'.csv') for n in ['FactDelivery','FactLabour','DimDate','DimDepartment']]
assert [len(t) for t in [delivery,labour,dates,depts]]==[42,126,42,3]
assert len({r['DateKey'] for r in delivery})==42
assert len({(r['DateKey'],r['DepartmentKey']) for r in labour})==126
assert len({r['DateKey'] for r in dates})==42 and len({r['DepartmentKey'] for r in depts})==3
datekeys={r['DateKey'] for r in dates};deptkeys={r['DepartmentKey'] for r in depts}
assert {r['DateKey'] for r in delivery}==datekeys
assert {r['DateKey'] for r in labour}==datekeys
assert {r['DepartmentKey'] for r in labour}==deptkeys
def n(r,k):return float(r[k])
def total(rows,k):return sum(n(r,k) for r in rows)
def equal(a,b):assert math.isclose(a,b,rel_tol=1e-9,abs_tol=1e-7),(a,b)
groups=defaultdict(list)
for r in labour:
 for k,v in r.items():
  if k not in ['DateKey','DepartmentKey']:assert float(v)>=0
 assert n(r,'EffectiveAvailableHours')>0
 assert n(r,'TrainingHours')<=n(r,'MovedInHours')
 equal(n(r,'SpareEffectiveHours'),max(0,n(r,'EffectiveAvailableHours')-n(r,'RequiredEffectiveHours')))
 equal(n(r,'LoadCapped'),min(1,n(r,'RequiredEffectiveHours')/n(r,'EffectiveAvailableHours')))
 if r['DepartmentKey']=='REC':assert n(r,'EffectiveAvailableHours')>=n(r,'RequiredEffectiveHours')
 groups[r['DateKey']].append(r)
for day in groups.values():equal(total(day,'MovedInHours'),total(day,'MovedOutHours'))
previous=120
for r in sorted(delivery,key=lambda r:r['DateKey']):
 equal(n(r,'OpeningBacklog'),previous)
 capacity=math.floor((n(r,'NativePaidHours')-n(r,'MentorHours')+(n(r,'TempPaidHours')-n(r,'TrainingHours'))*n(r,'TempEfficiency'))*n(r,'OrdersPerEffectiveHour')+1e-9)
 equal(n(r,'CapacityOrders'),capacity)
 equal(n(r,'CompletedOrders'),min(n(r,'OpeningBacklog')+n(r,'IncomingOrders'),capacity))
 equal(n(r,'ClosingBacklog'),n(r,'OpeningBacklog')+n(r,'IncomingOrders')-n(r,'CompletedOrders'))
 assert n(r,'ClosingBacklog')>=0
 dl=next(x for x in groups[r['DateKey']] if x['DepartmentKey']=='DEL')
 equal(n(r,'NativePaidHours'),n(dl,'HomePaidHours'))
 equal(n(r,'TempPaidHours'),n(dl,'MovedInHours'))
 equal(n(r,'TrainingHours'),n(dl,'TrainingHours'))
 equal(n(r,'MentorHours'),n(dl,'MentorHours'))
 previous=n(r,'ClosingBacklog')
assert max(n(r,'ClosingBacklog') for r in delivery)==868 and previous==638
equal(total(delivery,'TempPaidHours'),585);equal(total(delivery,'TrainingHours'),18)
phase={r['DateKey']:r['Phase'] for r in dates}
for name in ['Baseline','Disruption','Reassignment']:
 dr=[r for r in delivery if phase[r['DateKey']]==name]
 lr=[r for r in labour if phase[r['DateKey']]==name and r['DepartmentKey']=='REC']
 print(name, f"orders/paid hour={total(dr,'CompletedOrders')/(total(dr,'NativePaidHours')+total(dr,'TempPaidHours')):.2f}",f"recycling load={100*total(lr,'RequiredEffectiveHours')/total(lr,'EffectiveAvailableHours'):.1f}%")
print('Passed: keys, transfers, capacity, backlog, recycling cover and headline totals.')
