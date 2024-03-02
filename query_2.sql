SELECT
    group_id as group_id,
    AVG(m.mark) as average_score
FROM
    stud
JOIN marks m ON stud.id = m.stud_id
WHERE
    group_id IN (1, 2, 3) 
    AND m.les_id = 1
GROUP BY
    group_id;
