from flask import Flask
from app.utils.database import db
from app.routes.v1.routes_address import routes_address
import logging


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.config.from_object(config)
    app.register_blueprint(routes_address, url_prefix='/api')

    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()

    return app
