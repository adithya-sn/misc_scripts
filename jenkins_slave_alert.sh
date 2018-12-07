#!/bin/bash

slave_1_state=$(nc -vz IP1 PORT; echo $?)
slave_2_state=$(nc -vz IP2 PORT; echo $?)

if [ $slave_1_state != '0' ];then
  A="Slave 1 is down."
  curl -s -XPOST https://hooks.slack.com/services/  \
  -d '{
  "text": "'"$A"'"
  }'
fi

if [ $slave_2_state != '0' ];then
  B="Slave 2 is down."
  curl -s -XPOST https://hooks.slack.com/services/  \
  -d '{
  "text": "'"$B"'"
  }'
fi