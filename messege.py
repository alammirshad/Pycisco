#!/usr/bin/python3
  
from time import ctime,sleep
# only importing desired function
from subprocess import getstatusoutput,getoutput
from os import mkdir


options= '''press 1 to check current date and time:
    press 2 to run any command in your current OS:
    press 3 to create a directory
    press 4 to start a train
    press 5 ping any website '''

print(options)
# to capture input from user
choice = input()
print("You have chosen:", choice)
#conditional Statement with if
if choice == '1' :
    print(ctime())
elif int(choice) == 2 :
    cmd = input("Please enter any command:")
    output = getoutput(cmd)
    print(output)
elif choice == '3'  :
    d_name = input("Enter directory to create:")
    mkdir(d_name)
    print(d_name, "successfully created")
    # homework: give a message if directory is already present and ask for another name.
elif choice == '5'  :
    web = input("Enter Webesite name to ping:")
    print(getoutput("ping -c 5 "+web))



else :
    print("Wrong option")

