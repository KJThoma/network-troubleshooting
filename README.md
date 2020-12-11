# Network Troubleshooting Scripts

# findIPs.py
This script uses a regular expression on any text copied to the clipboard searching for IPv4 addresses. It then prints results on the screen to confirm, and outputs them on new lines in a ./hosts.txt file. In my current task, I then run the ping.py script here on the IPs in the hosts.txt file.

# ping.py
Simple script that prints a clean output of results on screen. Current commit has it acting on IPv4 addresses in a ./hosts.txt file, seperated by new lines.
