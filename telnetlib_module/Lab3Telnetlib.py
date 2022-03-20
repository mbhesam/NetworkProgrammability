from telnetlib import Telnet
from colorama import Fore,Back,Style
from time import sleep


ip_addr_distr = ["192.168.1.3","192.168.1.4","192.168.1.19","192.168.1.20"]
username_distr = ["MLS1","MLS2","MLS3","MLS4"]
ip_addr_access = ["192.168.1.1","192.168.1.2","192.168.1.17","192.168.1.18"]
username_access = ["Switch1","Switch2","Switch3","Switch4"]

password = "tehrantrain"
en_pass = "tehrantrain"

def vlan_conf(tn):
    for i in range(2,5):
        tn.write("conf t\n")
        sleep(0.5)
        tn.write("vlan "+str(i)+"\n")
        sleep(0.5)
        tn.write("name PY_VLAN_"+str(i)+"\n")
        sleep(0.5)
        tn.write("end\n")
        sleep(0.5)

def Access_interface(tn , vlan_nums):
    tn.write("conf t \n")
    sleep(0.5)
    tn.write("int e1/1 \n")
    sleep(0.5)
    tn.write("switchport mode access\n")
    sleep(0.5)
    tn.write("switchport access vlan "+str(vlan_nums)+"\n")
    sleep(0.5)
    tn.write("int e1/2 \n")
    sleep(0.5)
    tn.write("switchport mode access\n")
    sleep(0.5)
    tn.write("switchport access vlan "+str(vlan_nums)+"\n")
    sleep(0.5)
    tn.write("int e1/3 \n")
    sleep(0.5)
    tn.write("switchport mode access\n")
    sleep(0.5)
    tn.write("switchport access vlan "+str(vlan_nums)+"\n")
    sleep(0.5)
    tn.write("end\n")
    sleep(0.5)

def trunk_interface(tn):
    tn.write("conf t \n")
    sleep(0.5)
    tn.write("int e0/0 \n")
    sleep(0.5)
    tn.write("switchport trunk encapsulation dot1q\n")
    sleep(0.5)
    tn.write("switchport mode trunk\n")
    sleep(0.5)
    tn.write("int e0/1 \n")
    sleep(0.5)
    tn.write("switchport trunk encapsulation dot1q\n")
    sleep(0.5)
    tn.write("switchport mode trunk\n")
    sleep(0.5)
    tn.write("end\n")
    sleep(0.5)

if __name__ == "__main__":
    for i in range(len(ip_addr_access)):
        try:
            tn = Telnet(ip_addr_access[i],timeout=3)
        except:
            print Fore.RED +"telnet connection refuse"+ Style.RESET_ALL
        else:
            print Fore.GREEN + Style.BRIGHT + "telnet connect starts with access switch" + ip_addr_access[i]+Style.RESET_ALL
        tn.read_until("Username: ")
        tn.write(username_access[i]+"\n")
        sleep(0.5)
        tn.read_until("Password: ")
        tn.write(password+"\n")
        tn.write("en\n")
        sleep(0.5)
        tn.write(en_pass+"\n")
        sleep(0.5)
        vlan_conf(tn)
        vlan_num = i + 2
        Access_interface(tn,vlan_num)
        tn.close()

    for i in range(len(ip_addr_distr)):
        try:
            tn = Telnet(ip_addr_access[i],timeout=3)
        except:
            print Fore.RED +"telnet connection refuse"+ Style.RESET_ALL
        else:
            print Fore.GREEN + Style.BRIGHT + "telnet connect starts with distribution switch" + ip_addr_access[i]+Style.RESET_ALL
        tn.read_until("Username: ")
        tn.write(username_distr[i]+"\n")
        sleep(0.5)
        tn.read_until("Password: ")
        tn.write(password+"\n")
        tn.write("en\n")
        sleep(0.5)
        tn.write(en_pass+"\n")
        sleep(0.5)
        vlan_conf(tn)
        vlan_num = i + 2
        trunk_interface(tn)
        tn.close()
