from app.db import get_db

def create_user(username, password):
    db = get_db()
    db.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)",
        (username, password)
    )
    db.commit()

def get_user(username):
    db = get_db()
    return db.execute(
        "SELECT * FROM user WHERE username = ?",
        (username,)
    ).fetchone()