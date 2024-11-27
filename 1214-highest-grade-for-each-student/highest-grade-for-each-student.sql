# Write your MySQL query statement below
WITH t as (
SELECT student_id,course_id, grade,
rank() over (partition by student_id order by grade desc,course_id asc ) as r
FROM Enrollments
)

SELECT student_id,course_id,grade
FROM t 
WHERE r =1