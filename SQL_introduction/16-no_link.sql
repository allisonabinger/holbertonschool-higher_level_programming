-- lists all records of the table having a name value, ordered by desc score
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
