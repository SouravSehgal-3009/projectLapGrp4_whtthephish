import uuid

import pymongo

from src.secrets import USERNAME,PASSWORD

class Database(object):

    URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.txbjp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI,connect=False)
        Database.DATABASE = client['WhtThePhish']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

class Question:
    def __init__(self,url, url_brand, phishing, category,_id=None):
        self.url = url
        self.url_brand = url_brand
        self.phishing=phishing
        self._id = uuid.uuid4().hex if _id is None else _id
        self.category=category
        
    def json(self):
        return {
            "url": self.url,
            "_id": self._id,
            "url_brand": self.url_brand,
            "phishing":self.phishing,
            "category":self.category
        }
    def save_to_mongo(self):
        Database.insert("questions", self.json())
        
import csv

Database.initialize()
  
# csv file name
filename = "phishing.csv"
  
  
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.DictReader(csvfile)
    i=0
      
    for row in csvreader:
        i+=1
        print(i)
        question=Question(**row)
        question.save_to_mongo()
    print('Complete')