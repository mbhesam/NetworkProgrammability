from napalm import get_network_driver
from termcolor import colored

driver = get_network_driver("ios")
device_info = []
for i in range(3):
    device_info.append(driver(hostname="192.168.56.20"+str(i),username="hesam",password='tehrantrain'))
    device_info[i].open()
    if i == 0:
        device_info[i].load_merge_candidate(filename="IPSEC-cfg-CE-tehran.txt")
        print(colored(device_info[i].compare_config(),"red"))
        device_info[i].commit_config()
        device_info[i].close()
        print("########################################################################################")
    elif i == 1:
        device_info[i].load_merge_candidate(filename="IPSEC-cfg-CE-mashhad.txt")
        print(colored(device_info[i].compare_config(), "blue"))
        device_info[i].commit_config()
        device_info[i].close()
        print("########################################################################################")
    else:
        device_info[i].load_merge_candidate(filename="IPSEC-cfg-CE-qom.txt")
        print(colored(device_info[i].compare_config(), "yellow"))
        device_info[i].commit_config()
        device_info[i].close()
        print("########################################################################################")

