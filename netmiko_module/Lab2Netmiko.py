from netmiko import ConnectHandler
from threading import Thread
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
    "host": "192.168.2.10",
    "username": "Switch4",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

def port_security_configuration(net_connect):
    psc_list = ['interface range eth1/0-3','switchport port-security',
                'switchport port-security maximum 1', 'switchport port-security mac-address sticky',
                'switchport port-security violation restrict','switchport port-security aging type inactivity',
                'switchport port-security aging time 120']
    net_connect.send_config_set(psc_list)

net_connect_sw1 = ConnectHandler(**Switch1)
net_connect_sw2 = ConnectHandler(**Switch2)
net_connect_sw3 = ConnectHandler(**Switch3)
net_connect_sw4 = ConnectHandler(**Switch4)

net_connect_sw1.enable(cmd="enable 15")
net_connect_sw2.enable(cmd="enable 15")
net_connect_sw3.enable(cmd="enable 15")
net_connect_sw4.enable(cmd="enable 15")

connection_list = [net_connect_sw1,net_connect_sw2,net_connect_sw3,net_connect_sw4]
thread_list = []

for i in connection_list:
    TH = Thread(target=port_security_configuration,args=(i,))
    thread_list.append(TH)
    TH.start()

for i in thread_list:
    i.join()


