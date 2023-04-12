import psutil
import platform
import subprocess
import wmi
from datetime import datetime
"""system information"""
now = datetime.now()



dt_string = now.strftime("%H_%M_%S")
print("date and time =", dt_string)
dt_string="network_"+dt_string+".txt"

# # traverse the software list
Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(Data)
f = open(dt_string, "w")

try:
    for i in range(len(a)):
        buffer = (a.split("\\r\\r\\n")[i])
        f.write(buffer)

except IndexError as e:
 	print("All Done")

"""network_information"""
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
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            str2=(f"  IP Address: {address.address}\n")+(f"  Netmask: {address.netmask}\n")+(f"  Broadcast IP: {address.broadcast}\n")
            f.write(str2)
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            str2=(f"  MAC Address: {address.address}\n")+(f"  Netmask: {address.netmask}\n")+(f"  Broadcast MAC: {address.broadcast}\n")
            f.write(str2)
# get IO statistics since boot
net_io = psutil.net_io_counters()
str2=(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n")
f.write(str2)
str2=(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
f.write(str2)
