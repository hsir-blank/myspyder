from urllib.request import Request, urlopen
import ssl

ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
request = Request('http://www.12306.cn/morhweb/')
request.add_header('user-agent', ua)

# 忽略不信任的证书
context = ssl._create_unverified_context()
with urlopen(request, context=context) as res:
# res = urlopen(request)
# with res:
    print(res._method)
    print(res.geturl())
    print(res.read().decode())
