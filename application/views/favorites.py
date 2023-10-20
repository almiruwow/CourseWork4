from flask_restx import Namespace, Resource, fields
from application.container import favorite_service

favorites_ns = Namespace('favorites')

favorites_response = favorites_ns.model('FavoriteResponse', {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "movie_id": fields.Integer
    })


@favorites_ns.route('/movies/')
class FavoriteMovie(Resource):
    @favorites_ns.marshal_with(favorites_response, code=200, description='OK', as_list=True)
    def get(self):
        return favorite_service.get_all(), 200


@favorites_ns.route('/movies/<int:movie_id>')
class FavoritesMovie(Resource):
    @favorites_ns.response(201, description='OK', model=None)
    def post(self, movie_id):
        favorite_service.add_movie(movie_id)
        return '', 201

    @favorites_ns.response(204, description='OK', model=None)
    def delete(self, movie_id):
        favorite_service.delete_movie(movie_id)
        return '', 204

