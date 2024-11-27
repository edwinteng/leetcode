# Write your MySQL query statement below

SELECT distinct p1.email
FROM Person p1
JOIN Person p2
on p1.email=p2.email
WHERE p1.id!=p2.id