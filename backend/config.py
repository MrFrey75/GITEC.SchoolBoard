import os

# Find the absolute path of the directory containing this file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration class. Contains default settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data/schoolboard.db')

class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration for production."""
    DEBUG = False
    # Add other production-specific settings here, e.g.,
    # SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

# A dictionary to access the config classes by name
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}