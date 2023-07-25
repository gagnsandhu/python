import os
import secrets
from flask import Flask,request,jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort,Api
from db import db
from auth.routes import blp
from flask_jwt_extended import JWTManager
from auth.admin_routes import admin_blp
from auth.stocks import blp as stockblp
from models.shadow import Shadow


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)
    app.config["JWT_SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128)) 
    jwt = JWTManager(app)
    
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        obj=Shadow.query.filter_by(uid=identity).first()
        print(obj)
        if obj.role == 1:
            return {"is_admin": True}
        return {"is_admin": False}
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
    with app.app_context():
        db.create_all()

    api.register_blueprint(blp)
    api.register_blueprint(admin_blp)
    api.register_blueprint(stockblp)
    return app