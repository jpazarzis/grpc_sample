"""Exposes the Calculator service."""

from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    """Implements the Calculator service."""

    def add(self, integer_pair, context):
        """Implements the add method of the protocol buffer."""
        print(f"Adding: {integer_pair.i1} + {integer_pair.i2}")
        return calculator_pb2.Integer(i=integer_pair.i1 + integer_pair.i2)


def serve():
    """Starts the server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    host = 'localhost:50051'
    print(f"Starts server in {host}")
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()