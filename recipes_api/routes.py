from recipes_api.user.handlers import create_new_user


def setup_routes(app):
    app.router.add_post("/users", create_new_user)
