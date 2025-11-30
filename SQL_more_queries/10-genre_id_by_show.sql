-- task 10
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC