# Write your MySQL query statement below

## method 1
# select round(count(distinct player_id)/(select count(distinct player_id) from Activity),2) fraction
# from 
# (select player_id, event_date,
# min(event_date) over(partition by player_id order by event_date) first_date
# from Activity) a 
# where (event_date - first_date) = 1 

## method 2
select 
round(count(distinct(case when event_date - first_date = 1 then player_id else null end))/count(distinct player_id),2) fraction
from 
(select player_id, event_date,
min(event_date) over(partition by player_id order by event_date) first_date
from Activity) t
