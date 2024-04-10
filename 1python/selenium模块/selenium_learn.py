# 让程序连接到浏览器，让浏览器来完成各种复杂的操作，我们只接受最终的结果
# selenium：自动测试工具，像人一样操作，程序员可以从其中提取各种信息
# 环境搭建
# pip install selenium
# 下载浏览器驱动，把解压下来的放在python解释器所在的文件夹
import time
from webbrowser import Chrome

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 创建对象

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)
driver.get(r'https://www.bilibili.com')
print(driver.title)

#
# el=driver.find_element(By.XPATH,'//*[@id="i_cecream"]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[2]/a/div/div[1]/picture/img')
# el.click()
# driver.switch_to.window(driver.window_handles[-1])

# ———————————————————— 第一节课，初始学习————————————————————————
# print(selenium.__version__)第四版本网上教程比较少


# 找到某个元素点击
# el=driver.find_element_by_xpath('')
# el=web.find_element_by_xpath('//*[@id="search_input"]')
# el.click()


# 朝输入框中输入某个值并回车查询
# el=driver.find_element(By.XPATH,'//*[@id="search_input"]')
# el.click()
# 让浏览器缓一缓，如果碰到ajax局部刷新的时候，需要的东西没有进行刷新
# time.sleep(1)
# 等待元素出现的代码
# el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element_by_tag_name("p"))
# driver.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)

# 查找存放的数据，并进行内容处理

# lis=driver.find_element(By.TAG_NAME,)
# for li in lis:
#     li.find_Element().text


# ——————————————————————第二节课，切换窗口————————————————————
# 注意，在selenium眼中，新窗口默认是不切换过来的，selenium视角还是在原来的窗口中
# driver.switch_to.window(driver.window_handles[-1])
# -1代表最后一个
# 在新窗口中提取内容
# detail=driver.find_element(By.XPATH,'***').text

# 关掉子窗口
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.default_content()切换到原页面


# 处理iframe的时候，必须先拿到iframe的url值，再切换视角到iframe
# iframe=driver.find_element()
# driver.switch_to.frame(iframe)
# tx=driver.find_element().text

# ——————————————无头浏览器————————————————
# select=driver.find_element()
# 将select包装成下拉菜单
# sel=Select(select)
# for i in range(len(sel.options)):
#     sel.select_by_index()根据索引进行选择
#     sel.select_by_value()根据内容进行选择
#     visible_text根据text进行切换


# 无头浏览器设置
# options=webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# web=webdriver.Chrome(options=options)

# 如何拿到页面源代码，不用进行js操作之后
# print(driver.page_source)


# ————————————————验证码——————————————————
# 1.图像识别
# 2.选择互联网上成熟的验证码破解工具，超级鹰处理验证码
# chaojiying=Chaojiying_Client('','','')
# im=open('a.jspg','rb').read()
# print(chaojiying.PostPic(img,1902))

# 处理验证码
# img=driver.find_element().screenshot_as_png得到img图片
# 从获取的json中得到字符串结果

# 在页面之中填入
# .send_keys()

