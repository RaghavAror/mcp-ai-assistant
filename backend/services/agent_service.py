import os
import asyncio
from dotenv import load_dotenv
from mcp_use import MCPClient, MCPAgent
from langchain_openai import ChatOpenAI
from services.db_service import log_query  # ⬅️ Add this import


async def run_agent(query: str):
    load_dotenv()

    client = MCPClient.from_config_file("mcp_config.json")
    llm = ChatOpenAI(model="gpt-4o")  # or switch to Groq, etc.
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        result = await agent.run(query)
        await log_query(query, str(result))  # ⬅️ Log the query and result
        return str(result)
    finally:
        await client.close_all_sessions()
