from functools import wraps

from aiohttp import web

from recipes_api.db.queries.user import check_user_apikey


def check_auth(func):
    @wraps(func)
    async def wrapper(request):
        response = {}

        db = request.app["db"]
        apikey = request.headers.get("apikey")


        if apikey is None:
            message = "Sorry, apikey not found."

            response["message"] = message

            return web.json_response(response, status=401)

        is_valid_apikey = await check_user_apikey(db, apikey)

        if not is_valid_apikey:
            message = "Sorry, user with apikey not found."

            response["message"] = message

            return web.json_response(response, status=401)

        return await func(request)

    return wrapper
