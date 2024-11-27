# Write your MySQL query statement below
WITH red_sales as(
    SELECT s.sales_id
    FROM SalesPerson s
    JOIN Orders o
    on s.sales_id = o.sales_id
    JOIN Company c
    on o.com_id = c.com_id
    WHERE c.name = 'RED'
)
SELECT name
FROM SalesPerson
WHERE sales_id not in 
(SELECT sales_id
 FROM red_sales
)