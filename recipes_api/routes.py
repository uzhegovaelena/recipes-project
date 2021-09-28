from recipes_api.recipe.handlers import create_recipe
from recipes_api.recipe.handlers import get_recipes
from recipes_api.user.handlers import auth
from recipes_api.user.handlers import create_new_user
from recipes_api.user.handlers import get_top_users
from recipes_api.user.handlers import get_user_info


def setup_routes(app):
    # User routes
    app.router.add_post("/users", create_new_user)
    app.router.add_get("/users/auth", auth)
    app.router.add_get("/users/top", get_top_users)
    app.router.add_get("/users/{username}", get_user_info)

    # Recipe routes
    app.router.add_post("/recipes", create_recipe)
    app.router.add_get("/recipes", get_recipes)
