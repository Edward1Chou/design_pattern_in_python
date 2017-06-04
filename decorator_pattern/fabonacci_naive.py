#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: fibonacci_naive.py
module description: implement of fibonacci using naive method
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/31 19:50
"""
from timeit import Timer
import time


def fibonacci(n):
    assert (n >= 0), 'n must be >=0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    t = Timer('fibonacci(4)', 'from __main__ import fibonacci')
    print(t.timeit()) # default 重复1000000次
    start = time.time()
    fibonacci(5)
    print(time.time()-start) # time.time()的方法没有timeit的方法精准