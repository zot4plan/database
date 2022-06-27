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

CREATE PROCEDURE get_all_ge() 
BEGIN
DECLARE finished INTEGER DEFAULT 0;
DECLARE geId varchar(5) DEFAULT "false";
DECLARE cursor_ge CURSOR FOR SELECT id FROM general_education;

DECLARE CONTINUE HANDLER 
FOR NOT FOUND SET finished = 1;

SELECT id, name, note FROM general_education; 
SELECT courses.* FROM courses JOIN (SELECT DISTINCT(course_id) 
                   FROM courses_in_ge) as c ON courses.id = c.course_id; 

OPEN cursor_ge;
WHILE finished = 0 DO
    FETCH cursor_ge INTO geId;
    SELECT course_id from courses_in_ge where ge_id = geId;
END WHILE;
CLOSE cursor_ge;

END $$

DELIMITER ;

