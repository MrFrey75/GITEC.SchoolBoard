# seed.py

from app.main import create_app, db
from app.models.board import Board
from app.models.page import Page
from app.models.section import Section
from app.models.user import User
from app.models.settings import AppSetting

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    print("🧹 Dropped and recreated all tables.")

    print(f"📁 Database location: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # ---------------------------
    # Settings
    # ---------------------------

    setting1 = AppSetting()
    setting1.key = "background-color"
    setting1.value = "#ffffff"
    setting1.description = "Default background color for the application."

    setting2 = AppSetting()
    setting2.key = "text-color"
    setting2.value = "#000000"
    setting2.description = "Default text color for the application."

    db.session.add_all([setting1, setting2])

    print("⚙️ Added 2 app settings.")

    # ---------------------------
    # Users
    # ---------------------------
    user1 = User(username="admin")
    user1.set_password("adminpass")
    user2 = User(username="editor")
    user2.set_password("editorpass")
    user3 = User(username="viewer")
    user3.set_password("viewerpass")

    db.session.add_all([user1, user2, user3])
    print("👤 Added 3 users.")

    # ---------------------------
    # Board 1
    # ---------------------------
    board1 = Board(title="Board One", slug_identifier="board-one", is_published=True)
    db.session.add(board1)
    db.session.flush()

    page1_1 = Page(title="Page 1 of Board 1", board_id=board1.id, sort_order=1, is_published=True)
    page1_2 = Page(title="Page 2 of Board 1", board_id=board1.id, sort_order=2, is_published=True)
    page1_3 = Page(title="Page 3 of Board 1", board_id=board1.id, sort_order=3, is_published=True)
    db.session.add_all([page1_1, page1_2, page1_3])
    db.session.flush()

    section1 = Section(title="Section 1", page_id=page1_1.id, sort_order=1, is_published=True)
    section2 = Section(title="Section 2", page_id=page1_1.id, sort_order=2, is_published=True)
    section3 = Section(title="Section 3", page_id=page1_1.id, sort_order=3, is_published=True)
    section4 = Section(title="Section 4", page_id=page1_2.id, sort_order=1, is_published=True)
    section5 = Section(title="Section 5", page_id=page1_2.id, sort_order=2, is_published=True)
    section6 = Section(title="Section 6", page_id=page1_2.id, sort_order=3, is_published=True)
    section7 = Section(title="Section 7", page_id=page1_3.id, sort_order=1, is_published=True)
    section8 = Section(title="Section 8", page_id=page1_3.id, sort_order=2, is_published=True)
    section9 = Section(title="Section 9", page_id=page1_3.id, sort_order=3, is_published=True)
    db.session.add_all([section1, section2, section3, section4, section5, section6, section7, section8, section9])

    print("📋 Added Board 1 with 3 pages and 9 sections.")

    # ---------------------------
    # Board 2
    # ---------------------------
    board2 = Board(title="Board Two", slug_identifier="board-two", is_published=True)
    db.session.add(board2)
    db.session.flush()

    page2_1 = Page(title="Page 1 of Board 2", board_id=board2.id, sort_order=1, is_published=True)
    page2_2 = Page(title="Page 2 of Board 2", board_id=board2.id, sort_order=2, is_published=True)
    page2_3 = Page(title="Page 3 of Board 2", board_id=board2.id, sort_order=3, is_published=True)
    db.session.add_all([page2_1, page2_2, page2_3])
    db.session.flush()

    section10 = Section(title="Section 10", page_id=page2_1.id, sort_order=1, is_published=True)
    section11 = Section(title="Section 11", page_id=page2_1.id, sort_order=2, is_published=True)
    section12 = Section(title="Section 12", page_id=page2_1.id, sort_order=3, is_published=True)
    section13 = Section(title="Section 13", page_id=page2_2.id, sort_order=1, is_published=True)
    section14 = Section(title="Section 14", page_id=page2_2.id, sort_order=2, is_published=True)
    section15 = Section(title="Section 15", page_id=page2_2.id, sort_order=3, is_published=True)
    section16 = Section(title="Section 16", page_id=page2_3.id, sort_order=1, is_published=True)
    section17 = Section(title="Section 17", page_id=page2_3.id, sort_order=2, is_published=True)
    section18 = Section(title="Section 18", page_id=page2_3.id, sort_order=3, is_published=True)
    db.session.add_all([section10, section11, section12, section13, section14, section15, section16, section17, section18])

    print("📋 Added Board 2 with 3 pages and 9 sections.")

    # ---------------------------
    # Board 3
    # ---------------------------
    board3 = Board(title="Board Three", slug_identifier="board-three", is_published=True)
    db.session.add(board3)
    db.session.flush()

    page3_1 = Page(title="Page 1 of Board 3", board_id=board3.id, sort_order=1, is_published=True)
    page3_2 = Page(title="Page 2 of Board 3", board_id=board3.id, sort_order=2, is_published=True)
    page3_3 = Page(title="Page 3 of Board 3", board_id=board3.id, sort_order=3, is_published=True)
    db.session.add_all([page3_1, page3_2, page3_3])
    db.session.flush()

    section19 = Section(title="Section 19", page_id=page3_1.id, sort_order=1, is_published=True)
    section20 = Section(title="Section 20", page_id=page3_1.id, sort_order=2, is_published=True)
    section21 = Section(title="Section 21", page_id=page3_1.id, sort_order=3, is_published=True)
    section22 = Section(title="Section 22", page_id=page3_2.id, sort_order=1, is_published=True)
    section23 = Section(title="Section 23", page_id=page3_2.id, sort_order=2, is_published=True)
    section24 = Section(title="Section 24", page_id=page3_2.id, sort_order=3, is_published=True)
    section25 = Section(title="Section 25", page_id=page3_3.id, sort_order=1, is_published=True)
    section26 = Section(title="Section 26", page_id=page3_3.id, sort_order=2, is_published=True)
    section27 = Section(title="Section 27", page_id=page3_3.id, sort_order=3, is_published=True)
    db.session.add_all([section19, section20, section21, section22, section23, section24, section25, section26, section27])

    db.session.commit()

    print("📋 Added Board 3 with 3 pages and 9 sections.")
    print("----------------------------")
    print("✅ All manual seed data inserted.")
