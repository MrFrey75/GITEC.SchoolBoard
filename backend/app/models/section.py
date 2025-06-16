# app/models/section.py

import enum
from app.main import db

class Section(db.Model):
    __tablename__ = 'sections'
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'), nullable=False)
    sort_order = db.Column(db.Integer, default=0)

    title = db.Column(db.String(100), nullable=False)

    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)

    is_published = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_system = db.Column(db.Boolean, default=False)

    # This allows you to access the parent page of a section using `section.page`.
    page = db.relationship('Page', back_populates='sections')