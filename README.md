# Network Troubleshooting Scripts

# findIPs.py
This script checks for any IPv4 addresses copied to the clipboard, it then prints results on the screen to confirm, and outputs them on new lines in a ./hosts.txt file. In my current task, I then run the ping.py script here on the IPs in the hosts.txt file.

# ping.py
Simple script that will check if host IPs are reachable via ICMP, prints a clean output of results. Current commit has it acting on IPv4 addresses in a ./hosts.txt file, seperated by new lines.
