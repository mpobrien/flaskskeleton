from datetime import datetime
from pymongo import MongoClient

from flaskskeleton import app

db = MongoClient(app.config['MONGO_URL']).monitoring 

class Users:

    @staticmethod
    def get_by_name_pw(username, password):
        return db.users.find_one({"email":username, "password":password})

    @staticmethod
    def get_by_token(oid):
        return db.users.find_one({"token":oid})


