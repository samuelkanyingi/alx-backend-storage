-- stored procedure

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate total weight for the user's projects
        SET @total_weight = (SELECT SUM(p.weight)
                             FROM projects p
                             INNER JOIN corrections c ON p.id = c.project_id
                             WHERE c.user_id = user_id);

        -- Calculate sum of weighted scores for the user's projects
        SET @weighted_score_sum = (SELECT SUM(c.score * p.weight)
                                   FROM corrections c
                                   INNER JOIN projects p ON c.project_id = p.id
                                   WHERE c.user_id = user_id);

        -- Calculate the average weighted score
        IF @total_weight > 0 THEN
            SET @average_weighted_score = @weighted_score_sum / @total_weight;
        ELSE
            SET @average_weighted_score = 0;
        END IF;

        -- Update the user's average score in the users table
        UPDATE users
        SET average_score = @average_weighted_score
        WHERE id = user_id;

    END LOOP;

    CLOSE cur;
END
