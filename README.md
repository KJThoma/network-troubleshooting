# Network Troubleshooting

Welcome to my network-troubleshooting repo. This a space for scripts to simplify or automate some network troubleshooting steps I go through regularly.

# ping.py
Simple script that prints a clean output of results on screen. Current commit has it acting on IPv4 addresses in a hosts.txt file, seperated by new lines.

# findIPs.py
This script uses a regular expression on any text copied to the clipboard searching for IPv4 addresses. It then prints results on the screen to confirm, and outputs them on new lines in a hosts.txt file. In my current task, I then run the ping.py script here on the IPs in the hosts.txt file.
