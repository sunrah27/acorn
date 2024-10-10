from pymongo import MongoClient

# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client['acorn']

def get_users_collection():
        return db['users']

def get_projects_collection():
        return db['projects']