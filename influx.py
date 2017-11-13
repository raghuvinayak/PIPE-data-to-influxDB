#!usr/bin/python

import sys
import datetime
from influxdb import InfluxDBClient
import os
import time

client=InfluxDBClient('localhost',8086,'admin','admin',database='ANM')
client.create_database('ANM')
def store(bit_rate,time):
      json=[
              {
              "measurement":"tablename",
              "tags":{
                       "tag":"sample",

                       },
                       "time":time,
                       "fields":{
                               "bit_rate":bit_rate

                       }
      }
      ]
      client.write_points(json,time_precision='u')




while True:
	elements= raw_input().strip().split()
	time.sleep(1)
		if len(elements) == 2:
		bit_rate=elements[1]
		unixtime = elements[0].split('.')
		stdtime = datetime.datetime.utcfromtimestamp(long(float(unixtime[0]))).strftime('%Y-%m-%dT%H:%M:%S')
		influxtime = ".".join([stdtime,unixtime[1]])
		store(bit_rate,influxtime)
