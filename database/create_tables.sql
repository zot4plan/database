DROP DATABASE IF EXISTS zot4plandb;
CREATE DATABASE zot4plandb;
GO
USE zot4plandb;
GO
CREATE TABLE courses (
    id VARCHAR(25) NOT NULL,
    name VARCHAR(200) NOT NULL,
    department VARCHAR(20) NOT NULL,
    units INT NOT NULL,
    description VARCHAR(1000) NOT NULL,
    prerequisite VARCHAR(1000) NOT NULL,
    prerequisite_tree VARCHAR(300) NOT NULL,
    prerequisite_for VARCHAR(750) NOT NULL,
    restriction VARCHAR(1000) NOT NULL,
    repeatability INT NOT NULL,
    corequisite VARCHAR (1000),
    ge VARCHAR(25) NOT NULL,
    terms VARCHAR(350) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE programs(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    isMajor boolean NOT NULL,
    requirement json DEFAULT NULL,
    required_courses VARCHAR(2200),
    url VARCHAR(300) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE courses_in_ges(
    id INT NOT NULL AUTO_INCREMENT,
    courseId VARCHAR(25) NOT NULL,
    geId VARCHAR(5) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE general_educations(
    id VARCHAR(5) NOT NULL,
    name VARCHAR(55) NOT NULL,
    note VARCHAR(100) NOT NULL,
    PRIMARY KEY(id));

CREATE TABLE visits(
    id VARCHAR(5) NOT NULL,
    total INT NOT NULL,
    PRIMARY KEY(id));

INSERT INTO general_educations VALUES ("IA","Lower-Division Requirement","Two lower-division courses");
INSERT INTO general_educations VALUES ("IB","Upper-Division Requirement","One upper-division course");
INSERT INTO general_educations VALUES ("II","Science and Technology","Three courses");
INSERT INTO general_educations VALUES ("III","Social and Behavioral Sciences", "Three courses");
INSERT INTO general_educations VALUES ("IV","Arts and Humanities", "Three courses");
INSERT INTO general_educations VALUES ("VA","Quantitative Literacy", "One Course (and an additional course from either Va or Vb - total of three courses)");
INSERT INTO general_educations VALUES ("VB","Formal Reasoning","One Course (and an additional course from either Va or Vb - total of three courses)");
INSERT INTO general_educations VALUES ("VI", "Language Other Than English","One course");
INSERT INTO general_educations VALUES ("VII","Multicultural Studies","One course that may also satisfy another GE category");
INSERT INTO general_educations VALUES ("VIII", "International/Global Issues","One course that may also satisfy another GE category");

ALTER TABLE courses ADD FULLTEXT(id);