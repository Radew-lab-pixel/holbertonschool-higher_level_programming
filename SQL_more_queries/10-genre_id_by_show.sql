-- 10-genre_id_by_show.sql
-- LOAD DATABASE INFILE 'hbtn_0d_tvshows' TO DATABASE hbtn_0d_tvshows; cannot use on the sql dump
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id 
    FROM tvshows
    ORDER BY tv_shows.title, tv_show_genres.genre_id;

