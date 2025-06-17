# app/models/board.py

from app.main import db

class Board(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True)
    slug_identifier = db.Column(db.String(100), nullable=False, unique=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    is_published = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_system = db.Column(db.Boolean, default=False)

    # This allows you to access all pages of a board using `board.pages`.
    pages = db.relationship('Page', back_populates='board', lazy=True, order_by='Page.sort_order', cascade="all, delete-orphan")