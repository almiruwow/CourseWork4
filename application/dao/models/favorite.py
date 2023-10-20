from application.dao.models.base import Base
from application.dao.models.user import User
from application.dao.models.movie import Movie
from application.db import db


class Favorite(Base):
    __tablename__ = 'favorites'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id))

