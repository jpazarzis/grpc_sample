# Trivial g-rpc sample code


The project is deployed as a library so you need to install it as follows:

    sudo python3 setup.py develop

The protocol buffers are meant to be defined under the protos directory.

Start the VM running
    vagrant up
    vagrant ssh
    cd /vagrant
    

To build the grpc stubs:
    python3 -m grpc_tools.protoc -I./protos --python_out=./grpcsample/stubs --grpc_python_out=./grpcsample/stubs math.proto
