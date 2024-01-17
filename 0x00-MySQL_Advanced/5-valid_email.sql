--- create trigger to reset valid_email
--- when email is updated

-- Drop trigger if it exists
DROP TRIGGER IF EXISTS reset_valid_email;

-- Change delimiter for trigger creation
DELIMITER $$

-- Create trigger
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END $$

-- Restore default delimiter
DELIMITER ;
