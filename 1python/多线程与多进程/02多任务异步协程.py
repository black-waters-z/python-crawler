import time

"""
可以更加高效的利用CPU，所以使用协程来进行，线程与进程开的时候会产生大量IO堵塞
"""
import asyncio


"""
只是一个线程
# 已不再是个普通的函数,协程对象想要执行必须借助,该函数执行时得到的是一个协程对象
async def func():
    print("我是函数")

if __name__=='__main__':
    # 协程对象想要执行，必须借助于event_loop，运行一个协程对象，直到最后才停止
    # result=func()
    # print(result)
    f=func()
    # 1.拿到事件循环
    # event_loop=asyncio.get_event_loop()
    # # 执行协程对象，直到该对象内的内容执行完全为止
    # event_loop.run_until_complete(f)

    # 第二种方法,假如电脑报错：Event Loop ha closed，不能用第二种
    asyncio.run(f)

"""

async def func1():
    print("我是func1")
    await asyncio.sleep(1)
    # 异步睡眠
    print("func1结束")


async def func2():
    print("我是func2")
    await asyncio.sleep(2)
    print("func2结束")


async def func3():
    print("我是func3")
    await asyncio.sleep(3)
    print("func3结束")

async def main():
    # 第二种方式
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = {
        # 封装任务列表
        asyncio.create_task(f1),
        asyncio.create_task(f2),
        asyncio.create_task(f3),
    }
    # 等待完成，统一等到协程任务执行完毕
    await asyncio.wait(tasks)

if __name__=='__main__':
    """start=time.time()
    f1=func1()
    f2=func2()
    f3=func3()
    # 把三个任务放在一起
    # 1.tasks={
    #     f1,
    #     f2,
    #     f3,
    # }

    # wait表示等待，必须要等到三个任务全完成才行
    # asyncio.run(asyncio.wait(tasks))
    """
    asyncio.run(main())

"""
未来爬虫：
    1.扫url，拿到一堆url
    2.循环url，创建任务
    3.统一await
"""

