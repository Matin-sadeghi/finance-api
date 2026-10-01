from flask_smorest import Blueprint,abort
from flask.views import MethodView
from flask_jwt_extended import (create_access_token,create_refresh_token)

from app.schemas import UserSchema,LoginSchema,AuthSchema,RegisterSchema,TokenSchema
from app.services.auth_service import register_user,login_user
from app.services.exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
auth_bp = Blueprint("auth",__name__,url_prefix="/api/v1/auth",description="Authentication endpoints")


@auth_bp.route("/register")
class Register(MethodView):
    @auth_bp.arguments(RegisterSchema)
    @auth_bp.response(201,UserSchema)
    def post(self,data):
        """Register a new user."""


        try:
            user = register_user(data["email"].lower().strip(), data["password"])
        except EmailAlreadyRegisteredError:
            abort(409, message="User with this email already exists.")
        
        return user

@auth_bp.route("/login")
class Login(MethodView):
    @auth_bp.arguments(LoginSchema)
    @auth_bp.response(200,TokenSchema)
    def post(self,data):
        """Login a user and return access and refresh tokens."""

        try:
            user = login_user(data["email"].lower().strip(), data["password"])
        except InvalidCredentialsError:
            abort(401, message="Invalid email or password.")

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "message": "Login successful.",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user
        }