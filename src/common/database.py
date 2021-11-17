import pymongo
from src import secrets
import dns
import certifi


class Database(object):

    URI = f"mongodb+srv://{secrets.USERNAME}:{secrets.PASSWORD}@cluster0.txbjp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        ca = certifi.where()
        client = pymongo.MongoClient(Database.URI,connect=False, tlsCAFile=ca)
        Database.DATABASE = client['WhtThePhish']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
        
    @staticmethod
    def update(collection,query,updates):
        Database.DATABASE[collection].update_one(query,updates,upsert=False)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)