# Write your MySQL query statement below

# select distinct(t1.Num) ConsecutiveNums
# from 
# (select Num, 
# lag(Num, 1) over () prev1,
# lag(Num, 2) over () prev2
# from Logs) t1
# where t1.Num = prev1 and t1.Num = prev2

select distinct num ConsecutiveNums
from 
(
select num, 
lead(num,1) over() prev1, 
lead(num,2) over() prev2
from Logs
) t
where t.num = t.prev1 and t.prev1 = t.prev2