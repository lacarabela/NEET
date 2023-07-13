CREATE DATABASE manga_database;

CREATE TABLE Reading (
    manga_id BIGSERIAL PRIMARY KEY,
    title text,
    author VARCHAR(255),
    artist VARCHAR(255),
	last_read_chapter INT,
    chapter_count INT,
    start_date DATE,
    completion_date DATE
);

CREATE TABLE Completed (
    manga_id INT PRIMARY KEY,
    title text,
    author VARCHAR(255),
    artist VARCHAR(255),
	last_read_volume INT,
    volume_count INT,
    start_date DATE,
    completion_date DATE
);

INSERT INTO Reading (title, author, artist, last_read_volume, volume_count, start_date)
VALUES ('The Quintessential Quintuplets', 'Negi Haruba', NULL, 4, 14, '2023-06-26'),
       ('Chainsaw Man', 'Tatsuki Fujimoto', NULL, 11, NULL, NULL);


