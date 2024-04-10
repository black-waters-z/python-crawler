# 1.发送请求，从服务器获取到数据
# 2.beautifulsoup来解析源码
import time

import requests
from bs4 import BeautifulSoup

proxies={
    'http':'http://180.127.99.227:19443'
}
# 采用代理

resp=requests.get('https://tvax4.sinaimg.cn/crop.0.0.600.600.180/002TLsr9ly8hmxa6f543uj60go0gowfl02.jpg?KID=imgbed,tva&Expires=1712746234&ssig=2JgHJtCV2t',proxies=proxies)
# print(resp.content)
with open('a.jpg',mode='wb') as f:
    f.write(resp.content)

resp.close()




# img_divs=soup.find_all('div',attrs={'class':'sm-base-cover-img mode-top'})
#
# for div in img_divs:
#     img=div.find('img')
#     print(img.get("src"))


# resp.close()