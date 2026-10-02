from flask import Flask
from flask_smorest import Api
from app.openapi import configure_openapi
from config import Config
from app.extensions import db, migrate,jwt


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    api = Api(app)
    configure_openapi(api)

    from app.models import User,Transaction
    from app.routes import health_bp , auth_bp,transaction_bp , reports_blp

    api.register_blueprint(health_bp)
    api.register_blueprint(auth_bp)
    api.register_blueprint(transaction_bp)
    api.register_blueprint(reports_blp)



    return app