import paramiko
from time import sleep
import  csv
from colorama import Fore

device_info =[
    {"name":"MLS1","ip":"192.168.1.3","username":"MLS1","password":"tehrantrain","en_password":"tehrantrain"},
    {"name": "MLS2", "ip": "192.168.1.4", "username": "MLS2", "password": "tehrantrain", "en_password": "tehrantrain"},
    {"name": "MLS3", "ip": "192.168.1.11", "username": "MLS3", "password": "tehrantrain", "en_password": "tehrantrain"},
    {"name": "MLS4", "ip": "192.168.1.12", "username": "MLS4", "password": "tehrantrain", "en_password": "tehrantrain"},
    {"name": "Router1", "ip": "192.168.1.5", "username": "Router1", "password": "tehrantrain", "en_password": "tehrantrain"},
    {"name": "Router2", "ip": "192.168.1.13", "username": "Router2", "password": "tehrantrain", "en_password": "tehrantrain"}
]

ip_configuration_MLS1 = {
    "eth0/2":"10.0.0.2 255.255.255.252",
    "eth0/3": "10.0.0.6 255.255.255.252"
}

ip_configuration_MLS2 = {
    "eth0/2":"10.0.0.10 255.255.255.252",
    "eth0/3": "10.0.0.14 255.255.255.252"
}

ip_configuration_MLS3 = {
    "eth0/2":"10.0.0.18 255.255.255.252",
    "eth0/3": "10.0.0.22 255.255.255.252"
}

ip_configuration_MLS4 = {
    "eth0/2":"10.0.0.26 255.255.255.252",
    "eth0/3": "10.0.0.30 255.255.255.252"
}

ip_configuration_Router1 = {
    "eth0/0":"10.0.0.1 255.255.255.252",
    "eth0/1": "10.0.0.9 255.255.255.252",
    "eth0/2": "10.0.0.17 255.255.255.252",
    "eth0/3": "10.0.0.25 255.255.255.252",
    "eth1/0": "10.0.0.33 255.255.255.252"
}

ip_configuration_Router2 = {
    "eth0/0":"10.0.0.5 255.255.255.252",
    "eth0/1": "10.0.0.13 255.255.255.252",
    "eth0/2": "10.0.0.21 255.255.255.252",
    "eth0/3": "10.0.0.29 255.255.255.252",
    "eth1/0": "10.0.0.34 255.255.255.252"
}

