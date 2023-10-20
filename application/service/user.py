import base64

from application.service.base import BaseService
from application.dao.user import UserDAO
from application.dao.serialization.user import UserSchema
from application.service.exceptions import UserNotFound
from flask import request, current_app, abort
from base64 import b64encode
from application.service.exceptions import WrongToken
import hmac
import hashlib
import jwt


class UserService(BaseService[UserDAO]):
    def get_info(self):
        token_data = self.__decode_token()
        user_id = token_data['id']
        user = self.dao.get_info(user_id=user_id)

        if user is None:
            raise UserNotFound

        return UserSchema().dump(user)

    def update_user(self, data_update):
        token_data = self.__decode_token()
        user_id = token_data['id']

        self.dao.update_user(data_update=data_update, user_id=user_id)

    def update_password(self, old_password: str, new_password: str):
        token_data = self.__decode_token()
        user_id = token_data['id']
        user_pass = self.dao.get_info(user_id).password_hash

        if not self.__compare_passwords(
            password1=self.__get_hash(old_password),
            password2=user_pass
        ):
            abort(401)

        self.dao.update_password(user_id, self.__get_hash(new_password))


    @staticmethod
    def __decode_token():
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            res = jwt.decode(jwt=token, key=current_app.config['SECRET_KEY'], algorithms=[current_app.config['JWT_ALGO']])
        except Exception:
            raise WrongToken

        return res

    @staticmethod
    def __compare_passwords(password1, password2):
        return hmac.compare_digest(password1, password2)

    @staticmethod
    def __get_hash(password: str) -> str:
        password_hash = hashlib.pbkdf2_hmac(
            hash_name=current_app.config['HASH_NAME'],
            password=password.encode('utf-8'),
            salt=current_app.config['HASH_SALT'],
            iterations=current_app.config['HASH_ITERATION']
        )

        return b64encode(password_hash).decode('utf-8')
