import paramiko
from time import sleep
import threading
from getpass import getpass
from termcolor import colored

ip_addr = input("Enter ip address of dhcp srv\n")
username = input("Enter username of dhcp srv\n")
password = getpass("Enter password of dhcp srv\n")
en_pass = getpass("Enter enable password of dhcp srv\n")

vlan_info = {
    "network_vlan_5":"192.168.5.0 255.255.255.0",
    "network_vlan_6": "192.168.6.0 255.255.255.0",
    "gw_vlan_5":"192.168.5.254",
    "gw_vlan_6": "192.168.6.254"
}
session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect(hostname=ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False)
connection = session.invoke_shell()
connection.send("en \n")
sleep(0.5)
connection.send(en_pass + "\n")
sleep(0.5)
connection.send("conf t\n")
sleep(0.5)
connection.send("ip dhcp pool dhcp_vlan_5 \n")
sleep(0.5)
connection.send("network "+vlan_info["network_vlan_5"]+"\n")
sleep(0.5)
connection.send("dns-server 8.8.8.8 \n")
sleep(0.5)
connection.send("default router "+vlan_info["gw_vlan_5"]+"\n")
sleep(0.5)
connection.send("lease infinit\n")
sleep(0.5)
connection.send("exit \n")
sleep(0.5)
connection.send("ip dhcp pool dhcp_vlan_6 \n")
sleep(0.5)
connection.send("network "+vlan_info["network_vlan_6"]+"\n")
sleep(0.5)
connection.send("dns-server 8.8.8.8 \n")
sleep(0.5)
connection.send("default router "+vlan_info["gw_vlan_6"]+"\n")
sleep(0.5)
connection.send("lease infinit\n")
sleep(0.5)
connection.send("end \n")
sleep(0.5)
connection.send("show ip dhcp pool \n")
sleep(0.5)
dhcp_pool = connection.recv(65535)
print(colored("dhcp pool is configured: ","red"))
print(colored(dhcp_pool,"blue"))
