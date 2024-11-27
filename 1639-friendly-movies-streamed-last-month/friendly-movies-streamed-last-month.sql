# Write your MySQL query statement below

SELECT distinct c.title
FROM TVProgram t
JOIN Content c
on t.content_id = c.content_id
WHERE YEAR(t.program_date)=2020 and MONTH(t.program_date)=6 
and c.Kids_content='Y' and c.content_type='Movies'