from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Int()


class UserUpdateSchema(Schema):
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()

