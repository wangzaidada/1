# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月26日
"""
import requests

kv = {'wd': '"python"'}
r = requests.get("http://www.baidu.com/s", params=kv)
print(r.request.url)
