

-- create database
DROP DATABASE IF EXIST `Farm`;
CREATE DATABASE IF NOT EXISTS `Farm`;
USE `FARM`;

-- create table

CREATE TABLE `Customers` (
    `FirstName` varchar (20) NULL,
    `LastName`  varchar (20) NULL,
    `Emai`      varchar (30) NULL,
)

--INSERT IN