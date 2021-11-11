# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年06月07日
"""
import requests
if __name__ == "__main__":
    url = 'http://www.sogou.com/'   # step 1:指定url
    # step 2:发起请求
    response = requests.get(url=url)
    # step 3:获取响应数据.txt返回的是字符串形式的响应数据
    page_txt = response.text
    print(page_txt)
    # step 4:持久化存储
    with open('./sogou.html', 'w', encoding="utf-8") as fp:
        fp.write(page_txt)
    print("爬取数据结束！！！！")
