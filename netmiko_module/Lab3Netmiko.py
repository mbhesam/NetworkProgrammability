import arp_inspection_module

Switch1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "Switch1",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

Switch2 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.2",
    "username": "Switch2",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

Switch3 = {
    "device_type": "cisco_ios",
    "host": "192.168.2.9",
    "username": "Switch3",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

Switch4 = {
    "device_type": "cisco_ios",
    "host": "192.168.2.18",
    "username": "Switch4",
    "password": "tehrantrain",
    "port": 22,
    "secret": "tehrantrain"
}

sw1_obj=arp_inspection.Arp_inspection(Switch1)
sw1_obj.ai_config()
sw2_obj=arp_inspection.Arp_inspection(Switch2)
sw2_obj.ai_config()
sw3_obj=arp_inspection.Arp_inspection(Switch3)
sw3_obj.ai_config()
sw4_obj=arp_inspection.Arp_inspection(Switch4)
sw4_obj.ai_config()
