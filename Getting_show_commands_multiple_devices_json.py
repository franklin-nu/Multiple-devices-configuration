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



# Getting the json file from a directory

with open ("/Users/user.surname/your/directory/to/name.json") as json_file:   # .json file with all the credentials to connect to devices
    devices=json.load(json_file)


# Creating a loop to connect to all devices and running commands

for device in devices:
    
    net_connect = ConnectHandler(device_type=device['device_type'], ip=device['host'], 
                                username=device['username'], password=device['password'])
    
    Tstart = datetime.now()
    print("\n")
    print(Tstart)
    print('#'*100)
    print("Starting running show commands on this device", device['host'])
    print('#'*100)
    print("\n Loading configuration..........")
    
    with open ("/Users/user.surname/your/directory/to/show_commands.txt","r+") as x:                     # .txt file with all configuration to run
        x=net_connect.send_config_from_file("show_commands.txt")

    if "DS01-07-HQ01-MX#" in x:   
        with open ("/Users/user.surname/your/directory/to/DS01-07-HQ01-MX/DS01-07-HQ01-MX.txt","w+") as f:
            f.write(x)
    elif "DS02-07-HQ01-MX#" in x:
        with open ("/Users/fuser.surname/your/directory/to/DS02-07-HQ01-MX/DS02-07-HQ01-MX.txt","w+") as y:
            y.write(x)
    elif "SW01-07-HQ01-MX#" in x:    
        with open ("/Users/user.surname/your/directory/to/SW01-07-HQ01-MX/SW01-07-HQ01-MX.txt","w+") as z:
            z.write(x)
    
    print("\n")
    print("Ending running show commands on this device this device", device['host'])
    print("\n ....Configuration loaded")
    print("\n")    
    Tend = datetime.now()
    Tdiff = Tend - Tstart
    print("Time taken to push the configuration = " + str(Tdiff))





