from concurrent import futures
import grpc
import customer_pb2
import customer_pb2_grpc
from protoc_gen_validate.validator import validate, ValidationFailed

class CustomerManagerServicer(customer_pb2_grpc.CustomerManagerServicer):
    """Implements the Calculator service."""

    def get(self, request, context):
        """Implements the add method of the protocol buffer."""
        print("sending:", "Dow")
        return customer_pb2.Customer(name='Joe Dow', age=9)


def serve():
    """Starts the server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    customer_pb2_grpc.add_CustomerManagerServicer_to_server(
        CustomerManagerServicer(), server
    )
    host = 'localhost:50051'
    print(f"Starts server in {host}")
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
