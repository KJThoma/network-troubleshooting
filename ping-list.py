#!/usr/bin/python3
# This script will check availability of a list of hosts.

# Module to run the ping command
import subprocess

# List of IP's to ping
ip_list = ['192.168.1.254', '192.168.1.240', '192.168.1.9', '8.8.8.8']

# Adding some ---- for nicer formatting
print('-' * 40)

# For loop to ping objects in List
# Popen ping sending 5 requests and PIPE to hide stdout for cleaner results
# wait for the results
# Poll to check process response and print results, 0 is successful(or UP)
for ip in ip_list:
    ping = subprocess.Popen(['ping', '-c', '5', ip], stdout=subprocess.PIPE)

    ping.wait()

    if ping.poll() == 0:
        print(ip + ' is UP')
    else:
        print(ip + ' is DOWN')

print('-' * 40)
