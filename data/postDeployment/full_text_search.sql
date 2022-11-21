ALTER TABLE courses
    ADD COLUMN textsearchable_index_col tsvector
    GENERATED ALWAYS AS (to_tsvector('english', course_id)) STORED;

CREATE INDEX textsearch_idx ON courses USING GIST (textsearchable_index_col);