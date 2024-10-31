-- This script lists all the cities of California in database hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
    LIMIT 1
)
ORDER BY cities.id ASC;
