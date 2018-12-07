#!/usr/bin/python

import sys
from jsonpath_rw import parse
import boto3
from vars import *

client = boto3.client('resourcegroupstaggingapi', region_name='us-east-1', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

response = client.get_resources(
    TagFilters=[
        {
            'Key': 'Environment',
            'Values': [
                sys.argv[1],
            ]
        },
        {
            'Key': 'Service',
            'Values': [
                sys.argv[2],
            ]
        },
    ],
    ResourceTypeFilters=[
        'elasticloadbalancing',
    ]
)

jpath = parse("$.ResourceTagMappingList[*].ResourceARN")
j_response = [match.value for match in jpath.find(response)]
tmp1=str(j_response).lstrip("[\'u\'").rstrip("\']'")

tmp2 = tmp1.split(':')
notg = tmp2.count('aws')
result = str(tmp2).split('/')

z = 1
while z < (notg*2)+1:
    print(result[z])
    z = z+2