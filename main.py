import requests
from pyquery import pyquery as pq

url = 'https://greasyfork.org/zh-CN/scripts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
    ' Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
}
response = requests.get(url=url, headers=headers).text
doc = pq(response)
script_link = doc('.script-link')
print(script_link)
