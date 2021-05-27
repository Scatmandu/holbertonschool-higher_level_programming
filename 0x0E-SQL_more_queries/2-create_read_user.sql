-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grants usage to user
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
-- grants select privileges to user
GRANT SELECT PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
