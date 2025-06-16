# app/models/user.py

from app.main import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_system_admin = db.Column(db.Boolean, default=False, nullable=False) # Indicates if this is a system admin user - do not allow deletion

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # add def to check if a user is_system_admin
    def is_admin(self):
        return self.is_system_admin


def does_username_exist(username):
    return User.query.filter_by(username=username).first() is not None