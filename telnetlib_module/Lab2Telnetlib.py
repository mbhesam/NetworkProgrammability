from telnetlib import Telnet
from termcolor import colored
from time import sleep
device_file = open("devices.txt", "r")
device_file.readline()
info_list = device_file.read().split("\n")
security_file = open("Security_conmands.txt" , "r")
security_file.readline()
info_security = security_file.read().split("\n")
for i in range(10):
    each_info = info_list[i].split()
    try:
        tn = Telnet(each_info[0], timeout=1)
    except:
        print colored("connection refused " +each_info[0] ,"red")
    else:
        print colored("connection stablished" +each_info[0], "green")

    try:
        tn.read_until("Username: ")
        tn.write(each_info[1]+"\n")
        sleep(0.5)
    except:
        print colored("user or pass is not correct for " + each_info[0], "red")
    tn.write("en \n")
    sleep(0.5)
    tn.write(each_info[3] + "\n")
    sleep(0.5)
    tn.write("terminal length 0 \n")
    sleep(0.5)
    tn.write("conf t \n")
    sleep(0.5)
    for i in range(6):
        tn.write(info_security[i] + "\n")
        sleep(0.5)
    tn.write("end \n")
    sleep(0.5)
    tn.write("show run \n")
    print tn.read_all()
    tn.close()
device_file.close()


