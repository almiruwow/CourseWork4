from application.dao.director import DirectorDAO
from application.service.base import BaseService
from application.dao.models.director import Director
from application.dao.serialization.director import DirectorSchema


class DirectorService(BaseService[DirectorDAO]):
    def get_by_id(self, did):
        return DirectorSchema().dump(self.dao.get_by_id(Director, did))

    def get_all(self, page):
        return DirectorSchema(many=True).dump(self.dao.get_all(Director, page=page))

