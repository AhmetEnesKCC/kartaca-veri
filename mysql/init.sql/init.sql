CREATE DATABASE IF NOT EXISTS kartaca_db;

USE kartaca_db;

CREATE TABLE country (
    country_name varchar(50),
    country_code varchar(2)
);

CREATE TABLE currency (
    country_code varchar(2),
    currency varchar(3)
)