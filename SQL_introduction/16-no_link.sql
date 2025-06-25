-- List all record of a table with specific conditions
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
-- All record has been printed with name column only with values