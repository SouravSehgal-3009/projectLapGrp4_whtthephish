import uuid
from passlib.hash import sha256_crypt
from flask import session
from src.common.database import Database



class User(object):

    def __init__(self, email, password, name, _id=None,level1=0,level2=0,level3=0,level4=0,level5=0,level6=0,level7=0,stars=0):
        self.email = email
        self.password = password
        self.name=name
        self._id = uuid.uuid4().hex if _id is None else _id
        self.level1=level1
        self.level2=level2
        self.level3=level3
        self.level4=level4
        self.level5=level5
        self.level6=level6
        self.level7=level7
        self.stars=stars
        
    
    @staticmethod
    def validate_Form(name,email,password):
        valid=True
        if len(name)<3:
            valid=False
        if len(email)<5:
            valid=False
        if len(password)<5:
            valid = False
        return valid
    
    @staticmethod
    def updateUser(email,updateDict):
        user=User.get_by_email(email)
        Database.update("users",{'email': user.email,},{"$set":updateDict})

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        password=str(password)
        if user is not None:
            return sha256_crypt.verify(password,user.password)
        return False

    @classmethod
    def register(cls, email, password,name):
        user = cls.get_by_email(email)
        password=sha256_crypt.encrypt(str(password))
        if user is None:
            new_user = cls(email, password,name)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password,
            "name":self.name,
            "level1":self.level1,
            "level2":self.level2,
            "level3":self.level3,
            "level4":self.level4,
            "level5":self.level5,
            "level6":self.level6,
            "level7":self.level7,
            "stars":self.stars
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())