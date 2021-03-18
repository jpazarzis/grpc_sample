go get -d github.com/envoyproxy/protoc-gen-validate
cd src/github.com/envoyproxy/protoc-gen-validate
sudo apt install protobuf-compiler -y
sudo make build
export PATH=$PATH:/vagrant/src/github.com/envoyproxy/protoc-gen-validate
sudo pip3 install protoc-gen-validate