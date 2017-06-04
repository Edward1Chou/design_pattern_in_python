#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: mymath.py
module description: decoration for memorization
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/31 21:45
"""
import functools
from timeit import Timer


def memoize(level):
    known = dict()

    def decorator(fn):
        @functools.wraps(fn) # store original fn's name and doc
        def memoizer(*args):
            if level == "on":
                if args not in known:
                    known[args] = fn(*args)
                return known[args]
            if level == "off":
                return fn(*args)
        return memoizer
    return decorator


@memoize(level="on")
def nsum(n):
    """
    返回前n个数字之和
    :param n: 
    :return: 
    """
    assert (n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)


@memoize(level="off")
def fibonacci(n):
    """
    返回斐波那契数列的第n个数
    :param n: 
    :return: 
    """
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    measure = [{'exec': 'fibonacci(5)', 'import': 'fibonacci',
                'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum',
                                     'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import '
                                          '{}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time: {}'.format(
            m['func'].__name__, m['func'].__doc__, m['exec'], t.timeit()))
