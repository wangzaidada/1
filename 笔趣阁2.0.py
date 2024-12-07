# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年11月18日
"""
import requests
from bs4 import BeautifulSoup

headers = {  # 请求头伪装
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
                  ' Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
}


def getHTMLText(url):
    try:

        r = requests.get(url, headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getList(page):
    page_list = page.find('dl', class_="listmain").find_all('a')  # 解析目录
    return page_list


def getBookInfo(lst, baseurl, book_name, book_author):
    rp = " 笔趣阁 www.bbiquge.net，最快更新" + book_name + "最新章节！"
    book_name = book_name + ' ' + book_author + ".txt"
    f = open(book_name, 'w+', encoding='utf-8')
    for l in lst:
        new_url = baseurl + l['href']  # 定制url
        page1 = requests.get(new_url, headers=headers).text  # 获取文章页面
        page1_soup = BeautifulSoup(page1, 'lxml')  # 解析文章页面
        txt = page1_soup.find('div', id='content').text  # 提取文章内容
        txt = txt.replace(rp, '')  # 替换多余字符串
        txt = txt.replace("     ", '\n  ')
        f.write('\n' + l.text)
        f.write(txt)
        print('\r' + l.text + ' 已保存', end='')
    f.close()
    print('\n爬取结束')
    return True


def main():
    url = "https://www.3bqg.cc/book/88072/"  # 笔趣阁网址
    page = getHTMLText(url)
    page = BeautifulSoup(page, 'lxml')
    book = page.find('h1')
    book_author = ''
    book_name = book
    book_list = getList(page)
    print('开始下载：{}'.format(book_name))
    getBookInfo(book_list, url, book_name, book_author)


main()
