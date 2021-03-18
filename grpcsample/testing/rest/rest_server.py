import random

from aiohttp import web

import grpcsample.testing.msgs as msg


async def handler(request):
    try:
        index = random.randint(0, len(msg.MSGS)-1)
        return web.json_response(msg.MSGS[index])
    except Exception as ex:
        print(ex)


app = web.Application()
app.add_routes([web.get('/', handler)])

if __name__ == '__main__':
    web.run_app(app, port=8030)