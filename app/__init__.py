from flask import Flask
from config import Config


def createApp():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    from app.routes.health import health_bp
    app.register_blueprint(health_bp)

    return app