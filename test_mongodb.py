from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URL from the environment variable
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Ensure MONGO_DB_URL is retrieved correctly
if not MONGO_DB_URL:
    print("❌ MONGO_DB_URL is not set. Check your .env file.")
    exit()

# Use the correct variable reference
client = MongoClient(MONGO_DB_URL)

try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
