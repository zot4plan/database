DROP TABLE IF EXISTS courses_in_ge;
DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id VARCHAR(25) PRIMARY KEY,
    name TEXT,
    department TEXT,
    units numeric [],
    units_text TEXT,
    description TEXT,
    prerequisite TEXT,
    prerequisite_tree json,
    prerequisite_for TEXT [],
    corequisite TEXT,
    corequisite_tree json,
    prerequisite_or_corequisite TEXT,
    prerequisite_or_corequisite_tree json,
    restriction TEXT,
    same_as TEXT,
    overlaps_with TEXT,
    concurrent_with TEXT,
    repeatability integer,
    ge TEXT,
    past_terms TEXT
);

CREATE TABLE if not exists programs(
    program_id serial PRIMARY KEY,
    name TEXT NOT NULL,
    is_major boolean NOT NULL,
    requirement json DEFAULT NULL,
    departments TEXT [],
    url TEXT NOT NULL
);

CREATE TABLE if not exists general_education(
    ge_id VARCHAR(5) PRIMARY KEY,
    name TEXT NOT NULL,
    note TEXT NOT NULL
);

CREATE TABLE courses_in_ge(
    id serial PRIMARY KEY,
    course_id VARCHAR(25) NOT NULL,
    ge_id VARCHAR(5) NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (ge_id) REFERENCES general_education(ge_id)
);

CREATE TABLE if not exists schedules (
    schedule_id VARCHAR(64) PRIMARY KEY,
    schedule json NOT NULL,
    last_access_date DATE NOT NULL
);

/*CREATE TABLE sample_programs {
    sample_id serial PRIMARY KEY,
    program_ids integer [] NOT NULL,
    schedule json NOT NULL,
    author text,
}

CREATE TABLE if not exists schedules (
    schedule_id VARCHAR(64) PRIMARY KEY,
    schedule json NOT NULL,
    program_ids integer [],
    added_courses TEXT [],
    last_access_date DATE NOT NULL
);*/

CREATE TABLE if not exists visits(
    date_visit DATE PRIMARY KEY,
    number_of_visits integer DEFAULT 1
);