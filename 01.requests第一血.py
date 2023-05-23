# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年06月07日
"""
import requests

headers = {  # 请求头伪装
    'User-Agent': 'Mozilla/5.0'
}
url = 'https://buy.autohome.com.cn/110000/110100/index.html#pvareaid=3311447'
x = requests.get(url, headers=headers)
print(x.status_code)
fp = open('ce.html', 'w', encoding='utf-8')
fp.write(x.text)
fp.close()
print('ok')
