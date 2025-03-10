-- 14-my_genres.sql
SELECT tv_genres.name FROM tv_genres
    JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_shows.title = 'Dexter'
    ORDER BY tv_genres.name;