from netmiko import ConnectHandler


def connect_to_device(data):
    connection_info  = data["virtualBox"]
    device = {
        "host": connection_info["vmManagement"]["hostIp"],
        "port": connection_info["vmManagement"]["hostPort"],
        "username": connection_info["vmManagement"]["username"],
        "password": connection_info["vmManagement"]["password"],
        "device_type": connection_info["vmType"],
        "global_delay_factor": 2,
    }
    return ConnectHandler(**device)