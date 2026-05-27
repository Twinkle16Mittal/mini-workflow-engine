from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_URL)
mongo_db = client["workflow_logs"]