from flask import Blueprint, request
from models.model_address import AddressSchema, Address

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


@routes_address.route("/v1/address/<int:address_id>", methods=["GET"])
def get_address(address_id):
    try:
        address = Address.get(address_id)
        result = AddressSchema().dump(address)
        return result, 200
    except Exception as e:
        print(e)


@routes_address.route("/v1/address/<int:address_id>", methods=["PUT"])
def update_address(address_id):
    try:
        data = request.get_json()
        address = Address.get(address_id)
        address_schema = AddressSchema()
        address = address_schema.load(data, instance=address, partial=True)
        result = address_schema.dump(address.update())
        return result, 200
    except Exception as e:
        print(e)


@routes_address.route("/v1/address/<int:address_id>", methods=["DELETE"])
def delete_address(address_id):
    try:
        address = Address.get(address_id)
        result = AddressSchema().dump(address.delete())
        return result, 200
    except Exception as e:
        print(e)
