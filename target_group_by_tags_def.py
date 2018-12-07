#!/usr/bin/python

import sys
from jsonpath_rw import parse
import boto3
from vars import *

def get_tg(val_1, val_2):

    client = boto3.client('resourcegroupstaggingapi', region_name='us-east-1', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    response = client.get_resources(
        TagFilters=[
            {
                'Key': 'Environment',
                'Values': [
                    val_1,
                ]
            },
            {
                'Key': 'Service',
                'Values': [
                    val_2,
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
    no_of_tg = tmp2.count('aws')
    result = str(tmp2).split('/')

    z = 1
    while z < (no_of_tg*2)+1:
        print(result[z])
        z = z+2
    return

get_tg(sys.argv[1], sys.argv[2])