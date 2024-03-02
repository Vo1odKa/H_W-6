SELECT g.name as group_name, AVG(marks.mark) as average_score
FROM groups g
JOIN stud ON g.id = stud.groupe_id
JOIN marks ON stud.id = marks.stud_id
WHERE marks.les_id = your_lesson_id
GROUP BY g.name;
