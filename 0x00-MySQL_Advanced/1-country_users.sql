-- In and not out
CREATE TABLE 
IF NOT EXISTS
users(
	id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(255),
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY (id),
    UNIQUE (email)
    );
