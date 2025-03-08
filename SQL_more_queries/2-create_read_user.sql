-- 2-create_read_user.sql
-- mysql -u root -p < 2-create_read_user.sql
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
USE htbn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON htbn_0d_2 TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;