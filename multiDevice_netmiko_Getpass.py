#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko
#multi vendor library

from getpass import getpass
sec = getpass("Please enter password for the device: ") 
#accept password without showing on screen

device1 = {
	'device_type': 'cisco_ios',
	'host': '192.168.51.10',
	'username': 'root',
	'password': sec,
	'port': 22 	#optional, defaults to
	}

device2 = {
        'device_type': 'cisco_ios',
        'host': '192.168.51.166',
        'username': 'root',
        'password': sec,
        'port': 22      #optional, defaults to
        }

device3 = {
        'device_type': 'cisco_ios',
        'host': '192.168.51.168',
        'username': 'root',
        'password': sec,
        'port': 22      #optional, defaults to
        }

for i in [device1, device2, device3] :
	try:
		print("connecting with Router : ---->", i['host'])
		device_connect = netmiko.ConnectHandler(**i)
		#sending Command
		output = device_connect.send_command("sh ip int br")
		print(output)
		print("*************************************")
		print("_____________________________________")
		print("_____________________________________")
	
	except (TimeoutError, netmiko.ssh_exception.NetMikoTimeoutException) :
		print("Please check your IP or network device :", i['host'])
		
		
	






