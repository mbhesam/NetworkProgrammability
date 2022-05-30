import netmiko
import termcolor

Switch1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "Switch1",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

Switch2 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.2",
    "username": "Switch2",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

Switch3 = {
    "device_type": "cisco_ios",
    "host": "192.168.2.9",
    "username": "Switch3",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

Switch4 = {
    "device_type": "cisco_ios",
    "host": "192.168.2.18",
    "username": "Switch4",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

net_connect = netmiko.ConnectHandler(**Switch1)
net_connect.enable(cmd="enable 15")
net_connect.send_config_set("ip dhcp snooping")
net_connect.send_config_set("ip dhcp snooping vlan 5,6")
int_trust_list = ["interface range e0/0-1","ip dhcp snooping trust"]
net_connect.send_config_set(int_trust_list)
int_limit_list = ["interface range e1/0-3","ip dhcp snooping limit rate 5"]
net_connect.send_config_set(int_limit_list)
print(termcolor.colored(net_connect.send_command('show ip dhcp snooping'),"red"))
print(termcolor.colored(net_connect.send_command('show ip dhcp snooping binding'),"blue"))

