"""Implements a Calculator client."""

import random
import time

import grpc

import calculator_pb2
import calculator_pb2_grpc

IntegerPair = calculator_pb2.IntegerPair
Calculator = calculator_pb2_grpc.CalculatorStub

def main():
    """Executes the add method though RPC."""
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Calculator(channel)
        while True:
            i1 = random.randint(1, 100)
            i2 = random.randint(1, 100)
            response = stub.add(IntegerPair(i1=i1, i2=i2))
            print(i1, i2, response.i)
            time.sleep(0.2)


if __name__ == '__main__':
    main()
