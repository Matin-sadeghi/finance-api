from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import (create_access_token,create_refresh_token,jwt_required,get_jwt_identity)
from werkzeug.security import generate_password_hash,check_password_hash

from app.extensions import db
from app.models import User, user
from app.schemas import UserSchema,LoginSchema,AuthSchema,RegisterSchema,TokenSchema
from app.services.auth_service import register_user,login_user
auth_bp = Blueprint("auth",__name__,url_prefix="/api/v1/auth",description="Authentication endpoints")


@auth_bp.route("/register")
class Register(MethodView):
    @auth_bp.arguments(RegisterSchema)
    @auth_bp.response(201,UserSchema)
    def post(self,data):
        """Register a new user."""

        user = register_user(data["email"].lower().strip(), data["password"])
        if user is None:
            return {"message": "User with this email already exists."}, 409
        
        return user

@auth_bp.route("/login")
class Login(MethodView):
    @auth_bp.arguments(LoginSchema)
    @auth_bp.response(200,TokenSchema)
    def post(self,data):
        """Login a user and return access and refresh tokens."""

        user = login_user(data["email"].lower().strip(), data["password"])

        
        if user is None:
            return {"message": "Invalid email or password."}, 401

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "message": "Login successful.",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user
        }