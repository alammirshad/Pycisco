#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko #Multivendor

device1 = {
	'device_type': 'cisco_ios',
	'host': '192.168.51.165',
	'username': 'root',
	'password': 'cisco',
	'port': 22 	#optional, defaults to
	}

device2 = {
        'device_type': 'cisco_ios',
        'host': '192.168.51.166',
        'username': 'root',
        'password': 'cisco',
        'port': 22      #optional, defaults to
        }

device3 = {
        'device_type': 'cisco_ios',
        'host': '192.168.51.168',
        'username': 'root',
        'password': 'cisco',
        'port': 22      #optional, defaults to
        }

for i in [device1, device2, device3] :
	print("connecting with Router : ---->", i['host'])
	device_connect = netmiko.ConnectHandler(**i)
	#sending Command
	output = device_connect.send_command("sh ip int br")
	print(output)
	print("*************************************")
	print("_____________________________________")
	print("_____________________________________")
		





	
