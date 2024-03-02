SELECT
    s.name as student_name,
    s.s_name as student_s_name,
    t.name as teacher_name,
    t.s_name as teacher_s_name,
    l.name as course_name
FROM
    stud s
JOIN
    groups g ON s.group_id = g.id
JOIN
    murks m ON s.id = m.stud_id
JOIN
    lessons l ON m.les_id = l.id
JOIN
    teacher t ON l.tch_id = t.id
WHERE
    s.id = 21
    AND t.id = 2;
