#!/usr/bin/env bash

function create_ec2_instance {
	REGIONS=('us-west-1')
	STNAME='mysite'

	for r in ${REGIONS[*]};
	do
		aws cloudformation create-stack --stack-name $STNAME \
		--template-body file:///Users/symcprasad/Desktop/miniproject.yaml --region $r
	done

	for r in ${REGIONS[*]};
	do
		aws cloudformation wait stack-create-complete --stack-name $STNAME --region $r
	done
}


echo "run tests"
create_ec2_instance
echo "Completed creating EC2 instance"
#aws cloudformation create-stack --stack-name mysite --template-body file:///Users/symcprasad/Desktop/miniproject.yaml --region us-west-1
#aws cloudformation wait stack-create-complete --stack-name mysite
#aws cloudformation describe-stacks --stack-name mysite --region us-west-1 --query 'Stacks[*].StackStatus' --output text