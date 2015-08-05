#!/usr/bin/env python
# coding=utf8
import time
import requests
import json

api_url='http://api.yeelink.net/v1.0/device/89596/sensor/131831/datapoints'
api_headers={'U-ApiKey':'1896c43cef112d1ab0002d9d136a17e1','content-type':'application/json'}


def get_cpu_temp():
    try:
        cpu_temp_file = open('/sys/class/thermal/thermal_zone0/temp')
    except:
        print 'open cpu_temp_file error!'
    cpu_temp = cpu_temp_file.read()
    cpu_temp_file.close()
    return float(cpu_temp)/1000

while True:

    temp = get_cpu_temp()
    data = {'value':temp}
    r = requests.post(api_url,headers=api_headers,data=json.dumps(data))
    print 'cpu_temp:',get_cpu_temp()
    time.sleep(1)


