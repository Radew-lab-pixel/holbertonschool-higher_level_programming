-- 2-create_read_user.sql
-- mysql -u root -p < 2-create_read_user.sql
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
-- REVOKE ALL PRIVILEGES ON hbtn_0d_2.* FROM USER 'user_0d_2'@'localhost'; not working
-- REVOKE ALL PRIVILEGES ON hbtn_0d_2.* FROM 'user_0d_2'@'localhost';
-- FLUSH PRIVILEGES;
