# Write your MySQL query statement below

select Department,Employee,Salary
from 
(select d.Id, d.Name as Department, e.Name as Employee, e.Salary,
 dense_rank() over (partition by d.Id order by e.Salary desc) rk
from Employee e 
join Department d 
on e.DepartmentId = d.Id) t1 
where rk = 1 


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

# # select all employee in the department with the highest salasy 
# select name
# from Employee 
# where departmentId in (select departmentId from
# (select Department, departmentId,
# dense_rank() over (order by Salary desc) rk
# from
# (select t1.name Employee, t2.id as departmentId, t2.name as Department,
#  sum(salary) Salary 
#  from Employee t1 
#  left join Department t2 
#  on t1.departmentid = t2.id 
# group by t2.id,t2.name) a 
# ) b 
# where rk =1) 

