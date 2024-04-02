# Daniel McPherson (30186044)

# Creates the database
CREATE DATABASE Hospital;
use Hospital;

# Creates the table
CREATE TABLE Insurance(InsuranceID varchar(10) primary key, company varchar(45), address varchar(50), phone varchar(14));
CREATE TABLE Patient(patientID varchar(10) primary key, firstname varchar(20), surname varchar(30), postcode varchar(8), address varchar(50), phone varchar(12), email varchar(40), insuranceID varchar(10));
CREATE TABLE Visit(patientID varchar(10), doctorID varchar(4), dateofvisit date, symptoms varchar(200), diagnosis varchar(50), PRIMARY KEY(patientID, doctorID, dateofvisit));
CREATE TABLE Doctor(doctorID varchar(4) primary key, firstname varchar(20), surname varchar(30), address varchar(50), email varchar(40), specialization varchar(25), experience varchar(12));
CREATE TABLE Prescription(prescriptionID varchar(10) primary key, dateprescribed date, dosage int, duration int, comment varchar(200), drugID varchar(7), doctorID varchar(4), patientID varchar(10));
CREATE TABLE Drug(drugID varchar(7) primary key, name varchar(50), sideeffects varchar(200), benefits varchar(200));

# Inserts the data
SET GLOBAL local_infile=1;

LOAD DATA INFILE '/var/lib/mysql-files/CSVFiles/Insurance.csv' INTO TABLE Insurance FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/var/lib/mysql-files/CSVFiles/Patient.csv' INTO TABLE Patient FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/var/lib/mysql-files/CSVFiles/Visit.csv' INTO TABLE Visit FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/var/lib/mysql-files/CSVFiles/Doctor.csv' INTO TABLE Doctor FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/var/lib/mysql-files/CSVFiles/Prescription.csv' INTO TABLE Prescription FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/var/lib/mysql-files/CSVFiles/Drug.csv' INTO TABLE Drug FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;