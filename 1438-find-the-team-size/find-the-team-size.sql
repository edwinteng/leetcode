# Write your MySQL query statement below
WITH team_size as (
    SELECT team_id,count(*) as team_size
    FROM Employee
    GROUP BY team_id
)
SELECT e.employee_id,t.team_size
FROM Employee e
JOIN team_size t
on e.team_id = t.team_id