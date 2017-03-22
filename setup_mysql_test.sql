-- create the basic database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the basic user with password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- give that user only select privileges on p schema database
GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';

-- give all privileges on the test db to this user
GRANT ALL PRIVILEGES ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

-- ensure these are the privileges present
FLUSH PRIVILEGES;
