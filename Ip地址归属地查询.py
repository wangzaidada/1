# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月26日
"""
import requests
url = "www.ip138.com/iplookup.asp?ip=218.87.12.203"
kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get("www.ip138.com/iplookup.asp?ip=218.87.12.203",  headers=kv)
print(r.status_code)
print(r.text[-500:])

