#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko #Multivendor

cisco_CSR = {
	'device_type': 'cisco_ios',
	'host': '192.168.51.165',
	'username': 'root',
	'password': 'cisco',
	'port': 22 	#optional, defaults to
	}
#connectHandler supports dictionary format
# to connect target device use ConnectHandler
# By checking couple of things ConnectHandler will allow you to connect
'''
	device_type
'''
device_connect = netmiko.ConnectHandler(**cisco_CSR)
#print([i for i in dir(device_connect) if 'send' in i])

# now sending command
cmd = ["show ip int br", "show version"]
for i in cmd:
	print("Sending Commands: ",i)
	print("___________________")
	output = device_connect.send_command(i)	
	print(output)


	
