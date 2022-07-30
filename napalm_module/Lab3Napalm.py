from napalm import get_network_driver
import yaml
from threading import Thread

def config(info_driver,filename):
    info_driver.open()
    info_driver.load_merge_candidate(filename=filename)
    info_driver.commit_config()

def traceroute(info_driver,destination,source,ttl=258,timeout=2):
    info_driver.open()
    print(yaml.dump(info_driver.traceroute(destination=destination,source=source,ttl=ttl,timeout=timeout)))
    print("##############################################################################################")

driver = get_network_driver("ios")
dr_tehran = driver(hostname="192.168.56.200",username="hesam",password="tehrantrain")
dr_mashhad = driver(hostname="192.168.56.201",username="hesam",password="tehrantrain")
dr_qom = driver(hostname="192.168.56.202",username="hesam",password="tehrantrain")

TH = []
TH.append(Thread(target=config,args=(dr_tehran,"tehran_IPSEC_VTI.cfg",)))
TH.append(Thread(target=config,args=(dr_mashhad,"mashhad_IPSEC_VTI.cfg",)))
TH.append(Thread(target=config,args=(dr_qom,"qom_IPSEC_VTI.cfg",)))

for i in range(len(TH)):
    TH[i].start()

for i in range(len(TH)):
    TH[i].join()


TH = []
TH.append(Thread(target=traceroute,args=(dr_tehran,"192.168.2.254","192.168.1.254",)))
TH.append(Thread(target=traceroute,args=(dr_mashhad,"192.168.3.254","192.168.2.254",)))
TH.append(Thread(target=traceroute,args=(dr_qom,"192.168.2.254","192.168.3.254",)))

for i in range(len(TH)):
    TH[i].start()

for i in range(len(TH)):
    TH[i].join()

