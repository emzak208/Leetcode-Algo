# Write your MySQL query statement below

select distinct m.name
from Employee e
left join Employee m
on e.managerId = m.id 
group by e.managerId 
having count(m.id) >=5 

# select * # distinct m.name 
# from Employee e 
# left join Employee m 
# on e.managerId = m.id
# group by m.id
# having count(e.id) >=5