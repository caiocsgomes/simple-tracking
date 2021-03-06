from flask import Flask

from routes.v1.routes_address import routes_address
from routes.v1.routes_client import routes_client
from routes.v1.routes_company import routes_company
from utils.config import Config
from utils.database import db


def create_app(config: Config) -> str:
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    app.register_blueprint(routes_address, url_prefix='/api')
    app.register_blueprint(routes_client, url_prefix='/api')
    app.register_blueprint(routes_company, url_prefix='/api')
    app.app_context()
    db.init_app(app)

    return app
