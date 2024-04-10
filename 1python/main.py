from lxml import etree
import requests
import os
import time

Url="https://www.cuiman.com/woduzishengji"
Resp=requests.get(Url)
# print(resp.text)

tree=etree.HTML(Resp.text)
lis=tree.xpath('/html/body/div[4]/div[2]/div[2]/div[2]/ul//a')
j=0
for li in lis:
    href=li.get('href')
    print('https://www.cuiman.com/'+href)
    url = 'https://www.cuiman.com/'+href
    resp = requests.get(url)
    # print(resp.text)
    html = etree.HTML(resp.text)
    divs = html.xpath("/html/body/div[1]/div[2]//img")
    head = html.xpath("/html/body/div[1]/div[1]/div[2]/h1/a/text()")[0]
    print(head)
    j+=1
    if j<=22 or j>40 :
        continue
    folder_path = './{}'.format(head)
    os.makedirs(folder_path)

    # ///html/body/div[1]/div[2]//img
    i = 1;
    for img in divs:
        img_value = img.get('data-original')
        urll = img_value
        respp = requests.get(urll)
        with open('./{}/{}.jpg'.format(head, i), mode="wb") as f:
            f.write(respp.content)
            time.sleep(0.5)
        respp.close()
        print('./{}/{}.jpg,下载完毕'.format(head, i))
        i += 1

    resp.close()
    print("{}下载完毕".format(head))

Resp.close()