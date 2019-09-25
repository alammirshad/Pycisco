#!//Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from napalm import get_network_driver
driver = get_network_driver('ios')
device =driver('192.168.51.165', 'root', 'cisco')
device.open()

#merging configuration

print(device.load_merge_candidate(filename='myrouter.txt'))

# check the diff

print(device.compare_config())

# now to commit the applied config
c = input("Confirm with y/n to apply the configuration :")
if c == 'y' or c == 'Y' :
	print("Committing Configuration")
	device.commit_config()
	res = input("Do you want to rollback, press y/n :")
	if res == 'y' or res == 'Y':
		device.rollback()
		print("Rollback Completed")
	else :
		print("No Rollbacks applied")

elif c == 'n' or c == 'N' :
	print("Discarding the configuration")
	device.discard_config()
else :
	print("Please type only y|Y or n|N")










