from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    location = db.Column(db.String)


class Menus(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    restraunt_id = db.relationship(db.Integer, db.ForeignKey("restraunts.id"))
    
    menu_item = db.Column(db.String)
    price = db.Column(db.Float)




    
class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    receipt_id = db.Column(db.Float, db.ForeignKey("reciepts.id"))
   

    total = db.relationship(db.Float, db.ForeignKey("menus.price"))
    


class Receipt(db.Model):
    __tablename__ = "receipts"

    id = db.Column(db.String, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))