def ip_config(connection,ip_configuration):
    connection.send("conf t \n")
    sleep(0.5)
    interface_list = ip_configuration.keys()
    for i in interface_list:
        connection.send("interface "+i+"\n")
        sleep(0.5)
        connection.send("no shutdown \n")
        sleep(0.5)
        connection.send("no switchport\n")
        sleep(0.5)
        connection.send("ip address "+ip_configuration[i]+"\n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)

def static_route(connection,name):
    connection.send("conf t \n")
    with open("default_Routes_LAB4_Paramiko.csv","r") as reader:
        reading = csv.DictReader(reader)
        for i in reading:
            connection.send(i[name]+"\n")
            sleep(0.5)
        connection.send("end \n")
        sleep(0.5)

def nat_config(connection,name):
    if "1" in name or "2" in name:
        connection.send("conf t \n")
        sleep(0.5)
        connection.send("ip access-list standard 5 \n")
        sleep(0.5)
        connection.send("permit 192.168.5.0 0.0.0.255 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("ip access-list standard 6 \n")
        sleep(0.5)
        connection.send("permit 192.168.6.0 0.0.0.255 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("route-map to_router_1 \n")
        sleep(0.5)
        connection.send("match ip address 5 \n")
        sleep(0.5)
        connection.send("match ip address 6 \n")
        sleep(0.5)
        connection.send("match interface e0/2 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("route-map to_router_2 \n")
        sleep(0.5)
        connection.send("match ip address 5 \n")
        sleep(0.5)
        connection.send("match ip address 6 \n")
        sleep(0.5)
        connection.send("match interface e0/3 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("ip nat inside source route_map to_router_1 interface e0/2 \n")
        sleep(0.5)
        connection.send("ip nat inside source route_map to_router_2 interface e0/3 \n")
        sleep(0.5)
        connection.send("end \n")
        sleep(0.5)
    else:
        connection.send("conf t \n")
        sleep(0.5)
        connection.send("ip access-list standard 7 \n")
        sleep(0.5)
        connection.send("permit 192.168.7.0 0.0.0.255 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("ip access-list standard 7 \n")
        sleep(0.5)
        connection.send("permit 192.168.7.0 0.0.0.255 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("route-map to_router_1 \n")
        sleep(0.5)
        connection.send("match ip address 7 \n")
        sleep(0.5)
        connection.send("match ip address 8 \n")
        sleep(0.5)
        connection.send("match interface e0/2 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("route-map to_router_2 \n")
        sleep(0.5)
        connection.send("match ip address 7 \n")
        sleep(0.5)
        connection.send("match ip address 8 \n")
        sleep(0.5)
        connection.send("match interface e0/3 \n")
        sleep(0.5)
        connection.send("exit \n")
        sleep(0.5)
        connection.send("ip nat inside source route_map to_router_1 interface e0/2 \n")
        sleep(0.5)
        connection.send("ip nat inside source route_map to_router_2 interface e0/3 \n")
        sleep(0.5)
        connection.send("end \n")
        sleep(0.5)

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(hostname=device_info[0]["ip"], username=device_info[0]["username"], password=device_info[0]["password"], look_for_keys=False, allow_agent=False)
connection = session.invoke_shell()
connection.send("en \n")
connection.send(device_info[0]["enable_password"]+"\n")
ip_config(connection,ip_configuration_MLS3)
print(Fore.BLUE + "ip set on interfaces of MLS3")
static_route(connection,device_info[0]["name"])
print(Fore.BLUE + "static routes configured on MLS3")
nat_config(connection,device_info[0]["name"])
print(Fore.BLUE + "nat configuration enabled in MLS3")
session.close()

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(hostname=device_info[1]["ip"], username=device_info[1]["username"], password=device_info[3]["password"], look_for_keys=False, allow_agent=False)
connection = session.invoke_shell()
connection.send("en \n")
connection.send(device_info[1]["enable_password"]+"\n")
ip_config(connection,ip_configuration_MLS3)
print(Fore.RED + "ip set on interfaces of MLS3")
static_route(connection,device_info[1]["name"])
print(Fore.RED + "static routes configured on MLS3")
nat_config(connection,device_info[1]["name"])
print(Fore.RED + "nat configuration enabled in MLS3")
session.close()

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(hostname=device_info[2]["ip"], username=device_info[2]["username"], password=device_info[3]["password"], look_for_keys=False, allow_agent=False)
connection = session.invoke_shell()
connection.send("en \n")
connection.send(device_info[2]["enable_password"]+"\n")
ip_config(connection,ip_configuration_MLS3)
print(Fore.YELLOW + "ip set on interfaces of MLS3")
static_route(connection,device_info[2]["name"])
print(Fore.YELLOW + "static routes configured on MLS3")
nat_config(connection,device_info[2]["name"])
print(Fore.YELLOW + "nat configuration enabled in MLS3")
session.close()

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(hostname=device_info[3]["ip"], username=device_info[3]["username"], password=device_info[3]["password"], look_for_keys=False, allow_agent=False)
connection = session.invoke_shell()
connection.send("en \n")
connection.send(device_info[3]["enable_password"]+"\n")
ip_config(connection,ip_configuration_MLS3)
print(Fore.GREEN + "ip set on interfaces of MLS3")
static_route(connection,device_info[3]["name"])
print(Fore.GREEN + "static routes configured on MLS3")
nat_config(connection,device_info[3]["name"])
print(Fore.GREEN + "nat configuration enabled in MLS3")
session.close()

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(hostname=device_info[4]["ip"], username=device_info[4]["username"], password=device_info[3]["password"], look_for_keys=False, allow_agent=False)
connection = session.invoke_shell()
connection.send("en \n")
connection.send(device_info[4]["enable_password"]+"\n")
ip_config(connection,ip_configuration_MLS3)
print(Fore.BLACK + "ip set on interfaces of Router1")
session.close()

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(hostname=device_info[5]["ip"], username=device_info[5]["username"], password=device_info[3]["password"], look_for_keys=False, allow_agent=False)
connection = session.invoke_shell()
connection.send("en \n")
connection.send(device_info[5]["enable_password"]+"\n")
ip_config(connection,ip_configuration_MLS3)
print(Fore.WHITE + "ip set on interfaces of Router2")
session.close()



