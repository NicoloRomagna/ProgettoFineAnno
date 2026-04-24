from app.models import User
from app import db
from werkzeug.security import generate_password_hash

class UserRepository:

    def create_user(self, username, password):
        user = User(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return user

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_by_id(self, user_id):
        return User.query.get(user_id)