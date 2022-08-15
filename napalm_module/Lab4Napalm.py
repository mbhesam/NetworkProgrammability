from napalm import get_network_driver

class DMVPN(object):
    def __init__(self,hostname,username,password,driver,file_config):
        self.hostname=hostname
        self.username=username
        self.password=password
        self.driver=driver
        self.config_file=file_config
    def config(self):
        info_driver=self.driver(hostname=self.hostname,username=self.username,password=self.password)
        info_driver.open()
        info_driver.load_merge_candidate(filename=self.config_file)
        info_driver.commit_config()
        info_driver.close()

if __name__=="__main__":
    driver = get_network_driver("ios")
    tehran_obj= DMVPN(hostname="192.168.56.200",username="hesam",password="tehrantrain",driver=driver,file_config="tehran_DMVPN.cfg")
    mashhad_obj= DMVPN(hostname="192.168.56.201",username="hesam",password="tehrantrain",driver=driver,file_config="mashhad_DMVPN.cfg")
    qom_obj= DMVPN(hostname="192.168.56.202",username="hesam",password="tehrantrain",driver=driver,file_config="qom_DMVPN.cfg")
    tehran_obj.config()
    qom_obj.config()
    mashhad_obj.config()
