# Write your MySQL query statement below

WITH t as (
SELECT
log_id,
#lag(log_id,1) over (order by log_id asc) as prev,
#lead(log_id,1) over (order by log_id asc) as next,
#log_id - lag(log_id,1) over (order by log_id asc) as diff_prev,
log_id - lag(log_id,1) over (order by log_id asc) as diff_prev
FROM Logs
),
index_t as (
SELECT
log_id,
CASE WHEN diff_prev = 1 THEN 0 ELSE 1 END as flag
FROM t
),
group_t as (
SELECT
log_id,SUM(flag) over (order by log_id) as group_id
FROM index_t    
)
#SELECT * 
#FROM group_t
SELECT min(log_id) as start_id,max(log_id) as end_id
FROM group_t
GROUP BY group_id