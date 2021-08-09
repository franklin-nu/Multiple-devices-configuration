### Import modules

import time     # To pauses
import re       # To regex
import os
import io
import ipaddress  # Module for work with IP address range
import platform     # To check OS type
import subprocess   # To run OS commands, such "ping"
import getpass      # To input password in safe mode
import concurrent.futures # This is the module that will give us the ability to setup multi-threading.
#import textfsm      # To parse output of equipments
from pprint import pprint   # To usable print output
#from tabulate import tabulate    # To usable table output
#import xlsxwriter   # To save the files in Excel format
from netmiko import ConnectHandler      # To work with network equipment
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed   # Parallel work some processes
import json




with open ("/Users/franklin.pacheco/Documents/Networking/Python_Scripts/credenciales.json") as credenciales:
    devices=json.load(credenciales)

def get_input(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

for device in devices:
    net_connect = ConnectHandler(device_type=device['device_type'], ip=device['host'], 
                                username=device['username'], password=device['password'])
    Tstart = datetime.now()
    print("\n")
    print(Tstart)
    print("Starting running show commands on this device")
    print("\n Loading configuration..........")
    with open ("/Users/franklin.pacheco/Documents/Networking/Python_Scripts/show_commands.txt","r+") as x:
        x=net_connect.send_config_from_file("show_commands.txt")
    with open ("/Users/franklin.pacheco/Documents/Networking/Python_Scripts/Logs/Prechecks/DS01-07-HQ01-MX/DS01-07-HQ01-MX.txt","w+") as f:
        f.write(x)
    with open ("/Users/franklin.pacheco/Documents/Networking/Python_Scripts/Logs/Prechecks/DS02-07-HQ01-MX/DS02-07-HQ01-MX.txt","w+") as y:
        y.write(x)
    with open ("/Users/franklin.pacheco/Documents/Networking/Python_Scripts/Logs/Prechecks/SW01-07-HQ01-MX/SW01-07-HQ01-MX.txt","w+") as z:
        z.write(x)
    print("\n")
    print("Ending running show commands on this device this device", device['host'])
    print("\n ....Configuration loaded")
    print("\n")    
    Tend = datetime.now()
    Tdiff = Tend - Tstart
    print("Time taken to push the configuration = " + str(Tdiff))





