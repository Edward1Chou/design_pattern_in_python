#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: fibonacci.py
module description: implement of fibonacci using memoization
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/31 20:29
"""
from timeit import Timer

known = {0: 0, 1: 1}


def fibonacci(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

if __name__ == '__main__':
    t = Timer('fibonacci(100)', 'from __main__ import fibonacci')
    print(t.timeit())
