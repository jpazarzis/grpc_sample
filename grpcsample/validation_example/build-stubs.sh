python3 -m grpc_tools.protoc -I.:/vagrant/src/github.com/envoyproxy/protoc-gen-validate --python_out=. --grpc_python_out=. customer.proto
python3 -m grpc_tools.protoc -I /vagrant/src/github.com/envoyproxy/protoc-gen-validate --python_out=. --grpc_python_out=. validate/validate.proto

cp ./validate/* .
rm -rf validate