from flask_restx import Namespace, Resource, fields
from application.container import director_service
from application.views.parsers import page_parser

director_ns = Namespace('directors')


director_response = director_ns.model('DirectorResponse', {
    "id": fields.Integer,
    "name": fields.String
})


@director_ns.route('/')
class DirectorView(Resource):
    @director_ns.marshal_with(director_response, code=200, description='Возвращает список жанров', as_list=True)
    def get(self):
        page = page_parser.parse_args().get('page')
        return director_service.get_all(page=page)


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    @director_ns.response(200, description='Возвращает жанр', model=director_response)
    def get(self, did):
        return director_service.get_by_id(did)

