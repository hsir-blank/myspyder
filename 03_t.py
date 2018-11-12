# https://movie.douban.com/j/search_subjects?
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import simplejson

b_url = 'https://movie.douban.com/j/search_subjects'
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
# from urllib import parse
# s = 'tag=%E7%83%AD%E9%97%A8'
# ss = parse.unquote(s)
# print(ss)
data = urlencode({
    'type': 'movie',
    'tag': '热门',
    'page_limit': 20,
    'page_start': 10
})
url = '{}?{}'.format(b_url, data)

res = Request(url, headers={
    'User-agent': ua
})

response = urlopen(url, data=data.encode())  # POST
with response:
    # print(response._method)
    d = response.read().decode()
    print(d)
    print(type(d))
    s = simplejson.loads(d)
    print(s)
    print(type(s))
    print(len(s['subjects']))  # 20

