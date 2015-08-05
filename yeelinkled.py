#!/usr/bin/env python
# coding=utf-8
import requests
import RPi.GPIO as GPIO
import time
#程序结束后进行清理
GPIO.cleanup()
# BOARD编号方式，基于BCM
GPIO.setmode(GPIO.BCM)
# 输出模式
GPIO.setup(11,GPIO.OUT)
# 设备URI，填写你的开关URL
apiurl = 'http://api.yeelink.net/v1.0/device/89596/sensor/107192/datapoints'
# 用户密码，API KEY，替换成你自己的
apiheaders = {'U-ApiKey': '1896c43cef112d1ab0002d9d136a17e1'}
while True:
#发送请求
  r = requests.get(apiurl,headers=apiheaders)
  # 打印响应内容
  print(r.text)
  # 转换为字典类型 请注意 2.7.4版本使用r.json(),我的是2.7.3
  led = r.json()
  # {'value':x} x=1打开状态，x=0关闭状态
  if led['value'] == 1:
    print("led on")
    GPIO.output(11,GPIO.HIGH)
  else:
    print("led off")
    GPIO.output(11,GPIO.LOW)
  # 延时5S
  time.sleep(5)
#程序结束后进行清理
GPIO.cleanup()
