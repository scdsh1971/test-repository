
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') # specifies backwards link to items also, lazy=dynamic means dont create an object for all items that link to a store, can cause overhead
    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name' : self.name, 'items' : [item.json() for item in self.items.all()]} # means each time json methosd is called the items table is read



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
