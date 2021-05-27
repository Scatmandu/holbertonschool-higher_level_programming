-- create database and table with id state id and name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO INCREMENT NOT NULL PRIMARY KEY,
	state_id NOT NULL FOREIGN KEY REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
