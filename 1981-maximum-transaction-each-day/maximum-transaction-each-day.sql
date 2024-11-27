# Write your MySQL query statement below
WITH t as (
SELECT
transaction_id,
dense_rank() over (partition by DATE(day) order by amount desc) as r
FROM Transactions
)
SELECT transaction_id
FROM t
WHERE r=1
order by transaction_id asc