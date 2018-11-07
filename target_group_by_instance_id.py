#!/usr/bin/python

import sys
from jsonpath_rw import jsonpath, parse
import jsonpath
import boto3
import json
client = boto3.client('elbv2', region_name='ap-southeast-1')

response = client.describe_target_groups()
jpath = parse("$.TargetGroups[*].TargetGroupArn")
results = [match.value for match in jpath.find(response)]

output={}

no_tg = len(results)

for i in range(no_tg):
  tgpath = parse('$.TargetGroups['+str(i)+'].TargetGroupName')
  tgname = [match.value for match in tgpath.find(response)]

  jpath = parse("$.TargetGroups["+str(i)+"].TargetGroupArn")
  tmp1 = [match.value for match in jpath.find(response)]
  tmp2 = client.describe_target_health(TargetGroupArn=results[i],)
  jpath1 = parse("$.TargetHealthDescriptions[*].Target.Id")
  result = [match.value for match in jpath1.find(tmp2)]
  if len(result) > 1:
    for o in range(len(result)):
      striped=[x.strip() for x in str(result).split(',')]
      #print(striped[o])
      test_tmp0=str(striped[o]).lstrip("[\'")
      test_tmp0=str(test_tmp0).rstrip("\']'")
      test_tmp1=str(tgname).lstrip("[\'")
      test_tmp1=str(test_tmp1).rstrip("\']'")
      output[test_tmp0]=test_tmp1
  else:
      test_tmp0=str(result).lstrip("[\'")
      test_tmp0=str(test_tmp0).rstrip("\']'")

      test_tmp1=str(tgname).lstrip("[\'")
      test_tmp1=str(test_tmp1).rstrip("\']'")
      output[test_tmp0]=test_tmp1
final_op=(output)
op_path = parse("$."+sys.argv[1])
op=[match.value for match in op_path.find(final_op)]
op=str(op).lstrip("[\'")
op=str(op).rstrip("\']'")
print(op)
