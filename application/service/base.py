from application.dao.auth import BaseDAO
from typing import TypeVar, Generic

T = TypeVar('T', bound=BaseDAO)


class BaseService(Generic[T]):
    def __init__(self, dao: T, *args, **kwargs):
        self.dao = dao
