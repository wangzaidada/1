# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年11月15日
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.bbiquge.net/book_28709/"  # 笔趣阁网址
headers = {                                  # 请求头伪装
        'User-Agent': 'Mozilla/5.0'
    }
page = requests.get(url, headers=headers).text.replace('\ufffd', '')  # 获取图书目录
soup = BeautifulSoup(page, 'lxml')              # 解析
page_list = soup.find_all('dd')                 # 解析目录
bookname = soup.find('h1')
bookname = bookname.text.replace(bookname.find('small').text, '').replace(' ', '')
rp = " 笔趣阁 www.bbiquge.net，最快更新" + bookname + "最新章节！"
bookname = bookname + ".txt"
f = open(bookname, 'w+', encoding='gbk')
for i in range(len(page_list)):
    if i == -1:                        # 排除空标签
        continue
    else:
        new_url = url + page_list[i].a['href']  # 定制url
        page1 = requests.get(new_url, headers=headers).text.replace('\ufffd', '')     # 获取文章页面
        page1_soup = BeautifulSoup(page1, 'lxml')               # 解析文章页面
        txt = page1_soup.find('div', id='content').text         # 提取文章内容
        txt = txt.replace(rp, '')    # 替换多余字符串
        txt = txt.replace("     ", '\n')
        f.write('\n' + page_list[i].text)
        f.write(txt)
        print(page_list[i].text + '已保存')
    print(i)
f.close()
print('爬取结束')

