# Write your MySQL query statement below
WITH num_order as (
SELECT customer_number,count(*) as num_order
FROM Orders 
GROUP by customer_number
)
SELECT customer_number
FROM num_order 
WHERE num_order = (SELECT MAX(num_order) from num_order)
