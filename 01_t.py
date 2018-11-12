from urllib.request import urlopen, Request
import random
url = 'http://www.bing.com'
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/57.0.2987.133 Safari/537.36",
    # chrome
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko)Version/5.0.1 Safari/537.36",
    # safafi
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0",  # Firefox
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"  # IE
]


ua = random.choice(ua_list)
request = Request(url, headers={})
request.add_header('User-Agent', ua)
print(type(request))

# response = urlopen(url)  # GET 方法
response = urlopen(request)  # GET 方法
# print(response.closed)
print(1, type(response))

with response:
    print(2, response.status)  # 状态码
    print(21, response.reason)  # OK
    print(3, response.geturl())  # 返回真正的url
    print(4, response.info())  # headers
    print(5, response.read())  # 读取返回的内容
    print(6, response)

print(response.closed)
print('user-agent'.capitalize())  # 首字母大写
