from flask import make_response

ENTITY_NOT_FOUND_404 = {
    "http_code": 404,
    "message": "Entity not found",
    "code": "NotFound"
}

INVALID_INPUT_422 = {
    "http_code": 422,
    "code": "invalidInput",
    "message": "Invalid input"
}

MISSING_PARAMETERS_422 = {
    "http_code": 422,
    "code": "missingParameter",
    "message": "Missing parameters."
}

BAD_REQUEST_400 = {
    "http_code": 400,
    "code": "badRequest",
    "message": "Bad request"
}

SERVER_ERROR_500 = {
    "http_code": 500,
    "code": "serverError",
    "message": "Server error"
}

SERVER_ERROR_404 = {
    "http_code": 404,
    "code": "notFound",
    "message": "Resource not found"
}

UNAUTHORIZED_403 = {
    "http_code": 403,
    "code": "notAuthorized",
    "message": "You are not allowed to do that."
}

NOT_FOUND_HANDLER_404 = {
    "http_code": 404,
    "code": "notFound",
    "message": "There are no such handler"
}

SUCCESS_200 = {
    'http_code': 200,
    'code': 'success',
    'message': 'success'
}


def respond_with(response, body=None, error=None, headers={}):
    result = {}
    if body is None:
        result.update({"message": response["message"]})
        result.update({"code": response["code"]})
    else:
        result.update(body)

    if error is not None:
        result.update({"error": error})

    headers.update({"Access-Control-Allow-Origin": '*'})
    headers.update({"server": 'simple-tracking api'})

    return make_response(result, response["http_code"], headers)
