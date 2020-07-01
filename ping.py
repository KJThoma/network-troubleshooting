#!/usr/bin/python3
# Ping.py This script will check availability of a list of hosts in the hosts.txt file.

# Module to run the ping command
import subprocess

# Empty list where we'll store IPs
ip_list = []

# Open file with lists of IPs
with open('hosts.txt', 'r') as hosts_file:
    for ip in hosts_file:
        ip_list.append(ip.split('\n')[0])

# Adding some ---- for nicer formatting
print('-' * 30)

# For loop to ping objects in List
# Popen ping sending 5 requests and PIPE to hide stdout for cleaner results
# Wait for the results
# Poll to check process response and print results, 0 is successful(or UP)
for ip in ip_list:
    ping = subprocess.Popen(['ping', '-c', '5', ip], stdout=subprocess.PIPE)
    ping.wait()
    if ping.poll() == 0:
        print(ip + ' is UP')
    else:
        print(ip + ' is DOWN')

# Adding some ---- for nicer formatting
print('-' * 30)

# Close file
hosts_file.close()
