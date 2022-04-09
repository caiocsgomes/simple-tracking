from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

import utils.responses as responses
from models.model_address import AddressSchema, Address
from repository.repository_address import AddressRepository, AbstractRepository
from utils.logger import get_logger

routes_address = Blueprint("routes_address", __name__)
repo: AbstractRepository = AddressRepository()
logger = get_logger(__name__)
schema = AddressSchema()


@routes_address.route("/v1/address", methods=["POST"])
def create_address():
    try:
        data = request.get_json()
        address = schema.load(data)
        result = schema.dump(repo.create(address))
        return responses.respond_with(responses.SUCCESS_200, body=result)
    except ValidationError as e:
        error = str(e)
        logger.error(f"VALIDATIONERROR-POST: {error}")
        return responses.respond_with(responses.INVALID_INPUT_422, error=error)
    except Exception as e:
        error = str(e)
        logger.error(f"{type(e).__name__}: {error}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=error)


@routes_address.route("/v1/address/<int:address_id>", methods=["GET"])
def get_address(address_id):
    try:
        address = repo.get_by_id(address_id)
        if address is None:
            logger.info(f"ADDRESSIDNOTFOUND-GET: {address_id}")
            return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
        result = schema.dump(address)
        return responses.respond_with(responses.SUCCESS_200, body=result)
    except Exception as e:
        error = str(e)
        logger.error(f"{type(e).__name__}: {error}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=error)


@routes_address.route("/v1/address/<int:address_id>", methods=["PUT"])
def update_address(address_id):
    try:
        address = Address.get_by_id(address_id)
        if address is None:
            logger.info(f"USERIDNOTFOUND-GET: {address_id}")
            return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
        data = request.get_json()
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
