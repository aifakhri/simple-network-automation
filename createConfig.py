from jinja2 import Environment, FileSystemLoader



CONFIG_TEMPLATE = "vxlan_irb_template.txt"
CONFIG_DIRECTORY = "config_template/"


def create_config(deviceData):
    config_data = {}
    config_data["vrfName"] = deviceData["customers"]["customer03"]["vrf"]
    config_data["vlanId"] = deviceData["customers"]["customer03"]["vlan"]
    config_data["vniId"] = deviceData["customers"]["customer03"]["vni"]
    config_data["customerNetwork"] = deviceData["customers"]["customer03"]["allocatedNetwork"]
    config_data["anycastGw"] = deviceData["customers"]["customer03"]["allocatedGw"]
    config_data["anycastGwSubnet"] = deviceData["customers"]["customer03"]["allocatedSubnet"]
    config_data["remoteVtep"] = deviceData["vxlans"]["interface"]["remoteVtep"]
    config_data["vxlanInt"] = deviceData["vxlans"]["interface"]["intName"]
    config_data["localAs"] = deviceData["routing"]["bgp"]["localAs"]
    

    env = Environment(loader=FileSystemLoader(CONFIG_DIRECTORY))
    config_file = env.get_template(CONFIG_TEMPLATE)
    

    return config_file.render(config_data)