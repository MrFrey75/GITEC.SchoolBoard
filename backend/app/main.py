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
    # Create the Flask application instance
    app = Flask(__name__)

    # -------------------------------------------
    # Configuration Section
    # -------------------------------------------
    # <-- 2. Determine the config to use (e.g., 'development' or 'production')
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(config_by_name[config_name])

    # v-- 3. REMOVE THIS ENTIRE BLOCK --v
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # db_path = os.path.join(basedir, '../data/schoolboard.db')
    # os.makedirs(os.path.dirname(db_path), exist_ok=True)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET", "dev-secret")
    # ^-- 3. REMOVE THIS ENTIRE BLOCK --^

    # Ensure the instance folder exists for the database
    try:
        os.makedirs(os.path.dirname(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')))
    except OSError:
        pass

    # -------------------------------------------
    # Extensions Initialization
    # -------------------------------------------

    # Bind SQLAlchemy to the Flask app
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Import models here so that Alembic (Flask-Migrate) can see them
    from app.models import board, page, section, user, media

    return app