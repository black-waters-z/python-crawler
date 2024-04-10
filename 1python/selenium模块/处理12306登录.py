import os

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests


headers={
    'Referer':'https://weibo.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}


from selenium.webdriver import ActionChains

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)
driver.get("https://weibo.com/ttarticle/x/m/show#/id=2309404670196995457237&_wb_client_=1")

time.sleep(3)
# print(driver.page_source)
soup=BeautifulSoup(driver.page_source,"html.parser")
figure=soup.find_all('p')
# print(imgs)
i=1
title=soup.find('h2',attrs={'class':'f-art-tit'}).text
# os.mkdir('[4kcalうずら] REACTION (48P)')
for img in figure:
    imgg = img.find('img')
    if i<24:
        i+=1
        continue
    if imgg==None:
        continue
    img_src=imgg.get('src')
    print(img_src)
    resp=requests.get(img_src,headers=headers)
    with open(f'[4kcalうずら] REACTION (48P)/{i}.jpg',mode='wb') as f:
        f.write(resp.content)
        print(f'[4kcalうずら] REACTION (48P)/{i}.png下载成功')
    time.sleep(1)
    resp.close()
    i+=1


# 让鼠标移动到某一个位置，再进行点击
# ActionChains(driver).move_to_element_with_offset(img_element,x,y).click(

# 拖曳
# btn=driver.find_element()
# ActionChains(driver).drag_and_drop_by_offset(btn,300,0)