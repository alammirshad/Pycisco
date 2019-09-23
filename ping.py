#!/usr/bin/env python3

import sys
from subprocess import getoutput

data = sys.argv[1:]

for i in data  :
    print("PING request for server : "+i)
    print(getoutput("ping -c 3  "+i))
    print("____________________________")
    print("____________________________")

