# Write your MySQL query statement below

SELECT player_id,min(event_date) as first_login
FROM Activity
GROUP By player_id
