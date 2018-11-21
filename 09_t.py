import requests

url = "https://www.oschina.net/"

headers = {
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Connection': "keep-alive",
    'Content-Length': "0",
    'Cookie': "aliyungf_tc=AQAAAK0lShfNDwIAwFYkdUE9suwo3Cfp; _user_behavior_=b45d8c36-b784-4fdd-8575-78ad3b0635fb; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1542707856,1542792234; _reg_key_=pO6GPBuMcEdnGIL34Nkv; oscid=ZV2oveUqo28xv80qumQtfRqukWzpKq2brNqjn0Y0a5kFTeUQUUbcPj2dwLIiVt%2FuuSC4k5jSAd%2FPQOvqblGJiFIsRyvw3wGL8D4BffXxL1vV5AUUz3JocsoFMFKqWdLzKZanWq%2BEp3QJHt51I8Sgzzi8cmYuYVJbGoQMEsF7QV8%3D; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1542792433",
    'Host': "www.oschina.net",
    'Origin': "https://www.oschina.net",
    'Referer': "https://www.oschina.net/?nocache=1542792431860",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'Cache-Control': "no-cache",
    'Postman-Token': "fc16a254-7515-49bd-a9b2-a4c731112eb5"
    }

response = requests.request("GET", url, headers=headers)  # 带cookie   登录以后的页面
response1 = requests.request("GET", url, headers={
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
})   # 不带cookie， 登录，注册

with response1:
    with open('D:/o/oscn_logout.html', 'w', encoding='utf8') as f:
        text = response1.text
        f.write(text)
        print(text)
        print(response1.status_code, '**************')