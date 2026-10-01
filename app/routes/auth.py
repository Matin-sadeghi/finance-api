from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import (create_access_token,create_refresh_token,jwt_required,get_jwt_identity)
from werkzeug.security import generate_password_hash,check_password_hash

from app.extensions import db
from app.models import User
from app.schemas import UserSchema,LoginSchema,AuthSchema,RegisterSchema,TokenSchema

auth_bp = Blueprint("auth",__name__,url_prefix="/api/v1/auth",description="Authentication endpoints")


@auth_bp.route("/register")
class Register(MethodView):
    @auth_bp.arguments(RegisterSchema)
    @auth_bp.response(201,UserSchema)
    def post(self,data):
        """Register a new user."""

        email = data["email"].lower().strip()

        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists."}, 409

        user = User(email=email, password=generate_password_hash(data["password"]))

        db.session.add(user)
        db.session.commit()
        return user

@auth_bp.route("/login")
class Login(MethodView):
    @auth_bp.arguments(LoginSchema)
    @auth_bp.response(200,TokenSchema)
    def post(self,data):
        """Login a user and return access and refresh tokens."""

        email = data["email"].lower().strip()
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, data["password"]):
            return {"message": "Invalid email or password."}, 401

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "message": "Login successful.",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user
        }