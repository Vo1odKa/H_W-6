SELECT stud.id, stud.name, stud.s_name, AVG(marks.mark) as average_score
FROM stud
JOIN marks ON stud.id = marks.stud_id
GROUP BY stud.id
ORDER BY average_score DESC
LIMIT 5;