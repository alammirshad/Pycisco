#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from netmiko import connectHandler

cisco_CSR = {
	'device_type': 'cisco_ios'
	'host': '192.168.51.165'
	'username': 'root'
	'password': 'cisco'
	'port': 22 	#optional, defaults to
	}
#connectHandler is supporting dictionary format


	
