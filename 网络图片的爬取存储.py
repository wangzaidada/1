# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月26日
"""
import os
import requests

root = "C:/Users/DUAN/Downloads//"
url = "https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00132-1104.jpg"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path, 'wb') as f:
            write = f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在！")
except:
    print("爬取失败")
