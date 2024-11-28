# Write your MySQL query statement below
WITH t as (
SELECT
user_id,
visit_date,
IFNULL(datediff(lead(visit_date,1) over (partition by user_id order by visit_date asc),visit_date),datediff('2021-01-01',visit_date)) as date_diff
FROM UserVisits
)
SELECT user_id, max(date_diff) as biggest_window
FROM t 
group by user_id
