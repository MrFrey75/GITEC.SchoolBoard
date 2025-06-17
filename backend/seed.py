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
    setting1.key = "default-background-color"
    setting1.value = "#ffffff"
    setting1.description = "Default Background Color"

    setting2 = AppSetting()
    setting2.key = "default-text-color"
    setting2.value = "#000000"
    setting2.description = "Default Text Color"

    setting3 = AppSetting()
    setting3.key = "default-font"
    setting3.value = "Arial, sans-serif"
    setting3.description = "Default Font"

    setting4 = AppSetting()
    setting4.key = "home-zipcode"
    setting4.value = "48858"
    setting4.description = "Default Home Zip Code"

    db.session.add_all([setting1, setting2, setting3, setting4])

    print("⚙️ Added app settings.")

    # ---------------------------
    # Users
    # ---------------------------
    user1 = User(username="admin", is_system_admin = True)
    user1.set_password("password")
    user2 = User(username="editor", is_system_admin = False)
    user2.set_password("password")
    user3 = User(username="viewer", is_system_admin = False)
    user3.set_password("password")

    db.session.add_all([user1, user2, user3])
    print("👤 Added 3 users.")

    # ---------------------------
    # Board 1
    # ---------------------------
    board1 = Board(title="Board One", slug_identifier="board-one", description="This is the first board.")
    db.session.add(board1)
    db.session.flush()

    page1_1 = Page(title="Page 1 of Board 1", board_id=board1.id, sort_order=1, description="This is the first page of Board 1.")
    page1_2 = Page(title="Page 2 of Board 1", board_id=board1.id, sort_order=2, description="This is the second page of Board 1.")
    page1_3 = Page(title="Page 3 of Board 1", board_id=board1.id, sort_order=3, description="This is the third page of Board 1.")
    db.session.add_all([page1_1, page1_2, page1_3])
    db.session.flush()

    section1 = Section(title="Section 1", page_id=page1_1.id, sort_order=1)
    section1.content = "<p>This is the content of Section 1.</p>"
    section2 = Section(title="Section 2", page_id=page1_1.id, sort_order=2)
    section2.content = "<p>This is the content of Section 2.</p>"
    section3 = Section(title="Section 3", page_id=page1_1.id, sort_order=3)
    section3.content = "<p>This is the content of Section 3.</p>"
    section4 = Section(title="Section 4", page_id=page1_2.id, sort_order=1)
    section4.content = "<p>This is the content of Section 4.</p>"
    section5 = Section(title="Section 5", page_id=page1_2.id, sort_order=2)
    section5.content = "<p>This is the content of Section 5.</p>"
    section6 = Section(title="Section 6", page_id=page1_2.id, sort_order=3)
    section6.content = "<p>This is the content of Section 6.</p>"
    section7 = Section(title="Section 7", page_id=page1_3.id, sort_order=1)
    section7.content = "<p>This is the content of Section 7.</p>"
    section8 = Section(title="Section 8", page_id=page1_3.id, sort_order=2)
    section8.content = "<p>This is the content of Section 8.</p>"
    section9 = Section(title="Section 9", page_id=page1_3.id, sort_order=3)
    section9.content = "<p>This is the content of Section 9.</p>"

    db.session.add_all([section1, section2, section3, section4, section5, section6, section7, section8, section9])

    print("📋 Added Board 1 with 3 pages and 9 sections.")

    # ---------------------------
    # Board 2
    # ---------------------------
    board2 = Board(title="Board Two", slug_identifier="board-two", description="This is the second board.")
    db.session.add(board2)
    db.session.flush()

    page2_1 = Page(title="Page 1 of Board 2", board_id=board2.id, sort_order=1, description="This is the first page of Board 2.")
    page2_2 = Page(title="Page 2 of Board 2", board_id=board2.id, sort_order=2, description="This is the second page of Board 2.")
    page2_3 = Page(title="Page 3 of Board 2", board_id=board2.id, sort_order=3, description="This is the third page of Board 2.")
    db.session.add_all([page2_1, page2_2, page2_3])
    db.session.flush()

    section10 = Section(title="Section 10", page_id=page2_1.id, sort_order=1)
    section11 = Section(title="Section 11", page_id=page2_1.id, sort_order=2)
    section12 = Section(title="Section 12", page_id=page2_1.id, sort_order=3)
    section13 = Section(title="Section 13", page_id=page2_2.id, sort_order=1)
    section14 = Section(title="Section 14", page_id=page2_2.id, sort_order=2)
    section15 = Section(title="Section 15", page_id=page2_2.id, sort_order=3)
    section16 = Section(title="Section 16", page_id=page2_3.id, sort_order=1)
    section17 = Section(title="Section 17", page_id=page2_3.id, sort_order=2)
    section18 = Section(title="Section 18", page_id=page2_3.id, sort_order=3)
    db.session.add_all([section10, section11, section12, section13, section14, section15, section16, section17, section18])

    print("📋 Added Board 2 with 3 pages and 9 sections.")

    # ---------------------------
    # Board 3
    # ---------------------------
    board3 = Board(title="Board Three", slug_identifier="board-three", description="This is the third board.")
    db.session.add(board3)
    db.session.flush()

    page3_1 = Page(title="Page 1 of Board 3", board_id=board3.id, sort_order=1, description="This is the first page of Board 3.")
    page3_2 = Page(title="Page 2 of Board 3", board_id=board3.id, sort_order=2, description="This is the second page of Board 3.")
    page3_3 = Page(title="Page 3 of Board 3", board_id=board3.id, sort_order=3, description="This is the third page of Board 3.")
    db.session.add_all([page3_1, page3_2, page3_3])
    db.session.flush()

    section19 = Section(title="Section 19", page_id=page3_1.id, sort_order=1)
    section20 = Section(title="Section 20", page_id=page3_1.id, sort_order=2)
    section21 = Section(title="Section 21", page_id=page3_1.id, sort_order=3)
    section22 = Section(title="Section 22", page_id=page3_2.id, sort_order=1)
    section23 = Section(title="Section 23", page_id=page3_2.id, sort_order=2)
    section24 = Section(title="Section 24", page_id=page3_2.id, sort_order=3)
    section25 = Section(title="Section 25", page_id=page3_3.id, sort_order=1)
    section26 = Section(title="Section 26", page_id=page3_3.id, sort_order=2)
    section27 = Section(title="Section 27", page_id=page3_3.id, sort_order=3)
    db.session.add_all([section19, section20, section21, section22, section23, section24, section25, section26, section27])

    db.session.commit()

    print("📋 Added Board 3 with 3 pages and 9 sections.")
    print("----------------------------")
    print("✅ All manual seed data inserted.")
