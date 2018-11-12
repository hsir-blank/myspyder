from urllib.request import urlopen, Request
from urllib import parse
import simplejson

'''
    # 测试
    u = parse.urlencode({'name': '寒窑'})  # utf-8
    print(u)  # name=%E5%AF%92%E7%AA%91
    
    print('寒窑'.encode('utf8'))  # b'\xe5\xaf\x92\xe7\xaa\x91'
    print(parse.unquote(u))  # 解码 name=寒窑
'''

'''
    # POST
    keyword = input('>>>请输入搜索关键字:')
    data = parse.urlencode({
        'q': keyword
    })
    base_url = 'http://cn.bing.com/search'
    url = '{}?{}'.format(base_url, data)
    # 伪装
    ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
    
    res = Request(url, headers={
        'User-agent': ua
    })
    
    response = urlopen(res)
    with response as rep:
        with open('D:/o/search.html', 'wb') as f:
            f.write(rep.read())
    print('fin')
'''

request = Request('http://httpbin.org/post')  # POST
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
request.add_header(
    'User-agent', ua
)

data = parse.urlencode({'name': '张三,@=/&*', 'age': 6})
print(data)

response = urlopen(request, data=data.encode())
with response:
    s = response.read()
    d = simplejson.dumps(s)
    # print(response.read())
print(d)