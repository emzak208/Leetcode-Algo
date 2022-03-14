# Write your MySQL query statement below
# dense rank 

# select Score as score,
# dense_rank() over (order by Score desc) `Rank`
# from Scores 

select score, 
dense_rank() over(order by score desc) as `rank`
from Scores


