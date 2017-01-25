import sqlite3
from db import db

class ItemModel(db.Model): #
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) #2 dp

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
     # specify relationship for foreign key
    def __init__(self, name, price, store_id ):
        self.name = name
        self.price = price
        self.store_id = store_id
    def json(self):
        return {'name' : self.name, 'price' : self.price}



    def save_to_db(self):
        db.session.add(self) # session = objects
        db.session.commit()
        return self.json()

    @classmethod
    def find_by_name(cls, name):

        return cls.query.filter_by(name=name).first()  # alchemy model, which is the same as select from table where name = name
        # returns first one only



    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
