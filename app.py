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


def run_app(port):
    loop = asyncio.get_event_loop()

    app = loop.run_until_complete(create_app())

    web.run_app(app, port=port)

    try:
        web.run_app(app)
    except:
        print("Something went wrong.")


if __name__ == "__main__":
    run_app(port=8080)
