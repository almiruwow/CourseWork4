from application.dao.auth import AuthDAO
from application.dao.director import DirectorDAO
from application.dao.favorite import FavoriteDAO
from application.dao.genre import GenreDAO
from application.dao.movie import MovieDAO
from application.dao.user import UserDAO
from application.db import db
from application.service.auth import ServiceAuth
from application.service.director import DirectorService
from application.service.favorite import FavoriteService
from application.service.genre import GenreService
from application.service.movie import MovieService
from application.service.user import UserService

auth_dao = AuthDAO(session=db.session)
auth_service = ServiceAuth(dao=auth_dao)

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(dao=director_dao)

user_dao = UserDAO(session=db.session)
user_service = UserService(user_dao)

favorite_dao = FavoriteDAO(session=db.session)
favorite_service = FavoriteService(dao=favorite_dao)
