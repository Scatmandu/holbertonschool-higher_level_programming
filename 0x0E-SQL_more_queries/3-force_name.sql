-- creates atable with id and name where name cant be null
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
