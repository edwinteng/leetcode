# Write your MySQL query statement below
WITH sales2020 as(
    SELECT s.seller_id
    FROM Orders o
    JOIN Seller s
    on o.seller_id = s.seller_id
    WHERE '2020-01-01'<=o.sale_date and o.sale_date<='2020-12-31'
)

SELECT seller_name
FROM Seller
WHERE seller_id not in
(
    SELECT seller_id 
    FROM sales2020
)
ORDER by seller_name asc