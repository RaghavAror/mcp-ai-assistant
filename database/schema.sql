-- Create a table to log user queries and agent responses
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    query TEXT NOT NULL,
    response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
