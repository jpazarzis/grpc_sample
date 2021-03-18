"""Example of async grpc client."""

import asyncio
import datetime

import grpc

import grpcsample.testing.grpc.msg_pb2_grpc as msg_pb2_grpc
import grpcsample.testing.grpc.msg_pb2 as msg_pb2

async def retrieve(stub, i):
    response = await stub.get(None)
    if i % 1000 == 0:
        print(i)

async def main(n=100):
    """Executes the async add method though RPC."""
    async with grpc.aio.insecure_channel('localhost:8031') as channel:
        stub = msg_pb2_grpc.MessageProviderStub(channel)
        tasks = []
        for i in range(n):
            tasks.append(retrieve(stub, i))
        started = datetime.datetime.now()
        await asyncio.gather(*tasks)
        duration = (datetime.datetime.now() - started).total_seconds()
    print(f'durarion: {duration}')


if __name__ == '__main__':
    asyncio.run(main())
