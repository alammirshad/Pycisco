#!/usr/bin/env python3

'''
x = input("type number :")
print(x)
'''

import sys
from time import sleep

sum = 0

data = sys.argv[1:]
for i in data  :
    sum = sum + int(i)
print(sum)




