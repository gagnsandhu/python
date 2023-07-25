from db import db

class UserStock(db.Model):
    __tablename__ = 'user_stock'

    id=db.Column(db.Integer,nullable=False,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('shadow.uid'),nullable=False)
    stocks=db.Column(db.String,nullable=False)
    quantity=db.Column(db.Integer,nullable=False)

    user_details_connection=db.relationship('Shadow',back_populates='user_stock_connection')


