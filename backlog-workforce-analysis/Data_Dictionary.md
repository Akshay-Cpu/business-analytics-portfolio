# Data dictionary

All data is synthetic. DateKey joins the facts to DimDate; DepartmentKey joins labour to DimDepartment.

| File | Grain / key | Fields |
|---|---|---|
| DimDate | One date / DateKey | Date, DayIndex (1-42), WeekIndex, Phase |
| DimDepartment | One department / DepartmentKey | Department, Unit; DEL/REC/PCK |
| FactDelivery | One date / DateKey | Daily queue, labour and delivery calculations below |
| FactLabour | One date-department / DateKey + DepartmentKey | Department hours and load below |

## Delivery fields

IncomingOrders is new daily demand. OrdersPerEffectiveHour is an assumed capacity rate. NativePaidHours and TempPaidHours are delivery home and transferred paid hours. TrainingHours and MentorHours are included in paid time but reduce effective output. TempEfficiency discounts transferred-worker productive hours. CapacityOrders is the floored effective-hour capacity. OpeningBacklog, CompletedOrders and ClosingBacklog form the queue roll-forward.

## Labour fields

HomePaidHours is original department paid time. MovedOutHours and MovedInHours record reassignment, balancing across departments per day. TrainingHours and MentorHours reduce effective availability. EffectiveAvailableHours applies the assumed efficiency. RequiredEffectiveHours is the fixed demand snapshot. SpareEffectiveHours is nonnegative spare capacity. LoadCapped is min(1, required/available); calculate an uncapped ratio for overload reporting.

Delivery units are orders; other departments are measured in effective labour hours. Do not aggregate those workload units together. Paid hours are additive across dates; opening/closing backlog are balances and are not additive across dates.
