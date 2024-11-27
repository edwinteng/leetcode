# Write your MySQL query statement below
WITH t as (
SELECT
player_id,
device_id,
row_number() over (partition by player_id order by event_date asc) as seq
FROM Activity 
)
SELECT player_id,device_id
FROM t
WHERE seq = 1