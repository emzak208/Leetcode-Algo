# # Write your MySQL query statement below

# select round(avg(pct_rmv),2) average_daily_percent
# from
# (select action_date, count(distinct r.post_id)*100/count(distinct a.post_id) pct_rmv
# from Actions a
# left join Removals r
# on a.post_id = r.post_id 
# where action = 'report' and extra = 'spam'
# group by a.action_date) tmp

select round(avg(daily_removed_percent),2) average_daily_percent
from 
(
select a.action_date, 
count(distinct case when action = 'report' and extra = 'spam' and remove_date is not null then a.post_id else null end)*100/count(distinct a.post_id) daily_removed_percent
from Actions a 
left join Removals r
on a.post_id = r.post_id 
where action = 'report' and extra = 'spam' 
group by a.action_date
) tmp



 