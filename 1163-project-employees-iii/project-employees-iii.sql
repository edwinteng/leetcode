# Write your MySQL query statement below
WITH exp_t as (
SELECT p.project_id,e.employee_id,
rank() over (partition by project_id order by experience_years desc) as rnk
FROM Project p
JOIN Employee e
on p.employee_id=e.employee_id
)
SELECT project_id,employee_id
FROM exp_t
WHERE rnk=1
