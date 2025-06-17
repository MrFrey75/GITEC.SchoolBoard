# app/__init__.py
import os

from flask import Flask
from app.routes.auth_routes import auth_bp
from app.routes.admin_routes import bp as admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    app.secret_key = os.environ.get("SECRET_KEY", "changeme")

    from app.main import db
    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app