from recipes_api.user.handlers import auth, create_new_user


def setup_routes(app):
    app.router.add_get("/users/auth", auth)
    app.router.add_post("/users", create_new_user)
