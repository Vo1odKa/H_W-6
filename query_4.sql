SELECT
    les_id as lesson_id,
    AVG(m.mark) as average_score
FROM
    murks m
WHERE
    stud_id IN (SELECT id FROM stud WHERE group_id IN (1, 2, 3))
GROUP BY
    les_id;
