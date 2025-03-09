-- 10-genre_id_by_show.sql
-- LOAD DATABASE INFILE 'hbtn_0d_tvshows' TO DATABASE hbtn_0d_tvshows; cannot use on the sql dump
-- CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;  removed as failed checker but works on terminal
-- USE hbtn_0d_tvshows; removed as failed checker but works on terminal
SELECT tv_shows.title,
    tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres 
    ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;