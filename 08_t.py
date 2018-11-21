import requests
from bs4 import BeautifulSoup

file = 'D:/o/oscn.html'
file1 = 'D:/o/oscn_logout.html'

with open(file, 'r', encoding='utf8') as f:
    soup = BeautifulSoup(f, 'lxml')
    s = f.read()
    # print(s)
    x = soup.find(class_="box user-info")
    print(x.get_text().split())  # 分析登录与不登录的不同
