"""Example of async grpc client."""

import asyncio

import grpc

import grpcsample.stubs.math_pb2_grpc as math_pb2_grpc
import grpcsample.stubs.math_pb2 as math_pb2
import grpcsample.common.constants as constants


async def add(i1, i2):
    """Executes the async add method though RPC."""
    target = f'{constants.HOST}:{constants.GRPC_PORT}'
    async with grpc.aio.insecure_channel(target) as channel:
        stub = math_pb2_grpc.MathStub(channel)
        response = await stub.add(math_pb2.IntegerPair(i1=i1, i2=i2))
        return response.i


if __name__ == '__main__':
    print(asyncio.run(add(3, 7)))
