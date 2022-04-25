from flask import Blueprint, request
from marshmallow.exceptions import ValidationError

from src import utils as responses
from src.models.model_company import CompanySchema, Company
from src.repository.repository_base import AbstractRepository
from src.repository.repository_default import DefaultRepository
from src.utils.exceptions import NotFoundException
from src.utils.logger import get_logger

routes_company = Blueprint('routes_company', __name__)
logger = get_logger(__name__)
schema = CompanySchema()
repo: AbstractRepository = DefaultRepository(Company)


@routes_company.route("/v1/company", methods=['POST'])
def create_company():
    try:
        company = schema.load(request.get_json())
        result = schema.dump(repo.create(company))
        return responses.respond_with(responses.SUCCESS_200, body=result)
    except ValidationError as e:
        logger.error(f"VALIDATIONERROR-POST: {str(e)}")
        return responses.respond_with(responses.INVALID_INPUT_422, error=str(e))
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_company.route("/v1/company/<int:company_id>", methods=['GET'])
def get_company(company_id: int):
    try:
        company = repo.get_by_id(company_id)
        return responses.respond_with(responses.SUCCESS_200, body=schema.dump(company))
    except NotFoundException:
        logger.info(f"COMPANYIDNOTFOUND-GET: {company_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_company.route("/v1/company/<int:company_id>", methods=['PUT'])
def update_client(company_id: int):
    try:
        new_company = schema.load(request.get_json(), partial=True)
        updated_company = repo.update(company_id, new_company)
        return responses.respond_with(responses.SUCCESS_200, body=schema.dump(updated_company))
    except NotFoundException:
        logger.info(f"COMPANYIDNOTFOUND-GET: {company_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))


@routes_company.route("/v1/company/<int:company_id>", methods=['DELETE'])
def delete_company(company_id: int):
    try:
        repo.delete(company_id)
    except NotFoundException:
        logger.info(f"COMPANYIDNOTFOUND-GET: {company_id}")
        return responses.respond_with(responses.ENTITY_NOT_FOUND_404)
    except Exception as e:
        logger.error(f"{type(e).__name__}: {str(e)}")
        return responses.respond_with(responses.SERVER_ERROR_500, error=str(e))
    else:
        logger.info(f"COMPANYDELETED: {company_id}")
        return responses.respond_with(responses.SUCCESS_200)
