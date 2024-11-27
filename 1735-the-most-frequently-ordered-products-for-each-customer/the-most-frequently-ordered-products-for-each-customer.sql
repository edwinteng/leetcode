# Write your MySQL query statement below
WITH cus_pro_freq as (
    SELECT o.customer_id,o.product_id,count(*) as cnt
    FROM Orders o
    GROUP BY o.customer_id,o.product_id
),
rnk_t as (
SELECT customer_id,product_id,
Rank() over (partition by customer_id order by cnt desc) as rnk
FROM cus_pro_freq
)
SELECT r.customer_id,r.product_id,p.product_name
FROM rnk_t r
JOIN Products p
on r.product_id=p.product_id
WHERE r.rnk=1