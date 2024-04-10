import asyncio


async def func1():
    print("我是func1")
    await asyncio.sleep(1)
    # 异步睡眠
    print("func1结束")
    return "func1的返回值"


async def func2():
    print("我是func2")
    await asyncio.sleep(2)
    print("func2结束")
    return "func2的返回值"


async def func3():
    print("我是func3")
    await asyncio.sleep(3)
    print("func3结束")
    return "func3的返回值"


async def main():
    # 第二种方式
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [
        # 封装任务列表
        asyncio.create_task(f3),
        asyncio.create_task(f2),
        asyncio.create_task(f1),
    ]
    # 等待完成，统一等到协程任务执行完毕
    # 返回的值没有顺序
    # done,pending=await asyncio.wait(tasks)
    # for t in done:
    #     print(t.result())

    # # gather的返回值有顺序，按照你添加任务的顺序返回
    # true:如果有错误信息，返回错误信息，其他任务正常执行
    # false:所有任务直接停止
    result=await asyncio.gather(*tasks,return_exceptions=False) #,return_exceptions=False)
    print(result)

if __name__=='__main__':
    asyncio.run(main())