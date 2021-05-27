-- creates a table with id and name where id is unique and defaults to 1
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
