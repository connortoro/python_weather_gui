import os
import pymongo
from dotenv import load_dotenv, find_dotenv

# Load env variables
load_dotenv(find_dotenv())
username = os.environ.get("DB_USER")
pwd = os.environ.get("DB_PWD")

# Connect to mongodb
uri = f"mongodb+srv://{username}:{pwd}@cluster0.yuchdcc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri)
user_db = client.user.user

def insert_user(_username, _password):

    # Create user
    user = {
        "username": _username,
        "password": _password
    }

    # Insert user
    user_db.insert_one(user)


def check_password(_username, _password):
    user = user_db.find_one({"username": _username})
    if user:
        password = user.get("password")
        if _password == password:
            return True

    return False




