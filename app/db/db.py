import os
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from dotenv import load_dotenv

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

db = Database()



async def connect_to_mongo():
  print("Connecting to MongoDB...")
  MONGO_URI = os.getenv("MONGODB_URI")
  MONGO_DB = os.getenv("MONGO_DB", "ecommerce")
  db.client = AsyncIOMotorClient(MONGO_URI)
  db.db = db.client[MONGO_DB]
  print("Successfully connected to MongoDB!")


async def close_mongo_connection():
  print("Closing MongoDB connection.")
  db.client.close()
  print("MongoDB connection closed.")


def get_database() -> AsyncIOMotorDatabase:
  return db.db

def get_product_collection():
  return db.db.get_collection("products")

def get_order_collection():
  return db.db.get_collection("orders")
