# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.synced_folder "crawler", "/home/vagrant/crawler",
    type: "nfs", create: true

  config.vm.provision "shell", path: "bootstrap.sh"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end

end
