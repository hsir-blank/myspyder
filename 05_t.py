import urllib3
import requests
# <class 'urllib3.response.HTTPResponse'>
from urllib3.response import HTTPResponse
url = 'https://movie.douban.com/'
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
'''
# 连接池管理器
with urllib3.PoolManager() as http:
    response = http.request('GET', url, headers={
        'user-agent': ua
    })
    print(type(response))  # <class 'urllib3.response.HTTPResponse'>
    response: HTTPResponse = response
    print(response.status, response.reason)
    print(response.headers)
    print(response.data)
'''

response = requests.request('GET', url, headers={
    'user-agent': ua
})

with response:
    # from requests.models import Response
    print(type(response))  # <class 'requests.models.Response'>
    print(response.url)
    print(response.headers)
    print(response.request.headers)
    # print(response.text)
    with open('D:/o/movie.html', 'w', encoding='utf8') as f:
        f.write(response.text)
