"""
getpass to hide password while taking input
"""
import hashlib
from models.details import Detail
from models.shadow import Shadow
from db import db
from sqlalchemy.exc import SQLAlchemyError


class Signup():
    @staticmethod
    def user_signup(username,password,conf_password,age):
        if password != conf_password:
            return 1
        if len(password) < 8:
            return 2
        return 3
    
    @staticmethod
    def create_user(first_name,last_name,username,age,password,conf_password):
        data={
            "first_name":first_name,
            "last_name":last_name,
            "age":age,
            "username":username,
            "balance":0,
            "isSuspended":False
        }
        user=Detail(**data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            return 1
        return 2
    
    @staticmethod
    def update_user(username,password):
        obj = Detail.query.filter_by(username=username).first()
        data={
            "uid":obj.id,
            "username":username,
            "password":hashlib.sha512(password.encode()).hexdigest(),
            "role":2
        }
        user=Shadow(**data)
        try:
            db.session.add(user)
            db.session.commit()
            return 1
        except SQLAlchemyError as e:
            print(e)
        return 2


        
        