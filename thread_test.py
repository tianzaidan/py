#coding=utf-8
import re
import requests
import time
import os
import threading
import random

from concurrent.futures import ThreadPoolExecutor

def thread_test(num,num2,num3):
    print(str(num)+"start")
    #time.sleep(random.randint(1,4))

def main():
    num=40
    i=0
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures=[executor.submit(thread_test,n,n,n) for n in range(num)]
    print("end")
if __name__ == '__main__':
    main()
