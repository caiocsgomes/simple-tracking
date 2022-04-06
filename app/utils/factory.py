from flask import Flask
from utils.database import db
from routes.v1.routes_address import routes_address


def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)

    app.register_blueprint(routes_address, url_prefix='/api')

    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()

    return app
