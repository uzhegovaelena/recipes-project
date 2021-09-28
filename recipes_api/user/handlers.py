# Registration, authentication, user information

import uuid

from aiohttp import web

from recipes_api.db.queries.user import add_new_user, check_user_email_from_db


# Registration
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
