# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年11月04日
"""
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        r = requests.get(url, headers, timeout=30)
        r.raise_for_status()    # 判断异常 如果是200则正常 如果不是200则产生HttpError的异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    url = "https://www.shanghairanking.cn/rankings/bcur/2021"
    uinfo = []
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


main()
