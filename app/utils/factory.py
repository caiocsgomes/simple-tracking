from flask import Flask
from app.utils.database import db
from app.routes.v1.routes_address import routes_address

def create_app(config):
    app = Flask(config)

    app.config.from_object(config)

    app.register_blueprint(routes_address)

    db.init_app(app)
    
    return app