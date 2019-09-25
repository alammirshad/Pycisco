#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import paramiko, time

#using as ssh client
client = paramiko.SSHClient()
# auto adjust host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# time for connecting to remote cisco IOS.
addr = input("Enter your router IP:")
u = "root"
p = "cisco"
#connected with ssh session
client.connect(addr, username = u, password = p, allow_agent = False, look_for_keys = False)
# we have to ask for shell
device_access = client.invoke_shell()
# now sending command
device_access.send("show ip int br \n")
time.sleep(1)
# assume command got executed, so lets recieve data
output = device_access.recv(65000)
print(type(output))
print(output.decode('ascii'))


