-- 8-cities_of_california_subquery.sql
SELECT cities.id, cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = 'California'
    ORDER BY cities.id;
