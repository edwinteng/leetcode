# Write your MySQL query statement below
WITH dist as (
    SELECT user_id,sum(distance) as travelled_distance
    FROM Rides
    GROUP BY user_id
)
SELECT u.name,ifnull(d.travelled_distance,0) as travelled_distance
FROM Users u
left join dist d
on u.id = d.user_id
ORDER by d.travelled_distance desc, u.name asc
