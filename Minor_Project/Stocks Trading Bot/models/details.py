from db import db
from dataclasses import dataclass
@dataclass
class Detail(db.Model):
    __tablename__ = 'detail'

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(80),nullable=False)
    last_name=db.Column(db.String(80),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    balance=db.Column(db.Float,nullable=False)
    isSuspended=db.Column(db.Boolean,nullable=False)
    username=db.Column(db.String(255),nullable=False,unique=True)


    detail_connection=db.relationship('Shadow',back_populates='shadow_detail_connection')




    

