# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年11月01日
"""
from bs4 import BeautifulSoup
import requests
r = requests.get("https://python123.io/ws/demo.html")
print(r.text)
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.a)
print(soup.a.parent.name)
print(soup.title)   # 输出title标签(Tag)中的内容
print(soup.prettify())
