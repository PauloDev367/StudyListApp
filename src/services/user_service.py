from src.models.user import User
from src.data.db_context import db
from flask import session


class UserService:
    @staticmethod
    def create_user(username, email, password):
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email, password=password).first()
        session['user_id'] = user.id if user else None
        return user