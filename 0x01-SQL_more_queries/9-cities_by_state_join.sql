-- lists all cities contained within hbtn_0d_usa

SELECT cities.id, cities.name, states.name
FROM cities JOIN states on cities.state_id = states.id;