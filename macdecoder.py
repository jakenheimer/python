#!/usr/bin/env python3.6

import requests
import pyperclip
import pprint

macURL = 'http://macvendors.co/api/%s'

r = requests.get(macURL % pyperclip.paste().strip())


pprint.pprint(r.json())

