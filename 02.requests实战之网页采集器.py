# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年06月07日
"""
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41
# UA:User-Agent（请求载体的身份标识）
# UA伪装: 门户网站的服务器会检测对应请求的载体身份标识，如果监测到请求的载体身份标识
# 为某一款浏览器说明该请求是一个正常的请求。但是，如果监测到请求的载体身份标识不是基于
# 某一款浏览器则表示该请求为不正常的请求（爬虫），则服务器端就很有可能拒绝该请求
import requests
if __name__ == "__main__":
    # UA伪装：将对应的User-Agent封装到一个字典中
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
                      ' Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    url = 'https://www.baidu.com/s?'
    # 处理url携带的参数:封装到字典中
    kw = input('enter a word:')
    param = {
        'wd': kw
    }
    # 对指定的url发起的请求对应url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=header)

    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, "保存成功！！！")
