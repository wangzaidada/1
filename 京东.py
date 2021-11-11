# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年06月07日
"""
import requests

url = "https://item.jd.com/2967929.html"
try:
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.headers)

except:
    print("爬取失败")
