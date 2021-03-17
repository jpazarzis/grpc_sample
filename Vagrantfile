$script = <<SCRIPT
sudo apt update
sudo apt install python3-pip -y
sudo pip3 install grpcio
sudo pip3 install grpcio-tools
SCRIPT

$install_go = <<SCRIPT
cd /tmp
wget https://dl.google.com/go/go1.15.6.linux-amd64.tar.gz
sudo tar -xvf go1.15.6.linux-amd64.tar.gz
sudo mv go /usr/local
echo "export GOROOT=/usr/local/go" >> /home/vagrant/.profile
echo "export GOPATH=/vagrant" >> /home/vagrant/.profile
echo "export PATH=/vagrant:/usr/local/go/bin:$PATH" >> /home/vagrant/.profile
go get -d github.com/envoyproxy/protoc-gen-validate
cd src/github.com/envoyproxy/protoc-gen-validate
sudo apt install protobuf-compiler
sudo make build
echo "export PATH=/vagrant/src/github.com/envoyproxy/protoc-gen-validate:$PATH" >> /home/vagrant/.profile
sudo pip3 install protoc-gen-validate
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.provision "shell", inline: $script
  config.vm.provision "shell", inline: $install_go
end

