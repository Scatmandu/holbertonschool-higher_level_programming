-- lists all records of second_table where name exists

SELECT score, name
FROM second_table
WHERE EXISTS 
(SELECT name FROM second_table)
ORDER BY score DESC;