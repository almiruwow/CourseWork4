from sqlalchemy.orm import Session
from application.dao.models.base import Base
from application.dao.models.movie import Movie
from typing import Generic, TypeVar
from sqlalchemy import desc

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, model, pk):
        return self.session.query(model).get(pk)

    def get_all(self, model, page=None, status=None):
        if status:
            data = self.session.query(model).order_by(desc(model.year))
        else:
            data = self.session.query(model)

        if page:
            mov = data.paginate(per_page=3)
            return mov.items

        return data.all()






