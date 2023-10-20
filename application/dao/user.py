from application.dao.base import BaseDAO
from application.dao.models.user import User
from application.dao.serialization.user import UserUpdateSchema
import json


class UserDAO(BaseDAO):
    def get_info(self, user_id: int):
        return self.session.query(User).filter(User.id==user_id).first()

    def update_user(self, data_update: dict, user_id: int):
        user = self.get_info(user_id)

        if 'name' in data_update:
            user.name = data_update.get('name')

        if 'surname' in data_update:
            user.surname = data_update.get('surname')

        if 'favourite_genre' in data_update:
            user.favorite_genre = int(data_update.get('favourite_genre'))

        self.session.add(user)
        self.session.commit()

    def update_password(self, user_id: int, new_hash: str):
        user = self.get_info(user_id)

        user.password_hash = new_hash

        self.session.add(user)
        self.session.commit()


