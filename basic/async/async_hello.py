import asyncio
import threading
import time


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(10)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(2)
#     print('Hello again! (%s)' % threading.currentThread())


# @asyncio.coroutine
# def bye():
#     print('Bye bye world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(4)
#     print('Bye bye again! (%s)' % threading.currentThread())


# loop = asyncio.get_event_loop()
# tasks = [bye(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
