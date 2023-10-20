from application.dao.serialization.auth import UserSchema
from application.service.base import BaseService
from application.dao.auth import AuthDAO
import hashlib
from flask import current_app, abort
import base64
from application.service.exceptions import UserNotFound, WrongPassword, WrongToken
import hmac
from datetime import datetime, timedelta
import jwt


class ServiceAuth(BaseService[AuthDAO]):
    @staticmethod
    def __get_hash(password: str) -> str:
        password_hash = hashlib.pbkdf2_hmac(
            hash_name=current_app.config['HASH_NAME'],
            password=password.encode('utf-8'),
            salt=current_app.config['HASH_SALT'],
            iterations=current_app.config['HASH_ITERATION']
        )

        return base64.b64encode(password_hash).decode('utf-8')

    @staticmethod
    def __compare_password(password1: str, password2: str):
        return hmac.compare_digest(password1, password2)

    @staticmethod
    def __generate_tokens(user: UserSchema):

        payload = {
            'email': user['email'],
            'id': user['id'],
            'exp': datetime.utcnow() + timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
        }

        access_token = jwt.encode(
            payload=payload,
            key=current_app.config['SECRET_KEY'],
            algorithm=current_app.config['JWT_ALGO']
        )

        payload['exp'] = datetime.utcnow() + timedelta(minutes=current_app.config['TOKEN_EXPIRE_DAYS'])

        refresh_token = jwt.encode(
            payload=payload,
            key=current_app.config['SECRET_KEY'],
            algorithm=current_app.config['JWT_ALGO']
        )

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

    def register_user(self, email: str, password: str):

        password_hash = self.__get_hash(password=password)
        return self.dao.create(email=email, password=password_hash)

    def login(self, email, password):
        user = self.dao.get_by_email(email=email)

        if user is None:
            raise UserNotFound

        password_hash = self.__get_hash(password)

        if not self.__compare_password(user['password_hash'], password_hash):
            raise WrongPassword

        return self.__generate_tokens(user)

    def update_token(self, access, refresh):
        try:
            data = jwt.decode(
                jwt=refresh,
                key=current_app.config['SECRET_KEY'],
                algorithms=[current_app.config['JWT_ALGO']]
            )
        except Exception:
            return abort(400)

        user = self.dao.get_by_email(email=data.get('email'))

        if user is None:
            raise UserNotFound

        return self.__generate_tokens(user)




