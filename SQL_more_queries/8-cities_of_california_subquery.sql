-- 8-cities_of_california_subquery.sql
SELECT cities.id, cities.name FROM cities
    WHERE cities.state_id = 1
    ORDER BY cities.id;
