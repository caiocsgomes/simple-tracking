from flask import Flask

from routes.v1.routes_address import routes_address
from routes.v1.routes_client import routes_client
from utils.config import Config
from utils.database import db


def create_app(config: Config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    app.register_blueprint(routes_address, url_prefix='/api')
    app.register_blueprint(routes_client, url_prefix='/api')

    db.init_app(app)
    if config.DEVELOPMENT:
        with app.app_context():
            db.create_all()
            db.session.commit()

    return app
