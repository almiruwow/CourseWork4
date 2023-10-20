from application.dao.models.base import Base
from application.db import db


class Genre(Base):
    __tablename__ = 'genres'

    name = db.Column(db.String(100), unique=True, nullable=False)
