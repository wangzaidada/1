import requests
import random
from threading import Thread

url = 'http://10.16.170.184:8080/'


def get_ip(point):
    str_ip = ''
    for i in range(4):
        if i != 3:
            str_ip += str(random.choice(point)) + '.'
        else:
            str_ip += str(random.choice(point)) + ':' + str(random.choice([i for i in range(3000, 65535)]))
    return str_ip


def get_pool():
    point = [i for i in range(1, 255)]
    for i in range(10000):
        yield {"http": get_ip(point)}


def thread_request():
    while True:
        for i in range(10):
            r = requests.get(url)
            if r.status_code == 200:
                print('请求正常,继续。。。。。。。')


def main():
    thread_list = []
    for i in range(1000):
        thread = Thread(target=thread_request)
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    main()
