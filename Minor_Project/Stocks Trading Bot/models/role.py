from db import db

class Role(db.Model):
    __tablename__ = 'roles'

    id=db.Column(db.Integer, primary_key=True)
    role=db.Column(db.String(80),nullable=False)

    role_connection=db.relationship("Shadow",back_populates="user_connection")
    

