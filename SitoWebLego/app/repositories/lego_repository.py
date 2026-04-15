from app.db import get_db

def get_all_lego():
    db = get_db()
    return db.execute("SELECT * FROM lego").fetchall()

def add_lego(name, description, image):
    db = get_db()
    db.execute(
        "INSERT INTO lego (name, description, image) VALUES (?, ?, ?)",
        (name, description, image)
    )
    db.commit()