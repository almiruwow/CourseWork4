from flask import Flask, render_template
from flask_restx import Api
from application.views.auth import auth_ns
from application.views.director import director_ns
from application.views.favorites import favorites_ns
from application.views.genre import genre_ns
from application.views.movie import movie_ns
from application.db import db
from application.views.user import user_ns
from application.dao.models.favorite import Favorite

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    @app.route('/')
    def views_index():
        return render_template('index.html')

    api = Api(
        authorizations={
            'Bearer': {'type': 'apiKey', 'in': 'header', 'name': 'Authorization'}
        },
        doc='/docs'

    )
    api.init_app(app)
    api.add_namespace(auth_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favorites_ns)
    db.init_app(app)

    # with app.app_context():
    #     db.create_all()
    #     fav = Favorite(user_id=1, movie_id=1)
    #     db.session.add(fav)
    #     db.session.commit()


    return app

