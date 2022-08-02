import yaml
import os

from netmikoSession import connect_to_device
from createConfig import create_config


DIR = "device_info/"
DEVICES = os.listdir(DIR)


# Function to load YAML file
def load_dev_data(devicefl):
    return yaml.load(open(devicefl), Loader=yaml.Loader)



### Change Configuration Section
for i, device in enumerate(DEVICES, start=1):
    config_file_name = f"vxlan_config_device0{i}.txt"
    
    data = load_dev_data(DIR+device) 
    
    config_data = create_config(data)
    with open(config_file_name, 'w') as confl:
        confl.write(config_data)

    connect = connect_to_device(data)
    connect.enable()
    response = connect.send_config_from_file(config_file_name)

    print(response, end=" ")

    connect.disconnect()


### Gather Information Section
for i, device in enumerate(DEVICES, start=1):
    data = load_dev_data(DIR+device)
    connect = connect_to_device(data)
    with open(f"verification_device0{i}.txt", "w") as fl:
        fl.write("\n========================\n")
        fl.write(connect.send_command("show interface vxlan1"))
        fl.write("\n========================\n")
        fl.write(connect.send_command("show vxlan vni"))
        fl.write("\n========================\n")
        fl.write(connect.send_command("show bgp evpn"))

    connect.disconnect()



if __name__ == "__main__":
    pass