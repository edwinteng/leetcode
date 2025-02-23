# Write your MySQL query statement below
SELECT activity_date as day, count(distinct user_id) as active_users
FROM activity
WHERE activity_date between  '2019-07-27'-interval '29' day and '2019-07-27' 
GROUP BY activity_date
HAVING count(distinct user_id) >0