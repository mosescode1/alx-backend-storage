--  We are all unique!
CREATE TABLE 
IF NOT EXISTS
users(
	id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(255),
    name VARCHAR(255),
	PRIMARY KEY (id),
    UNIQUE (email)
    );
