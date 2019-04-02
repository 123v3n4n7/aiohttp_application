from aiohttp import web
from .routes import setup_routes
import aiohttp_jinja2
import jinja2
import asyncpgsa


async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    setup_routes(app)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    config = app['config']#['database_uri']
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])

    # app['db'] = await asyncpgsa.create_pool(
    #     host=config['host'],
    #     port=config['port'],
    #     database=config['database'],
    #     user=config['user'],
    #     password=config['password'],
    #     #min_size=config['min_size'],
    #     #max_size=config['max_size']
    # )


async def on_shutdown(app):
    await app['db'].close()
