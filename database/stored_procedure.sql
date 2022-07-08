GO 
USE zot4plandb;
GO

DROP PROCEDURE IF EXISTS get_program;
DROP PROCEDURE IF EXISTS get_all_ge;

DELIMITER $$

CREATE PROCEDURE get_program(IN p_id INT) 
BEGIN
SELECT id, name, is_major, requirement, url FROM programs WHERE id = p_id;     
SELECT course_id as id, name ,department, units , description, 
prerequisite, prerequisite_tree, prerequisite_for, 
restriction, repeatability, corequisite, ge, terms
FROM (SELECT DISTINCT(course_id) 
                   FROM courses_in_programs 
                   WHERE program_id = p_id) as p LEFT JOIN courses ON courses.id = p.course_id; 
END $$

DELIMITER ;




