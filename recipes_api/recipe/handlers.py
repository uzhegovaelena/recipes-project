from aiohttp import web

from recipes_api.db.queries.recipe import add_recipe, select_recipe
from recipes_api.db.queries.recipe import select_recipes
from recipes_api.db.queries.user import select_username_by_apikey
from recipes_api.decorators import check_auth


@check_auth
async def create_recipe(request):
    response = {}
    message = ""

    db = request.app["db"]

    apikey = request.headers.get("apikey")

    body = await request.json()

    title = body.get("title")
    description = body.get("description")

    username = await select_username_by_apikey(db, apikey)

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


@check_auth
async def get_recipes(request):
    response = {}

    db = request.app["db"]

    limit = int(request.query.get("limit", 10))
    offset = int(request.query.get("offset", 10))

    recipes = await select_recipes(db=db, limit=limit, offset=offset)

    if recipes is None:
        message = f"Sorry, recipes not found."

        response["message"] = message

        return web.json_response(response)

    response["recipes"] = recipes

    return web.json_response(response)


@check_auth
async def get_recipe_info(request):
    response = {}

    db = request.app["db"]

    recipe_id = int(request.match_info["recipe_id"])

    recipe = await select_recipe(db=db, recipe_id=recipe_id)

    if recipe is None:
        message = f"Sorry, recipe not found."

        response["message"] = message

        return web.json_response(response)

    response["recipe"] = recipe

    return web.json_response(response)
