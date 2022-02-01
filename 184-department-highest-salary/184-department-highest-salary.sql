# Write your MySQL query statement below

# select Department,Employee,Salary
# from 
# (select d.Id, d.Name as Department, e.Name as Employee, e.Salary,
#  dense_rank() over (partition by d.Id order by e.Salary desc) rk
# from Employee e 
# join Department d 
# on e.DepartmentId = d.Id) t1 
# where rk = 1 

## select employee with max salary 
# select Name
# from Employee 
# where Salary = (select max(Salary) from Employee)

##select Employee from the department with the max total salary 
# select Name, Salary 
# from Employee e
# where e.DepartmentId in (select DepartmentId from 
# (select DepartmentId, max(total_salary) max_salary
# from 
# (select DepartmentId, sum(Salary) total_salary from Employee
# group by DepartmentId) a ) b)

select t.Department,t.Employee,t.Salary
from 
(select d.id, d.name Department, e.name Employee, e.Salary, 
dense_rank() over (partition by d.id order by e.salary desc) rk 
from Employee e 
join Department d
on e.departmentId = d.id) t
where rk = 1
