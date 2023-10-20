from application.dao.genre import GenreDAO
from application.service.base import BaseService
from application.dao.models.genre import Genre
from application.dao.serialization.genre import GenreSchema


class GenreService(BaseService[GenreDAO]):
    def get_by_id(self, gid):
        return GenreSchema().dump(self.dao.get_by_id(Genre, gid))

    def get_all(self, page):
        return GenreSchema(many=True).dump(self.dao.get_all(Genre, page=page))

