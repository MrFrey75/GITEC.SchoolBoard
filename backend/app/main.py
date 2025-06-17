# app/main.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import config_by_name  # <-- 1. Import the config dictionary

# Initialize SQLAlchemy (used later with app context)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(config_by_name[config_name])

    try:
        os.makedirs(os.path.dirname(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')))
    except OSError:
        pass

    db.init_app(app)
    migrate = Migrate(app, db)

    from app.models import board, page, section, user, media

    # ✅ Add this line to fix the BuildError
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    try:
        from app.routes.board_routes import bp as board_bp
        app.register_blueprint(board_bp)
    except ImportError:
        pass

    try:
        from app.routes.admin_routes import bp as admin_bp
        app.register_blueprint(admin_bp)
    except ImportError:
        pass

    with app.app_context():
        from app.models import board, page, section, user, media, settings
        db.create_all()

    return app