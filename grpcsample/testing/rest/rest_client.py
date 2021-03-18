import aiohttp
import asyncio
import datetime

async def retrieve(session, i):
    async with session.get('http://localhost:8030') as response:
        payload = await response.json()
        if i % 1000 == 0:
            print(i)

async def main(n=100):
    tasks = []
    async with aiohttp.ClientSession() as session:
        started = datetime.datetime.now()
        for i in range(n):
            tasks.append(retrieve(session, i))
        await asyncio.gather(*tasks)
        duration = (datetime.datetime.now() - started).total_seconds()
    print(f'durarion: {duration}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())