from telnetlib import Telnet
from getpass import getpass
from termcolor import colored
from time import sleep

ip_addr  = ["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4","192.168.1.5","192.168.1.6","192.168.1.17"
    ,"192.168.1.18","192.168.1.19","192.168.1.20"]
username = "admin"
password = "tehrantrain"
en_pass = "tehrantrain"
hostname = ["Switch1","Switch2","MLS1","MLS2","Router1","Router2","Switch3","Switch4","MLS3","MLS4"]
tn = []
for i in ip_addr:
    try:
        tn.append(Telnet(i))
    except:
        print colored("host unreachble of telnet not config on "+i , "red")
for i in range(len(ip_addr)):
    try:
        tn[i].read_until("Username: ")
        tn[i].write(username+ "\n")
        sleep(0.5)
        tn[i].read_until("Password: ")
        tn[i].write(password + "\n")
    except:
        print colored("user or pass is incorrect on "+ip_addr[i] , "red")
    else:
        print colored("connection stablished on"+ip_addr[i],"green")

    hostname_cmd = "hostname "+hostname[i]+"\n"
    ntp_srv_cmd = "ntp server 172.16.1.1 \n"
    disable_log_con_cmd = "no logging console \n"

    tn[i].write("en \n")
    sleep(0.5)
    tn[i].write(en_pass+"\n")
    sleep(0.5)
    tn[i].write("conf t\n")
    sleep(0.5)
    tn[i].write(hostname_cmd)
    sleep(0.5)
    tn[i].write(ntp_srv_cmd)
    sleep(0.5)
    tn[i].write(disable_log_con_cmd)
    sleep(0.5)
    print colored("command executed on device"+ip_addr[i],"yellow")
