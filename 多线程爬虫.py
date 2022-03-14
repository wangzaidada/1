# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年03月11日
"""
# import requests
# import time
#
# link_list = []
# with open('alexa.txt', 'r') as file:
#     file_list = file.readlines()
#     for eachone in file_list:
#         link = eachone.split('\t')[1]
#         link = link.replace('\n', '')
#         link_list.append(link)
#
# start = time.time()
# for eachone in link_list:
#     try:
#         r = requests.get(eachone, timeout=10)
#         print(r.status_code, eachone)
#     except Exception as e: # 异常捕获 赋值给e
#         print('Error: ', e)
# end = time.time()
# print('串行的总时间为', end - start)
# # 串行的总时间为 1780.65341091156
