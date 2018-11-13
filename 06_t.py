from lxml import etree  # 红色波浪线不影响
import requests

'''
    # 测试etree
    root = etree.Element('html')
    body = etree.Element('body')
    print(type(root))
    print(root.tag)
    root.append(body)
    print(etree.tostring(root).decode())
    sub = etree.SubElement(body, 'child1')
    sub = etree.SubElement(body, 'child2').append(etree.Element('child21'))
    print(etree.tostring(root, pretty_print=True).decode())
'''

url = 'https://movie.douban.com/'
ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
with requests.get(url, headers={'user-agent': ua}) as response:
    content = response.text  # HTML内容
    html = etree.HTML(content)
    # titles = html.xpath("//div[@class='billboard-bd']//tr/td/a")
    titles = html.xpath("//div[@class='billboard-bd']//tr")
    for t in titles:
        # print(t)
        t1 = t.xpath('.//text()')
        print(t1)
        print(' '.join(map(lambda x: x.strip(), t1)))
        print('-'*30)
