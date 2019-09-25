#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import netmiko, time

device1 = {
	'device_type': 'cisco_ios',
	'host': '192.168.51.165',
	'username': 'root',
	'password': 'cisco',
	'port': 22 	
	}
device_connect = netmiko.ConnectHandler(**device1)
output = device_connect.send_command("show ip int br")
output1 = device_connect.send_command("show ip int br", use_textfsm=True)
print(output)
print(output1)

for i in output1 :
	print("My interface name is ", i['intf'], "with IP " , i['ipaddr'], "having status up", i['status'])
	time.sleep(1)




	
