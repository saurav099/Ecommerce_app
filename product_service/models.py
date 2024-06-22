from sqlalchemy.orm import versioned_session
from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    version = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.version = 1
