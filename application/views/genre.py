from flask_restx import Namespace, Resource, fields
from application.container import genre_service
from application.views.parsers import page_parser

genre_ns = Namespace('genres')

genre_response = genre_ns.model('GenreRespomse', {
    "id": fields.Integer,
    "name": fields.String
})


@genre_ns.route('/')
class GenreView(Resource):
    @genre_ns.marshal_with(genre_response, code=200, description='Возвращает список жанров', as_list=True)
    def get(self):
        page = page_parser.parse_args().get('page')
        return genre_service.get_all(page=page), 200


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    @genre_ns.response(200, description='Возвращает жанр', model=genre_response)
    def get(self, gid):
        return genre_service.get_by_id(gid), 200

