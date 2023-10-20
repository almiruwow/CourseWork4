from flask_restx import Namespace, Resource, fields
from application.container import movie_service
from application.views.parsers import page_parser

movie_ns = Namespace('movies')


movie_response = movie_ns.model("MoviesResponse",
    {
        'id': fields.Integer,
        'title': fields.String,
        'description': fields.String,
        'trailer': fields.String,
        'year': fields.Integer,
        'rating': fields.Integer,
        'genre_id': fields.Integer,
        'director_id': fields.Integer,
    })


@movie_ns.route('/')
class MovieView(Resource):
    @movie_ns.expect(page_parser)
    @movie_ns.marshal_with(movie_response, code=200, description='Возвращает список фильмов', as_list=True)
    def get(self):
        page = page_parser.parse_args().get('page')
        status = page_parser.parse_args().get('status')
        return movie_service.get_movies(page=page, status=status), 200


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):
    @movie_ns.response(200, description='Возвращает фильм', model=movie_response)
    def get(self, mid):
        return movie_service.get_movie_by_id(mid), 200

