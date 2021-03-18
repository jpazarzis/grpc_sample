import random
import time

import grpc

import customer_pb2
import customer_pb2_grpc
from google.protobuf import wrappers_pb2 as wrappers
from protoc_gen_validate.validator import validate, ValidationFailed



Customer = customer_pb2.Customer
CustomerManager = customer_pb2_grpc.CustomerManager

def main():
    """Executes the add method though RPC."""
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = customer_pb2_grpc.CustomerManagerStub(channel)
        while True:
            response = stub.get(wrappers.StringValue(value="John"))
            try:
                validate(response)
            except ValidationFailed as err:
                print(err)

            print(response.name)
            time.sleep(0.2)


if __name__ == '__main__':
    main()
