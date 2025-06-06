-- Optional seed data for logs table
INSERT INTO logs (query, response)
VALUES
('What is LangChain?', 'LangChain is a framework for developing applications powered by language models.'),
('How to run the MCP agent?', 'Use npx @playwright/mcp@latest and configure mcp_config.json as needed.');
