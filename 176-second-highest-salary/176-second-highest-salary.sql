# Write your MySQL query statement below
# select 
#   ifnull((select distinct Salary
#       from Employee
#       order by Salary desc 
#       limit 1 offset 1), NULL) as SecondHighestSalary

select 
ifnull(
    (select distinct salary 
    from Employee
    order by salary desc 
    limit 1, 1
    ), null) as SecondHighestSalary