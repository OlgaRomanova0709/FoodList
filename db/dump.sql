PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE pets (
	id INTEGER NOT NULL, 
	nickname VARCHAR(64), 
	age INTEGER, 
	PRIMARY KEY (id)
);
INSERT INTO pets VALUES(3,'Mika',100);
CREATE TABLE foods (
	id INTEGER NOT NULL, 
	name VARCHAR(64), 
	cuisine VARCHAR(64), 
	PRIMARY KEY (id)
);
INSERT INTO foods VALUES(1,'soup','mex');
COMMIT;