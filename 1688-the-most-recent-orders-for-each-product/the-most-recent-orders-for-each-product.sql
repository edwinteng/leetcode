# Write your MySQL query statement below
WITH t as (
SELECT o.product_id,o.order_id,o.order_date,
rank() over (partition by o.product_id order by o.order_date desc) as r
FROM Orders o
)
SELECT p.product_name,t.product_id,t.order_id,t.order_date
FROM t
join Products p
on t.product_id=p.product_id
where t.r=1
order by product_name asc, product_id asc, order_id asc