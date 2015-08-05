#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import requests  
#import smbus  
import RPi.GPIO as GPIO  
import time  
# 打开 /dev/i2c-1  
#bus = smbus.SMBus(1)  
# 设备URI  
apiurl = 'http://api.yeelink.net/v1.0/device/89596/sensor/107192/datapoints'  
# 用户密码  
apiheaders = {'U-ApiKey': '1896c43cef112d1ab0002d9d136a17e1'}  
while True:  
  #发送请求  
  r = requests.get(apiurl,headers=apiheaders)  
  # 打印响应内容  
  print(r.text)  
  # 转换为字典类型 请注意 2.7.4版本使用r.json()  
  led = r.json()  
  # {'value':x} x=1打开状态，x=0关闭状态  
  if led['value'] == 1:  
    print("led on")  
    #bus.write_byte( 0x20 , 1 )  
  else:  
    print("led off")  
    #bus.write_byte( 0x20 , 0 )  
  # 延时5S  
  time.sleep(1)
