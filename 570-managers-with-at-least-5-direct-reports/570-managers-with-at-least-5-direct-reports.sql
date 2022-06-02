# Write your MySQL query statement below

# select distinct m.name
# from Employee e
# left join Employee m
# on e.managerId = m.id 
# group by e.managerId 
# having count(m.id) >=5 
# ;

## or 
# select m.name 
# from Employee e 
# left join Employee m 
# on e.managerId = m.id 
# group by m.name
# having count(*) >= 5
# ;

select e2.Name
from employee e1
join employee e2
on e1.ManagerId=e2.Id
group by e2.name
having count(*)>=5