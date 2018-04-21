#!/usr/bin/env python
import boto3, sys, os, time

ec2 = boto3.resource('ec2')
user_data_shell = """#!/bin/bash
yum install httpd -y
yum update -y
echo "<html><body><h1> Automation for the people </h1></body></html>" >> /var/www/html/index.html
service httpd start
chkconfig httpd on"""
myInstance = ''
def createEC2Instance():
    instance = ec2.create_instances(
        ImageId='ami-bf5540df',
        MinCount=1,
        MaxCount=1,
        InstanceType='m3.medium', UserData=user_data_shell)
    print instance[0].id



def scriptrun():
    print "test bootable script"
#ListInstance
def listInstance:
    for instance in ec2.instances.all():
        print instance.id, instance.state
        print "Instance creation successful"

#Terminate Instance
def terminateInstance():
    for instance_id in sys.argv[1:]:
        instance = ec2.Instance(instance_id)
        response = instance.terminate()
        print response

def main():


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print >> sys.stderr, "Error parsing command arguments: %s" % e
        #remove_local_files()
        sys.exit(1)

