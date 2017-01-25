import sqlite3
from db import db

# models are pour interperation of the data, like a helper, internal to the developer
# resourcers are external to the user
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80)) # max length 80
    password = db.Column(db.String(80)) # max length 80

    def save_to_db(self):
        db.session.add(self) # session = objects
        db.session.commit()


    def __init__(self,  username, password): # these object fields, id ,username and password must match the db definitions above

        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()  # alchemy model, which is the same as select from table where name = name
        # returns first one only



    @classmethod
    def find_by_id(cls, _id):      # id = db field _id is the parameter
        return cls.query.filter_by(id = _id)  # alchemy model, which is the same as select from table where name = name
