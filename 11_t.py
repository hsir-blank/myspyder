from selenium import webdriver
import datetime
import random
import time

# 指定phantomjs的执行文件路径
driver = webdriver.PhantomJS('D:/o/phantomjs.exe')

driver.set_window_size(1280, 2400)  # 设置窗口大小

# 打开网页GET方法，模拟浏览器输入网址
# http://cn.bing.com/search?q=靳梦佳
url = 'https://cn.bing.com/search?q=%E9%9D%B3%E6%A2%A6%E4%BD%B3'
driver.get(url)

# 保存图片
def save_pic():
    dir = 'D:/o/'
    filename = '{}{:%Y%m%d%H%MS}{:>03}.png'.format(dir, datetime.datetime.now(), random.randint(1, 100))
    driver.save_screenshot(filename)
# save_pic()
# time.sleep(5)
# save_pic()


maxretry = 5  # 最大重试次数
for i in range(maxretry):
    time.sleep(1)
    try:
        ele = driver.find_element_by_id("b_content")
        print('ok')
        save_pic()
        break

    except Exception as e:
        print(e)
driver.close()
