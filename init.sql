CREATE TABLE IF NOT EXISTS movies (
    movie_id serial PRIMARY KEY,
    preference_key INTEGER NOT NULL,
    movie_title VARCHAR NOT NULL,
    rating DOUBLE NOT NULL,
    year INTEGER NOT NULL,
    place INTEGER,
    vote INTEGER,
    link VARCHAR,
    created_at DATE NOT NULL
);