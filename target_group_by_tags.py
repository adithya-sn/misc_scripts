#!/usr/bin/python

import sys
from jsonpath_rw import jsonpath, parse
import boto3
from vars import *
print(AWS_ACCESS_KEY_ID)
'''
client = boto3.client('resourcegroupstaggingapi', region_name='ap-southeast-1')

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
#    ResourcesPerPage=2,
    ResourceTypeFilters=[
        'elasticloadbalancing',
    ]
)

jpath = parse("$.ResourceTagMappingList[*].ResourceARN")
j_response = [match.value for match in jpath.find(response)]
#print(j_response)
tmp1=str(j_response).lstrip("[\'u\'")
tmp1=str(tmp1).rstrip("\']'")
#print(tmp1)

tmp2 = tmp1.split(':')
notg = tmp2.count('aws')
#print(tmp2)
result = str(tmp2).split('/')
#print(tmp2)
z = 1
if notg > 1:
  while z < (notg*2)+1:
    print(result[z])
    z = z+2
else:
  print(result[1])
'''