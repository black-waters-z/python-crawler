import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

# def func(name):
#     for i in range(100):
#         print(name,i)
#
# if __name__=='__main__':
#     # 创建线程,args传值
#     t1=Thread(target=func,args=("a"))
#     t2=Thread(target=func,args=("b"))
#     t3=Thread(target=func,args=("c"))
#
#     t1.start()
#     t2.start()
#     t3.start()
#
#     print("我是主线程")



# 多线程-写法2，面向对象
# 继承Thread
# class MyThread(Thread):
#     def __init__(self,name):
#         super(MyThread, self).__init__()
#         self.name=name
#
#     def run(self):
#         for i in range(100):
#             print(self.name,i)
#
# if __name__=='__main__':
#     t1=MyThread("a")
#     t2=MyThread("b")
#     t3=MyThread("c")
#
#     t1.start()
#     t2.start()
#     t3.start()

# 线程池，将任务塞到线程池之中，一瞬间会拿出一些任务，拿出的线程进行工作，任意一个线程结束之后，自动再开辟一个线程，将接等待的任务塞入

#
# def func(name,i):
#     print('我是',name)
#     time.sleep(i)
#     return name
#
# def fn(res):
#     print(res.result())
#
# if __name__=='__main__':
#     # 设置最多十个任务一起跑
#     with ThreadPoolExecutor(3) as t:
#         # for i in range(10):
#         #     # 当前任务结束后，将返回值给fn，立即执行绑定的任务继续进行
#         #     t.submit(func,f'线程{i}').add_done_callback(fn)
#         result=t.map(func,["周杰伦","王力宏","王富贵"],[2,1,3])
#         for r in result:
#             print(r)
#             # map返回值是生成器，返回的内容和任务分发的顺序是一致的
#
#

# 进程池

def func(name):
    for i in range(100):
        print(name,i)

if __name__=='__main__':
    p1=Process(target=func,args=("周杰伦",))
    p2=Process(target=func,args=("王富贵",))
    p1.start()
    p2.start()

# 何时使用多线程，何时使用多进程
# 1.多线程：当逻辑和结构极其相似的时候
# 2.多进程：多个任务相互独立，很少有交集
# 免费IP池：
# 1.从各个免费网站上抓取代理IP
# 2.验证代理IP是否可用
# 3.准备对外的接口

"""
队列：可以进行进程之间的通信
q=Queue()
p1=Process(target=func,args=(q,))q为参数
p2=Process(target=func,args=(q,))

q.put(src)往队列里头装东西

q.get()从队列之中获取数据,如果没有数据就会阻塞
while 1:
    src=q.get()
    线程池进行缓冲
"""