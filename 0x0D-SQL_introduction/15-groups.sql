-- lists number of scores with same value sorted by number descending
SELECT score, COUNT(score) AS number FROM second_table GROUP BY number DESC;
