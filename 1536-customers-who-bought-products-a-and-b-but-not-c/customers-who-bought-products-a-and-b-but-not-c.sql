# Write your MySQL query statement below
WITH count_t as (
SELECT customer_id,
CASE WHEN product_name='A' 
THEN 1
ELSE 0 END as a_count,
CASE WHEN product_name='B'
THEN 1 
ELSE 0 END as b_count,
CASE WHEN product_name='C'
THEN 1 
ELSE 0 END as c_count
FROM Orders 
),
count_summarized as (
SELECT customer_id,
sum(a_count) as a_count,
sum(b_count) as b_count,
sum(c_count) as c_count
FROM count_t
GROUP BY customer_id
)
SELECT cu.customer_id,cu.customer_name
FROM Customers cu
LEFT JOIN count_summarized co
on cu.customer_id = co.customer_id
WHERE co.a_count>=1 and co.b_count>=1 and co.c_count =0
ORDER by cu.customer_id asc