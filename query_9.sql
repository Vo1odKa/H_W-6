SELECT
    s.name as student_name,
    s.s_name as student_s_name,
    l.name as course_name
FROM
    stud s
JOIN
    groups g ON s.group_id = g.id
JOIN
    marks m ON s.id = m.stud_id
JOIN
    lessons l ON m.les_id = l.id
WHERE
    s.id = 11
GROUP BY
    s.id, l.id
ORDER BY
    l.name;
