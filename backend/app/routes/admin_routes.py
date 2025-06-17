# app/routes/admin_routes.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from functools import wraps
from app.models.board import Board
from app.models.page import Page
from app.models.section import Section
from app.models.settings import AppSetting
from app.models.user import User
from app.main import db
from werkzeug.utils import secure_filename, datetime
import os

bp = Blueprint('admin', __name__, url_prefix='/admin')

UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'uploads'))
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

# -----------------------------
# Settings
# -----------------------------

@bp.route("/settings", methods=["GET"])
@login_required
def settings():
    appsettings = AppSetting.query.all()
    return render_template("admin/manage_settings.html", appsettings=appsettings)

@bp.route("/settings/update", methods=["POST"])
@login_required
def update_settings():
    appsettings = request.form.to_dict()
    for key, value in appsettings.items():
        setting = AppSetting.query.filter_by(key=key).first()
        if setting:
            setting.value = value
        else:
            new_setting = AppSetting(key=key, value=value)
            db.session.add(new_setting)
    db.session.commit()
    flash("Settings updated successfully.", "success")
    return redirect(url_for("admin.settings"))

@bp.route("/settings/create", methods=["POST"])
@login_required
def create_setting():
    key = request.form.get("new_key").strip()
    value = request.form.get("new_value").strip()
    description = request.form.get("new_description", "").strip()

    if not key or not value:
        flash("Key and value are required.", "danger")
        return redirect(url_for("admin.settings"))

    existing = AppSetting.query.filter_by(key=key).first()
    if existing:
        flash("A setting with that key already exists.", "danger")
        return redirect(url_for("admin.settings"))

    new_setting = AppSetting(key=key, value=value, description=description)
    db.session.add(new_setting)
    db.session.commit()
    flash("New setting added.", "success")
    return redirect(url_for("admin.settings"))


# -----------------------------
# Users
# -----------------------------

@bp.route("/users", methods=["GET"])
@login_required
def users():
    users = User.query.filter_by(is_deleted=False).all()
    return render_template("admin/manage_users.html", users=users)

@bp.route("/users/delete/<int:user_id>", methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if user and not user.is_system_admin:
        user.is_deleted = True
        db.session.commit()
        flash("User deleted successfully.", "success")
    else:
        flash("Cannot delete system admin user.", "danger")
    return redirect(url_for("admin.users"))

@bp.route("/users/create", methods=["GET", "POST"])
@login_required
def create_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.does_username_exist(username):
            flash("Username already exists.", "danger")
            return redirect(url_for("admin.create_user"))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("User created successfully.", "success")
        return redirect(url_for("admin.users"))

    return render_template("admin/create_user.html")

@bp.route("/users/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    user = User.query.get(user_id)
    if not user or user.is_system_admin:
        flash("Cannot edit system admin user.", "danger")
        return redirect(url_for("admin.users"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.does_username_exist(username) and username != user.username:
            flash("Username already exists.", "danger")
            return redirect(url_for("admin.edit_user", user_id=user_id))

        user.username = username
        if password:
            user.set_password(password)
        db.session.commit()
        flash("User updated successfully.", "success")
        return redirect(url_for("admin.users"))

    return render_template("admin/edit_user.html", user=user)


# -----------------------------
# Media
# -----------------------------

@bp.route("/media", methods=["GET"])
@login_required
def media():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("admin/manage_media.html", files=files)

@bp.route("/media/upload", methods=["POST"])
@login_required
def upload_media():
    if 'file' not in request.files:
        flash("No file part in the request.", "danger")
        return redirect(url_for("admin.media"))

    file = request.files['file']
    if file.filename == '':
        flash("No selected file.", "danger")
        return redirect(url_for("admin.media"))

    if file:
        # Ensure the uploads folder is inside /static/uploads
        UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'uploads'))
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Secure the filename
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        try:
            file.save(filepath)
            flash("File uploaded successfully.", "success")
        except Exception as e:
            flash(f"File upload failed: {str(e)}", "danger")

    return redirect(url_for("admin.media"))

@bp.route("/media/delete/<filename>", methods=["POST"])
@login_required
def delete_media(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash("File deleted successfully.", "success")
    else:
        flash("File not found.", "danger")
    return redirect(url_for("admin.media"))

# -----------------------------
# Boards
# -----------------------------

@bp.route("/board/edit/<int:board_id>", methods=["GET"])
@login_required
def edit_board(board_id):
    if board_id == 0:
        board = Board()
        flash("Creating a new board.", "info")
    else:
        board = Board.query.get(board_id)
        flash("Editing board.", "info")

    return render_template("admin/edit_board.html", board=board)

@bp.route("/board/update/<int:board_id>", methods=["POST"])
@login_required
def update_board(board_id):
    if board_id == 0:
        board = Board()
        flash("Board created successfully.", "success")
    else:
        board  = Board.query.get(board_id)
        flash("Board updated successfully.", "success")

    return redirect(url_for("admin.edit_board", board_id=board.id))

@bp.route("/board/delete/<int:board_id>", methods=["POST"])
@login_required
def delete_board(board_id):
    board = Board.query.get(board_id)
    board.is_deleted = True
    db.session.commit()
    flash("Board deleted successfully.", "success")
    return redirect(url_for("admin.dashboard"))

# -----------------------------
# Pages
# -----------------------------

@bp.route("/page/delete/<int:page_id>", methods=["POST"])
@login_required
def delete_page(page_id):
    page = Page.query.get(page_id)
    if page:
        db.session.delete(page)
        db.session.commit()
        flash("Page deleted.", "success")
    return redirect(request.referrer or url_for("admin.dashboard"))

@bp.route("/section/delete/<int:section_id>", methods=["POST"])
@login_required
def delete_section(section_id):
    section = Section.query.get(section_id)
    if section:
        db.session.delete(section)
        db.session.commit()
        flash("Section deleted.", "success")
    return redirect(request.referrer or url_for("admin.dashboard"))

# -----------------------------
# Sections
# -----------------------------

@bp.route("/section/update/<int:section_id>", methods=["POST"])
@login_required
def update_section(section_id):
    section = Section.query.get_or_404(section_id)

    section.title = request.form.get("title", section.title)
    section.section_type = request.form.get("section_type", section.section_type.name)
    section.content = request.form.get("content", section.content)

    start_time = request.form.get("start_time")
    end_time = request.form.get("end_time")

    if start_time:
        section.start_time = datetime.fromisoformat(start_time)
    else:
        section.start_time = None

    if end_time:
        section.end_time = datetime.fromisoformat(end_time)
    else:
        section.end_time = None

    db.session.commit()
    flash("Section updated successfully.", "success")
    return redirect(request.referrer or url_for("admin.dashboard"))


