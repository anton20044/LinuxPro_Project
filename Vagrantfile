MACHINES = {
  :log01 => {
        :box_name => "jammy",
        :vm_name => "log01",
        :cpus => 2,
        :memory => 4096,
        :net => [
                   ["192.168.56.13", 2, "255.255.255.0", "net1"],
                   ["192.168.57.13", 3],
                ]
  },

  :etcd01 => {
        :box_name => "jammy",
        :vm_name => "etcd01",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.2", 2, "255.255.255.0", "net1"],
                   ["192.168.57.2", 3],
                ]
  },
  :etcd02 => {
        :box_name => "jammy",
        :vm_name => "etcd02",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.3", 2, "255.255.255.0", "net1"],
                   ["192.168.57.3", 3],
                ]
  },
  :etcd03 => {
        :box_name => "jammy",
        :vm_name => "etcd03",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.4", 2, "255.255.255.0", "net1"],
                   ["192.168.57.4", 3],
                ]
  },
  :router01 => {
        :box_name => "jammy",
        :vm_name => "router01",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.21", 2, "255.255.255.0", "net1"],
		   #["192.168.58.21", 3],
                   ["192.168.57.21", 5],
                ]
  },
  :router02 => {
        :box_name => "jammy",
        :vm_name => "router02",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.22", 2, "255.255.255.0", "net1"],
		   #["192.168.58.22", 3],
                   ["192.168.57.22", 5],
                ]
  },
  :backup => {
        :box_name => "jammy",
        :vm_name => "backup",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.5", 2, "255.255.255.0", "net1"],
                   ["192.168.57.5", 3],
                ]
  },
  :monitor => {
        :box_name => "jammy",
        :vm_name => "monitor",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.6", 2, "255.255.255.0", "net1"],
                   ["192.168.57.6", 3],
                ]
  },
  :hp01 => {
        :box_name => "jammy",
        :vm_name => "hp01",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.7", 2, "255.255.255.0", "net1"],
                   ["192.168.57.7", 3],
                ]
  },
  :hp02 => {
        :box_name => "jammy",
        :vm_name => "hp02",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.8", 2, "255.255.255.0", "net1"],
                   ["192.168.57.8", 3],
                ]
  },
  :pg01 => {
        :box_name => "jammy",
        :vm_name => "pg01",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.9", 2, "255.255.255.0", "net1"],
                   ["192.168.57.9", 3],
                ]
  },
  :pg02 => {
        :box_name => "jammy",
        :vm_name => "pg02",
        :cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.10", 2, "255.255.255.0", "net1"],
                   ["192.168.57.10", 3],
                ]
  },
  :dns01 => {
        :box_name => "jammy",
        :vm_name => "dns01",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.11", 2, "255.255.255.0", "net1"],
                   ["192.168.57.11", 3],
                ]
  },
  :dns02 => {
        :box_name => "jammy",
        :vm_name => "dns02",
	:cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.12", 2, "255.255.255.0", "net1"],
                   ["192.168.57.12", 3],
                ]
  },
  :app01 => {
        :box_name => "jammy",
        :vm_name => "app01",
        :cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.14", 2, "255.255.255.0", "net1"],
                   ["192.168.57.14", 3],
                ]
  },
  :app02 => {
        :box_name => "jammy",
        :vm_name => "app02",
        :cpus => 1,
        :memory => 756,
        :net => [
                   ["192.168.56.15", 2, "255.255.255.0", "net1"],
                   ["192.168.57.15", 3],
                ]
  },
}

Vagrant.configure("2") do |config|

  MACHINES.each do |boxname, boxconfig|
    
    config.vm.define boxname do |box|
   
      box.vm.box = boxconfig[:box_name]
      box.vm.host_name = boxconfig[:vm_name]

      box.vm.provider "virtualbox" do |v|
        v.memory = boxconfig[:memory]
        v.cpus = boxconfig[:cpus]
       end

      box.vm.synced_folder ".", "/vagrant", disabled: true

        box.vm.provision "shell", inline: <<-SHELL
          mkdir -p ~root/.ssh
          cp ~vagrant/.ssh/auth* ~root/.ssh
          sed -i 's/^PasswordAuthentication.*$/PasswordAuthentication yes/' /etc/ssh/sshd_config.d/60-cloudimg-settings.conf        
          systemctl restart sshd.service
        SHELL


      if boxconfig[:vm_name] == "log01"
         box.vm.network "forwarded_port", guest: 5601, host: 5601
      end

      if boxconfig[:vm_name] == "hp01"
         box.vm.network "forwarded_port", guest: 7000, host: 7000
      end
  
      if boxconfig[:vm_name] == "hp02"
         box.vm.network "forwarded_port", guest: 7000, host: 7001
      end



      if boxconfig[:vm_name] == "monitor"
         box.vm.network "forwarded_port", guest: 3000, host: 3000
         box.vm.network "forwarded_port", guest: 9090, host: 9090
         box.vm.network "forwarded_port", guest: 9093, host: 9093
      end


      #if boxconfig[:vm_name] == "app02"
       #box.vm.provision "ansible" do |ansible|
        #ansible.playbook = "ansible/provision.yml"
        #ansible.inventory_path = "ansible/hosts"
        #ansible.host_key_checking = "false"
        #ansible.limit = "all"
       #end
      #end

      boxconfig[:net].each do |ipconf|
        box.vm.network("private_network", ip: ipconf[0], adapter: ipconf[1], netmask: ipconf[2], virtualbox__intnet: ipconf[3])
      end

      if boxconfig[:vm_name] == "router01"
         box.vm.network "public_network", ip: "192.168.50.238", adapter: 3,  bridge: "br0"
      end
      if boxconfig[:vm_name] == "router02"
         box.vm.network "public_network", ip: "192.168.50.239", adapter: 3,  bridge: "br0"
      end


     end
  end
end
