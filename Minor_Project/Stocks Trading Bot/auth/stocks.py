
from flask_smorest import Blueprint
from flask import request
from schema import UserSignupSchema
from flask.views import MethodView
from db import db
from models.stocks import StockModel
from flask_smorest import abort
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity,get_jwt
from schema import StockSchema


blp=Blueprint("stocks",__name__,description="Stock portfolio")


@blp.route('/stocks')
class Stock(MethodView):
    @blp.response(200,StockSchema(many=True))
    def get(self):
        return StockModel.query.all()
    

@blp.route('/add_stock')
class AddStock(MethodView):
    @blp.arguments(StockSchema)
    @jwt_required()
    def post(self,stock):
        jwt=get_jwt()
        if not jwt.get("is_admin"):
            abort(401,messsage="Admin provilege required")
        data=StockModel(**stock)
        db.session.add(data)
        db.session.commit()
        return {"message":"stock added successfully"}
