from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)


class AuthRegisterReqSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class TokensSchema(Schema):
    access_token = fields.Str(required=True)
    refresh_token = fields.Str(required=True)
