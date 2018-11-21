from bs4 import BeautifulSoup
import re

file = 'D:/o/test.html'
with open(file, encoding='utf8') as f:
    soup = BeautifulSoup(f, 'lxml')
    # print(0, soup.children)
    # print(1, soup.text)
    # print(2, soup.builder)
    # print(1, soup.prettify())
    # print(30, soup.div.name, 31,  soup.div.attrs)  # 属性为字典
    # print(3, soup.div)  # 深度优先查找
    # print(4, soup.p.get('i'))  # 找不着返回None
    # print(5, soup.div.get('id'))
    # print(6, soup.h3['class'])  # 多值属性
    # print(7, soup.p.string)  # 返回输出标记内只包含的文本，包含其他则返回None
    # print(8, ''.join(soup.div.strings))  # 返回生成器
    # print(80, " ".join(soup.div.stripped_strings))  # 去除多余空白符
    # print(9, soup.img.get('src'))
    # soup.img['src'] = 'wwww.xixixi.com'  # 修改属性
    # print(90, soup.img.get('src'))
    # del soup.input['type']  # 删除属性
    # print(10, soup.input)
    # print(soup.div.parent.name)  # 第一个div的父节点
    # # 遍历兄弟节点
    # print('{}[{}]'.format(1, soup.p.next_sibling))
    # print('{}[{}]'.format(2, soup.p.previous_sibling))
    # # 遍历其他元素
    # print(list(soup.p.next_element))
    # print(soup.p.next_element.next_element)
    # find系
    # print(soup.find_all(name=['p', re.compile('h\d')]))  # 三种方法，正则，列表
    # print(soup.find_all(id=re.compile('\d+')))
    print(soup.find_all(id=True, src=True))  # and
    print(soup.find_all(attrs={
        'class': True
    }))
