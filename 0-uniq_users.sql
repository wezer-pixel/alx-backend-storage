--- create a table users with id email, name
CREATE TABLE IF NOT EXISTS users(id INT NOT NULL AUTO INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE, 
	name VARCHAR(255);
