# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年03月13日
"""
import threading
import time

import requests
import queue

link_list = []
with open('alexa.txt', 'r') as file:     # 解析文件提取url
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)

start = time.time()  # 开始计时


class myThread(threading.Thread):   # 创建线程类
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                crawler(self.name, self.q)
            except:
                break
        print("Exiting " + self.name)


def crawler(threadName, q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=20)
        print(q.qsize(), threadName, r.status_code, url)
    except Exception as e:
        print(q.qsize(), threadName, url, "Error: ", e)


threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5","Thread-6", "Thread-7", "Thread-8", "Thread-9", "Thread-10"]
workQueue = queue.Queue(maxsize=1000)
threads = []

# 填充队列
for url in link_list:
    workQueue.put(url)

# 创建新线程
for tName in threadList:
    thread = myThread(tName, workQueue)
    thread.start()
    threads.append(thread)


# 等待所有线程完成
for t in threads:
    t.join()

end = time.time()
print('Queue多线程爬虫的总时间为：', end - start)
print("Exiting Main Thread")
# Queue多线程爬虫的总时间为： 331.5664792060852
