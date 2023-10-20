from application.dao.movie import MovieDAO
from application.service.base import BaseService
from application.dao.serialization.movie import MovieSchema
from application.dao.models.movie import Movie


class MovieService(BaseService[MovieDAO]):
    def get_movie_by_id(self, mid: int) -> MovieSchema:
        return MovieSchema().dump(self.dao.get_by_id(Movie,mid))

    def get_movies(self, page, status) -> MovieSchema:
        return MovieSchema(many=True).dump(self.dao.get_all(Movie, page=page, status=status))
