from netmiko import ConnectHandler

class Arp_inspection(object):
    def __init__(self,info_dict):
        self.info_dict = info_dict

    def ai_config(self):
        net_connect = ConnectHandler(**self.info_dict)
        net_connect.enable(cmd="enable 15")
        if self.info_dict["host"]=="192.168.1.1" or self.info_dict["host"]=="192.168.1.2":
            config_list = ["ip arp inspection vlan 5,6","interface range eth0/0-1","ip arp inspection trust"]
            net_connect.send_config_set(config_list)
            print("ip address "+self.info_dict["host"] + ":\n")
            print(net_connect.send_command("show ip arp inspection valn 5"))
            print(net_connect.send_command("show ip arp inspection valn 6"))
            print(net_connect.send_command("show ip arp inspection interfaces"))
        if self.info_dict["host"]=="192.168.2.9" or self.info_dict["host"]=="192.168.2.18":
            config_list = ["ip arp inspection vlan 7,8", "interface range eth0/0-1", "ip arp inspection trust"]
            net_connect.send_config_set(config_list)
            print("ip address " + self.info_dict["host"] + ":")
            print(net_connect.send_command("show ip arp inspection valn 5"))
            print(net_connect.send_command("show ip arp inspection valn 6"))
            print(net_connect.send_command("show ip arp inspection interfaces"))
        else:
            print("no such device in network")
