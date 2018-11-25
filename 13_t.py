# 模拟开源中国登陆
from selenium import webdriver
import datetime
import random
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS('D:/o/phantomjs.exe')

driver.set_window_size(1280, 2400)  # 设置窗口大小

# 保存图片
def save_pic():
    dir = 'D:/o/'
    filename = '{}{:%Y%m%d%H%MS}{:>03}.png'.format(dir, datetime.datetime.now(), random.randint(1, 100))
    driver.save_screenshot(filename)

# 打开网页GET方法，模拟浏览器地址栏输入网址
url = 'https://www.oschina.net/home/login'
driver.get(url)
save_pic()

# 模拟键盘输入
# userMail  userPassword
username = driver.find_element_by_id('userMail')
username.send_keys('wei.xu@magedu.com')
pwd = driver.find_element_by_id('userPassword')
pwd.send_keys('magedu.com18')
save_pic()

# 模拟回车
pwd.send_keys(Keys.ENTER)
print('+'*30)
print(driver.current_url)
save_pic()
time.sleep(1)
save_pic()

while True:
    time.sleep(1)
    print(driver.current_url)
    try:
        userinfo = driver.find_element_by_class_name("box user-info")
        print(1, userinfo.text)
        save_pic()
        break
    except Exception as e:
        print(2, e)
        break

cookies = driver.get_cookies()  # 获取长期登陆的cookie
print(cookies)
