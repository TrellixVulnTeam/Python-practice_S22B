#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def consumer():
#     r = 'here'
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'

# def produce(c):
#     r = c.send(None)
#     print(r)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()

# c = consumer()
# produce(c)

# import time
# import asyncio


# def now(): return time.time()


# async def do_some_thing(x):
#     print('Waiting: ', x)

# # print(now())

# loop = asyncio.get_event_loop()
# # loop.run_until_complete()
# # print(time.time())

# # coroutine = do_some_thing('x')
# # task = loop.create_task(coroutine)
# tasks = [do_some_thing(2)]
# # print(task)
# loop.run_until_complete(asyncio.wait(tasks))


# ============================================================

import time
import asyncio
import functools


# def now(): return time.time()


# async def do_some_work(x):
#     print('Waiting: ', x)
#     return 'Done after {}s'.format(x)


# def callback(future):
#     print('Callback: ', future.result())


# def callback_again(t, future):
#     print('Callback:', t, future.result())


# start = now()

# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# task.add_done_callback(functools.partial(callback_again, 2))
# loop.run_until_complete(task)

# async def do_some_work(x):
#     print('Waiting {}'.format(x))
#     return 'Done after {}s'.format(x)

# start = now()

# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# # task = asyncio.ensure_future(coroutine)
# task = loop.create_task(coroutine)
# loop.run_until_complete(task)

# print('Task ret: {}'.format(task.result()))
# print('TIME: {}'.format(now() - start))

# async def do_some_work(x):
#     print('Waiting: ', x)
 
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
 
# start = now()
 
# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(4)
 
# # tasks = [
# #     asyncio.ensure_future(coroutine1),
# #     asyncio.ensure_future(coroutine2),
# #     asyncio.ensure_future(coroutine3)
# # ]
 
# tasks = [coroutine1, coroutine2, coroutine3]
# # 这种 没有 result

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
 
# for task in tasks:
#     print('Task ret: ', task.result())
 
# print('TIME: ', now() - start)

def next_id():
    return '%1d000' % int(time.time() * 1000)


idd = next_id()
print(idd)