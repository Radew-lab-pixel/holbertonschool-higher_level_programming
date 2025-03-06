-- 16-no_link.sql
SELECT * FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;