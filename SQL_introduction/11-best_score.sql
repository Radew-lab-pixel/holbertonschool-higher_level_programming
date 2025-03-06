-- 11-best_score.sq
SELECT score, name FROM second_table
    WHERE score >=10
    ORDER BY score DESC;