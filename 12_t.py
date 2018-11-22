# 处理下拉框，例：oschina

from selenium import webdriver
import datetime
import random
from selenium.webdriver.support.ui import Select

driver = webdriver.PhantomJS('D:/o/phantomjs.exe')
driver.set_window_size(1280, 2400)


# 保存图片
def save_pic():
    dir = 'D:/o/'
    filename = '{}{:%Y%m%d%H%MS}{:>03}.png'.format(dir, datetime.datetime.now(), random.randint(1, 100))
    driver.save_screenshot(filename)

# 打开网GET方法，模拟浏览器地址地址输入网址
url = 'https://www.oschina.net/search?scope=project&q=python'
driver.get(url)

# 获取select
ele = driver.find_element_by_name("tag1")  # 获取元素
print(ele.tag_name)  # 标签名
save_pic()

s = Select(ele)
s.select_by_index(1)
print(driver.current_url)  # 新页面

save_pic()
driver.close()
