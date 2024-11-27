# Write your MySQL query statement below
WITH t as (
SELECT d.name as Department,e.name,e.salary,
rank() over (partition by e.departmentId order by e.salary desc) as rank_salary
FROM Employee e
JOIN Department d
on e.departmentId = d.id
)
SELECT Department,name as Employee, salary as Salary
FROM t
Where rank_salary =1