# Write your MySQL query statement below

# select b.Name 
# from Employee a
# left join Employee b
# on a.ManagerId = b.Id
# group by a.ManagerId
# having count(b.Id) >=5


select distinct m.name
from Employee e
left join Employee m
on e.managerId = m.id 
group by e.managerId 
having count(m.id) >=5 
