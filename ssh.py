import sys
import os, json
import netmiko
import time
from pprint import pprint
from netmiko import ConnectHandler
import ntc_templates
import textfsm
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
#from dotenv import load_dotenv
import subprocess
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import SSHException

##print('Bien moi truong la: ',os.environ['NET_TEXTFSM'])

with open(r"IPAddressList.txt", "r") as ip_addr:
    devices = []
    for ip_device in ip_addr:
        devices.append(ip_device)
# Import username and password from file
#with open ("cisco_credentials.txt ", 'w') as f:
#  f.write("tranhuyhoang_v\n")
#  f.write("12345a@")
credential = open(r'cisco_credentials.txt','r')
a = credential.readlines()
username = a[0].strip()
password = a[1].strip()
# Enable_Pass = input("What's the enable password:")

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
    for ip in devices:
        Network_Device = {"host": ip,
                     "username": username,
                     "password": password,
                     "device_type": "cisco_ios",
                     #"secret": Enable_Pass,
                     }

    #Connect_to_Device = ConnectHandler(**Network_Device)
    #result = Connect_to_Device.send_command(devices, ["show ip int brief | in up", "sh int des"])
        result = send_show_command(Network_Device, ["sh clock", "sh ip int br | in up", "sh int des","sh run | in snmp"])
        print(ip)
        pprint(result, width=120)

