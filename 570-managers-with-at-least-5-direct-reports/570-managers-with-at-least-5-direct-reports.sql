# Write your MySQL query statement below

# select distinct m.name
# from Employee e
# left join Employee m
# on e.managerId = m.id 
# group by e.managerId 
# having count(m.id) >=5 
# ;

## or 
select m.name 
from Employee e 
join Employee m 
on e.managerId = m.id 
group by m.id # m.name
having count(*) >= 5
;
