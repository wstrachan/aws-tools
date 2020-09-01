#!/usr/bin/env python3


import boto3
import sys

# specify AWS keys
auth = {"aws_access_key_id": "<key_id>", "aws_secret_access_key": "<access_key>"}

# convert user input into a list
def processInput(string):
    li = list(string.split(" ")) 
    return li

# instance_id = processInput(input("Enter instance id: "))

instance_id = processInput(sys.argv[2])

def main():
    # read arguments from the command line and 
    # check whether at least two elements were entered
    if len(sys.argv) < 2:
	    print("Usage: python3 ec2-start-stop.py {start|stop}\n")
	    sys.exit(0)
    else:
	    action = sys.argv[1] 

    if action == "start":
	    startInstance()
    elif action == "stop":
    	stopInstance()
    else:
    	print("Usage: python3 ec2-start-stop.py {start|stop}\n")

def startInstance():
    print("Starting the instance...", instance_id)

    # change "us-east-1" region if different
    try:
        ec2 = boto3.client('ec2', region_name='us-east-1')

    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    # change instance ID appropriately  
    try:
         ec2.start_instances(InstanceIds=instance_id)

    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

def stopInstance():
    print("Stopping the instance...", instance_id)

    try:
        ec2 = boto3.client('ec2', region_name='us-east-1')

    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
         ec2.stop_instances(InstanceIds=instance_id)

    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

if __name__ == '__main__':
    main()