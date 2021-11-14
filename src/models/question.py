import uuid
from passlib.hash import sha256_crypt
from flask import session
from src.common.database import Database



class Question(object):

    def __init__(self, url, url_brand, phishing, category, _id=None):
        self.url = url
        self.url_brand = url_brand
        self.phishing=phishing
        self._id = uuid.uuid4().hex if _id is None else _id
        self.category=category
        
    @classmethod
    def get_by_category_and_phishing(cls, category, phishing):
        cursor = Database.find("questions", {"category": str(category), "phishing": str(phishing)})
        data = []
       
        for document in cursor:
            data.append(cls(**document))
            
        return data

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("questions", {"_id": _id})
        if data is not None:
            return cls(**data)
