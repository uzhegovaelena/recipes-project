from recipes_api.recipe.handlers import create_recipe
from recipes_api.user.handlers import (auth, create_new_user, get_top_users,
                                       get_user_info)


def setup_routes(app):
    app.router.add_get("/users/auth", auth)
    app.router.add_get("/users/top", get_top_users)
    app.router.add_get("/users/{username}", get_user_info)
    app.router.add_post("/users", create_new_user)

    app.router.add_post("/recipe", create_recipe)
