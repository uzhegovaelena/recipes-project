import asyncio
import asyncpg
from aiohttp import web

from recipes_api.routes import setup_routes


async def create_app():
    app = web.Application()

    app["db"] = await asyncpg.create_pool(
        database="recipes",
        user="postgres",
        password="Ghysolk89h&",
        host="localhost",
        port=5432,
    )

    setup_routes(app)

    return app
