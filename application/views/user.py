from flask_restx import Namespace, Resource, fields
from flask import request
from application.decorators import check_token
from application.container import user_service

user_ns = Namespace('user')

headers_parser = user_ns.parser()
headers_parser.add_argument('Authorization', location='headers')
user_response = user_ns.model('UserRespomse', {
    "id": fields.Integer,
    "email": fields.String,
    "name": fields.String,
    "surname": fields.String,
    "favorite_genre": fields.Integer
})


@user_ns.route('/')
class UserView(Resource):
    @user_ns.expect(headers_parser)
    @user_ns.response(200, description='Возвращает пользователя', model=user_response)
    @check_token
    def get(self):
        return user_service.get_info(), 200

    @user_ns.expect(headers_parser)
    @user_ns.response(204, description='OK', model=None)
    @check_token
    def patch(self):
        data = request.get_json()
        user_service.update_user(data)
        return '', 204


@user_ns.route('/password/')
class UserPassword(Resource):
    @user_ns.expect(headers_parser)
    @user_ns.response(204, description='OK', model=None)
    @check_token
    def put(self):
        passwords = request.get_json()
        user_service.update_password(passwords['old_password'], passwords['new_password'])
        return '', 204

