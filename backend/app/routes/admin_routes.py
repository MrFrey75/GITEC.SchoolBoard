# app/routes/admin_routes.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from functools import wraps
from app.models.board import Board
import os

bp = Blueprint('admin', __name__, url_prefix='/admin')

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

# -----------------------------
# Dashboard
# -----------------------------

@bp.route("/", methods=["GET"])
@login_required
def dashboard():
    boards = Board.query.filter_by(is_deleted=False).all()
    return render_template("admin/dashboard.html", boards=boards)