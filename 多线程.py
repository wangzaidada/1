# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年03月13日
"""
# import threading
# import time
# import requests
#
#
# class myThread(threading.Thread):
#     def __init__(self, name, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print("Starting " + self.name)
#         print_time(self.name, self.delay)
#         print("Exiting " + self.name)
#
#
# def print_time(threadName, delay):
#     counter = 0
#     while counter < 3:
#         time.sleep(delay)
#         print(threadName, time.ctime())
#         counter += 1
#
#
# threads = []
#
# # 创建线程
# thread1 = myThread("Thread-1", 1)
# thread2 = myThread("Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
#
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
#
# print("Exiting Main Thread")
'''
Starting Thread-1
Starting Thread-2
Thread-1 Sun Mar 13 15:11:36 2022
Thread-2 Sun Mar 13 15:11:37 2022
Thread-1 Sun Mar 13 15:11:37 2022
Thread-1 Sun Mar 13 15:11:38 2022
Exiting Thread-1
Thread-2 Sun Mar 13 15:11:39 2022
Thread-2 Sun Mar 13 15:11:41 2022
Exiting Thread-2
Exiting Main Thread
'''
# import threading
# import time
#
# import requests
#
#
# class myThread(threading.Thread):
#     def __init__(self, name, url):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.url = url
#
#     def run(self):
#         print("Starting " + self.name)
#         print_get(self.url)
#         print("Exiting " + self.name)
#
#
# def print_get(url):
#     try:
#         r = requests.get(url, timeout=10)
#         print(r.status_code, url)
#     except Exception as e:  # 异常捕获 赋值给e
#         print('Error: ', e)
#
#
# start = time.time()
# threads = []
# link_list = []
# with open('alexa.txt', 'r') as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1]
#         link = link.replace('\n', '')
#         link_list.append(link)
#
# for eachone in range(0, len(link_list), 5):
#     thread1 = myThread("Thread-" + str(1), link_list[eachone + 0])
#     thread2 = myThread("Thread-" + str(2), link_list[eachone + 1])
#     thread3 = myThread("Thread-" + str(3), link_list[eachone + 2])
#     thread4 = myThread("Thread-" + str(4), link_list[eachone + 3])
#     thread5 = myThread("Thread-" + str(5), link_list[eachone + 4])
#     thread1.start()
#     thread2.start()
#     thread3.start()
#     thread4.start()
#     thread5.start()
#     threads.append(thread1)
#     threads.append(thread2)
#     threads.append(thread3)
#     threads.append(thread4)
#     threads.append(thread5)
#     # 等待所有线程完成
#     for t in threads:
#         t.join()
# end = time.time()
# print('多线程的总时间为', end - start)
'''
多线程的总时间为 1015.1332452297211
'''

# import threading
# import time
#
# import requests
#
#
# class myThread(threading.Thread):
#     def __init__(self, name, link_rang_list):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.link_rang_list = link_rang_list
#
#     def run(self):
#         print("Starting " + self.name)
#         print_get(self.name, self.link_rang_list)
#         print("Exiting " + self.name)
#
#
# def print_get(name, link_rang_list):
#     for j in range(link_rang_list[0], link_rang_list[1]):
#         try:
#             r = requests.get(link_list[j], timeout=10)
#             print(r.status_code, link_list[j])
#         except Exception as e:  # 异常捕获 赋值给e
#             print(name + 'Error: ', e)
#
#
# start = time.time()
# threads = []
# link_list = []
# link_rang_list = [(0, 200), (200, 400), (400, 600), (600, 800), (800, 1000)]
# with open('alexa.txt', 'r') as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1]
#         link = link.replace('\n', '')
#         link_list.append(link)
# for i in range(1, 6):
#     thread = myThread("Thread-" + str(i),link_rang_list[i-1])
#     thread.start()
#     threads.append(thread)
# for t in threads:
#     t.join()
# end = time.time()
# print('多线程的总时间为', end - start)
''' 
# 多线程的总时间为 328.87460827827454
'''  # 结果

