# Adding recipe
async def add_recipe(db, username, title, description):
    async with db.acquire() as connection:
        result = await connection.fetchrow(
            """
            INSERT INTO recipes (
                username,
                title, 
                description
            )
            VALUES (
                $1,
                $2,
                $3 
            )
            RETURNING recipe_id
            """,
            username,
            title,
            description,
        )

        recipe_id = result.get("recipe_id")

        return recipe_id


# Get information about all recipes
async def select_recipes(db, username, limit=10, offset=10):
    result = []

    async with db.acquire() as connection:
        recipes = await connection.fetch(
            """
            SELECT username, title, description, status
            FROM recipes
            WHERE status='active' and username=$3
            ORDER BY created_at DESC
            LIMIT $1
            OFFSET $2
            """,
            limit,
            offset,
            username
        )

        for recipe in recipes:
            result.append(dict(recipe))

        return result

# Get information about recipe
async def select_recipe(db, recipe_id):
    recipe = None

    async with db.acquire() as connection:
        recipe = await connection.fetchrow(
            """
            SELECT recipe_id, recipes.username, title, description, recipes.status, user_id, users.status
            FROM recipes
                JOIN users
                    ON recipes.username=users.username
                    WHERE recipe_id = $1 
                    ORDER BY created_at DESC
            """,
            recipe_id
        )

        return dict(recipe)
