from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from src import utils as responses
from src.models.model_client import Client
from src.models.model_client import ClientSchema
from src.repository.repository_default import DefaultRepository, AbstractRepository
from src.utils.exceptions import NotFoundException
from src.utils.logger import get_logger

routes_client = Blueprint("routes_client", __name__)
logger = get_logger(__name__)
schema = ClientSchema()
repo: AbstractRepository = DefaultRepository(Client)


@routes_client.route("/v1/client", methods=['POST'])
def create_client():
    try:
        client = schema.load(request.get_json())
        result = schema.dump(repo.create(client))
        return responses.respond_with(responses.SUCCESS_200, body=result)
    except ValidationError as e:
        logger.error(f"VALIDATIONERROR-POST: {str(e)}")
        return responses.respond_with(responses.INVALID_INPUT_422, error=str(e))
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_client.route("/v1/client/<int:client_id>", methods=['GET'])
def get_client(client_id: int):
    try:
        client = repo.get_by_id(client_id)
        return responses.respond_with(responses.SUCCESS_200, body=schema.dump(client))
    except NotFoundException:
        logger.info(f"CLIENTIDNOTFOUND-GET: {client_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_client.route("/v1/client/<int:client_id>", methods=['PUT'])
def update_client(client_id: int):
    try:
        new_client = schema.load(request.get_json(), partial=True)
        updated_client = repo.update(client_id, new_client)
        return responses.respond_with(responses.SUCCESS_200, body=schema.dump(updated_client))
    except NotFoundException:
        logger.info(f"CLIENTIDNOTFOUND-GET: {client_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_client.route("/v1/client/<int:client_id>", methods=['DELETE'])
def delete_client(client_id: int):
    try:
        repo.delete(client_id)
    except NotFoundException:
        logger.info(f"CLIENTIDNOTFOUND-GET: {client_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))
    else:
        logger.info(f"CLIENTDELETED: {client_id}")
        return responses.respond_with(responses.SUCCESS_200)
