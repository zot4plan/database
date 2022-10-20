ALTER TABLE visits
RENAME COLUMN number_of_visits to home;

ALTER TABLE visits
ADD COLUMN virtual_cafe integer DEFAULT 0;

ALTER TABLE schedules
RENAME COLUMN last_access_date to active_date;

ALTER TABLE schedules
ADD COLUMN created_date date;

UPDATE schedules
SET created_date = active_date;

CREATE TABLE IF not exists playlists(
    playlist_id VARCHAR(64) PRIMARY KEY,
    thumbnail VARCHAR(64) NULL,
    name VARCHAR(128) NOT NULL,
    author VARCHAR(128),
    share_by VARCHAR(128),
    original_url VARCHAR(256) NOT NULL,
    embed_url VARCHAR(256) NOT NULL,
    language VARCHAR(64),
    genre TEXT [],
    like integer DEFAULT 0,
    view integer DEFAULT 0,
    created_date DATE NOT NULL,
    is_verified BOOLEAN DEFAULT false
);

ALTER TABLE playlists
RENAME COLUMN "thumdnail" to thumbnail;