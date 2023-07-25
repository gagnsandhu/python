from flask_smorest import Blueprint
from flask import request
from schema import UserSignupSchema
from flask.views import MethodView
from db import db
from flask_smorest import abort
from auth.signup import Signup
from schema import PlainLoginSchema
from auth.login import UserLogin
from flask_jwt_extended import create_access_token
from models.details import Detail
from flask_jwt_extended import jwt_required, get_jwt_identity
from schema import InfoSchema
from trade.trade import price_of_stock
from schema import BuySchema
from auth.stock_buy import check_balance,add_stock
from schema import MoneySchema


blp=Blueprint("Auth","auth",description="Authentication functions")

@blp.route('/auth/signup')
class Auth(MethodView):
    @blp.arguments(UserSignupSchema)
    def post(self, data):
        username=data.get('username')
        password=data.get('password')
        conf_password=data.get('conf_password')
        age=data.get('age')
        response=Signup.user_signup(username,password,conf_password,age)
        match response:
            case 1:
                return {"message":"Password did not match"},200
            case 2:
                return {"message":"Password length very short"},200
        is_user=Signup.create_user(**data)
        if is_user==2:
            response=Signup.update_user(username,password)
            if response == 1:
                return {"message":"user created successfully"},200
        return {"message":"username already taken"},200


@blp.route('/auth/login')
class Login(MethodView):
    @blp.arguments(PlainLoginSchema)
    def post(self,data):
        '''check if the user is logged in and password is correct'''
        response=UserLogin.user_login(**data)
        match response:
            case 1:
                return {"message": "username incorrect"}
            case 2:
                return {"message": "password incorrect"}
        user=Detail.query.filter(Detail.username==data["username"]).first()
        access_token=create_access_token(identity=user.id)
        return {"access_token": access_token},200


@blp.route('/my-info')
class MyInfo(MethodView):
    @jwt_required()
    @blp.response(200,InfoSchema)
    def get(self):
        token=get_jwt_identity()
        obj=Detail.query.filter_by(id=token).first()
        try:
            user=Detail.query.get_or_404(obj.id)
        except AttributeError:
            return {"message":"User not logged in"},200
        return user

            
@blp.route('/buy/stocks')
class Buy(MethodView):
    @jwt_required()
    @blp.arguments(BuySchema)
    def post(self,data):
        token=get_jwt_identity()
        obj=Detail.query.filter_by(id=token).first()
        stock_price=price_of_stock(data['stock'])
        total_price=stock_price * data["quantity"]
        response=check_balance(total_price,obj.balance)
        match response:
            case 1:
                return {"message":"Not enough balance"}
            case 2:
                add_stock(data,obj.id)
                obj.balance=obj.balance-total_price
                db.session.commit()
                return {"message":"Finally Bought"}
        return {"message":"Bought"}
        


@blp.route('/addMoney')
class AddMoney(MethodView):
    @jwt_required()
    @blp.arguments(MoneySchema)
    def post(self, money):
        token=get_jwt_identity()
        obj=Detail.query.filter_by(id=token).first()
        obj.balance=money['balance']
        db.session.commit()
        return {"message":"Money Added"},200



        
        

