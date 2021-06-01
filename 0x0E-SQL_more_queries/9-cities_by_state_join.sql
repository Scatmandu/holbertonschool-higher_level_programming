-- displays city id, city name, and state name from database
SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id;
