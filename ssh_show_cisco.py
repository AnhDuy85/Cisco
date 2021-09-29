from pprint import pprint
#import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

if __name__ == "__main__":
    device = {
        "device_type": "cisco_ios_ssh",
        "host": "10.4.7.58",
        "username": "truongtrilinh_a",
        "password": "12345a@"
        #"secret": "cisco",
    }
    ssh_connect = ConnectHandler(**device)
    result = send_show_command(device, ["sh clock detail\n"])
    #result = send_show_command(device, ["sh clock\n", "sh ip int br | in up\n", "sh int des | in up\n","sh run | in snmp"])
    pprint(result, width=120)
    commands = ['config t','clock timezone UTC +7']
    result = ssh_connect.send_config_set(commands)
    pprint(result, width=120)
