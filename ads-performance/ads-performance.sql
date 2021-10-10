# Write your MySQL query statement below

select ad_id, 
ifnull(round(total_clicks *100/ (total_clicks + total_reviews),2),0) ctr
from 
    (select ad_id, 
    sum(case when action = "Clicked" then 1 else 0 end) total_clicks,
    sum(case when action = 'Viewed' then 1 else 0 end) total_reviews
    from Ads
    group by ad_id) a 
order by ctr desc, ad_id