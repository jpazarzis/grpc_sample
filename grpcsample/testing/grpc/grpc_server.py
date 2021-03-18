import logging
import asyncio
import random

import grpc

import grpcsample.testing.grpc.msg_pb2_grpc as msg_pb2_grpc
import grpcsample.testing.grpc.msg_pb2 as msg_pb2
import grpcsample.testing.msgs as msg

class MessageProviderServicer(msg_pb2_grpc.MessageProviderServicer):

    async def get(self, request,  context):
        """Implements the add method of the protocol buffer."""
        index = random.randint(0, len(msg.MSGS) - 1)
        data = msg.MSGS[index]
        return msg_pb2.Message(
            name=data['name'],
            story1=data['story1'],
            story2=data['story2'],
            story3=data['story3']
        )


async def serve() -> None:
    server = grpc.aio.server()
    msg_pb2_grpc.add_MessageProviderServicer_to_server(MessageProviderServicer(), server)
    server.add_insecure_port(f'localhost:8031')
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
