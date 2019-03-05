!/usr/bin/python
  
import sys
from jsonpath_rw import jsonpath, parse
import jsonpath
import boto3
import json

client = boto3.client('resourcegroupstaggingapi', region_name='ap-southeast-1')

response = client.get_resources(
    TagFilters=[
        {
            'Key': 'owner',
            'Values': [
                sys.argv[1],
            ]
        },
    ],
    ResourceTypeFilters=[
        'ec2:instance',
    ]
)

jpath = parse("$.ResourceTagMappingList[*].ResourceARN")
j_response = [match.value for match in jpath.find(response)]

for arn in j_response:
    tmp=(str(arn).split("/"))
    print(tmp[1])