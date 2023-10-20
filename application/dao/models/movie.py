from application.dao.models.base import Base
from application.db import db
from application.dao.models.genre import Genre
from application.dao.models.director import Director


class Movie(Base):
    __tablename__ = 'movies'

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey(Genre.id), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey(Director.id), nullable=False)
