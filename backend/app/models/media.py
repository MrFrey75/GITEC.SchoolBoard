# app/models/media.py

import enum
from app.main import db

class MediaAsset(db.Model):
    __tablename__ = 'media-assets'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filetype = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    caption = db.Column(db.String(100), nullable=True)
    attribution = db.Column(db.String(100), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)  # Indicates if this media asset is deleted

    def __repr__(self):
        return f"<MediaAsset {self.filename} (ID: {self.id})>"

    def __init__(self, filename, filepath, filetype, description=None, caption=None, attribution=None):
        self.filename = filename
        self.filepath = filepath
        self.filetype = filetype
        self.description = description
        self.caption = caption
        self.attribution = attribution
        self.is_deleted = False

    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'filepath': self.filepath,
            'filetype': self.filetype,
            'description': self.description,
            'caption': self.caption,
            'attribution': self.attribution,
            'is_deleted': self.is_deleted
        }

    @staticmethod
    def get_by_id(media_id):
        return MediaAsset.query.get(media_id)

    @staticmethod
    def get_all_media():
        return MediaAsset.query.filter_by(is_deleted=False).all()

    @staticmethod
    def get_media_by_filename(filename):
        return MediaAsset.query.filter_by(filename=filename, is_deleted=False).first()

    @staticmethod
    def create_media(filename, filepath, filetype, description=None, caption=None, attribution=None):
        new_media = MediaAsset(
            filename=filename,
            filepath=filepath,
            filetype=filetype,
            description=description,
            caption=caption,
            attribution=attribution
        )
        db.session.add(new_media)
        db.session.commit()
        return new_media

    @staticmethod
    def update_media(media_id, filename=None, filepath=None, filetype=None, description=None, caption=None, attribution=None):
        media = MediaAsset.query.get(media_id)
        if media:
            if filename:
                media.filename = filename
            if filepath:
                media.filepath = filepath
            if filetype:
                media.filetype = filetype
            if description:
                media.description = description
            if caption:
                media.caption = caption
            if attribution:
                media.attribution = attribution
            db.session.commit()
            return media
        return None

    @staticmethod
    def delete_media(media_id):
        media = MediaAsset.query.get(media_id)
        if media:
            media.is_deleted = True
            db.session.commit()
            return True
        return False
