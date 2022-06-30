from netmiko import ConnectHandler
import  csv
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

net_connect_sw1 = ConnectHandler(**Switch1)
net_connect_sw2 = ConnectHandler(**Switch2)
net_connect_sw3 = ConnectHandler(**Switch3)
net_connect_sw4 = ConnectHandler(**Switch4)

net_connect_sw1.enable(cmd="enable 15")
net_connect_sw2.enable(cmd="enable 15")
net_connect_sw3.enable(cmd="enable 15")
net_connect_sw4.enable(cmd="enable 15")

con_list = [net_connect_sw1,net_connect_sw2,net_connect_sw3,net_connect_sw4]
switch_names = ["Switch1","Switch2","Switch3","Switch4"]
with open("command_IPSG_LAB4_Netmiko.csv","r") as reader:
    reading = csv.DictReader(reader)
    for i in range(len(con_list)):
        for j in reading:
            con_list.send_config_set(j[switch_names[i]])
        reader.seek(0)
    counter = 0
    for k in con_list:
        print("device "+i+"\n"+k.send_command("show ip source binding"))
        counter+=1

