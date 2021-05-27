-- converts database to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
--converts table to UTF-8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts name to UTF-8
ALTER TABLE first_table MODIFY COLUMN name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
