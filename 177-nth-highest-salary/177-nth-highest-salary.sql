CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N = N-1;
  RETURN (
      # Write your MySQL query statement below.
    select
      ifnull((select distinct Salary 
          from Employee
          order by Salary desc 
          limit 1 offset N), NULL)     
  );

END

# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN 
# set N = N - 1;
#     RETURN (
#         select ifnull((select distinct salary 
#                      from Employee 
#                      order by salary 
#                      limit 1 offset N), null)
#     );
# end; 


