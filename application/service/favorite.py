from application.service.base import BaseService
from application.dao.favorite import FavoriteDAO
from application.dao.models.favorite import Favorite
from application.dao.serialization.favorite import FavoritesSchema
from application.service.exceptions import WrongToken
from flask import request, current_app
import jwt


class FavoriteService(BaseService[FavoriteDAO]):
    def get_all(self):
        return FavoritesSchema(many=True).dump(self.dao.get_all(Favorite))

    def add_movie(self, movie_id):
        data_token = self.__decode_token()
        user_id = data_token['id']

        self.dao.add_movie(user_id, movie_id)

    def delete_movie(self, movie_id):
        data_token = self.__decode_token()
        user_id = data_token['id']
        self.dao.delete_movie(user_id, movie_id)

    @staticmethod
    def __decode_token():
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            res = jwt.decode(jwt=token, key=current_app.config['SECRET_KEY'],
                             algorithms=[current_app.config['JWT_ALGO']])
        except Exception:
            raise WrongToken

        return res
