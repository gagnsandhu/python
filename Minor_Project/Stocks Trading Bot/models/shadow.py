from db import db

class Shadow(db.Model):
    __tablename__ = 'shadow'

    uid =db.Column(db.Integer,db.ForeignKey('detail.id'),autoincrement=True)
    username=db.Column(db.String(80),primary_key=True)
    password=db.Column(db.String(256),nullable=False)
    role=db.Column(db.Integer,db.ForeignKey('roles.id'))

    user_connection=db.relationship("Role",back_populates="role_connection")
    shadow_detail_connection=db.relationship('Detail',back_populates='detail_connection')
    user_stock_connection=db.relationship('UserStock',back_populates='user_details_connection')




