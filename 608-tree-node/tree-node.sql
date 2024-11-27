# Write your MySQL query statement below

SELECT distinct t1.id,
CASE WHEN t1.p_id is not null and t2.id is not null
THEN 'Inner'
WHEN t1.p_id is null
THEN 'Root'
ELSE 'Leaf'
END as type
FROM Tree t1
LEFT JOIN Tree t2
on t1.id = t2.p_id