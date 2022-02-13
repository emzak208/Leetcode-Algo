# # Write your MySQL query statement below
# select e1.employee_id 
# from Employees e1 
# left join Employees e2 
# on e1.manager_id = e2.employee_id
# left join Employees e3 
# on e2.manager_id = e3.employee_id
# where e3.manager_id = 1 and e1.employee_id != 1

select distinct e.employee_id
from Employees e
left join Employees m1
on e.manager_id = m1.employee_id
left join Employees m2
on m1.manager_id = m2.employee_id
where m2.manager_id = 1 and e.employee_id != 1