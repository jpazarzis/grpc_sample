"""Exposes a grpc server."""

from concurrent import futures

import logging

import grpc

import grpcsample.stubs.math_pb2_grpc as math_pb2_grpc
import grpcsample.stubs.math_pb2 as math_pb2
import grpcsample.common.constants as constants

MAX_WORKERS = 2

class Math(math_pb2_grpc.MathServicer):
    """Implements the match service."""

    def add(self, integer_pair, context):
        """Implements the add method of the protocol buffer."""
        return math_pb2.Integer(i=integer_pair.i1 + integer_pair.i2)


def serve():
    """Starts the server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    math_pb2_grpc.add_MathServicer_to_server(Math(), server)
    server.add_insecure_port(f'[::]:{constants.GRPC_PORT}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
