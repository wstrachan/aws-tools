#!/usr/bin/env python3

import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
# vpc = ec2.Vpc("vpc-716d5814")

# inst_names = [tag['Value'] for i in vpc.instances.all() for tag in i.tags if tag['Key'] == 'Name']
# print(inst_names)

instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'terminated', 'running']}])

for instance in instances:
    print(instance.id, instance.instance_type)

