from pymongo import MongoClient

# Replace the connection string with your own if necessary
client = MongoClient("mongodb://localhost:27017/")

# Test connection
try:
    client.admin.command('ping')  # This sends a ping to the MongoDB server
    print("Connection to MongoDB successful!")
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    client.close()
