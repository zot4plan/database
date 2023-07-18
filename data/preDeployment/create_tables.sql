-- DROP TABLE IF EXISTS courses_in_ge;
-- DROP TABLE IF EXISTS courses;

CREATE TABLE if not exists courses (
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
    terms TEXT,
    alt_course_id VARCHAR(25) UNIQUE
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

CREATE TABLE if not exists courses_in_ge(
    id serial PRIMARY KEY,
    course_id VARCHAR(25) NOT NULL,
    ge_id VARCHAR(5) NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (ge_id) REFERENCES general_education(ge_id)
);

CREATE TABLE if not exists schedules (
    schedule_id VARCHAR(64) PRIMARY KEY,
    schedule json NOT NULL,
    ap_exam json NULL, 
    active_date DATE NOT NULL,
    created_date DATE NOT NULL
);

CREATE TABLE if not exists ap_exam(
    ap_exam_id serial PRIMARY KEY,
    name text NOT NULL,
    score int NOT NULL,
    unit int DEFAULT 0,
    course TEXT [],
    ge TEXT []
);

CREATE INDEX name_idx ON ap_exam (name) WITH (deduplicate_items = off);

CREATE TABLE IF not exists playlists(
    playlist_id VARCHAR(64) PRIMARY KEY,
    thumbnail VARCHAR(64) NULL,
    name VARCHAR(128) NOT NULL,
    author VARCHAR(128),
    shared_by VARCHAR(128),
    original_url VARCHAR(256) NOT NULL,
    embed_url VARCHAR(256) NOT NULL,
    language VARCHAR(64),
    genre TEXT [],
    "like" integer DEFAULT 0,
    "view" integer DEFAULT 0,
    created_date timestamp DEFAULT CURRENT_TIMESTAMP,
    is_verified BOOLEAN DEFAULT false
);

CREATE TABLE IF not exists reports (
    report_id serial PRIMARY KEY,
    playlist_id VARCHAR(64) NOT NULL,
    reason VARCHAR(256) NOT NULL,
    created_date timestamp DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id)
);

CREATE TABLE if not exists visits(
    date_visit DATE PRIMARY KEY,
    home integer DEFAULT 1,
    virtual_cafe integer DEFAULT 0
);
