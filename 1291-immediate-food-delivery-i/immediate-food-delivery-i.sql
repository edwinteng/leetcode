# Write your MySQL query statement below

WITH t as(
SELECT delivery_id,
CASE WHEN order_date=customer_pref_delivery_date
THEN 1
ELSE 0
END as type
FROM Delivery
)

SELECT ROUND(100.0*SUM(type)/COUNT(*),2) as immediate_percentage 
FROM t
