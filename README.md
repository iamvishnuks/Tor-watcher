# Tor-watcher
This script can be used to mine informations of exit relays in TOR network

# Run below SQL query to create database

CREATE TABLE ip_info(ID INT(20) PRIMARY KEY AUTO_INCREMENT,IP INT(50) UNIQUE, REGION  VARCHAR(100) NOT NULL,COUNTRY VARCHAR(10),CITY VARCHAR(100), ORG VARCHAR(100))
