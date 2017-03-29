-- create the basic database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create the basic user with password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- give that user only select privileges on p schema database
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';

-- give all privileges on the dev db to this user
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- ensure these are the privileges present
FLUSH PRIVILEGES;
