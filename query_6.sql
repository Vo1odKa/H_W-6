SELECT
    s.id as student_id,
    s.name as student_name,
    s.s_name as student_s_name
FROM
    stud s
WHERE
    s.group_id = 1; 
