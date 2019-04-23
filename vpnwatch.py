#!/usr/bin/env python3

import requests
import socket
import os


r = requests.get('http://icanhazip.com')

myIP = socket.gethostbyaddr(r.text)

if 'windstream' in myIP[0]:
	os.system('reboot')
else:
	exit
