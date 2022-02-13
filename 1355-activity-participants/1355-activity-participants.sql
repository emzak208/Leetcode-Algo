# Write your MySQL query statement below

# select activity 
# from 
# (select activity, count(id) num_prts,
# min(count(id)) over() min_prts, max(count(id)) over() max_prts
# from Friends 
# group by activity) t1 
# where num_prts != min_prts and num_prts != max_prts

select activity 
from 
(select activity, count(id) num_prts,
min(count(id)) over() min_num_prts, max(count(id)) over() max_num_parts
from Friends 
group by activity) a 
where num_prts != min_num_prts and num_prts != max_num_parts

