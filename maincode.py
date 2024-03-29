import psutil
import platform
import subprocess
import wmi
from datetime import datetime
"""system information"""
now = datetime.now()









        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")


















dt_string = now.strftime("%H_%M_%S")
print("date and time =", dt_string)
dt_string=dt_string+".txt"
#network file name 
var="network_"+dt_string
#system info file name
var2="system_"+dt_string
#memory usage fname
var3="memory_"+dt_string
#events log fname
var4="eventlogs_"+dt_string
#process dump
var1="pinfo_"+dt_string
# # traverse the software list
Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(Data)
f = open(var1, "w")

try:
    for i in range(len(a)):
        buffer = (a.split("\\r\\r\\n")[i])
        f.write(buffer)

except IndexError as e:
 	print("All Done")

"""---------------------------------------network_information---------------------------------------------------"""
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Network information
f1=open(var,"w")
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        
        f1.write(f"=== Interface: {interface_name} ===\n")
        if str(address.family) == 'AddressFamily.AF_INET':
            str2=(f"  IP Address: {address.address}\n")+(f"  Netmask: {address.netmask}\n")+(f"  Broadcast IP: {address.broadcast}\n")
            f1.write(str2)
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            str2=(f"  MAC Address: {address.address}\n")+(f"  Netmask: {address.netmask}\n")+(f"  Broadcast MAC: {address.broadcast}\n")
            f1.write(str2)
# get IO statistics since boot
net_io = psutil.net_io_counters()
str2=(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n")
f1.write(str2)
str2=(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
f1.write(str2)
