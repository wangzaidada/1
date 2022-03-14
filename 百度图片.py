# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年12月01日
"""

import requests
url = 'https://image.baidu.com/search/index'
word = 'input()'
headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.45Safari / 537.36"
}
params = {
    "tn": "baiduimage",
    'word': word
}
response = requests.get(url=url, params=params, headers=headers)
print(response.url)

