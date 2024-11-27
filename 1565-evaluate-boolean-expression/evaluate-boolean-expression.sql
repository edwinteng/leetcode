# Write your MySQL query statement below

SELECT e.left_operand,e.operator,e.right_operand,
CASE 
WHEN operator='>' and (v1.value>v2.value)
THEN 'true'
WHEN operator='=' and (v1.value=v2.value)
THEN 'true'
WHEN operator='<' and (v1.value<v2.value)
Then 'true'
ELSE 'false'
END as value
FROM Expressions e
JOIN variables v1
on v1.name = e.left_operand 
JOIN variables v2
on v2.name = e.right_operand
order by e.right_operand desc