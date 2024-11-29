# Write your MySQL query statement below
WITH score as (
SELECT e.exam_id,e.student_id,s.student_name,
dense_rank() over (partition by exam_id order by score desc) score_rank_desc,
dense_rank() over (partition by exam_id order by score asc) score_rank_asc
FROM Exam e
JOIN Student s
on e.student_id = s.student_id
),
t2 as (
    SELECT
    student_id,student_name,
    CASE WHEN score_rank_desc=1 THEN 1
    ELSE 0 END as rank_one,
    CASE WHEN score_rank_asc=1 THEN 1
    ELSE 0 END as rank_last
    FROM score

)
SELECT student_id,student_name
FROM t2
GROUP BY student_id,student_name
HAVING SUM(rank_one)=0 and SUM(rank_last)=0
ORDER BY student_id
#SELECT distinct s.student_id #,s.student_name
#FROM score s
#WHERE s.student_id not in (
#    SELECT distinct student_id
#    FROM score s2
#    WHERE score_rank_desc=1 or score_rank_asc=1
#)
