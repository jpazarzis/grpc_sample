import logging
import asyncio

import grpc

import grpcsample.stubs.math_pb2_grpc as math_pb2_grpc
import grpcsample.stubs.math_pb2 as math_pb2
import grpcsample.common.constants as constants


class Math(math_pb2_grpc.MathServicer):
    """Implements the match service."""

    async def add(self, integer_pair, context):
        """Implements the add method of the protocol buffer."""
        return math_pb2.Integer(i=integer_pair.i1 + integer_pair.i2)



async def serve() -> None:
    server = grpc.aio.server()
    math_pb2_grpc.add_MathServicer_to_server(Math(), server)
    server.add_insecure_port(f'[::]:{constants.GRPC_PORT}')
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        # Shuts down the server with 0 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(0)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
