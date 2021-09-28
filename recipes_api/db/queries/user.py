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


# Getting the apikey for authentication
async def get_apikey(db, email, password):
    apikey = None

    async with db.acquire() as connection:
        user_info = await connection.fetchrow(
            """
            SELECT * 
            FROM users 
            WHERE email = $1 AND password = $2
            """,
            email,
            password,
        )

        if user_info:
            apikey = user_info.get("apikey")

        return apikey


# Checking the apikey in the DB
async def check_user_apikey(db, apikey):
    async with db.acquire() as connection:
        user_info = await connection.fetchrow(
            """
            SELECT *
            FROM users
            WHERE apikey = $1
            """,
            apikey,
        )

        return bool(user_info)


# Get information about users from the DB
async def select_user_info(db, username):
    user_info = None

    async with db.acquire() as connection:
        user_info = await connection.fetchrow(
            """
            SELECT user_id, username, status
            FROM users
            WHERE username = $1
            """,
            username,
        )

        return dict(user_info)


# Get information about top 10 users from the DB
async def select_top_users(db):
    result = []

    async with db.acquire() as connection:
        users = await connection.fetch(
            """
            SELECT user_id, users.username, users.status, count(title) AS number_of_recipes
            FROM users
                JOIN recipes
                    ON users.username=recipes.username
                WHERE users.status = 'active' AND recipes.status='active'
                GROUP BY user_id
                ORDER BY number_of_recipes DESC
                LIMIT 10
            """,
            record_class=None,
        )

        for user in users:
            result.append(dict(user))

        return result
