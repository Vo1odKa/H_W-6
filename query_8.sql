SELECT
    t.name as teacher_name,
    t.s_name as teacher_s_name,
    AVG(m.mark) as average_score
FROM
    teacher t
JOIN
    lessons l ON t.id = l.tch_id
JOIN
    marks m ON l.id = m.les_id
GROUP BY
    t.id
ORDER BY
    t.name, t.s_name;
