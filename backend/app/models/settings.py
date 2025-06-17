# app/models/settings.py

from app.main import db

class AppSetting(db.Model):
    __tablename__ = 'app_settings' # Renamed to avoid conflict with the Settings model
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the app setting
    key = db.Column(db.String(50), unique=True, nullable=False) # Key for the app setting
    value = db.Column(db.String(255), nullable=False) # Value for the app setting
    description = db.Column(db.String(255), nullable=False) # Description of the app setting
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp()) # Timestamp for when the app setting was created

