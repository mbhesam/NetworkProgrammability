import paramiko
from time import sleep
import threading

def tune_stp_root(ip_addr, username, password, en_pass):
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    session.connect(hostname=ip_addr,username=username,password=password,look_for_keys=False,allow_agent=False)
    connection = session.invoke_shell()
    connection.send("en \n")
    sleep(0.5)
    connection.send("conf t \n")
    sleep(0.5)
    connection.send("spanning-tree backbonefast \n")
    sleep(0.5)
    connection.send("spanning-tree vlan 5 priority 4096 \n")
    sleep(0.5)
    connection.send("spanning-tree vlan 6 priority 4096 \n")
    sleep(0.5)
    session.close()

def tune_stp_access(ip_addr, username, password, en_pass):
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    session.connect(hostname=ip_addr,username=username,password=password,look_for_keys=False,allow_agent=False)
    connection = session.invoke_shell()
    connection.send("en \n")
    sleep(0.5)
    connection.send("conf t \n")
    sleep(0.5)
    connection.send("spanning-tree backbonefast \n")
    sleep(0.5)
    connection.send("spanning-tree uplinkfast \n")
    sleep(0.5)
    connection.send("int range e1/1-3 \n")
    sleep(0.5)
    connection.send("spanning-tree portfast \n")
    sleep(0.5)
    connection.send("spanning-tree bpduguard enable \n")
    sleep(0.5)
    session.close()

def tune_stp_distr(ip_addr, username, password, en_pass):
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    session.connect(hostname=ip_addr,username=username,password=password,look_for_keys=False,allow_agent=False)
    connection = session.invoke_shell()
    connection.send("en \n")
    sleep(0.5)
    connection.send("conf t \n")
    sleep(0.5)
    connection.send("spanning-tree backbonefast \n")
    sleep(0.5)
    session.close()

if __name__ == '__main__':
    ip_addr_access = ["192.168.1.1","192.168.1.2","192.168.1.17","192.168.1.18"]
    username_access = ["Switch1","Switch2","Switch3","Switch4"]

    ip_addr_root = ["192.168.1.3","192.168.1.19"]
    username_root = ["MLS1","MLS3"]

    ip_addr_distr = ["192.168.1.4","192.168.1.20"]
    username_distr = ["MLS2","MLS4"]

    TH = []
    for i in range(len(ip_addr_access)):
        thr =  threading.Thread(target=tune_stp_access,args=(ip_addr_access[i],username_access[i],"tehrantrain","tehrantrain",))
        thr.start()
        TH.append(thr)

    for i in range(len(ip_addr_root)):
        thr =  threading.Thread(target=tune_stp_root,args=(ip_addr_root[i],username_root[i],"tehrantrain","tehrantrain",))
        thr.start()
        TH.append(thr)

    for i in range(len(ip_addr_distr)):
        thr =  threading.Thread(target=tune_stp_distr,args=(ip_addr_distr[i],username_distr[i],"tehrantrain","tehrantrain",))
        thr.start()
        TH.append(thr)

