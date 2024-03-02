SELECT
    s.name as student_name,
    s.s_name as student_s_name,
    l.name as lesson_name,
    m.mark as mark
FROM
    stud s
JOIN
    marks m ON s.id = m.stud_id
JOIN
    lessons l ON m.les_id = l.id
JOIN
    groups g ON s.group_id = g.id
WHERE
    g.id = 1 
    AND l.id = 2; 