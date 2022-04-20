import paramiko
from time import sleep
import threading
from termcolor import colored

def make_vlan(ip_addr,username,password,en_pass,vlan_num):
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    session.connect(hostname=ip_addr,username=username,password=password,look_for_keys=False,allow_agent=False)
    connection = session.invoke_shell()
    connection.send("en \n")
    sleep(0.5)
    connection.send(en_pass+"\n")
    sleep(0.5)
    connection.send("conf t\n")
    sleep(0.5)
    for i in range(len(vlan_num)):
        connection.send("vlan "+vlan_num[i]+"\n")
        sleep(0.5)
        connection.send("name HESAM_VLAN "+vlan_num[i]+"\n")
        sleep(0.5)
    session.close()

def vlan_route_vrrp(ip_addr,username,password,en_pass,vlan_num):
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    session.connect(hostname=ip_addr,username=username,password=password,look_for_keys=False,allow_agent=False)
    connection = session.invoke_shell()
    connection.send("en \n")
    sleep(0.5)
    connection.send(en_pass+"\n")
    sleep(0.5)
    connection.send("conf t\n")
    sleep(0.5)
    connection.send("ip routing \n")
    sleep(0.5)
    for i in range(len(vlan_num)):
        connection.send("int vlan "+ vlan_num[i]+"\n")
        sleep(0.5)
        connection.send("no shutdown \n")
        sleep(0.5)
        connection.send("ip address 192.168."+vlan_num[i]+"253 255.255.255.0 \n")
        sleep(0.5)
        connection.send("description gateway_vlan_"+vlan_num[i]+"\n")
        sleep(0.5)
        connection.send("vrrp 10 ip 192.168."+vlan_num[i]+"254 \n")
        sleep(0.5)
    session.close()

if __name__ == "__main__":
    ip_addr = input(colored("Please Enter the ip address of MLS switches of switchblock with , as seprator [ex: 192.168.1.1,192.168.1.2]","blue"))
    ip_addr_list = ip_addr.split(",")
    for i in range(len(ip_addr_list)):
        ip_addr_list[i]=ip_addr_list[i].strip()
    username = input(colored("Please Enter the username of MLS switches of switchblock with , as seprator [ex: Switch1,Switch2]","yellow"))
    username_list = username.split(",")
    for i in range(len(username_list)):
        username_list[i]=username_list[i].strip()
    password = input(colored("Please Enter the password of MLS switches of switchblock with , as seprator [ex: cisco,cisco]","green"))
    password_list = password.split(",")
    for i in range(len(password_list)):
        password_list[i]=password_list[i].strip()
    en_pass = input(colored("Please Enter the enable password of MLS switches of switchblock with , as seprator [ex: cisco,cisco]","purple"))
    en_pass_list = en_pass.split(",")
    for i in range(len(password_list)):
        en_pass_list[i]=en_pass_list[i].strip()
    vlan_numbers = input(colored("Please Enter vlans of MLS switches of switchblock with , as seprator [ex: 10,20]","black"))
    vlan_numbers_list = vlan_numbers.split(",")
    for i in range(len(vlan_numbers_list)):
        vlan_numbers_list[i]=vlan_numbers_list[i].strip()
    for i in range(len(ip_addr_list)):
        make_vlan(ip_addr_list[i],username_list[i],password_list[i],en_pass_list[i],vlan_numbers_list[i])
        vlan_route_vrrp(ip_addr_list[i],username_list[i],password_list[i],en_pass_list[i],vlan_numbers_list[i])
