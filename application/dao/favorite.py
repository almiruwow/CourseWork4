from application.dao.base import BaseDAO
from application.dao.models.favorite import Favorite


class FavoriteDAO(BaseDAO):
    def favorite_movie(self, user_id: int, movie_id: int):
        favorite_movie = self.session.query(Favorite).filter(Favorite.user_id==user_id,
                                                             Favorite.movie_id==movie_id).first()
        return favorite_movie

    def add_movie(self, user_id: int, movie_id: int):
        fav = Favorite(user_id=user_id, movie_id=movie_id)
        self.session.add(fav)
        self.session.commit()

    def delete_movie(self, user_id: int, movie_id: int):
        favorite_movie = self.favorite_movie(user_id, movie_id)
        self.session.delete(favorite_movie)
        self.session.commit()

