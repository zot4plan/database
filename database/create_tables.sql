GO
USE zot4plandb;
GO
DROP TABLE IF EXISTS courses_in_ge;
DROP TABLE IF EXISTS courses_in_programs;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS programs;
CREATE TABLE courses (
    id VARCHAR(25) NOT NULL,
    name VARCHAR(200) NOT NULL,
    department VARCHAR(20) NOT NULL,
    units INT NOT NULL,
    units_text VARCHAR(10) NOT NULL,
    description VARCHAR(1000) NOT NULL,
    prerequisite VARCHAR(1000) NOT NULL,
    prerequisite_tree VARCHAR(300) NOT NULL,
    prerequisite_for VARCHAR(750) NOT NULL,
    restriction VARCHAR(1000) NOT NULL,
    repeatability INT NOT NULL,
    corequisite VARCHAR (1000),
    pre_or_core VARCHAR (1000) NOT NULL,
    same_as VARCHAR(300) NOT NULL,
    overlaps_with VARCHAR(300) NOT NULL,
    concurrent_with VARCHAR(300) NOT NULL,
    ge VARCHAR(25) NOT NULL,
    terms VARCHAR(350) NOT NULL,
    PRIMARY KEY(id),
    FULLTEXT(id));

CREATE TABLE programs(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    is_major boolean NOT NULL,
    requirement json DEFAULT NULL,
    url VARCHAR(300) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE general_education(
    id VARCHAR(5) NOT NULL,
    name VARCHAR(55) NOT NULL,
    note VARCHAR(100) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE depts_in_programs(
    id INT NOT NULL AUTO_INCREMENT, 
    dept_id VARCHAR(25) NOT NULL,
    program_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (program_id) REFERENCES programs(id));

CREATE TABLE courses_in_ge(
    id INT NOT NULL AUTO_INCREMENT,
    course_id VARCHAR(25) NOT NULL,
    ge_id VARCHAR(5) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (ge_id) REFERENCES general_education(id));

CREATE TABLE schedules (
    id VARCHAR(64) NOT NULL ,
    schedule json NOT NULL,
    last_access_date DATE NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE visits(
    id VARCHAR(5) NOT NULL,
    total INT NOT NULL,
    PRIMARY KEY(id));

INSERT INTO general_education VALUES ("IA","Lower-Division Requirement","Two lower-division courses");
INSERT INTO general_education VALUES ("IB","Upper-Division Requirement","One upper-division course");
INSERT INTO general_education VALUES ("II","Science and Technology","Three courses");
INSERT INTO general_education VALUES ("III","Social and Behavioral Sciences", "Three courses");
INSERT INTO general_education VALUES ("IV","Arts and Humanities", "Three courses");
INSERT INTO general_education VALUES ("VA","Quantitative Literacy", "One Course (and an additional course from either Va or Vb - total of three courses)");
INSERT INTO general_education VALUES ("VB","Formal Reasoning","One Course (and an additional course from either Va or Vb - total of three courses)");
INSERT INTO general_education VALUES ("VI", "Language Other Than English","One course");
INSERT INTO general_education VALUES ("VII","Multicultural Studies","One course that may also satisfy another GE category");
INSERT INTO general_education VALUES ("VIII", "International/Global Issues","One course that may also satisfy another GE category");

/*
ALTER TABLE courses ADD FULLTEXT(id);
ALTER TABLE programs RENAME COLUMN isMajor TO is_major;
ALTER TABLE courses_in_ge RENAME COLUMN geId TO ge_id;
ALTER TABLE courses_in_ge RENAME COLUMN courseId TO course_id;
ALTER TABLE courses_in_programs RENAME COLUMN courseId TO course_id;
ALTER TABLE courses_in_programs RENAME COLUMN programId TO program_id;
ALTER TABLE courses_in_ge ADD FOREIGN KEY (course_id) REFERENCES courses(id);
ALTER TABLE courses_in_ge ADD FOREIGN KEY (ge_id) REFERENCES general_education(id);
ALTER TABLE courses_in_programs ADD FOREIGN KEY (program_id) REFERENCES programs(id);
*/
