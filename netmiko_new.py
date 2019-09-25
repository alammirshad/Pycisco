#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko

device1 = {
	'device_type': 'cisco_ios',
	'host': '192.168.51.165',
	'username': 'root',
	'password': 'cisco',
	'port': 22 	#optional, defaults to
	}
device_connect = netmiko.ConnectHandler(**device1)
print([i for i in dir(device_connect) if 'send' in i])

# now sending configuration for devices

conf = ["int lo3", "ip add 3.3.3.3 255.255.255.255","exit"]
output = device_connect.send_config_set(conf)
print(output)

# sending config from file.

output1 = device_connect.send_config_from_file('myrouter.txt')
print(output1)



	
