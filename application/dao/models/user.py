from application.dao.models.base import Base
from application.db import db
from application.dao.models.genre import Genre


class User(Base):
    __tablename__ = 'users'

    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.Integer)
    favorite_genre = db.Column(db.Integer, db.ForeignKey(Genre.id))

