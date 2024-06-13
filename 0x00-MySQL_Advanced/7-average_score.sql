-- 7-average_score.sql

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the given user_id
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average_score
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END;
