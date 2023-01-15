CREATE TABLE if not exists ap_exam(
    ap_exam_id serial PRIMARY KEY,
    name text NOT NULL,
    score int NOT NULL,
    unit int DEFAULT 0,
    course TEXT [],
    ge TEXT []
);

CREATE INDEX name_idx ON ap_exam (name) WITH (deduplicate_items = off);

ALTER TABLE IF EXISTS courses ADD COLUMN alt_course_id VARCHAR(25) UNIQUE

ALTER TABLE IF EXISTS courses DROP COLUMN textsearchable_index_col

delete from courses_in_ge;

delete from courses;