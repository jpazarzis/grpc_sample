"""Trivial client of the Math protocol buffer."""

import grpc

import grpcsample.stubs.math_pb2_grpc as math_pb2_grpc
import grpcsample.stubs.math_pb2 as math_pb2
import grpcsample.common.constants as contants


def add(i1, i2):
    """Executes the add method though RPC."""
    target = f'{contants.HOST}:{contants.GRPC_PORT}'
    with grpc.insecure_channel(target) as channel:
        stub = math_pb2_grpc.MathStub(channel)
        response = stub.add(math_pb2.IntegerPair(i1=i1, i2=i2))
        return response.i


if __name__ == '__main__':
    print(add(i1=2, i2=3))
