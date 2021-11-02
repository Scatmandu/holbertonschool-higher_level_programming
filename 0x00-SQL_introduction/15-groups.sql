-- lists number of records with same score in second_table

SELECT COUNT(score)
FROM second_table
GROUP BY score ORDER BY score DESC;