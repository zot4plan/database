GO 
USE zot4plandb;
GO

DROP PROCEDURE IF EXISTS get_program;
DROP PROCEDURE IF EXISTS get_schedule_by_id;

DELIMITER $$

CREATE PROCEDURE get_program(IN p_id INT) 
BEGIN
SELECT id, name, is_major, requirement, url FROM programs WHERE id = p_id;     
SELECT DISTINCT(dept_id) as department FROM depts_in_programs WHERE program_id = p_id;
END $$

CREATE PROCEDURE get_schedule_by_id(IN user_id VARCHAR(32)) 
BEGIN
UPDATE schedules SET last_access_date = CURRENT_DATE() WHERE id = user_id;
SELECT schedule FROM schedules WHERE id = user_id;     
END $$

DELIMITER ;




