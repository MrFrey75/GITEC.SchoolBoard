# app/models/media.py

import enum
from app.main import db

class MediaAsset(db.Model):
    __tablename__ = 'media-assets'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filepath = db.Column(db.String(100), nullable=False)
    filetype = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    caption = db.Column(db.String(100), nullable=True)
    attribution = db.Column(db.String(100), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)  # Indicates if this media asset is deleted
