from flask_restx import Namespace, Resource, fields
from flask import request, abort
from application.container import auth_service
from application.dao.serialization.auth import AuthRegisterReqSchema, TokensSchema

auth_ns = Namespace('auth')

register_doc = auth_ns.model('Register', {
    'email': fields.String,
    'password': fields.String
})

token = auth_ns.model("Login", {
    'access_token': fields.String,
    'refresh_token': fields.String
})


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    @auth_ns.expect(register_doc)
    @auth_ns.response(201, description='OK')
    @auth_ns.response(400, description='Такой пользователь существует в базе данных')
    def post(self):
        data = request.get_json()
        validated_data = AuthRegisterReqSchema().load(data)

        auth_service.register_user(
            email=validated_data['email'],
            password=validated_data['password']
        ),
        return '', 201


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    @auth_ns.expect(register_doc)
    @auth_ns.response(200, description='OK', model=token)
    def post(self):
        data = request.get_json()

        validate_data = AuthRegisterReqSchema().load(data)

        tokens = auth_service.login(
            validate_data['email'],
            validate_data['password']
        )

        return tokens, 201

    @auth_ns.expect(token)
    @auth_ns.response(200, description='OK', model=token)
    @auth_ns.response(400, description='Bad request')
    def put(self):
        data = request.get_json()

        if 'refresh_token' not in data:
            return abort(400)

        validate_data = TokensSchema().load(data)

        tokens = auth_service.update_token(
            access=validate_data['access_token'],
            refresh=validate_data['refresh_token']
        )

        return tokens, 200
