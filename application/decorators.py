from flask import request, abort, current_app
import jwt
from application.container import user_service


def check_token(func):
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            return abort(401)

        data = request.headers['Authorization']

        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(jwt=token, key=current_app.config['SECRET_KEY'], algorithms=[current_app.config['JWT_ALGO']])
        except Exception:
            abort(400)

        return func(*args, **kwargs)

    return wrapper



