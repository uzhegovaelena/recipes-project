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
