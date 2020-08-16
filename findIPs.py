#!/usr/bin/python3
# findIPs.py - This program will check clipboard and extract IPv4 addresses on new lines to the hosts.txt file.

import pyperclip, re

# Create IP regex.
IPRegex = re.compile(r'''(
    (\d{2,3})+          # First Octet
    .                   # First seperator
    (\d{1,3})+          # Second Octet
    .                   # Second seperator
    (\d{1,3})+          # Third Octet
    .                   # Third seperator
    (\d{1,3})+          # Fourth Octet
    )''', re.VERBOSE)

# Find matches in clipboard text and group them.
text = str(pyperclip.paste())
matches = []
for groups in IPRegex.findall(text):
    matches.append(groups[0])

# Print the copied IPs to confirm the output.
if len(matches) > 0:
    print('IPs copied to the hosts.txt file:')
    print('\n'.join(matches))
else:
    print('No IPs found.')

# Write matches into the hosts.txt file on new lines.
with open('hosts.txt', 'w') as hosts_file:
    hosts_file.writelines("%s\n" % host for host in matches)
