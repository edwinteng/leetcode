# Write your MySQL query statement below
WITH t as (
SELECT e.employee_id,e.manager_id,e2.manager_id as second_manager,
e3.manager_id as third_manager
FROM Employees e
LEFT JOIN Employees e2
on e.manager_id = e2.employee_id
LEFT JOIN EMployees e3
on e2.manager_id = e3.employee_id
)
SELECT distinct employee_id 
FROM t where (manager_id = 1 or second_manager=1 or third_manager=1 )and employee_id!=1