from flask import Flask
from config import Config
from app.extensions import db, migrate,jwt


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.models import User

    from app.routes import health_bp , auth_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)


    return app