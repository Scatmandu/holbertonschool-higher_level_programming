-- lists all records that have a name in descending order based on score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
