# Write your MySQL query statement below
WITH t as (
SELECT seat_id,free,lag(free,1) over(order by seat_id asc) as prev_free, lead(free,1) over(order by seat_id asc) as next_free 
FROM Cinema
)
SELECT seat_id
FROM t
where free=1 and (next_free=1 or prev_free=1)
order by seat_id
