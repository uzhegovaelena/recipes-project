def check_user_email_from_db(email):
    if email == "test@gmail.com":
        return True
    else:
        return False


async def add_new_user(db, username, email, password, apikey):
    async with db.acquire() as connection:
        result = await connection.fetchrow(
            """
            INSERT INTO users (
                username, 
                email, 
                password,
                apikey
            )
            VALUES (
                $1,
                $2,
                $3,
                $4 
            )
            RETURNING user_id
            """,
            username,
            email,
            password,
            apikey,
        )

        user_id = result.get("user_id")

        return user_id
