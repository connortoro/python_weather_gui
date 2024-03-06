import os
import pymongo
import bcrypt
from dotenv import load_dotenv, find_dotenv

# Load env variables
load_dotenv(find_dotenv())
username = os.environ.get("DB_USER")
pwd = os.environ.get("DB_PWD")

# Connect to mongodb
uri = f"mongodb+srv://{username}:{pwd}@cluster0.yuchdcc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri)
user_db = client.user.credentials

def insert_user(username, password):

    # Hash Password
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Create user
    user = {
        "username": username,
        "hash": hashed_pwd,
        "salt": salt
    }

    # Insert user
    user_db.insert_one(user)


def check_password(username, password):
    user = user_db.find_one({"username": username})
    if user:
        hash = user.get("hash")
        salt = user.get("salt")
        new_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return new_hash == hash

    return False




