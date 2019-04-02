import uvloop
import asyncio
import argparse
from demo import create_app
from aiohttp import web
import aioreloader
from demo.settings import load_config

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


parse = argparse.ArgumentParser()
parse.add_argument('--host', help='Host', default='localhost')
parse.add_argument('--port', help='Port', default='8000')
parse.add_argument('--reload', action='store_true', help='Development reload')
parse.add_argument('--config', type=argparse.FileType('r'))

args = parse.parse_args()
app = create_app(config=load_config(args.config))

if args.reload:
    print("Start with reload", args.reload)
    aioreloader.start()


if __name__ == "__main__":
    web.run_app(app, host=args.host, port=args.port)
