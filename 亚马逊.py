# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月26日
"""
import requests
kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y", headers=kv)
r.encoding = r.apparent_encoding
print(r.status_code)
print(r.text)
