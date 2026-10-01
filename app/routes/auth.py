from flask import Blueprint,request,jsonify
from flask_jwt_extended import (create_access_token,create_refresh_token,jwt_required,get_jwt_identity)
from werkzeug.security import generate_password_hash,check_password_hash

from app.extensions import db
from app.models import User

auth_bp = Blueprint("auth",__name__,url_prefix="/api/v1/auth")


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True)

    if not isinstance(data,dict):
        return jsonify({"error":"Invalid JSON body"}),400
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error":"Email and password are required"}),400

    email = email.strip().lower()

    if len(password) < 8:
        return jsonify({"error":"Password must be at least 8 characters"}),400

    existing_user = User.query.filter_by(email = email).first()

    if existing_user :
        return jsonify({"error":"Email already registerd"}), 409

    user = User(email=email,password = generate_password_hash(password))

    db.session.add(user)
    db.session.commit()
    return jsonify({
        "message":"User Registerd successfully",
        "user":{
            "id":user.id,
            "email":user.email
        }
    }),201

@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True)
    if not isinstance(data,dict):
        return jsonify({"error":"Invalid JSON body"}),400
    
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error":"Email and password are required"}),400

    email = email.strip().lower()

    if len(password) < 8:
        return jsonify({"error":"Password must be at least 8 characters"}),400

    user = User.query.filter_by(email = email).first()

    if not user or not check_password_hash(user.password,password):
        return jsonify({"error":"Invalid email or password"}),401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify({
        "message":"Login successful",
        "access_token":access_token,
        "refresh_token":refresh_token,
        "user":{
            "id":user.id,
            "email":user.email
        }
    }),200

@auth_bp.get("/me")
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = db.session.get(User,int(user_id))

    if not user:
        return jsonify({"error":"User not found"}),404

    return jsonify({"id":user.id,"email":user.email,"created_at":user.created_at.isoformat()}),200




