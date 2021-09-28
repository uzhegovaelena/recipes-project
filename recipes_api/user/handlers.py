# Registration, authentication, user information

import uuid

from aiohttp import web

from recipes_api.db.queries.user import add_new_user
from recipes_api.db.queries.user import check_user_email_from_db
from recipes_api.db.queries.user import get_apikey
from recipes_api.db.queries.user import select_top_users
from recipes_api.db.queries.user import select_user_info
# Registration
from recipes_api.decorators import check_auth


async def create_new_user(request):
    response = {}
    message = ""

    db = request.app["db"]
    data = await request.json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    apikey = str(uuid.uuid4())  # generate unique apikey

    is_user_exist = check_user_email_from_db(email)

    if is_user_exist:
        message = f"Sorry, but User with email {email} is exist. Please, try with another email."
    else:
        user_id = await add_new_user(db, username, email, password, apikey)

        message = f"New User with email {email} is created"

    response["user_id"] = user_id
    response["message"] = message
    response["apikey"] = apikey

    return web.json_response(response)


# Authentication
async def auth(request):
    response = {}

    db = request.app["db"]
    data = await request.json()

    email = data.get("email")
    password = data.get("password")

    apikey = await get_apikey(db, email, password)

    if apikey:
        response["apikey"] = apikey
    else:
        message = f"Sorry something is wrong"

        response["message"] = message

    return web.json_response(response)


# Getting user profile
@check_auth
async def get_user_info(request):
    response = {}

    db = request.app["db"]

    username = request.match_info["username"]


    user_info = await select_user_info(db, username)

    if user_info is None:
        message = f"Sorry, user with username {username} not found."

        response["message"] = message

        return web.json_response(response)

    response["profile"] = user_info

    return web.json_response(response)


# Getting top 10 users
@check_auth
async def get_top_users(request):
    response = {}

    db = request.app["db"]

    top_users = await select_top_users(db)

    if top_users is None:
        message = f"Sorry, users not found."

        response["message"] = message

        return web.json_response(response)

    response["top_users"] = top_users

    return web.json_response(response)
