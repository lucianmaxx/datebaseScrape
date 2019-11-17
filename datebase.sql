DROP DATABASE IF EXISTS datebase;
CREATE DATABASE datebase;

-- creating account samples, 50 random profiles (no photos) from text file, then adding a userID to each account
USE datebase;
DROP TABLE IF EXISTS userAccount;
CREATE TABLE userAccount (
firstName VARCHAR(20) NOT NULL,
lastName VARCHAR(30) NOT NULL,
email VARCHAR(40) NOT NULL,
userPassword VARCHAR(30) NOT NULL,
birthday VARCHAR(40) NOT NULL,
addressCity VARCHAR(40) NOT NULL,
gender VARCHAR(20) NOT NULL,
occupation VARCHAR(60) NOT NULL,
phone VARCHAR(30) NOT NULL
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/users.txt' INTO TABLE userAccount;
ALTER TABLE `userAccount` ADD `userID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;


