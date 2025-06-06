# backend/db.py

from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["ai_assistant_db"]
logs_collection = db["query_logs"]

async def log_query(query: str, result: str):
    await logs_collection.insert_one({
        "query": query,
        "result": result,
        "timestamp": datetime.utcnow()
    })
