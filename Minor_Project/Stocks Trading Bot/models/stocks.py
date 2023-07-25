from db import db

class StockModel(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    token = db.Column(db.String(80),nullable=False)
    
