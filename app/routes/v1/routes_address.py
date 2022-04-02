from crypt import methods
from flask import Blueprint

routes_address = Blueprint("routes_address", __name__)

@routes_address("/v10/address", methods="POST")
def create_address():
    pass