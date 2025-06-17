# app/models/page.py

from app.main import db

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'), nullable=False)
    sort_order = db.Column(db.Integer, default=0)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    is_published = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_system = db.Column(db.Boolean, default=False)

    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)


    # This allows you to access the parent board of a page using `page.board`.
    board = db.relationship('Board', back_populates='pages')

    # This is what makes the template loop `for section in page.sections` work.
    sections = db.relationship('Section', back_populates='page', lazy=True, order_by='Section.sort_order', cascade="all, delete-orphan")