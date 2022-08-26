GO
CREATE DATABASE IF NOT EXISTS zot4plandb;
/d zot4plandb;
GO

DROP TABLE IF EXISTS courses_in_ge;
DROP TABLE IF EXISTS depts_in_programs;
DROP TABLE IF EXISTS general_education;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS programs;

CREATE TABLE courses (
    course_id TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    units integer NOT NULL,
    units_text TEXT NOT NULL,
    description TEXT NOT NULL,
    prerequisite TEXT,
    prerequisite_tree json,
    prerequisite_for TEXT,
    restriction TEXT,
    repeatability integer NOT NULL,
    corequisite TEXT,
    pre_or_core TEXT,
    same_as TEXT,
    overlaps_with TEXT,
    concurrent_with TEXT,
    ge TEXT,
    terms TEXT NOT NULL
);

CREATE TABLE programs(
    program_id serial PRIMARY KEY,
    name TEXT NOT NULL,
    is_major boolean NOT NULL,
    requirement json DEFAULT NULL,
    depts TEXT [],
    url TEXT NOT NULL
);

CREATE TABLE general_education(
    ge_id VARCHAR(5) PRIMARY KEY,
    name TEXT NOT NULL,
    note TEXT NOT NULL
);

CREATE TABLE courses_in_ge(
    id serial PRIMARY KEY,
    course_id VARCHAR(25) NOT NULL,
    ge_id VARCHAR(5) NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (ge_id) REFERENCES general_education(id)
);

CREATE TABLE if not exists schedules (
    schedule_id VARCHAR(64) PRIMARY KEY,
    schedule json NOT NULL,
    last_access_date DATE NOT NULL,
);

CREATE TABLE if not exists visits(
    id VARCHAR(5) NOT NULL,
    total integer NOT NULL,
    PRIMARY KEY(id)
);