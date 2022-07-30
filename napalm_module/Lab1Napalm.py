import napalm
driver = napalm.get_network_driver("ios")
#configuration_tehran
device_info_T = driver(hostname="192.168.56.200",username="hesam",password="tehrantrain",optional_args={"port":22})
device_info_T.open()
device_info_T.load_merge_candidate(filename="GRE-tehran.cfg")
print(device_info_T.compare_config())
device_info_T.commit_config()
device_info_T.close()
print("finish on Tehran")
#configuration_mashhad
device_info_T = driver(hostname="192.168.56.201",username="hesam",password="tehrantrain",optional_args={"port":22})
device_info_T.open()
device_info_T.load_merge_candidate(filename="GRE-qom.cfg")
print(device_info_T.compare_config())
device_info_T.commit_config()
device_info_T.close()
print("finish on Mashhad")
#configuration_qom
device_info_T = driver(hostname="192.168.56.202",username="hesam",password="tehrantrain",optional_args={"port":22})
device_info_T.open()
device_info_T.load_merge_candidate(filename="GRE-mashhad.cfg")
print(device_info_T.compare_config())
device_info_T.commit_config()
device_info_T.close()
print("finish on Qom")

