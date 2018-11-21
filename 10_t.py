from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import logging
from bs4 import BeautifulSoup
from lxml import etree
from queue import Queue


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
e = threading.Event()

# https://www.cnblogs.com/news/#p10
base_url = 'https://www.cnblogs.com'
news_page = '/news/#p'


# 创建博客园新闻的10页urls
def create_urls(start, end):
    for n in range(start, end+1):
        url = '{}{}{}'.format(base_url, news_page, n)
        urls.put(url)


headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

urls = Queue()  # 带爬取队列
htmls = Queue()  # 响应数据队列
outputs = Queue()  # 结果输出队列

# create_urls(1, 10)
# print(urls.qsize())
# while not urls.empty():
#     print(urls.get())


# 爬取页面线程函数，发起requests返回response
def crawler():
    while not e.is_set():
        try:
            url = urls.get(True, 1)
            with requests.get(url, headers=headers) as response:
                html = response.text
                htmls.put(html)  # 返回响应加入待处理队列
                # print(type(html))  # str
        except Exception as er:
            logging.info(er)


# 解析线程函数，分析数据
def parse():
    while not e.is_set():
        try:
            html = htmls.get(True, 1)
            # soup = BeautifulSoup(html, 'lxml')
            # titles = soup.select('h3 a')  # ?? 不会写了。。
            # for t in titles:
            #     outputs.put(t.text)
            #     print(t.text)
            content = etree.HTML(html)
            titles = content.xpath('//h3/a/text()')
            for t in titles:
                outputs.put(t)
                print(t)
        except Exception as er:
            logging.info(er)


# 持久化线程函数,用文件保存起来
def save(path):
    with open(path, 'a+') as f:
        while not e.is_set():
            try:
                text = outputs.get(True, 1)
                print(text)
                f.write('\n'+text)
                f.flush()
            except Exception as er:
                print(er)


# 线程池
exector = ThreadPoolExecutor(10)
exector.submit(create_urls(1, 10))
exector.submit(parse)
exector.submit(save, 'D:/o/news.txt')
for i in range(7):
    exector.submit(crawler)

while True:
    s = input('>>>')
    if s.strip() == 'q':
        e.set()
        print('closing......')
        break
