SELECT
    DISTINCT l.name as course_name
FROM
    lessons l
JOIN teacher t ON l.tch_id = t.id
WHERE
    t.name = 'Dan'; 
