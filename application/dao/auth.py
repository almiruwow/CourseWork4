import sqlite3
from flask import abort
from application.dao.base import BaseDAO
from application.dao.models.user import User
from application.dao.serialization.auth import UserSchema
from application.service.exceptions import WrongToken

class AuthDAO(BaseDAO):
    def get_by_email(self, email: str):
        user = self.session.query(User).filter(
            User.email==email
        ).one_or_none()

        if user is not None:
            return UserSchema().dump(user)

        return None

    def create(self, email: str, password: str) -> UserSchema:
        try:
            new_user = User(
                email=email,
                password_hash=password
           )
            print('+')
            self.session.add(new_user)
            self.session.commit()

            return UserSchema().dump(new_user)
        except Exception:
            return abort(409)




