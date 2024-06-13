-- stored procedure

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_score_sum FLOAT DEFAULT 0;
    DECLARE average_weighted_score FLOAT DEFAULT 0;

    -- Calculate the total weight for the user's projects
    SELECT SUM(p.weight) INTO total_weight
    FROM projects p
    INNER JOIN corrections c ON p.id = c.project_id
    WHERE c.user_id = user_id;

    -- Calculate the sum of weighted scores for the user's projects
    SELECT SUM(c.score * p.weight) INTO weighted_score_sum
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET average_weighted_score = weighted_score_sum / total_weight;
    ELSE
        SET average_weighted_score = 0;
    END IF;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = average_weighted_score
    WHERE id = user_id;
END
