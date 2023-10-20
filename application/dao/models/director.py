from application.dao.models.base import Base
from application.db import db


class Director(Base):
    __tablename__ = 'directors'

    name = db.Column(db.String(100), unique=True, nullable=False)
