# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "williamyeh/ubuntu-trusty64-docker"

  config.vm.network "forwarded_port", guest: 8123, host: 8123

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y vim python-pip

    docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 8123:15672 rabbitmq:3-management

  SHELL
end
