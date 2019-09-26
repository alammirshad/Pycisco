#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import requests

from requests.auth import HTTPBasicAuth

# This is for supplying http basic authentication

cred = HTTPBasicAuth('root', 'cisco')

h = {'Accept' : 'application/json'}
#headers = {'Accept' : 'text/html'}
url = "http://192.168.51.165/level/15/exec/-/sh/run/CR"

# Now connection to restconf -OR --http protocol

output = requests.get(url, headers = h, auth = cred)
print(output)
# only giving HTTP response code
print(output.text)
# giving HTMP based response

