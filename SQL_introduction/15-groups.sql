-- lists number of records with the same score in the table second_table
-- displays the score and number of records for this score with the label number, desc order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
