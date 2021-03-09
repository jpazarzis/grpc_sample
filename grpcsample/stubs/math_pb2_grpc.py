
import grpc

import grpcsample.stubs.math_pb2 as math__pb2


class MathStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add = channel.unary_unary(
                '/Math/add',
                request_serializer=math__pb2.IntegerPair.SerializeToString,
                response_deserializer=math__pb2.Integer.FromString,
                )


class MathServicer(object):
    """Missing associated documentation comment in .proto file."""

    def add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MathServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add': grpc.unary_unary_rpc_method_handler(
                    servicer.add,
                    request_deserializer=math__pb2.IntegerPair.FromString,
                    response_serializer=math__pb2.Integer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Math', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Math(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Math/add',
            math__pb2.IntegerPair.SerializeToString,
            math__pb2.Integer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
