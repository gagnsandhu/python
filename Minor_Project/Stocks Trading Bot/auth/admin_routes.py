
from flask_smorest import Blueprint
from flask import request,jsonify
from flask.views import MethodView
from db import db
from flask_smorest import abort
from flask_jwt_extended import create_access_token
from models.details import Detail
from flask_jwt_extended import jwt_required, get_jwt_identity,get_jwt
from schema import AdminDetailSchema,ChangeRoleSchema
from models.shadow import Shadow
from schema import SingleUserSchema
from models.users_stock import UserStock


admin_blp=Blueprint("admin",__name__,description="Admin Panel")

@admin_blp.route('/view_detail')
class AdminPanel(MethodView):
    @jwt_required()
    @admin_blp.response(200,AdminDetailSchema(many=True))
    def get(self):
        jwt=get_jwt()
        if not jwt.get("is_admin"):
            abort(401,message="Admin provilege required")
        return Detail.query.all()
    @admin_blp.arguments(SingleUserSchema)
    def post(self,data):
        username=data.get('username')
        obj=Detail.query.filter_by(username=username).first()
        user=Detail.query.get_or_404(obj.id)
        return user
        

@admin_blp.route('/change_role')
class ChangeRole(MethodView):
    @jwt_required()
    @admin_blp.arguments(ChangeRoleSchema)
    def put(self,username):
        jwt=get_jwt()
        if not jwt.get("is_admin"):
            abort(401,messsage="Admin provilege required")
        
        try:
            obj=Shadow.query.get_or_404(username)
            obj.role=1
            db.session.commit()
            return {"Message":"successfuly changed role"}
        except TypeError:
            return {"Message":"No Such User"}

@admin_blp.route('/delete')    
class DeleteUser(MethodView):
    @jwt_required()
    @admin_blp.arguments(ChangeRoleSchema)
    def delete(self,username):
        jwt=get_jwt()
        if not jwt.get("is_admin"):
            abort(401,messsage="Admin provilege required")
        
        obj=Shadow.query.get_or_404(username)
        id=obj.uid
        db.session.delete(obj)
        db.session.commit()
        user=Detail.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message":"user deleted successfully"}



@admin_blp.route('/user/<int:id>')
class AdminPrivileage(MethodView):
    @jwt_required()
    def get(self,id):
        try:
            obj=Detail.query.filter_by(id=id).first()
            return obj
        except AssertionError:
            return {"message":"User dont exists"}
        
    def delete(self,id):
        jwt=get_jwt()
        if not jwt.get("is_admin"):
            abort(401,message="Admin provilege required")
        obj=Detail.query.filter_by(id=id).first_or_404()
        db.session.delete(obj)
        db.session.commit()

        obj=Shadow.query.filter_by(uid=id).first_or_404()
        db.session.delete(obj)
        db.session.commit()

        obj=UserStock.query.filter_by(uid=id).first_or_404()
        db.session.delete(obj)
        db.session.commit()
