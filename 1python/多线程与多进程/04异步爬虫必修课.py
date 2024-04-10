
# aiohttp,aiofile
import asyncio

import aiohttp
import aiofiles


async def download(url,name):
    # 相当于request
    async with aiohttp.ClientSession() as session:
        # 发送网络请求
        async with session.get(url) as resp:
            # await resp.text()  # =>resp.text
            # await resp.content.read()  # =>resp.content
            # await resp.json()
            content=await resp.content.read()
            async with aiofiles.open(f'{name}.jpg',mode="wb") as f:
                await f.write(content)
                await f.close()
    print(f"开始下载{name}")


async def main():
    url = [
        'https://tse3-mm.cn.bing.net/th/id/OIP-C.AOI88v8TvFyVKmc7eRezDAHaEo?w=248&h=180&c=7&r=0&o=5&dpr=1.4&pid=1.7',
        'https://tse2-mm.cn.bing.net/th/id/OIP-C.c8N17v38k4YchHz2kk0k1wHaFj?rs=1&pid=ImgDetMain',
        'https://tse3-mm.cn.bing.net/th/id/OIP-C.xvySeBRQe-EVXZx_qyrs_wHaFv?rs=1&pid=ImgDetMain'
    ]
    name=['a','b','c']

    tasks=[]
    i=0
    for urll in url:
        t=asyncio.create_task(download(urll,name[i]))
        i+=1
        tasks.append(t)

    await asyncio.wait(tasks)

if __name__=='__main__':
    asyncio.run(main())