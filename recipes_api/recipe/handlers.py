from aiohttp import web

from recipes_api.db.queries.recipe import add_recipe
from recipes_api.db.queries.user import check_user_apikey


async def create_recipe(request):
    response = {}
    message = ""

    db = request.app["db"]
    data = await request.json()

    apikey = request.headers.get("apikey")

    # TODO: check if apikey is exist in headers
    #  if apikey param is not exist return 401 with message about required apikey
    if apikey is None:
        message = "Sorry, apikey not found."

        response["message"] = message

        return web.json_response(response, status=401)

    is_valid_apikey = await check_user_apikey(db, apikey)

    # TODO: check if apikey is exist in DB
    if not is_valid_apikey:
        message = "Sorry, user with apikey not found."

        response["message"] = message

        return web.json_response(response, status=401)

    username = data.get("username")
    title = data.get("title")
    description = data.get("description")

    recipe_id = await add_recipe(db, username, title, description)

    if recipe_id is None:
        message = f"Sorry, recipe not add."

        response["message"] = message

        return web.json_response(response)

    response["recipe_id"] = recipe_id
    response["username"] = username
    response["title"] = title
    response["description"] = description

    return web.json_response(response)
