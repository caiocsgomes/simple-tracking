from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

import utils.responses as responses
from models.model_address import AddressSchema
from repository.repository_address import AddressRepository, AbstractRepository
from utils.exceptions import NotFoundException
from utils.logger import get_logger

routes_address = Blueprint("routes_address", __name__)
repo: AbstractRepository = AddressRepository()
logger = get_logger(__name__)
schema = AddressSchema()


@routes_address.route("/v1/address", methods=["POST"])
def create_address():
    try:
        address = schema.load(request.get_json())
        result = schema.dump(repo.create(address))
        return responses.respond_with(responses.SUCCESS_200, body=result)
    except ValidationError as e:
        logger.error(f"VALIDATIONERROR-POST: {str(e)}")
        return responses.respond_with(responses.INVALID_INPUT_422, error=str(e))
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_address.route("/v1/address/<int:address_id>", methods=["GET"])
def get_address(address_id):
    try:
        address = repo.get_by_id(address_id)
        return responses.respond_with(responses.SUCCESS_200, body=schema.dump(address))
    except NotFoundException:
        logger.info(f"ADDRESSIDNOTFOUND-GET: {address_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_address.route("/v1/address/<int:address_id>", methods=["PUT"])
def update_address(address_id):
    try:
        new_address = schema.load(request.get_json(), partial=True)
        updated_address = repo.update(address_id, new_address)
        return responses.respond_with(responses.SUCCESS_200, body=schema.dump(updated_address))
    except NotFoundException:
        logger.info(f"ADDRESSIDNOTFOUND-GET: {address_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_address.route("/v1/address/<int:address_id>", methods=["DELETE"])
def delete_address(address_id):
    try:
        repo.delete(address_id)
    except NotFoundException:
        logger.info(f"ADDRESSIDNOTFOUND-GET: {address_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))
    else:
        logger.info(f"ADDRESSDELETED: {address_id}")
        return responses.respond_with(responses.SUCCESS_200)
