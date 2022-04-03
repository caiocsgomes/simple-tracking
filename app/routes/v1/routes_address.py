from flask import Blueprint, request
from app.models.model_address import AddressSchema
routes_address = Blueprint("routes_address", __name__)


@routes_address.route("/v1/address", methods=["POST"])
def create_address():
    try:
        data = request.get_json()
        address_schema = AddressSchema()
        address = address_schema.load(data)
        result = address_schema.dump(address.create())
        return result, 200
    except Exception as e:
        print(e)
