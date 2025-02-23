# Write your MySQL query statement below
SELECT activity_date as day, count(distinct user_id) as active_users
FROM activity
WHERE activity_date > '2019-07-27' - interval '30' day and activity_date <= '2019-07-27'
GROUP BY activity_date
