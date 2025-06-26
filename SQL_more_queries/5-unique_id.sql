    -- Create a table with an unique id 
    CREATE TABLE IF NOT EXISTS unique_id(
        id INT NOT NULL DEFAULT 1 UNIQUE,
        name VARCHAR(256)
    );
    -- The table unique_id has been created with an unique id 