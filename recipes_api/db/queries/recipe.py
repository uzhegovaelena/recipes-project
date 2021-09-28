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
async def select_recipes(db, limit=10, offset=10):
    result = []

    async with db.acquire() as connection:
        recipes = await connection.fetch(
            """
            SELECT username, title, description, status
            FROM recipes
            WHERE status='active'
            ORDER BY created_at DESC
            LIMIT $1
            OFFSET $2
            """,
            limit,
            offset
        )

        for recipe in recipes:
            result.append(dict(recipe))

        return result
