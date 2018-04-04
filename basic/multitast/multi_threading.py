#!/user/bin/env python3
# -*- coding: utf-8 -*-

# import time, threading

# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.')

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# Lock
# 多线程和多进程最大的不同在于，
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

# 来看看多个线程同时操作一个变量怎么把内容给改乱了：

# import time
# import threading

# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()


# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n


# def run_thread(n):
#     for i in range(999999):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()


# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()